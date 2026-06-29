const INSPECTION_FORMS_PROMISE = frappe.call({
	method: 'quality_itagksa.quality_itag_ksa.api.shared.get_inspection_forms',
	no_spinner: true,
}).then((r) => r.message || []);


frappe.ui.form.on('Job Card', {
	onload(frm) {
		INSPECTION_FORMS_PROMISE.then((forms) => apply_inspection_form_options(frm, forms));
	},

	refresh(frm) {
		window.quality_itagksa.filter_quality_connections(frm);
	},

	custom_start_inspection(frm) {
		if (!frm.doc.custom_inspection_form) {
			frappe.msgprint(__('Please select an Inspection Form first.'));
			return;
		}

		const proceed = () => {
			frappe.call({
				method: 'quality_itagksa.quality_itag_ksa.api.job_card.start_jc_inspection',
				args: {
					job_card: frm.doc.name,
					inspection_form: frm.doc.custom_inspection_form,
				},
				freeze: true,
				freeze_message: __('Creating inspection report...'),
				callback(r) {
					if (r.message) {
						frappe.set_route('Form', r.message.doctype, r.message.name);
					}
				},
			});
		};

		if (frm.is_new() || frm.is_dirty()) {
			frm.save().then(proceed);
			return;
		}
		proceed();
	},
});


function apply_inspection_form_options(frm, forms) {
	if (!forms.length) return;
	const ctrl = frm.fields_dict.custom_inspection_form;
	if (!ctrl) return;
	ctrl.df.options = forms;
	if (ctrl.set_data) {
		ctrl.set_data(forms);
	}
}
