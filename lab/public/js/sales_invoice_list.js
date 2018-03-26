frappe.provide("lab.sinv");
$.extend(frappe.listview_settings["Sales Invoice"], {
	"post_render": function(list) {
		var options = list.page.fields_dict.customer_group.$input.children();

		if (options.length > 2) 
		{
			list.page.fields_dict.customer_group.$input.empty();
			list.page.fields_dict.customer_group.$input.add_options(["Consulta Privada", "Consulta Seguro", "Proveedores"]);
		}

		lab.sinv.set_customer_query(list);
	}
});

$.extend(lab.sinv, {
	"set_customer_query": function(list) {
		var customer_group = list.page.fields_dict.customer_group.value;

		list.page.fields_dict.customer.df.get_query = function() {
			return {
				"query": "lab.queries.customer_query",
				"filters": {
					"tipo_de_factura": customer_group
				}
			}
		}
	}
});