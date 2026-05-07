---
name: build-account-brief
description: Build a sales account brief and outreach sequence from target account samples.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        []
      bins:
        - python3
---

# build-account-brief

Build a sales account brief and outreach sequence from target account samples.

## Invocation
This skill is discovered from `.rad/skills/build-account-brief/SKILL.md` and executed via the shared Gemini tool bridge in `~/.gemini/tools/`.

## Parameters
```json
{
  "type": "object",
  "properties": {
    "args": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Optional positional arguments passed to the skill entrypoint."
    }
  },
  "additionalProperties": false
}
```

## Runtime
- Entrypoint: `run.py`
- Working directory: repository root
- Secrets: `.rad/secrets/.env` injected by the daemon when available
