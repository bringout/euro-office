# (c) Copyright Ascensio System SIA 2024
# Copyright 2026 bring.out d.o.o.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# Adapted from eurooffice_odoo_documents for OCA DMS

from odoo import api, models


class DmsFile(models.Model):
    _inherit = "dms.file"

    @api.depends("content")
    def _compute_thumbnail(self):
        super()._compute_thumbnail()
        for record in self:
            if record.mimetype == "application/pdf":
                record.thumbnail = False
