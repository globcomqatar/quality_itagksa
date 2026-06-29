### Quality ITAG KSA

Quality Module Custom Development for ITAG KSA


## Changelog

> Every push to GitHub must bump `__version__` in `quality_itagksa/__init__.py` and add an entry here. See `CLAUDE.md`.

### 15.0.1 — 2026-06-29
- Initial port of Quality Module from `quality_itagqatar` (re-namespaced for KSA).

## Ported Contents

Ported from `quality_itagqatar` (re-namespaced for KSA). Tracked under feature **f001 — Port Qatar Quality Module to KSA**.

### DocTypes (13) — 6 inspection reports + 7 child tables

| Inspection Report (parent) | Child table(s) |
|---|---|
| Assembly Traceability Record | Assembly Traceability Record Details |
| Certificate of Conformity | Certificate of Conformity Details |
| Dimensional Inspection Report | Dimensional Inspection Details |
| Final Machining Visual Examination Report | Final Machining Visual Examination Report Details |
| QC Material Release Note | QC Material Release Note Details |
| Visual Examination Report | Visual Examination Details, Inspection Evidence Attachment |

### Ported components (f001)

- `c01` reference-retarget — Qatar → KSA references (module, import paths, hooks, fixture tags).
- `c02` doctypes — the 13 DocTypes above (controllers are thin stubs; logic in service layer).
- `c03` fixtures — `custom_field.json` + `property_setter.json` on Stock Entry, Purchase Receipt, Quality Inspection, Job Card.
- `c04` inspection service layer — `inspection/` dispatcher, QI bridge, report factory, dashboard links (JC → QI → report flow).
- `c05` quality-verification gate — `services/quality_verification.py` submit-gate for Stock Entry + Purchase Receipt.
- `c06` api/job-card — `api/job_card.py:start_jc_inspection` + `api/shared.py` (inspection forms / linked reports).
- `c07` client scripts — `public/js`: job_card, quality_inspection, inspection_report_common, quality_connections.
- `c08` hooks wiring — `doctype_js`, dashboards override, `doc_events` (SE + PR), fixtures filtered by module.

**Plus:** `patches/v1_0/create_quality_verifier_role.py` — creates the `Quality Verifier` role (post_model_sync, idempotent).

**Excluded by decision:** prefill engine (f006) and Qatar `tests/` dir.

### License

mit
