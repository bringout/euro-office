import json

from odoo import api, models

from odoo.addons.eurooffice_odoo.utils import config_constants


class EuroOfficeTemplate(models.Model):
    _name = "eurooffice.odoo"
    _description = "Euro-Office"

    @api.model
    def get_demo(self):
        mode = self.env["ir.config_parameter"].sudo().get_param(config_constants.DOC_SERVER_DEMO)
        date = self.env["ir.config_parameter"].sudo().get_param(config_constants.DOC_SERVER_DEMO_DATE)
        return json.dumps({"mode": mode, "date": date})

    @api.model
    def get_same_tab(self):
        same_tab = self.env["ir.config_parameter"].sudo().get_param(config_constants.SAME_TAB)
        return json.dumps({"same_tab": same_tab})
