/** @odoo-module **/
import { patch } from "@web/core/utils/patch"
import { FormController } from "@web/views/form/form_controller"
import { TemplateDialog } from "../dialog/eurooffice_dialog"

patch(FormController.prototype, "FormController.ActionButton", {
  /**
   * @override
   **/
  getActionMenuItems() {
    const menuItems = this._super()
    menuItems.other.push({
      callback: () => {
        this.env.services.dialog.add(TemplateDialog, {
          resId: this.model.root.resId,
          resModel: this.props.resModel,
        })
      },
      description: this.env._t("Print with Euro-Office"),
      skipSave: true,
    })
    return menuItems
  },
})
