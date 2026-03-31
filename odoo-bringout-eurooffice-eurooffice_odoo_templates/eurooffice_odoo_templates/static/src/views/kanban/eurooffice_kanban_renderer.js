/** @odoo-module **/

import { KanbanRenderer } from "@web/views/kanban/kanban_renderer"
import { EuroofficeKanbanRecord } from "./eurooffice_kanban_record"

export class EuroofficeKanbanRenderer extends KanbanRenderer {
  setup() {
    super.setup()
  }

  /**
   * @override
   **/
  canQuickCreate() {
    return false
  }

  /**
   * @override
   **/
  canCreateGroup() {
    return false
  }
}

EuroofficeKanbanRenderer.components = {
  ...KanbanRenderer.components,
  KanbanRecord: EuroofficeKanbanRecord,
}
