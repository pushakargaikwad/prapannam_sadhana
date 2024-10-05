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
