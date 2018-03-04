frappe.ui.form.on("Medico", {
	"refresh": (frm) => {
		console.log("Done");
	},
	"nombre_completo": (frm) => {
		frm.set_value("nombre_completo", frm.doc.nombre_completo.trim().toUpperCase());
	},
	"especialidad": (frm) => {
		frm.set_value("especialidad", frm.doc.especialidad.trim().toUpperCase());
	},
	"centro": (frm) => {
		frm.set_value("centro", frm.doc.centro.trim().toUpperCase());
	}


});


frappe.ui.form.on("Telefono", {
	"telefono": (frm, cdt, cdn) => {
		row = frappe.get_doc(cdt, cdn);
		frappe.model.set_value(cdt, cdn, "telefono", mask_phone(row.telefono));
	},
	"tipo": (frm, cdt, cdn) => {
		row = frappe.get_doc(cdt, cdn);
		frappe.model.set_value(cdt, cdn, "tipo", mask_phone(row.tipo));
	}	
});