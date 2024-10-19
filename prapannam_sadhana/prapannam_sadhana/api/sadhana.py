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
    
# API that creates Sadhana Log record for given date, user and group. then creates sadhana log items for that newly created Sadhana Log
@frappe.whitelist()
def create_sadhana_log_and_items():
    #Get parameters from the POST request's form data
    params = frappe.form_dict
    current_user = frappe.session.user
    # check if the user is a member of the given group
    #TODO
    print(f"User is {current_user}")
    #Create Sadhana Log
    sadhana_log_record = frappe.get_doc({
        "doctype": "Sadhana Log", 
        "date": params.get('date'), 
        "by": current_user, 
        "group": params.get('group')
        })
    sadhana_log_record.insert()
    print(f"sadhana log record {sadhana_log_record}")
    
    # Create Sadhana Log Items
    if sadhana_log_record:
        sadhana_log_item = frappe.get_doc({
            "doctype": "Sadhana Log Item", 
            "sadhana_type": params.get('sadhana_type'),
            "qty": params.get('qty'),
            "parent": sadhana_log_record.name,
            "parentfield": "log_items",
            "parenttype": "Sadhana Log"
            })
        if sadhana_log_item:
            print(f"sadhana log item {sadhana_log_item}")
            sadhana_log_item.insert()
            return {
                "status": "ok", 
                "message": "Sadhana Log and Sadhana Log Items created successfully",
                "sadhana_log": sadhana_log_record,
                "sadhana_log_items": sadhana_log_item
                }
        else:
            return {
                 "status":  "failed", 
                 "message":  "Sadhana Log Item creation failed"
                 }
    else: 
        return {
             "status":  "failed", 
             "message":  "Sadhana Log creation failed"
             }
    

    

