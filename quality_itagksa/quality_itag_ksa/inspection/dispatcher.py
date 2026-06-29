import frappe
from frappe import _

from quality_itagksa.quality_itag_ksa.inspection import qi_bridge, report_factory


def start_inspection(job_card, inspection_form):
    jc = frappe.get_doc("Job Card", job_card)
    if not jc.has_permission("write"):
        frappe.throw(_("Insufficient permissions on Job Card"))

    qi_name = qi_bridge.create_qi_for_jc(jc, inspection_form)
    return report_factory.create_report(inspection_form, qi_name)
