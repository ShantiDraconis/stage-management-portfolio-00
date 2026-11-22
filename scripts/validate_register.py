#!/usr/bin/env python3
"""Standard-library-only validator for synthetic operational CSVs."""
import csv
from pathlib import Path
from datetime import date
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {'ticket_id','venue_alias','asset_id','severity','status','reported_at','due_at','owner_role','symptom','action','evidence_ref'}
VALID_SEVERITIES = {'P1','P2','P3'}
VALID_STATUSES = {'OPEN','IN_PROGRESS','BLOCKED','VERIFIED','CLOSED'}

def main():
    with (ROOT/'examples'/'fault_register.csv').open(newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        assert REQUIRED <= set(reader.fieldnames or []), 'Missing required columns'
        rows=list(reader)
    ids=set()
    for row in rows:
        assert row['ticket_id'] and row['ticket_id'] not in ids, 'Missing/duplicate ticket ID'
        ids.add(row['ticket_id'])
        assert row['severity'] in VALID_SEVERITIES, 'Invalid severity'
        assert row['status'] in VALID_STATUSES, 'Invalid status'
        for field in ('reported_at','due_at'):
            date.fromisoformat(row[field])
        assert row['due_at'] >= row['reported_at'], 'Due date before reported date'
    open_count=sum(row['status'] not in ('CLOSED','VERIFIED') for row in rows)
    print(f'VALID: {len(rows)} synthetic tickets; {open_count} pending; {len(rows)-open_count} verified/closed')

if __name__=='__main__':
    main()
