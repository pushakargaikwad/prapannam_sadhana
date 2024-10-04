# Copyright (c) 2024, Pushakar Gaikwad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SadhanaLog(Document):
	
	def before_save(self):
		self.validate_log_entry_doesnt_exist()
		self.validate_user_is_member_of_group()

	def validate_log_entry_doesnt_exist(self):
		# check if entry already exists for given date for given user
		existing_entry = frappe.db.exists("Sadhana Log", {
			"by": self.by,
			"date": self.date,
			"group": self.group
		},)
		if existing_entry:
			frappe.throw("Entry already exists for given user for this date")

	# check if user is member of the group 
	# TODO: optimize this
	def validate_user_is_member_of_group(self):
		group = frappe.get_doc("Sadhana Group", self.group)

		for member in group.members:
			if member.user == self.by:
				return
			
		frappe.throw(f"User {self.by} is not a member of {self.group}")
		
