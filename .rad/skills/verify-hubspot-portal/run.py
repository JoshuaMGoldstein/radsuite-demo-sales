#!/usr/bin/env python3
from pathlib import Path
import json
import os
import urllib.request
import urllib.error
import urllib.parse

root = Path(__file__).resolve().parents[3]

def load_env_file(path: Path):
    if not path.exists():
        return
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip())

load_env_file(root / '.rad' / 'secrets' / '.env')
load_env_file(root / '.env')

token = os.getenv('HUBSPOT_ACCESS_TOKEN') or os.getenv('HUBSPOT_SERVICE_KEY')
portal_id = os.getenv('HUBSPOT_PORTAL_ID')

if not token:
    raise SystemExit('Missing HUBSPOT_ACCESS_TOKEN or HUBSPOT_SERVICE_KEY')
if not portal_id:
    raise SystemExit('Missing HUBSPOT_PORTAL_ID')

base = 'https://api.hubapi.com/crm/v3/objects/companies'
query = urllib.parse.urlencode({'limit': 1, 'properties': 'name'})
url = f'{base}?{query}'
req = urllib.request.Request(
    url,
    headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req, timeout=20) as response:
        payload = json.loads(response.read().decode('utf-8'))
except urllib.error.HTTPError as exc:
    body = exc.read().decode('utf-8', errors='replace')
    print(body)
    raise SystemExit(f'HubSpot verification failed with HTTP {exc.code}')

results = payload.get('results', [])
company_preview = None
if results:
    props = results[0].get('properties', {})
    company_preview = props.get('name')

print(json.dumps({
    'configuredPortalId': portal_id,
    'tokenAccepted': True,
    'sampleCompanyName': company_preview,
    'resultCount': len(results),
    'note': 'Private app token verified against HubSpot CRM companies endpoint. Portal ID remains a configured value for demo context.'
}, indent=2))
