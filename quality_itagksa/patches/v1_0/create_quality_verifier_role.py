"""Create the "Quality Verifier" role used by the quality verification gate.

The role is referenced by services/quality_verification.py and by the
custom field `depends_on` expressions (frappe.user.has_role("Quality Verifier")),
but no fixture or DocType ships it, so it must be created on migrate.

Idempotent — safe to re-run.
"""

import frappe

ROLE_NAME = "Quality Verifier"


def execute():
    if frappe.db.exists("Role", ROLE_NAME):
        return
    frappe.get_doc({
        "doctype": "Role",
        "role_name": ROLE_NAME,
        "desk_access": 1,
    }).insert(ignore_permissions=True)
    frappe.db.commit()
