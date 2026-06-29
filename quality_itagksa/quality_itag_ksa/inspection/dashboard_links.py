"""Resolve which inspection report doctypes are linked to a parent record.

Each of the 6 report doctypes (see ``INSPECTION_FORMS``) carries a back-link
field that points at the source record. The fieldname differs by source type;
this module centralizes the dispatch so callers do not need to know it.
"""

import frappe

from quality_itagksa.quality_itag_ksa.inspection.constants import INSPECTION_FORMS

_LINK_FIELD_BY_REFERENCE = {
    "Job Card": "job_card",
    "Quality Inspection": "quality_inspection",
}


def get_linked_report_doctypes(reference_doctype, reference_name):
    link_field = _LINK_FIELD_BY_REFERENCE.get(reference_doctype)
    if not link_field or not reference_name:
        return []

    linked = []
    for dt in INSPECTION_FORMS:
        if frappe.db.exists(dt, {link_field: reference_name, "docstatus": ["<", 2]}):
            linked.append(dt)
    return linked
