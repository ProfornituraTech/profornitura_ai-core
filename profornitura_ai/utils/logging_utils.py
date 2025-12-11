import frappe

def log_info(message, ref_doctype=None, ref_name=None):
    frappe.logger().info(message)

def log_error(message, ref_doctype=None, ref_name=None):
    frappe.logger().error(message)
