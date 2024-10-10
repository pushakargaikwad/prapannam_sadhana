import frappe

# test ping
@frappe.whitelist()
def test_ping():
    current_user = frappe.session.user
    
    return {
        "status": "ok!",
        "user": current_user,
        "message": "pong",
    }

# get sadhana by date

@frappe.whitelist()
def get_sadhana_by_date(date):
    sadhana_list = frappe.db.get_list("Sadhana Log",
                                      filters={
                                          "date": date,
                                          "by": frappe.session.user
                                      },
                                      fields=["*"])
    
    if not sadhana_list:
        return {
            "status": "failed",
            "message": "No Sadhana found for the given date"
        }
    else:
        return {
            "status": "ok",
            "message": "Sadhana found",
            "sadhana_list": sadhana_list
        }

@frappe.whitelist()
def get_sadhana_log_items(sadhana_log):
    sadhana_log_items = frappe.db.get_all("Sadhana Log Item",
                                          filters={
                                              "parent": sadhana_log
                                          },
                                          fields=["*"])
    
    if not sadhana_log_items:
        return {
            "status": "failed",
            "message": "No Sadhana Log Items found for the given Sadhana Log"
        }
    else:
        return {
            "status": "ok",
            "message": "Sadhana Log Items found",
            "sadhana_log_items": sadhana_log_items
        }
