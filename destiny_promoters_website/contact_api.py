# import frappe

# @frappe.whitelist(allow_guest=True)
# def send_suggestion():
#     """Save suggestion and send email"""
#     data = frappe.local.form_dict

#     name = data.get("name")
#     email = data.get("email")
#     contact = data.get("contact")
#     subject = data.get("subject")
#     message = data.get("message")

#     # Save in Suggestion DocType
#     doc = frappe.get_doc({
#         "doctype": "Suggestion",
#         "name1": name,
#         "email": email,
#         "contact_number": contact,
#         "subject": subject,
#         "message": message
#     })
#     doc.insert(ignore_permissions=True)
#     frappe.db.commit()

#     # Send email
#     frappe.sendmail(
#         recipients=["wequantumberg@gmail.com"],   # receiver = your inbox
#         sender="wequantumberg@gmail.com",         # must match your Email Account
#         reply_to=email,                           # user’s email for replies
#         subject=f"Suggestion from {name}: {subject or '-'}",
#         message=f"""
#             <b>Name:</b> {name}<br>
#             <b>Email:</b> {email}<br>
#             <b>Contact:</b> {contact}<br>
#             <b>Message:</b> {message or '-'}
#         """
#     )

#     return {"status": "success", "message": "Suggestion submitted successfully!"}


# import frappe

# @frappe.whitelist(allow_guest=True)
# def send_suggestion(name, email, contact, subject, message):
#     try:
#         # Receiver (fixed email)
#         receiver = "wequantumberg@gmail.com"

#         # Email content
#         email_subject = f"Suggestion from {name}: {subject}"
#         email_message = f"""
#         <b>Name:</b> {name}<br>
#         <b>Email:</b> {email}<br>
#         <b>Contact:</b> {contact}<br><br>
#         <b>Message:</b><br>{message}
#         """

#         frappe.sendmail(
#             recipients=[receiver],            
#             sender=email,                     
#             subject=email_subject,
#             message=email_message,
#             delayed=False
#         )

#         return {"status": "success", "message": "Suggestion submitted successfully!"}
#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), "Contact Us Email Failed")
#         return {"status": "error", "message": str(e)}

import frappe
import json

@frappe.whitelist(allow_guest=True)
def send_suggestion():
    """Save suggestion and send email"""
    data = frappe.local.form_dict

    # If frontend sends JSON, parse it
    if isinstance(data, str):
        data = json.loads(data)

    name = data.get("name")
    email = data.get("email")
    contact = data.get("contact")
    subject = data.get("subject")
    message = data.get("message")

    # Save in Suggestion DocType
    doc = frappe.get_doc({
        "doctype": "Suggestion",
        "name1": name,
        "email": email,
        "contact_number": contact,
        "subject": subject,
        "message": message
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    # Send email
    frappe.sendmail(
        recipients=["wequantumberg@gmail.com"],   # ✅ your inbox
        sender="wequantumberg@gmail.com",         # ✅ must match Email Account login_id
        reply_to=email,                           # ✅ user email for replies
        subject=f"Suggestion from {name}: {subject or '-'}",
        message=f"""
            <b>Name:</b> {name}<br>
            <b>Email:</b> {email}<br>
            <b>Contact:</b> {contact}<br>
            <b>Message:</b> {message or '-'}
        """,
        delayed=False   # ✅ force send now
    )

    return {"status": "success", "message": "Suggestion submitted successfully!"}

