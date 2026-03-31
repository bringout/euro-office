#
# (c) Copyright Ascensio System SIA 2024 - original eurooffice_odoo_documents
# Copyright 2026 bring.out d.o.o. - OCA DMS adaptation
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
# Based on eurooffice_odoo_documents/controllers/controllers.py
# Adapted to use dms.file instead of documents.document
#

import json
import logging

import requests
from werkzeug.exceptions import Forbidden

from odoo import http
from odoo.exceptions import AccessError
from odoo.http import request
from odoo.tools.translate import _

from odoo.addons.eurooffice_odoo.controllers.controllers import Eurooffice_Connector
from odoo.addons.eurooffice_odoo.utils import file_utils

_logger = logging.getLogger(__name__)


class EuroofficeDms_Connector(http.Controller):
    @http.route("/eurooffice/dms/file/create", auth="user", methods=["POST"], type="json")
    def post_file_create(self, directory_id, supported_format, title, url=None):
        result = {"error": None, "file_id": None}

        try:
            _logger.info(f"Getting new file template {request.env.user.lang} {supported_format}")

            if url:
                response = requests.get(url, stream=True, timeout=30)
                response.raise_for_status()
                file_data = response.content
            else:
                file_data = file_utils.get_default_file_template(
                    request.env.user.lang, supported_format
                )

            import base64

            dms_file = request.env["dms.file"].create({
                "name": title + "." + supported_format,
                "directory_id": int(directory_id),
                "content": base64.b64encode(file_data),
            })

            request.env["eurooffice.dms.access"].create({
                "file_id": dms_file.id,
                "internal_users": "none",
                "link_access": "viewer",
            })
            request.env["eurooffice.dms.access.user"].create({
                "file_id": dms_file.id,
                "user_id": request.env.user.id,
                "role": "editor",
            })
            result["file_id"] = dms_file.id

        except Exception as ex:
            _logger.exception(f"Failed to create DMS file {str(ex)}")
            result["error"] = _("Failed to create document")

        return json.dumps(result)


class EuroofficeDms_Inherited_Connector(Eurooffice_Connector):
    @http.route(
        "/eurooffice/editor/dms/<int:file_id>",
        auth="public", type="http", website=True,
    )
    def render_dms_editor(self, file_id, access_token=None):
        return request.render(
            "eurooffice_odoo.eurooffice_editor",
            self.prepare_dms_editor(file_id, access_token),
        )

    def prepare_dms_editor(self, file_id, access_token):
        dms_file = request.env["dms.file"].browse(int(file_id))
        try:
            dms_file.check_access_rule("read")
        except AccessError:
            _logger.error("User has no read access to this DMS file")
            raise Forbidden()

        # DMS files store content as ir.attachment
        attachment = dms_file.attachment_id
        if not attachment:
            _logger.error("DMS file has no attachment")
            raise Forbidden()

        attachment_record = self.get_attachment(attachment.id)
        if not attachment_record:
            raise Forbidden()

        try:
            dms_file.check_access_rule("write")
            return self.prepare_editor_values(attachment_record, access_token, True)
        except AccessError:
            return self.prepare_editor_values(attachment_record, access_token, False)
