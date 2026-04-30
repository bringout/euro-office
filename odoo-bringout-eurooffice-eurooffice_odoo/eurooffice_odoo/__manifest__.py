# Based on onlyoffice_odoo by Ascensio System SIA (ONLYOFFICE)
# Adapted and rebranded for Euro-Office by bring.out d.o.o.
# pylint: disable=pointless-statement
{
    "name": "Euro-Office",
    "summary": "Edit and collaborate on office files within Odoo Documents.",
    "description": "The Euro-Office app allows users to edit and collaborate on office files within Odoo Documents using Euro-Office Docs. You can work with text documents, spreadsheets, and presentations, co-author documents in real time using two co-editing modes (Fast and Strict), Track Changes, comments, and built-in chat.",  # noqa: E501
    "author": "Euro-Office",
    "website": "https://github.com/Euro-Office/eurooffice_odoo",
    "category": "Productivity",
    "version": "19.0.6.3.0",
    "depends": ["base", "mail"],
    "external_dependencies": {"python": ["pyjwt"]},
    # always loaded
    "data": [
        "views/templates.xml",
        "views/res_config_settings_views.xml",
    ],
    "license": "LGPL-3",
    "support": "support@eurooffice.com",
    "images": [
        "static/description/main_screenshot.png",
        "static/description/document.png",
        "static/description/sales_section.png",
        "static/description/discuss_section.png",
        "static/description/settings.png",
    ],
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "eurooffice_odoo/static/src/actions/*",
            "eurooffice_odoo/static/src/components/*/*.xml",
            "eurooffice_odoo/static/src/models/*.js",
            "eurooffice_odoo/static/src/views/**/*",
            "eurooffice_odoo/static/src/css/*",
        ],
    },
}
