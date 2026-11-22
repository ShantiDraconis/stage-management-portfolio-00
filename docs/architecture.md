# Reference operating architecture — show-operations

**Illustrative system, not a ship's actual network.**

```mermaid
flowchart LR
 A[Show requirement] --> B[Readiness checklist]
 B --> C[System and asset register]
 C --> D{Test passed?}
 D -->|Yes| E[Authorized show operation]
 D -->|No| F[Fault ticket and escalation]
 F --> G[Controlled repair and retest]
 G --> D
 E --> H[Handover and KPI review]
```

System boundaries: operations data, physical equipment, show control and organizational approval. No vessel IP addresses, access topology or proprietary configurations are represented.
