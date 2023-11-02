// Copyright (c) 2023, citrus and contributors
// For license information, please see license.txt

frappe.ui.form.on("Pre-Approval", {
"eta_at_vendor":function(frm) {
var date_diff = frappe.datetime.get_day_diff(frm.doc.eta_at_vendor,frappe.datetime.nowdate());
cur_frm.set_value("days_until_eta",date_diff);
},
"vendor_name":function(frm){
    vendor_number =frappe.get_value('Vendor',2,'vendor_number');
    cur_frm.set_value("vendor_number",vendor_number);
    }
});
