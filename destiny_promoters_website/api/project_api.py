import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_projects():
    projects = frappe.get_all(
        "Real Estate Project",
        fields=[
            "name",
            "project_name",
            "heading_project_location",
            "status",
            "project_location",
            "heading_project_area",
            "project_area",
            "builder",
            "super_built_up_area",
            "project_type",
            "floors",
            "bath",
            "bhk",
            "full_location",
            "heading_first",
            "description",
            "thumbnail",
            "owner",
            "creation",
            "modified",
            "modified_by",
            "docstatus",
            "idx"
        ]
    )

    # fetch child tables
    for project in projects:
        project["carousel_images"] = frappe.get_all(
            "Project Carousel Image",
            filters={"parent": project["name"]},
            fields=["name", "image", "parent", "parentfield", "parenttype", "idx"]
        )
        project["gallery_images"] = frappe.get_all(
            "Project Gallery Image",
            filters={"parent": project["name"]},
            fields=["name", "image", "parent", "parentfield", "parenttype", "idx"]
        )

    return projects
