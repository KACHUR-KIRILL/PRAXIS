#!/usr/bin/env python3
"""Minimal deterministic integrity checks for the PRAXIS repository.

Adapted from the STIMULUS checker (commit 8a18eed, 2026-09-22). This checker
intentionally covers only current deterministic invariants and already
observed failure classes. It reports defects and never edits files.
CommonMark links/images are checked for file existence only; section anchors
and raw HTML links require review. External URLs are not fetched.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    Path("README.md"),
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
    Path("roles/FOUNDER-COPILOT.md"),
    Path("product/PRAXIS-BRIEF-v0.1.md"),
    Path("standards/PROJECT-START-PROTOCOL-v0.1.md"),
    Path("roadmap/PRAXIS-ROADMAP-v0.1.md"),
    Path("tools/check_project.py"),
    Path("tools/test_check_project.py"),
    Path("tools/requirements.txt"),
    Path(".github/workflows/project-integrity.yml"),
    Path(".agents/skills/response-self-check/SKILL.md"),
    Path(".agents/skills/project-brief/SKILL.md"),
]

CURRENT_CONCEPT = "product/PRAXIS-BRIEF-v0.1.md"
MARKDOWN = MarkdownIt("commonmark")
EXCLUDED_DIRS = {".git", ".codex", ".venv", "__pycache__"}


def text_files() -> list[Path]:
    files: list[Path] = []
    for directory, dirs, names in os.walk(ROOT):
        dirs[:] = sorted(name for name in dirs if name not in EXCLUDED_DIRS)
        for name in sorted(names):
            path = Path(directory) / name
            if path.is_file() and path.suffix.lower() in {".md", ".py", ".yml", ".yaml", ".txt", ".json"}:
                files.append(path)
    return files


def markdown_targets(tokens):
    for token in tokens:
        attribute = {"link_open": "href", "image": "src"}.get(token.type)
        if attribute:
            target = token.attrGet(attribute)
            if target:
                yield target
        if token.children:
            yield from markdown_targets(token.children)


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required carrier: {rel}")


def check_adapters(errors: list[str]) -> None:
    agents = ROOT / "AGENTS.md"
    claude = ROOT / "CLAUDE.md"
    if not agents.is_file() or not claude.is_file():
        return
    a = agents.read_text(encoding="utf-8")
    c = claude.read_text(encoding="utf-8")
    if a != c:
        errors.append("AGENTS.md and CLAUDE.md diverged; adapters must remain identical thin pointers")
    for required_pointer in ("roles/FOUNDER-COPILOT.md", "README.md"):
        if required_pointer not in a:
            errors.append(f"agent adapters do not point to {required_pointer}")
    if len(a.splitlines()) > 12:
        errors.append("agent adapters are no longer thin pointers (more than 12 lines)")


def check_internal_markdown_links(errors: list[str]) -> None:
    for path in text_files():
        if path.suffix.lower() != ".md":
            continue
        content = path.read_text(encoding="utf-8")
        for target in markdown_targets(MARKDOWN.parse(content)):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"broken internal link in {path.relative_to(ROOT)} -> {target}")


def check_current_concept_pointer(errors: list[str]) -> None:
    readme = ROOT / "README.md"
    if not readme.is_file():
        return
    if CURRENT_CONCEPT not in readme.read_text(encoding="utf-8"):
        errors.append(f"README does not point to current concept: {CURRENT_CONCEPT}")


def check_single_role_contract(errors: list[str]) -> None:
    role_dir = ROOT / "roles"
    if not role_dir.exists():
        return
    matches = [p for p in role_dir.glob("*FOUNDER*COPILOT*.md") if p.is_file()]
    if len(matches) != 1 or matches[0].name != "FOUNDER-COPILOT.md":
        names = ", ".join(p.name for p in matches) or "none"
        errors.append(f"expected exactly one Founder Co-Pilot contract; found: {names}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_adapters(errors)
    check_internal_markdown_links(errors)
    check_current_concept_pointer(errors)
    check_single_role_contract(errors)

    if errors:
        print("PRAXIS project integrity: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PRAXIS project integrity: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
