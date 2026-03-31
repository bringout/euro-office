/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl"
import { EuroofficePreview } from "@eurooffice_odoo/views/preview/eurooffice_preview"
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"

export class TemplatesTree extends Component {
  setup() {
    this.orm = useService("orm")
    this.state = useState({
      loading: true,
      selected: [],
      structure: {},
    })

    onWillStart(async () => {
      await this.loadTemplates()
    })
  }

  async loadTemplates() {
    try {
      const data = await this.orm.call("eurooffice.odoo.demo.templates", "get_template_data")
      this.state.structure = data.structure || {}
      this.state.selected = data.selected || []
    } catch (error) {
      console.error("Failed to load templates:", error)
    } finally {
      this.state.loading = false
    }
  }

  toggleTemplate(path, checked) {
    if (checked) {
      this.state.selected.push(path)
    } else {
      this.state.selected = this.state.selected.filter((p) => p !== path)
    }
    if (this.props.record) {
      this.props.record.update({ selected_templates: JSON.stringify(this.state.selected) })
    }
  }

  async saveSelection() {
    const value = JSON.stringify({
      selected: this.state.selected,
      structure: this.state.structure,
    })

    await this.orm.write("eurooffice.odoo.demo.templates", [this.props.record.resId], { selected_templates: value })

    if (this.props.update) {
      this.props.update(value)
    }
  }

  previewTemplate(path) {
    const url = `/eurooffice/template/template_content/${encodeURIComponent(path.replace("/", "_"))}`

    this.env.services.dialog.add(
      EuroofficePreview,
      {
        close: () => {
          this.env.services.dialog.close()
        },
        title: path.split("/").pop(),
        url: url,
      },
      {
        onClose: () => {
          return
        },
      },
    )
  }
}

TemplatesTree.template = "eurooffice_odoo_templates.TemplatesTree"

registry.category("fields").add("eurooffice_template_tree", TemplatesTree)
