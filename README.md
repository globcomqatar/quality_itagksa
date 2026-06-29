### Quality ITAG KSA

Quality Module Custom Development for ITAG KSA

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app quality_itagksa
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/quality_itagksa
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

## Changelog

> Every push to GitHub must bump `__version__` in `quality_itagksa/__init__.py` and add an entry here. See `CLAUDE.md`.

### 15.0.1 — 2026-06-29
- Set version baseline to `15.0.1` (track Frappe/ERPNext v15).

### 0.0.1 — 2026-06-29
- Initial port of Quality Module from `quality_itagqatar` (re-namespaced for KSA).
- Added `Quality Verifier` role patch (`patches/v1_0/create_quality_verifier_role.py`).

### License

mit
