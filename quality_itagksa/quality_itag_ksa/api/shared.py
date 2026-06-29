import frappe

from quality_itagksa.quality_itag_ksa.inspection.constants import INSPECTION_FORMS
from quality_itagksa.quality_itag_ksa.inspection.dashboard_links import (
	get_linked_report_doctypes,
)


@frappe.whitelist()
def get_inspection_forms() -> list[str]:
	return list(INSPECTION_FORMS)


@frappe.whitelist()
def get_linked_inspection_reports(reference_doctype: str, reference_name: str) -> list[str]:
	return get_linked_report_doctypes(reference_doctype, reference_name)
