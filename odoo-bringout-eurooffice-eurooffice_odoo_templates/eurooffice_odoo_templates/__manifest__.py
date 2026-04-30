# Based on onlyoffice_odoo by Ascensio System SIA (ONLYOFFICE)
# Adapted and rebranded for Euro-Office by bring.out d.o.o.
# pylint: disable=pointless-statement
{
    "name": "Euro-Office Templates",
    "summary": "Automate form creation with inserting fields from Odoo in templates.",
    "description": "Work with fillable templates in Odoo using Euro-Office. Create templates based on the data and fields available in Odoo, fill them out and print with several clicks.",  # noqa: E501
    "author": "Euro-Office",
    "website": "https://github.com/Euro-Office/eurooffice_odoo",
    "category": "Productivity",
    "version": "19.0.4.3.2",
    "depends": ["base", "eurooffice_odoo", "web"],
    "external_dependencies": {"python": ["pyjwt"]},
    # always loaded
    "data": [
        "security/eurooffice_templates_security.xml",
        "security/ir.model.access.csv",
        "views/eurooffice_menu_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "demo": ["data/templates_data.xml"],
    "license": "LGPL-3",
    "support": "support@eurooffice.com",
    "images": [
        "static/description/main_screenshot.png",
        "static/description/create_templates.png",
        "static/description/edit_templates.png",
        "static/description/access_rights.png",
        "static/description/work_with_templates.png",
    ],
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "eurooffice_odoo_templates/static/src/css/*",
            "eurooffice_odoo_templates/static/src/views/**/*",
        ],
    },
}
