import frappe

from frappe.model.naming import make_autoname

def autoname(self, event):
	series = "CP-.#####" if self.tipo_de_factura == "Consulta Privados" else "CS-.#####" if self.tipo_de_factura == "Consulta Seguro" else "PR-.#####"
	self.name = make_autoname(series)
	self.ncf = make_autoname(self.naming_series)

def on_submit(self, event):
	pass
	# for item in self.items:
	# 	for name in (item.paid_sales_invoices or "").split(","):
	# 		if not name: return 
			
	# 		doc = frappe.get_doc("Sales Invoice", name)
	# 		# update payment_status [PAID|PARTIALLY PAID|UNPAID]
	# 		doc.payment_status = "PAID"

	# 		doc.db_update()
			
	# frappe.db.commit()

def on_cancel(self, event):
	pass
	# for item in self.items:
	# 	for name in (item.paid_sales_invoices or "").split(","):
	# 		if not name: return 

	# 		doc = frappe.get_doc("Sales Invoice", name)
	# 		# update payment_status [PAID|PARTIALLY PAID|UNPAID]
	# 		doc.payment_status = "UNPAID"

	# 		doc.db_update()

	# frappe.db.commit()

