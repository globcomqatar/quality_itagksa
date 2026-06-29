import frappe
from frappe import _

# Each doctype gates the Quality Verification tab on its own Check field.
# The submit check is scoped to that flag — without it set, the Verification
# Status field is hidden and every document would be blocked by an unfillable field.
QUALITY_GATE_FIELD = {
	"Stock Entry": "custom_inward_inspection_required",
	"Purchase Receipt": "custom_quality_verification_of_purchase",
}

# Item Type values (custom_product_type on Purchase Receipt Item, owned by
# globcom_manufacturing) that force the purchase into quality verification.
PRODUCT_TYPE_FIELD = "custom_product_type"
QUALITY_REQUIRED_PRODUCT_TYPES = {"Critical", "Non-Critical"}


def set_purchase_quality_gate(doc, method=None):
	"""Tick the Quality Verification gate when any item is Critical / Non-Critical."""
	requires_verification = any(
		row.get(PRODUCT_TYPE_FIELD) in QUALITY_REQUIRED_PRODUCT_TYPES for row in doc.items
	)
	if requires_verification:
		doc.custom_quality_verification_of_purchase = 1


def validate_quality_verification(doc, method=None):
	"""Block submission when quality verification is required but no status is recorded."""
	gate_field = QUALITY_GATE_FIELD.get(doc.doctype)
	if gate_field and doc.get(gate_field) and not doc.custom_verification_status:
		frappe.throw(
			_(
				"<b>Action required:</b> Submission cannot be completed until a verification "
				"status is selected in the Quality Verification tab. Quality verification "
				"must be completed by a Quality Verifier prior to submission."
			)
		)
