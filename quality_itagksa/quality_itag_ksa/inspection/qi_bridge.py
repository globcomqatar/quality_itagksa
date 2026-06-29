import frappe
from frappe import _


def create_qi_for_jc(jc, inspection_form):
    """Create a Draft Quality Inspection for a Job Card.

    QI stays in Draft. It is only submitted when the linked inspection report
    (e.g. Dimensional Inspection Report) is submitted — see submit_linked_qi.
    """
    qi = frappe.get_doc({
        "doctype": "Quality Inspection",
        "reference_type": "Job Card",
        "reference_name": jc.name,
        "item_code": jc.production_item,
        "inspection_type": "In Process",
        "status": "Accepted",
        "manual_inspection": 1,
        "inspected_by": frappe.session.user,
        "sample_size": 1,
    })
    qi.insert()
    return qi.name
