"""Additive dashboard override for Quality Inspection.

Appends a Quality Forms transactions group listing the 6 inspection report
doctypes. The shared client filter (public/js/quality_connections.js) narrows
this to the single report actually linked to the current QI.

Reports link back via their `quality_inspection` Link field; that fieldname is
set as the dashboard default because Quality Inspection has no upstream
`*_dashboard.py`, so `data["fieldname"]` would otherwise be None and Frappe's
`get_external_links` would return zero counts.
"""

from frappe import _

from quality_itagksa.quality_itag_ksa.inspection.constants import INSPECTION_FORMS


def get_dashboard_data(data):
    data = data or {}
    data.setdefault("transactions", [])
    if not data.get("fieldname"):
        data["fieldname"] = "quality_inspection"

    data["transactions"].append({
        "label": _("Quality Inspection"),
        "items": list(INSPECTION_FORMS),
    })

    return data
