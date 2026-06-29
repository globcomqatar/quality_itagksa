const INSPECTION_REPORT_DOCTYPES = [
	'Assembly Traceability Record',
	'Certificate of Conformity',
	'Dimensional Inspection Report',
	'Final Machining Visual Examination Report',
	'QC Material Release Note',
	'Visual Examination Report',
];

INSPECTION_REPORT_DOCTYPES.forEach(function (doctype) {
	frappe.ui.form.on(doctype, {
		on_submit(frm) {
			if (!frm.doc.quality_inspection) return;
			frappe.show_alert({
				message: __('Opening Quality Inspection {0}', [frm.doc.quality_inspection]),
				indicator: 'green',
			}, 3);
			frappe.model.clear_doc('Quality Inspection', frm.doc.quality_inspection);
			frappe.set_route('Form', 'Quality Inspection', frm.doc.quality_inspection);
		},
	});
});
