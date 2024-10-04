# Copyright (c) 2024, Pushakar Gaikwad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SadhanaLog(Document):
	
	def before_save(self):
		self.validate_log_entry_doesnt_exist()

	def validate_log_entry_doesnt_exist(self):
		# check if entry already exists for given date for given user
		existing_entry = frappe.db.exists("Sadhana Log", {
			"by": self.by,
			"date": self.date,
			"group": self.group
		},)
		if existing_entry:
			frappe.throw("Entry already exists for given user for this date")
