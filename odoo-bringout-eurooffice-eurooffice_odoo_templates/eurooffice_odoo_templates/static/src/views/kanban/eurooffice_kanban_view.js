/** @odoo-module */
import { registry } from "@web/core/registry"
import { kanbanView } from "@web/views/kanban/kanban_view"
import { OnlyofficeKanbanController } from "./eurooffice_kanban_controller"
import { OnlyofficeKanbanRenderer } from "./eurooffice_kanban_renderer"

export const euroofficeKanbanView = {
  ...kanbanView,
  Controller: OnlyofficeKanbanController,
  Renderer: OnlyofficeKanbanRenderer,
}

registry.category("views").add("eurooffice_kanban", euroofficeKanbanView)
