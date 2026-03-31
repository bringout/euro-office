# (c) Copyright Ascensio System SIA 2024
# Copyright 2026 bring.out d.o.o.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# Adapted from eurooffice_odoo_documents for OCA DMS

from odoo import _, fields, models


class EuroofficeDmsAccess(models.Model):
    _name = "eurooffice.dms.access"
    _description = "Euro-Office DMS Access"

    file_id = fields.Many2one("dms.file", required=True, ondelete="cascade")
    internal_users = fields.Selection(
        [
            ("none", _("None")),
            ("viewer", _("Viewer")),
            ("commenter", _("Commenter")),
            ("reviewer", _("Reviewer")),
            ("editor", _("Editor")),
            ("form_filling", _("Form Filling")),
            ("custom_filter", _("Custom Filter")),
        ],
        default="none",
        string="Internal Users Access",
    )
    link_access = fields.Selection(
        [
            ("none", _("None")),
            ("viewer", _("Viewer")),
            ("commenter", _("Commenter")),
            ("reviewer", _("Reviewer")),
            ("editor", _("Editor")),
            ("form_filling", _("Form Filling")),
            ("custom_filter", _("Custom Filter")),
        ],
        default="viewer",
        string="Link Access",
    )
