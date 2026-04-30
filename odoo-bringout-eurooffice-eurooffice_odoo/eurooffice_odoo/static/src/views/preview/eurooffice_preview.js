/** @odoo-module **/

import { Component, onMounted, onWillUnmount } from "@odoo/owl"

export class OnlyofficePreview extends Component {
  static template = "eurooffice_odoo.OnlyofficePreview"

  static props = {
    close: Function,
    title: String,
    url: String,
  }

  setup() {
    this.title = "Preview - " + this.props.title
    this.url =
      "/eurooffice/preview" +
      `?url=${encodeURIComponent(this.props.url)}&` +
      `title=${encodeURIComponent(this.props.title)}`

    const handleKeyDown = (ev) => {
      if (ev.key === "Escape") {
        ev.stopPropagation()
        ev.preventDefault()
        this.props.close()
      }
    }

    onMounted(() => {
      document.addEventListener("keydown", handleKeyDown, { capture: true })
      document.querySelectorAll(".o-overlay-item").forEach((item) => {
        if (item.querySelector(".o-eurooffice-preview")) {
          item.classList.add("o-eurooffice-overlay-item")
        }
      })
    })

    onWillUnmount(() => {
      document.removeEventListener("keydown", handleKeyDown, { capture: true })
    })
  }

  onClickOutside(ev) {
    const isHeader = ev.target.closest(".o-eurooffice-preview-header")
    const isBody = ev.target.closest(".o-eurooffice-preview-body")

    if (!isHeader && !isBody) {
      this.props.close()
    }
  }
}
