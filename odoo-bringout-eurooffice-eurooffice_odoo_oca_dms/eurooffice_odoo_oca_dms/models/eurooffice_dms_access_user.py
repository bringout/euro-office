# (c) Copyright Ascensio System SIA 2024
# Copyright 2026 bring.out d.o.o.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# Adapted from eurooffice_odoo_documents (Euro-Office, LGPL-3)

from odoo import _, fields, models


class EuroofficeDmsAccessUser(models.Model):
    _name = "eurooffice.dms.access.user"
    _description = "Euro-Office DMS Access Users"

    file_id = fields.Many2one("dms.file", required=True, ondelete="cascade")
    user_id = fields.Many2one("res.users", required=True, string="User")
    role = fields.Selection(
        [
            ("none", _("None")),
            ("viewer", _("Viewer")),
            ("commenter", _("Commenter")),
            ("reviewer", _("Reviewer")),
            ("editor", _("Editor")),
            ("form_filling", _("Form Filling")),
            ("custom_filter", _("Custom Filter")),
        ],
        required=True,
        string="Access Level",
    )
