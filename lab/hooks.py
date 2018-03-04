# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lab"
app_title = "Laboratory"
app_publisher = "Lewin Villar"
app_description = "Application for a clinic laboratory"
app_icon = "fa fa-flask"
app_color = "#469"
app_email = "lab_appl@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/lab/css/lab.css"
app_include_js = "/assets/lab/js/lab.js"

# include js, css files in header of web template
# web_include_css = "/assets/lab/css/lab.css"
# web_include_js = "/assets/lab/js/lab.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Customer" : "public/js/customer.js",
	"Item" : "public/js/item.js",
	"Sales Invoice" : "public/js/sales_invoice.js"
}

doctype_list_js = {
	"Customer" : "public/js/customer_list.js",
	"Sales Invoice" : "public/js/sales_invoice_list.js",
	"Medico" : "public/js/medico.js"
	# "Account" : "public/js/account.js",
	# "Custom Script" : "public/js/custom_script.js",
	# "Item" : "public/js/item.js",
	# "Supplier" : "public/js/supplier.js"

}

# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "lab.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lab.install.before_install"
# after_install = "lab.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lab.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"autoname": "lab.sales_invoice.autoname",
		"on_submit": "lab.sales_invoice.on_submit",
		"on_cancel": "lab.sales_invoice.on_cancel",
	},
	"Customer": {
		"after_insert": "lab.customer.after_insert",
		"on_trash": "lab.customer.on_trash"
	},
	"Medico": {
		"after_insert": "lab.medico.after_insert",
		"on_trash": "lab.medico.on_trash"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lab.tasks.all"
# 	],
# 	"daily": [
# 		"lab.tasks.daily"
# 	],
# 	"hourly": [
# 		"lab.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lab.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lab.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lab.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lab.event.get_events"
# }
boot_session = "lab.boot.boot_session"
