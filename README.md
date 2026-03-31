# Euro-Office Odoo Modules

Odoo 16.0 modules for Euro-Office Document Server integration.

Based on [onlyoffice_odoo](https://github.com/ONLYOFFICE/onlyoffice_odoo) by
Ascensio System SIA (ONLYOFFICE), rebranded and adapted for Euro-Office by
[bring.out d.o.o.](https://www.bring.out.ba)

## Modules

### eurooffice_odoo
Base Euro-Office integration. Edit office files (DOCX, XLSX, PPTX) directly
in Odoo with real-time collaborative editing via Euro-Office Document Server.

- Based on: onlyoffice_odoo by ONLYOFFICE (LGPL-3)
- License: LGPL-3
- Dependencies: `base`, `mail`, `pyjwt`

### eurooffice_odoo_templates
Document templates for creating new files from templates.

- Based on: onlyoffice_odoo_templates by ONLYOFFICE (LGPL-3)
- License: LGPL-3
- Dependencies: `eurooffice_odoo`, `web`, `pyjwt`

### eurooffice_odoo_oca_dms
Integration with OCA DMS (Document Management System). Open-source alternative
to the proprietary Odoo Enterprise `documents` module integration.

- Based on: onlyoffice_odoo_documents by ONLYOFFICE (LGPL-3)
- Adapted by: bring.out d.o.o.
- License: LGPL-3
- Dependencies: `eurooffice_odoo`, `dms` (OCA), `pyjwt`

## Attribution

Original software by Ascensio System SIA, published under LGPL-3.
Euro-Office rebranding and OCA DMS adaptation by bring.out d.o.o.
