# Based on onlyoffice_odoo by Ascensio System SIA (ONLYOFFICE)
# Rebranded for Euro-Office by bring.out d.o.o.
# (c) Copyright Ascensio System SIA 2024 - original eurooffice_odoo_documents
# Copyright 2026 bring.out d.o.o. - OCA DMS adaptation
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
# Based on eurooffice_odoo_documents by Euro-Office (LGPL-3):
#   https://github.com/Euro-Office/eurooffice_odoo/tree/16.0/eurooffice_odoo_documents
# The original module depends on Odoo Enterprise 'documents' module.
# This adaptation replaces that dependency with OCA DMS (dms),
# the open-source Document Management System from the Odoo Community Association.
{
    "name": "Euro-Office DMS",
    "summary": "Edit and collaborate on office files within OCA DMS.",
    "description": """
        Based on eurooffice_odoo_documents by Euro-Office (Ascensio System SIA).

        This module adapts the original Euro-Office Documents integration to work
        with OCA DMS (dms) instead of the proprietary Odoo Enterprise 'documents'
        module. It provides the same functionality: edit and collaborate on office
        files stored in OCA Document Management System using Euro-Office/Euro-Office
        Docs, with real-time co-editing support.

        Original: https://github.com/Euro-Office/eurooffice_odoo
    """,
    "author": "Euro-Office, bring.out d.o.o.",
    "website": "https://www.bring.out.ba",
    "category": "Document Management",
    "version": "16.0.1.0.0",
    "depends": ["eurooffice_odoo", "dms"],
    "external_dependencies": {"python": ["pyjwt"]},
    "data": [
        "security/ir.model.access.csv",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "assets": {
        "web.assets_backend": [
            "eurooffice_odoo_oca_dms/static/src/dms_view/**/*",
            "eurooffice_odoo_oca_dms/static/src/components/*/*.xml",
        ],
    },
}
