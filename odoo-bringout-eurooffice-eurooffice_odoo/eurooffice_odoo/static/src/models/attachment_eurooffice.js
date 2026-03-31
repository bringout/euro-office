/** @odoo-module **/

/*
 *
 * (c) Copyright Ascensio System SIA 2024
 *
 */

import { registerPatch } from "@mail/model/model_core"
import { attr } from "@mail/model/model_field"

let formats = []
const loadFormats = async () => {
  try {
    const data = await fetch("/eurooffice_odoo/static/assets/document_formats/eurooffice-docs-formats.json")
    formats = await data.json()
  } catch (error) {
    console.error("Error loading formats data:", error)
  }
}

loadFormats()

registerPatch({
  name: "Attachment",
  recordMethods: {
    async onClickEuroofficeEdit(ev) {
      ev.stopPropagation()
      const demo = JSON.parse(
        await this.messaging.rpc({
          method: "get_demo",
          model: "eurooffice.odoo",
        }),
      )
      if (demo && demo.mode && demo.date) {
        const isValidDate = (d) => d instanceof Date && !isNaN(d)
        demo.date = new Date(Date.parse(demo.date))
        if (isValidDate(demo.date)) {
          const today = new Date()
          const difference = Math.floor((today - demo.date) / (1000 * 60 * 60 * 24))
          if (difference > 30) {
            this.messaging.userNotificationManager.sendNotification({
              message: this.env._t(
                "The 30-day test period is over, you can no longer connect to demo Euro-Office Docs server",
              ),
              title: this.env._t("Euro-Office Docs server"),
              type: "warning",
            })
            return
          }
        }
      }

      const { same_tab } = JSON.parse(
        await this.messaging.rpc({
          method: "get_same_tab",
          model: "eurooffice.odoo",
        }),
      )
      if (same_tab) {
        this.openSameTabEuroofficeEditor()
      } else {
        this.openNewTabEuroofficeEditor()
      }
    },
    openNewTabEuroofficeEditor() {
      window.open(this.euroofficeEditorUrl, "_blank")
    },
    openSameTabEuroofficeEditor() {
      const action = {
        params: { attachment_id: this.id },
        tag: "eurooffice_editor",
        target: "current",
        type: "ir.actions.client",
      }
      return this.env.services.action.doAction(action)
    },
  },
  // eslint-disable-next-line sort-keys
  fields: {
    euroofficeCanEdit: attr({
      compute() {
        const format = formats.find((f) => f.name === this.extension.toLowerCase())
        return format && format.actions && format.actions.includes("edit")
      },
    }),
    euroofficeCanView: attr({
      compute() {
        const format = formats.find((f) => f.name === this.extension.toLowerCase())
        return format && format.actions && (format.actions.includes("view") || format.actions.includes("edit"))
      },
    }),
    euroofficeEditorUrl: attr({
      compute() {
        const accessTokenQuery = this.accessToken ? `?access_token=${this.accessToken}` : ""
        return `/eurooffice/editor/${this.id}${accessTokenQuery}`
      },
    }),
  },
})
