import frappe

@frappe.whitelist(allow_guest=True)
def send_suggestion():
    """Save suggestion and send email"""
    data = frappe.form_dict

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
        recipients=["wequantumberg@gmail.com"],
        subject=f"Suggestion from {name}: {subject}",
        message=f"""
            <p><b>Name:</b> {name}</p>
            <p><b>Email:</b> {email}</p>
            <p><b>Contact:</b> {contact}</p>
            <p><b>Message:</b> {message}</p>
        """
    )

    return {"status": "success", "message": "Suggestion submitted successfully!"}
