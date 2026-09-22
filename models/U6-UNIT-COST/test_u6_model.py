"""Checks for the U6 model: a hand-computed case and input completeness.

Run from the repository root:
    python -B -m unittest discover -s models/U6-UNIT-COST -p "test_*.py" -v
"""

import unittest

import u6_model

# Hand-computed case (see README section "Method"): 10 dialogs, n=2, t=1, e=0.5,
# static prefix 1000, card 100, exchange 200, tool result 50, aux 500.
CASE = {
    "visits_per_month": 10, "dialogs_per_visit": 1, "client_msgs_per_dialog": 2, "tool_calls_per_dialog": 1,
    "escalation_share": 0.5, "reminders_per_visit": 2,
    "system_tokens": 0, "kb_tokens": 0, "tools_tokens": 1000, "card_tokens": 100,
    "exchange_tokens": 200, "tool_result_tokens": 50, "output_tokens_per_reply": 100, "output_tokens_per_tool_call": 10,
    "aux_instruction_tokens": 500, "card_update_output_tokens": 40, "escalation_output_tokens": 20,
    "overhead_multiplier": 1.0, "cache_hit_rate": 0.5,
}
PRICE = {"input": 1.0, "output": 5.0, "cache_write_1h": 2.0, "cache_read": 0.1, "tokenizer_factor": 1.0}


class HandComputedCase(unittest.TestCase):
    def test_token_volumes(self):
        t = u6_model.monthly_tokens(CASE)
        self.assertEqual(t["dialogs"], 10)
        self.assertEqual(t["agent_replies"], 20)
        self.assertEqual(t["static_input"], 30_000)   # (2 + 1) calls * 1000 * 10
        self.assertEqual(t["dynamic_input"], 24_500)  # (200 + 400 + 350 + 1500) * 10
        self.assertEqual(t["output"], 2_600)          # (200 + 10 + 40 + 10) * 10

    def test_reply_input_matches_explicit_sum(self):
        n, card, exch = 2, 100, 200
        explicit = sum(card + (i - 1) * exch + exch / 2 for i in range(1, n + 1))
        self.assertEqual(explicit, n * card + exch * n * n / 2)

    def test_costs(self):
        self.assertAlmostEqual(u6_model.model_cost(CASE, PRICE, cached=False), 0.0675)
        self.assertAlmostEqual(u6_model.model_cost(CASE, PRICE, cached=True), 0.069)
        scaled = {**CASE, "overhead_multiplier": 1.2}
        self.assertAlmostEqual(
            u6_model.model_cost(scaled, {**PRICE, "tokenizer_factor": 1.3}, cached=False), 0.0675 * 1.56)

    def test_whatsapp(self):
        self.assertAlmostEqual(u6_model.whatsapp_cost(CASE, 0.01, 0.005), 0.3)


class InputCompleteness(unittest.TestCase):
    def setUp(self):
        self.inputs = u6_model.load_inputs()

    def test_every_scenario_defines_every_labelled_parameter(self):
        params = set(self.inputs["parameters"])
        for name, scenario in self.inputs["scenarios"].items():
            self.assertEqual(set(scenario), params, name)

    def test_every_parameter_is_labelled(self):
        labels = set(self.inputs["meta"]["labels"])
        for key, spec in self.inputs["parameters"].items():
            self.assertIn(spec["label"], labels, key)

    def test_h5_min_price_meets_both_thresholds(self):
        price = self.inputs["model_prices"]["models"]["claude-sonnet-5"]
        need = u6_model.h5_min_price(self.inputs, price)
        shares = self.inputs["h5_thresholds"]["max_share_of_price"]
        for name, share in shares.items():
            cost = u6_model.model_cost(self.inputs["scenarios"][name], price, True)
            self.assertLessEqual(cost / need["binding"], share + 1e-12, name)
        self.assertAlmostEqual(max(need["base"], need["high"]), need["binding"])

    def test_render_runs(self):
        text = u6_model.render(self.inputs)
        self.assertIn("## 2. Model cost per month", text)
        self.assertIn("## 5. One-at-a-time sensitivity", text)


if __name__ == "__main__":
    unittest.main()
