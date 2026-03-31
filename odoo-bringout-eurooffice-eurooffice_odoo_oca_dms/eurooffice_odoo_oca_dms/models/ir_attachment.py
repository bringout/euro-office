# (c) Copyright Ascensio System SIA 2024
# Copyright 2026 bring.out d.o.o.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# Adapted from eurooffice_odoo_documents for OCA DMS

from odoo import fields, models


class Attachment(models.Model):
    _inherit = "ir.attachment"
    oo_attachment_version = fields.Integer(default=1)
