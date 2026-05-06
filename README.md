# RADSuite Sales Demo

This repository contains the `Sales` channel demo for RADSuite.

## Demo Goal
Show how a Gemini agent can operate like a department-specific teammate when given:
- repo-local instructions in `GEMINI.md`
- scoped tool settings in `.gemini/settings.json`
- runnable scripts in `.rad/tools/`
- sample inputs in `samples/`
- workflow docs in `docs/` and `workflows/`

## Systems In Scope
- HubSpot CRM

## Suggested Demo Flow
1. Launch the agent in this repo.
2. Ask it to inspect `GEMINI.md`, `.gemini/settings.json`, and `samples/`.
3. Give it the live task from `docs/demo-script.md`.
4. Let it use `.rad/tools/build_account_brief.py` if appropriate.
5. Review the output as a department-specific workflow artifact.

## Key Files
- `GEMINI.md`
- `.gemini/settings.json`
- `.rad/tools/build_account_brief.py`
- `docs/demo-script.md`
- `docs/channel-design.md`
- `docs/integration-notes.md`
- `samples/`
- `workflows/`
