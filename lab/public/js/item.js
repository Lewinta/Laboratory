frappe.ui.form.on("Item",{
	refresh: function(frm){
		frm.set_query("item_group", function() {
			return {
				"filters": {
					"parent_item_group": "Tipos de Pruebas"
				}
			}
		
		});
	},
	// onload_post_render: function(frm){
	// 	// I just don't need this field to be available for the user
	// 	frm.set_df_property("naming_series", "hidden", 1, frm.doc.docname)
		
	// 	if(frm.is_new())
	// 		frm.set_value("naming_series","PRB-")
	// }
});