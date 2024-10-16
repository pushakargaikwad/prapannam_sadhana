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

@frappe.whitelist()
def get_sadhana_groups():
    # returns the sadhana group for the current user
    current_user = frappe.session.user
    
    sadhana_group_members_list = frappe.db.get_all("Sadhana Group Member",
                                        filters={"user": current_user},
                                          fields=["*"]
                                          )
                                          

    # the parent field in the sadhana_group_members_list is the group Name
    sadhana_groups_list = []
    for sadhana_group_member in sadhana_group_members_list: 
        sadhana_groups_list.append(sadhana_group_member.parent)

    if not sadhana_groups_list:
        return {
            "status": "failed",
            "message": "No Sadhana Groups found for the given user"
            }
            
    else:
        return {
            "status": "ok",
            "message": "Sadhana Groups found",
            "sadhana_groups_list": sadhana_groups_list
        }