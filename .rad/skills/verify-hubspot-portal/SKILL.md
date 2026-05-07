---
name: verify-hubspot-portal
description: Verify HubSpot private app token access against a CRM endpoint.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - HUBSPOT_ACCESS_TOKEN
        - HUBSPOT_PORTAL_ID
      bins:
        - python3
    primaryEnv: HUBSPOT_ACCESS_TOKEN
---

# verify-hubspot-portal

Verify HubSpot private app token access against a CRM endpoint.

## Invocation
This skill is discovered from `.rad/skills/verify-hubspot-portal/SKILL.md` and executed via the shared Gemini tool bridge in `~/.gemini/tools/`.

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
