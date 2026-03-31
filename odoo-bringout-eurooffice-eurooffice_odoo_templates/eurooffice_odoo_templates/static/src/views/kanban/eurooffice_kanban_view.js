/** @odoo-module */
import { registry } from "@web/core/registry"
import { kanbanView } from "@web/views/kanban/kanban_view"
import { EuroofficeKanbanController } from "./eurooffice_kanban_controller"
import { EuroofficeKanbanRenderer } from "./eurooffice_kanban_renderer"

export const euroofficeKanbanView = {
  ...kanbanView,
  Controller: EuroofficeKanbanController,
  Renderer: EuroofficeKanbanRenderer,
  buttonTemplate: "eurooffice_odoo_templates.EuroofficeKanbanController.Buttons",
}

registry.category("views").add("eurooffice_kanban", euroofficeKanbanView)
