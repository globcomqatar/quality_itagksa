import frappe
from frappe import _

from quality_itagksa.quality_itag_ksa.inspection import dispatcher
from quality_itagksa.quality_itag_ksa.inspection.constants import INSPECTION_FORMS


@frappe.whitelist()
def start_jc_inspection(job_card, inspection_form):
    if not job_card or not inspection_form:
        frappe.throw(_("Job Card and Inspection Form are required"))
    if inspection_form not in INSPECTION_FORMS:
        frappe.throw(_("Invalid inspection form: {0}").format(inspection_form))
    return dispatcher.start_inspection(job_card, inspection_form)
