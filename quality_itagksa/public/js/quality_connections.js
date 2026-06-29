// Shared connections-dashboard filter.
//
// The Quality group on Stock Entry / Job Card / Quality Inspection dashboards
// lists every inspection report doctype statically. This filter trims that
// list to only the report(s) that actually have a doc linked to the current
// record, so users see one card per active inspection instead of a wall of
// greyed-out placeholders.
//
// Each form script (stock_entry.js, quality_inspection.js, job_card.js) calls
// quality_itagksa.filter_quality_connections(frm) from its refresh handler.
//
// The canonical list of inspection report doctypes lives in Python at
// quality_itag_ksa/inspection/constants.py (INSPECTION_FORMS) and is fetched
// from get_inspection_forms() on first use; never hardcode it here.

window.quality_itagksa = window.quality_itagksa || {};

let _report_doctypes_cache = null;

async function load_report_doctypes() {
	if (_report_doctypes_cache) return _report_doctypes_cache;
	const r = await frappe.call({
		method: 'quality_itagksa.quality_itag_ksa.api.shared.get_inspection_forms',
	});
	_report_doctypes_cache = (r && r.message) || [];
	return _report_doctypes_cache;
}

window.quality_itagksa.filter_quality_connections = async function (frm) {
	if (!frm || frm.is_new() || !frm.doc || !frm.doc.name) return;

	const [report_dts, linked_r] = await Promise.all([
		load_report_doctypes(),
		frappe.call({
			method: 'quality_itagksa.quality_itag_ksa.api.shared.get_linked_inspection_reports',
			args: { reference_doctype: frm.doctype, reference_name: frm.doc.name },
		}),
	]);
	apply_filter(frm, report_dts, (linked_r && linked_r.message) || []);
};

function apply_filter(frm, report_dts, linked) {
	if (!frm.dashboard || !frm.dashboard.parent) return;

	const $root = $(frm.dashboard.parent);
	$root.find('[data-doctype]').each(function () {
		const dt = $(this).attr('data-doctype');
		if (!report_dts.includes(dt)) return;
		$(this).toggle(linked.includes(dt));
	});
}
