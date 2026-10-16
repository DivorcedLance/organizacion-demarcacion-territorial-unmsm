# Organización y Demarcación Territorial (ODT) — UNMSM 2026-II

Repositorio académico que contiene los solucionarios maestros, resúmenes ejecutivos, scripts cartográficos y materiales de referencia para el curso de **Organización y Demarcación Territorial** (UNMSM 2026-II), completamente alineados al **D.S. N° 134-2025-PCM** (Nuevo Reglamento de la Ley N° 27795).

---

## 📄 Documentos Principales Compilados (PDF & LaTeX)

1. **[PCD_Aplicativo_Solucionario_Maestro.pdf](./PCD_Aplicativo_Solucionario_Maestro.pdf)** (44 páginas)
   - Solucionario exhaustivo de las 10 preguntas del PCD Aplicativo.
   - Incluye 19 figuras vectoriales e infografías cartográficas de alta resolución con mapas base georreferenciados (Contextily / Esri WorldTopoMap) y código Python reproducible.
   - Cumple con todos los estándares técnicos del nuevo D.S. N° 134-2025-PCM (ETDM, EDZ, EVAC, saneamiento de límites, redelimitación, etc.).

2. **[EP_Sustentado_Solucionario_Maestro.pdf](./EP_Sustentado_Solucionario_Maestro.pdf)** (16 páginas)
   - Solucionario sustentado del Examen Parcial (EP SUSTENTADO).
   - Desarrollo en profundidad de las 4 preguntas analíticas:
     1. Reestructuración integral del Sistema Nacional de Demarcación Territorial (D.S. 134-2025-PCM vs. D.S. 019-2003-PCM).
     2. Diagnóstico, tipificación y saneamiento del conflicto limítrofe Puno–Moquegua (Pasto Grande).
     3. Rediseño del esquema de categorización y recategorización de centros poblados.
     4. Matriz metodológica del Estudio Técnico de Demarcación y Organización Territorial (ETDM) y su articulación multiescalar.
   - Acompañado de cartografía analítica y diagramas de flujo metodológico.

3. **[Resumen_Ejecutivo_Parcial_ODT.pdf](./Resumen_Ejecutivo_Parcial_ODT.pdf)** (14 páginas)
   - Compendio teórico y técnico sintético de las Sesiones 1 a 6 del curso para el Examen Parcial.

---

## 🗺️ Estructura del Repositorio

- `figuras_pcd/`: 19 figuras vectoriales (SVG, PDF, PNG) con mapas base de alta resolución para el PCD Aplicativo.
- `figuras_ep/`: Cartografía analítica y diagramas vectoriales para el EP Sustentado.
- `generar_figuras_v3.py` & `generar_figuras_definitivas.py`: Scripts en Python (Cartopy, Contextily, Matplotlib, Shapely) para la generación cartográfica automatizada.
- `generar_pcd_latex.py` & `escribir_ep_latex.py`: Scripts de orquestación y compilación LaTeX.
- `*.pdf`: Materiales de lectura y sesiones de clase originales (Sesiones 1, 3, 5, Guía de Campo Checras, D.S. 134-2025-PCM).

---

## 🛠️ Tecnologías y Herramientas

- **Tipografía y Documentación:** XeLaTeX / pdfLaTeX con `tcolorbox`, `booktabs`, `microtype`, `geometry`.
- **Cartografía y Visualización:** Python 3, `matplotlib`, `geopandas`, `cartopy`, `contextily` (Esri WorldTopoMap & OpenStreetMap tiles), `shapely`.
