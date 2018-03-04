// Copyright (c) 2018, Lewin Villar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Resultado', {
	"refresh" : (frm) => {
		frm.add_fetch("consulta", "medico", "medico");
		frm.add_fetch("consulta", "institucion", "institucion");
		frm.add_fetch("consulta", "customer", "paciente");
		frm.set_query("consulta", () => {
			return {
				"filters": {
					"tipo_de_factura" : "Consulta Privada",
					"docstatus" : 1 
				}
			}	
		});
	}
});
