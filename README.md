# 💆‍♀️ Módulo Odoo: Tratamientos Faciales

![Odoo](https://img.shields.io/badge/Odoo-16%2B-00A09D?logo=odoo&logoColor=white)
![Licencia](https://img.shields.io/badge/Licencia-MIT-blue)
![Estado](https://img.shields.io/badge/Estado-Listo%20para%20producción-brightgreen)

Módulo personalizado para **Odoo** que permite gestionar el historial de tratamientos faciales por cliente, incluyendo productos usados, observaciones, fechas y próximas citas. Ideal para clínicas de estética, spas o centros de belleza.

---

## 🌟 Características principales

- ✅ Registro detallado de tratamientos faciales por cliente  
- 📅 Gestión de fecha del tratamiento y **próxima cita**  
- 🧴 Selección de **productos usados** (con soporte para variantes)  
- 📝 Campo de observaciones para notas personalizadas  
- 📊 Estados: **Borrador**, **Completado**, **Cancelado**  
- 🗂️ Historial visible directamente en la ficha del cliente  
- 📅 Vista de **calendario** para visualizar próximas citas  
- 🔐 Permisos integrados para usuarios internos (`base.group_user`)  
- 🔢 Referencias automáticas con secuencia: `TRAT/00001`, `TRAT/00002`, etc.

---

## 📦 Dependencias

Este módulo requiere los siguientes módulos estándar de Odoo:

- `sale` – Para integración futura con pedidos  
- `product` – Para gestionar productos usados  
- `calendar` – Para la vista de calendario de próximas citas  

> Compatible con **Odoo 14, 15, 16 y 17**.

---

## 🚀 Instalación

1. Clona este repositorio en la carpeta `addons` de tu instancia de Odoo:
   ```bash
   git clone https://github.com/tu-usuario/tratamientos_faciales.git
