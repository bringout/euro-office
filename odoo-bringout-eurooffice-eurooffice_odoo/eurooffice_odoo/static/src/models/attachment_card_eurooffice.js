/** @odoo-module **/

/*
 *
 * (c) Copyright Ascensio System SIA 2024
 *
 */

import { registerPatch } from "@mail/model/model_core"
import { attr } from "@mail/model/model_field"

registerPatch({
  fields: {
    showEuroofficeButton: attr({
      compute() {
        return this.attachment.euroofficeCanEdit || this.attachment.euroofficeCanView
      },
    }),
  },
  name: "AttachmentCard",
})
