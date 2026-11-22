# Data dictionary and privacy rules

All rows in `examples/` are **synthetic examples**. No actual employer, ship, person, serial number or proprietary cue file is included.

- `asset_id`: pseudonymous equipment identifier, not a serial number
- `venue_alias`: fictional identifier
- `severity`: P1 safety/show-stop; P2 degraded show; P3 planned repair
- `status`: OPEN, IN_PROGRESS, BLOCKED, VERIFIED, CLOSED
- `reported_at`, `due_at`: ISO-8601 dates or timestamps
- `owner_role`: function, not a named individual
- `evidence_ref`: safe reference to approved/redacted evidence

**No secrets, private incident narratives, real ship schematics, access details, staff names, passenger data or employer documents.**
