# Copyright (c) 2023, Ami and Contributors
# See license.txt

import frappe
import unittest
import frappe.utils
from frappe.tests.utils import FrappeTestCase

test_records = frappe.get_test_records("Employee Management")


class TestEmployeeManagement(FrappeTestCase):
	def test_employee_management(self):
		emp1 = make_employee_management("Pooja")
		emp1_doc = frappe.get_doc("Employee Management", emp1)
		emp1_doc.save()
		emp1_doc.reload()

	def tearDown(self):
		frappe.db.rollback()
 
def make_employee_management(name, **kwargs):
	if not frappe.db.get_value("Employee Management"):
		employee_management = frappe.get_doc(
			{
				"doctype": "Employee Management",
				"first_name": name,
				"middle_name": "F",
				"last_name": "Dave",
				"gender": "Female",
				"date_of_birth": "2000-08-15",
				"salutation": "Miss"
			}
		)
		if kwargs:
			employee_management.update(kwargs)
		employee_management.insert()
		return employee_management
	else:
		frappe.db.set_value("Employee Management")
		return frappe.db.get_value("Employee Management")
