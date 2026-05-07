#!/usr/bin/env python3
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[3]
accounts = list(csv.DictReader((root / 'samples' / 'target_accounts.csv').read_text().splitlines()))
top = next((row for row in accounts if row['priority'] == 'high'), accounts[0])

print('Sales Account Brief')
print('===================')
print()
print(f"Account: {top['account_name']}")
print(f"Industry: {top['industry']}")
print(f"Notes: {top['notes']}")
print()
print('Outreach Sequence:')
print('1. Intro email focused on fit and relevance')
print('2. Follow-up with a short proof point and meeting ask')
print('3. Final touch with a concise value summary')
print()
print('CRM Notes:')
print('- Priority: high')
print('- Suggested angle: rewarded video demand fit')
