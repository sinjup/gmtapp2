# Copyright (c) 2023, citrus and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import today


class PreApproval(Document):
	def validate(self):
		if self.year <= 0:
			print("invalid")
			frappe.throw("Not a valid year")

	def on_update(self):
		try:
			if self.boss_approval == 'Declined':
				passed = frappe.new_doc("Pass")
				passed.vehicle_status = self.vehicle_status
				passed.boss_approval = self.boss_approval
				passed.date = today()
				passed.invoice = self.invoice
				passed.vendor_name = self.vendor_name
				passed.vendor_number = self.vendor_number
				passed.buying_entity = self.buying_entity
				passed.vin = self.vin
				passed.eta_at_vendor = self.eta_at_vendor
				passed.days_until_eta = self.days_until_eta
				passed.notes_updates = self.notes_updates
				passed.year = self.year
				passed.make = self.make
				passed.model = self.model
				passed.trim = self.trim
				passed.colour = self.colour
				passed.msrp = self.msrp
				passed.vehicle_cost_vendor = self.vehicle_cost_vendor
				passed.buyer_agent = self.buyer_agent
				passed.row_id = self.row_id
				passed.status = self.status
				passed.confirmed = self.confirmed
				passed.contact_date = today()
				passed.insert()

				
			if self.confirmed == True and self.boss_approval == 'Approved':
				intake = frappe.new_doc("Intake")
				intake.status = self.status
				intake.boss_approval = self.boss_approval
				intake.date = self.date
				intake.invoice = self.invoice
				intake.vendor_name =self.vendor_name
				intake.vendor_number =self.vendor_number
				intake.buying_entity = self.buying_entity
				intake.vin = self.vin
				intake.eta_at_vendor = self.eta_at_vendor
				intake.days_until_eta = self.days_until_eta
				intake.notes_updates = self.notes_updates
				intake.year = self.year
				intake.model =self.model
				intake.make =self.make
				intake.trim =self.trim
				intake.colour = self.colour
				intake.msrp = self.msrp
				intake.vehicle_cost_vendor = self.vehicle_cost_vendor
				intake.buyer_agent = self.buyer_agent
				intake.insert()
			frappe.db.commit()
		except Exception:
			frappe.db.rollback()
			frappe.log_error(frappe.get_traceback())
			frappe.throw("Error in moving record")
