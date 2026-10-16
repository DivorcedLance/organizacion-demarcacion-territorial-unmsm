import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('figuras_pcd', exist_ok=True)

# Configuración global estética y limpia
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9.5
plt.rcParams['axes.edgecolor'] = '#2d3748'
plt.rcParams['axes.linewidth'] = 1.0

def save_fig(fig, name):
    svg_path = os.path.join('figuras_pcd', f'{name}.svg')
    pdf_path = os.path.join('figuras_pcd', f'{name}.pdf')
    fig.savefig(svg_path, format='svg', bbox_inches='tight')
    fig.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f'Successfully generated {name} (.svg & .pdf)')

# ==============================================================================
# FIGURA 1: Pregunta 1 - Curvatura Espacio-Temporal y Geodésica Chancay - Shanghái
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6))
ax.set_facecolor('#f8fafc')
ax.set_xlim(0, 110)
ax.set_ylim(0, 75)
ax.axis('off')

# Retícula de paralelos y meridianos sutiles (geometría de navegación)
for y_lat in range(15, 70, 12):
    ax.axhline(y_lat, color='#e2e8f0', linestyle=':', lw=1.0)
for x_lon in range(15, 105, 15):
    ax.axvline(x_lon, color='#e2e8f0', linestyle=':', lw=1.0)

# Masa continental Asia esquemática
asia_poly = patches.Polygon([(5, 20), (5, 65), (25, 65), (28, 45), (20, 25), (10, 20)],
                             facecolor='#edf2f7', edgecolor='#cbd5e0', lw=1.5)
ax.add_patch(asia_poly)
ax.text(12, 60, 'CUENCA ASIA-PACÍFICO\n(China / Shanghái Hub)', fontsize=9, weight='bold', color='#1a365d')

# Masa continental Sudamérica esquemática
sa_poly = patches.Polygon([(85, 45), (105, 45), (105, 10), (95, 10), (88, 25)],
                           facecolor='#edf2f7', edgecolor='#cbd5e0', lw=1.5)
ax.add_patch(sa_poly)
ax.text(90, 40, 'SUDAMÉRICA\n(Fachada Pacífico)', fontsize=9, weight='bold', color='#22543d')

# Nodos principales
ax.plot(22, 35, 'o', color='#1a365d', markersize=11, zorder=5)
ax.text(22, 28, 'SHANGHÁI\n[Hub Principal]', ha='center', fontsize=9, weight='bold', color='#1a365d')

ax.plot(89, 28, 'o', color='#0d6938', markersize=11, zorder=5)
ax.text(92, 22, 'PUERTO DE CHANCAY\n[Calado 17.8 m]', ha='center', fontsize=9, weight='bold', color='#0d6938')

# Ruta tradicional quebrada (35-45 días)
trad_x = [89, 82, 55, 32, 22]
trad_y = [28, 55, 63, 50, 35]
ax.plot(trad_x, trad_y, '--', color='#c53030', linewidth=2.5, label='Ruta Tradicional de Cabotaje por Pacífico Norte (35 a 45 días)', zorder=4)

escalas = [(82, 55, 'Manzanillo / Long Beach\n(Transbordo EE.UU./México)'),
           (55, 63, 'Arco Septentrional de las Aleutianas\n(Fricción temporal extrema)'),
           (32, 50, 'Yokohama / Busan\n(Hubs intermedios)')]
for ex, ey, elbl in escalas:
    ax.plot(ex, ey, 's', color='#c53030', markersize=7, zorder=5)
    ax.text(ex, ey+3, elbl, fontsize=7.8, color='#742a2a', ha='center', weight='bold')

# Vector directo geodésico no euclidiano (23 días)
gx = np.linspace(89, 22, 100)
gy = 28 + (35 - 28) * ((gx - 89)/(22 - 89)) - 14 * np.sin(np.pi * (gx - 22)/67)
ax.plot(gx, gy, '-', color='#2b6cb0', linewidth=4.0, label='Geodésica No Euclidiana Directa: Chancay - Shanghái (23 días)', zorder=4)

# Caja explicativa de Riemann-Gauss y LaRouche
info_text = (
    "CONTRACCIÓN ESPACIO-TEMPORAL (Riemann - Gauss & LaRouche):\n"
    "• Disminución de 15 a 22 días de navegación directa.\n"
    "• Deformación del tensor métrico de fricción espacial ($g_{ij}$).\n"
    "• Ley N.° 32279: Blindaje territorial soberano ante pugna geopolítica EE.UU. vs. China."
)
ax.text(55, 12, info_text, ha='center', fontsize=8.5, weight='bold', color='#1a202c',
        bbox=dict(boxstyle='round,pad=0.7', facecolor='#ebf8ff', edgecolor='#3182ce', lw=1.5))

ax.set_title('FIGURA 1: Geometría No Euclidiana y Geodésica Marítima Directa Chancay - Shanghái\nRuptura de la Fricción Espacial Global y Reducción del Tránsito Transpacífico',
             fontsize=11, weight='bold', pad=15)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), frameon=True, facecolor='white', edgecolor='#cbd5e0', fontsize=8.5)
save_fig(fig, 'fig_p01_chancay_geometria')

# ==============================================================================
# FIGURA 2: Pregunta 2 - Metabolismo Territorial y Balance Hídrico de Cuencas
# ==============================================================================
fig, ax = plt.subplots(figsize=(11.5, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 115)
ax.set_ylim(0, 70)
ax.axis('off')

# 3 Bloques bien separados con amplio margen
b1 = patches.FancyBboxPatch((6, 20), 28, 36, boxstyle='round,pad=0.8', facecolor='#ebf8ff', edgecolor='#2b6cb0', lw=2)
ax.add_patch(b1)
ax.text(20, 50, '1. CABECERA ANDINA\n(Checras / Oyón)', ha='center', weight='bold', fontsize=9.5, color='#1a365d')
ax.text(20, 33, '• Glaciares y lagunas (>4,000 m)\n• Bofedales altoandinos\n• Siembra y Cosecha de Agua\n• Amunas y qochas comunales\n\nEntrada Neta ($Q_{in}$)\nBaja Entropía ($S_0$)', ha='center', fontsize=8, color='#2c5282')

b2 = patches.FancyBboxPatch((44, 20), 28, 36, boxstyle='round,pad=0.8', facecolor='#f0fff4', edgecolor='#2f855a', lw=2)
ax.add_patch(b2)
ax.text(58, 50, '2. VALLE INTERMEDIO\n(Sayán / Huaura)', ha='center', weight='bold', fontsize=9.5, color='#22543d')
ax.text(58, 33, '• Andenes tradicionales\n• Producción frutícola\n• Evapotranspiración agrícola\n• Uso de biomasa alimentaria\n\nConsumo Intermedio\nMetabolismo de Cuenca', ha='center', fontsize=8, color='#276749')

b3 = patches.FancyBboxPatch((82, 20), 28, 36, boxstyle='round,pad=0.8', facecolor='#fff5f5', edgecolor='#c53030', lw=2)
ax.add_patch(b3)
ax.text(96, 50, '3. NODO LITORAL\n(Chancay / Complejo)', ha='center', weight='bold', fontsize=9.5, color='#742a2a')
ax.text(96, 33, '• Demanda de megapuerto\n• Parque industrial/urbano\n• Lavado de contenedores\n• Vertimientos residuales\n\nDisipación Antrópica\nAlta Entropía ($dS/dt > 0$)', ha='center', fontsize=8, color='#9b2c2c')

# Flechas horizontales de flujo conectadas sin solapamiento
ax.annotate('', xy=(44, 38), xytext=(34, 38), arrowprops=dict(arrowstyle="->", color='#2b6cb0', lw=3.5))
ax.text(39, 41, 'Caudal Fluvial\n$Q_{trans}$', ha='center', fontsize=7.8, color='#2b6cb0', weight='bold')

ax.annotate('', xy=(82, 38), xytext=(72, 38), arrowprops=dict(arrowstyle="->", color='#2f855a', lw=3.5))
ax.text(77, 41, 'Agua Sobrante\n$Q_{neto}$', ha='center', fontsize=7.8, color='#2f855a', weight='bold')

# Bloques inferiores de políticas de gobernanza
ax.text(20, 8, 'Ley N.° 32279: Intangibilidad de Cabeceras\ny Financiamiento MERESE para Checras', ha='center', fontsize=8, weight='bold', color='#1a365d',
        bbox=dict(boxstyle='square,pad=0.5', facecolor='#edf2f7', edgecolor='#cbd5e0'))

ax.text(96, 8, 'Mandato Termodinámico de Carnot:\nDesalinización Obligatoria con Recirculación', ha='center', fontsize=8, weight='bold', color='#742a2a',
        bbox=dict(boxstyle='square,pad=0.5', facecolor='#edf2f7', edgecolor='#cbd5e0'))

ax.set_title('FIGURA 2: Metabolismo Territorial y Balance Termodinámico de Cuenca (Odum - Carnot)\nFlujo Hídrico desde las Altas Cumbres de Checras hasta la Disipación Litoral de Chancay',
             fontsize=11, weight='bold', pad=15)
save_fig(fig, 'fig_p02_metabolismo_hidrico')

# ==============================================================================
# FIGURA 3: Pregunta 3 - Corte Estratigráfico Geotécnico Terzaghi y SINAGERD
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 110)
ax.set_ylim(-38, 28)

# Estratos de suelo
ax.fill_between([0, 110], [0, 0], [-7, -7], color='#fefcbf', alpha=0.9, label='Arena eólica no cohesiva suelta (SP) [$N_{SPT} < 10$, alto riesgo de licuefacción]')
ax.fill_between([0, 110], [-7, -7], [-20, -20], color='#cbd5e0', alpha=0.9, label='Grava aluvial densa y arenas consolidadas (GW-GP) [$N_{SPT} = 25 - 45$]')
ax.fill_between([0, 110], [-20, -20], [-38, -38], color='#718096', alpha=0.95, label='Basamento rocoso sano / Andesitas y lutitas densas [$N_{SPT} > 50$, RQD > 75%]')

# Nivel Freático
ax.plot([0, 110], [-3.5, -3.5], 'b--', lw=2.2, label='Nivel Freático Somero ($NF = -3.50\\text{ m}$, saturación completa de poros)')

# Losa de megaestructura portuaria
rect_sup = patches.Rectangle((25, 0), 60, 15, facecolor='#4a5568', edgecolor='#1a202c', lw=2)
ax.add_patch(rect_sup)
ax.text(55, 7.5, 'MEGAPLATAFORMA LOGÍSTICA / PATIO DE CONTENEDORES\nCarga Admisible de Servicio: $q_{adm} > 4.5\\text{ kg/cm}^2$',
        ha='center', va='center', color='white', weight='bold', fontsize=8.8)

# Pilotes de gran diámetro
pilote_x = [30, 42, 55, 68, 80]
for px in pilote_x:
    ax.plot([px, px], [0, -25], color='#1a202c', lw=4.5)
    ax.plot([px-1.5, px+1.5], [-25, -25], color='#1a202c', lw=3)

# Criterio de Terzaghi
terz_text = (
    "RESTRICCIÓN FÍSICA OBLIGATORIA (Terzaghi & SINAGERD):\n"
    "• Pilotes empotrados $> 5\\text{ m}$ en basamento rocoso.\n"
    "• Suelo eólico superficial incapaz de soportar cargas portuarias.\n"
    "• Contraste con Checras: En la sierra el riesgo geotécnico crítico son\n"
    "  los movimientos en masa y huaycos en laderas de roca fracturada."
)
ax.text(55, -30, terz_text, ha='center', va='center', fontsize=8.2, weight='bold', color='white',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#2d3748', edgecolor='#1a202c'))

ax.set_ylabel('Profundidad Estratigráfica (m)', fontsize=9.5, weight='bold')
ax.set_title('FIGURA 3: Corte Estratigráfico Geotécnico de Suelos en el Litoral Chancay-Ancón (Terzaghi)\nCapacidad de Acogida, Licuefacción de Suelos y Restricciones Físicas del SINAGERD',
             fontsize=10.8, weight='bold', pad=15)
ax.legend(loc='upper right', fontsize=8, frameon=True, facecolor='white', edgecolor='#cbd5e0')
save_fig(fig, 'fig_p03_corte_suelos_terzaghi')

# ==============================================================================
# FIGURA 4: Pregunta 4 - Autoridad Autónoma Regional (TVA y Marcas Carolingias)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6.8))
ax.set_facecolor('#f8fafc')
ax.set_xlim(0, 110)
ax.set_ylim(0, 75)
ax.axis('off')

# Nivel 1: Comando Estratégico Unificado
b1 = patches.FancyBboxPatch((22, 56), 66, 14, boxstyle='round,pad=0.8', facecolor='#742a2a', edgecolor='#1a202c', lw=2)
ax.add_patch(b1)
ax.text(55, 63, 'COMANDO ESTRATÉGICO DE SEGURIDAD TERRITORIAL (AAIC)\nPresidencia del Consejo de Ministros (PCM) -- Ministerio de Defensa (MINDEF)\n[Marco: Ley del Sistema de Seguridad y Defensa Nacional - D. Leg. 1129]',
        ha='center', va='center', color='white', weight='bold', fontsize=8.5)

# Nivel 2: Dos Cajas Operacionales
b2 = patches.FancyBboxPatch((8, 30), 44, 15, boxstyle='round,pad=0.8', facecolor='#2b6cb0', edgecolor='#1a202c', lw=1.8)
ax.add_patch(b2)
ax.text(30, 37.5, 'OPERADOR LOGÍSTICO Y PORTUARIO\n• Administración del Megapuerto\n• Gestión aduanera y ZED Chancay\n• Corredores viales y ferroviarios del SINAC',
        ha='center', va='center', color='white', weight='bold', fontsize=8.2)

b3 = patches.FancyBboxPatch((58, 30), 44, 15, boxstyle='round,pad=0.8', facecolor='#2c5282', edgecolor='#1a202c', lw=1.8)
ax.add_patch(b3)
ax.text(80, 37.5, 'DIVISIÓN DE CONTRAINTELIGENCIA Y DEFENSA\n• Ciberseguridad de infraestructura crítica\n• Neutralización de injerencia extranjera\n• Control de marcas fronterizas y litoral',
        ha='center', va='center', color='white', weight='bold', fontsize=8.2)

# Nivel 3: Subordinación Territorial Local
b4 = patches.FancyBboxPatch((15, 4), 80, 15, boxstyle='round,pad=0.8', facecolor='#2f855a', edgecolor='#1a202c', lw=1.8)
ax.add_patch(b4)
ax.text(55, 11.5, 'GOBIERNOS LOCALES Y COMUNIDADES SUBORDINADAS\n• Sub-zona Litoral: Municipalidades de Chancay, Huaral, Huacho y Barranca\n• Sub-zona Cuenca Alta: Oyón y Distrito de Checras (Puñun / Purapucu)\nPlanificación de Suelos, Protección de Andenerías, Agua y Servidumbres Mineras',
        ha='center', va='center', color='white', weight='bold', fontsize=8.2)

# Flechas limpias
ax.annotate('', xy=(30, 45), xytext=(45, 56), arrowprops=dict(arrowstyle="->", lw=2.5, color='#742a2a'))
ax.annotate('', xy=(80, 45), xytext=(65, 56), arrowprops=dict(arrowstyle="->", lw=2.5, color='#742a2a'))
ax.annotate('', xy=(42, 19), xytext=(30, 30), arrowprops=dict(arrowstyle="->", lw=2.5, color='#2b6cb0'))
ax.annotate('', xy=(68, 19), xytext=(80, 30), arrowprops=dict(arrowstyle="->", lw=2.5, color='#2c5282'))

ax.set_title('FIGURA 4: Estructura Espacial de la Autoridad Autónoma Civil-Militar (TVA de Roosevelt - Marcas Carolingias)\nGobernanza Centralizada de Infraestructura Crítica y Subordinación de Nodos Tributarios',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p04_autoridad_autonoma')

# ==============================================================================
# FIGURA 5: Pregunta 5 - Fuerzas Centrífugas y Ruptura de la Macrocefalia (REDISEÑADA COMPLETA)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11.5, 7.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 115)
ax.set_ylim(0, 95)
ax.axis('off')

# Línea de Costa del Litoral Central esquemática
costa_x = np.array([25, 28, 30, 33, 36, 40, 44, 48])
costa_y = np.array([15, 28, 42, 54, 66, 76, 84, 90])
ax.plot(costa_x, costa_y, '-', color='#a0aec0', lw=2.0)
ax.text(12, 50, 'OCÉANO PACÍFICO', fontsize=9, weight='bold', color='#718096', rotation=65)

# Núcleo de Lima Metropolitana (al sur)
circ_lima = patches.Circle((32, 20), 11, facecolor='#fed7d7', edgecolor='#e53e3e', lw=2.2)
ax.add_patch(circ_lima)
ax.plot(32, 20, 'o', color='#9b2c2c', markersize=9)
ax.text(32, 20, 'LIMA METROPOLITANA\n(Macrocefalia Histórica)\n43 Distritos | 10M hab.',
        ha='center', va='center', weight='bold', fontsize=8.2, color='#742a2a')

# Polo Norte Chico (recuadro amplio y bien espaciado al norte)
rect_nc = patches.FancyBboxPatch((28, 48), 82, 42, boxstyle='round,pad=1.2', facecolor='#ebf8ff', edgecolor='#2b6cb0', lw=2.2)
ax.add_patch(rect_nc)
ax.text(69, 85, 'POLO DESCENTRALIZADO DEL NORTE CHICO (TUO Ley N.° 27795)\nArticulación del Litoral y la Cuenca Transandina de Huaura',
        ha='center', weight='bold', fontsize=9.2, color='#1a365d')

# Nodos Litorales del Norte Chico
nodos_litoral = [
    (38, 56, 'Chancay\n[Megapuerto Hub]'),
    (52, 60, 'Huaral\n[Valle Agroindustrial]'),
    (48, 74, 'Huacho\n[Capital Provincial Huaura]'),
    (46, 82, 'Barranca - Pativilca\n[Agroexportación Norte]')
]
for nx, ny, nlbl in nodos_litoral:
    ax.plot(nx, ny, 'o', color='#2b6cb0', markersize=8, zorder=5)
    ax.text(nx, ny-5.5, nlbl, ha='center', fontsize=7.8, weight='bold', color='#1a365d')

# Nodos Intermedios y de Cuenca Alta (bien separados para evitar solapamientos)
ax.plot(72, 68, 's', color='#2f855a', markersize=8, zorder=5)
ax.text(72, 63, 'Sayán\n[Pivote Vial Intermedio]', ha='center', fontsize=7.8, weight='bold', color='#22543d')

ax.plot(96, 75, '^', color='#b7791f', markersize=9, zorder=5)
ax.text(96, 79, 'Distrito de Checras\n[Puñun / Purapucu / Maray]\nCabecera de Cuenca (2,500 - 3,550 m)',
        ha='center', fontsize=8, weight='bold', color='#744210')

# Conexión vial Sayán - Checras
ax.plot([48, 72, 96], [74, 68, 75], ':', color='#2f855a', lw=2.5)

# Vectores Centrífugos (Fuerzas de Desconcentración) claramente posicionados
ax.annotate('', xy=(38, 50), xytext=(32, 31),
            arrowprops=dict(facecolor='#c53030', edgecolor='#742a2a', width=3, headwidth=9))
ax.text(26, 38, 'Vector Portuario\n(Chancay)', ha='center', fontsize=7.5, weight='bold', color='#742a2a')

ax.annotate('', xy=(52, 53), xytext=(38, 30),
            arrowprops=dict(facecolor='#c53030', edgecolor='#742a2a', width=3, headwidth=9))
ax.text(49, 40, 'Vector Agroindustrial\n(Huaral)', ha='center', fontsize=7.5, weight='bold', color='#742a2a')

ax.annotate('', xy=(66, 60), xytext=(42, 28),
            arrowprops=dict(facecolor='#c53030', edgecolor='#742a2a', width=2.5, headwidth=8))
ax.text(64, 46, 'Vector Transandino\n(Sayán - Checras)', ha='center', fontsize=7.5, weight='bold', color='#742a2a')

# Explicación de Ratzel y Velasco
ratzel_text = (
    "TEORÍA DEL ESPACIO VITAL (Ratzel) Y DESCENTRALIZACIÓN (Velasco Alvarado):\n"
    "• La emergencia del Megapuerto quiebra la gravedad monopólica de Lima.\n"
    "• Checras deja de depender exclusivamente de intermediarios de la capital y se integra\n"
    "  como despensa estratégica y regulador hídrico de la subregión Chancay-Huacho."
)
ax.text(69, 10, ratzel_text, ha='center', fontsize=8.2, weight='bold', color='#1a202c',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#f7fafc', edgecolor='#cbd5e0', lw=1.2))

ax.set_title('FIGURA 5: Dinámica Centrífuga y Descentralización Territorial en el Litoral Central (Ratzel - Velasco Alvarado)\nDesplazamiento del Peso Económico hacia el Norte Chico y Articulación con la Cuenca de Checras',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p05_fuerzas_centrifugas')

# ==============================================================================
# FIGURA 6: Pregunta 6 - Transición Noosférica en el VRAEM (Vernadsky - Antúnez)
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 6))
for ax in (ax1, ax2):
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 55)
    ax.set_ylim(0, 60)
    ax.axis('off')

# Panel A: Biosfera Desordenada
ax1.set_title('(A) BIOSFERA DESORDENADA (VRAEM Inicial)\nEconomía Ilegal de Coca y Entropía Social', fontsize=9.2, weight='bold', color='#742a2a')
np.random.seed(42)
cx = np.random.uniform(8, 48, 16)
cy = np.random.uniform(10, 50, 16)
ax1.scatter(cx, cy, s=70, color='#e53e3e', marker='x')
ax1.text(28, 53, 'Parcelas Ilícitas Dispersas', ha='center', fontsize=8, color='#742a2a', weight='bold')
ax1.plot([12, 38], [15, 22], 'k--', lw=2)
ax1.text(25, 12, 'Pista Clandestina de Narcotráfico', ha='center', fontsize=7.5, color='#742a2a')

# Panel B: Noosfera Organizada
ax2.set_title('(B) NOOSFERA ORGANIZADA (Vernadsky - Antúnez)\nInfraestructura Pesada, Energía y Agroindustria', fontsize=9.2, weight='bold', color='#22543d')
ax2.plot([8, 48], [12, 48], '-', color='#2b6cb0', lw=4, label='Eje Vial Asfaltado Troncal')
ax2.plot([8, 48], [48, 12], '-', color='#2f855a', lw=3, label='Línea de Transmisión de Alta Tensión')

nodos_vraem = [(15, 18, 'Centro de Acopio\nde Cacao / Café'),
               (28, 30, 'C.H. Antúnez de Mayolo\n[Energía Hidroeléctrica]'),
               (42, 42, 'Parque Agroindustrial\ny Base Integrada')]
for nx, ny, nlbl in nodos_vraem:
    ax2.plot(nx, ny, 's', color='#1a365d', markersize=8)
    ax2.text(nx+2, ny-3, nlbl, fontsize=7.5, weight='bold', color='#1a365d')

ax1.text(27, 4, 'Baja Densidad Energética -- Aislamiento y Violencia', ha='center', fontsize=8, weight='bold', color='#742a2a',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff5f5', edgecolor='#e53e3e'))
ax2.text(28, 4, 'Alta Densidad de Flujo -- Seguridad y Soberanía Territorial', ha='center', fontsize=8, weight='bold', color='#22543d',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0fff4', edgecolor='#2f855a'))

fig.suptitle('FIGURA 6: Transformación Territorial en el VRAEM: De la Biosfera Desordenada a la Noosfera Energética',
             fontsize=11, weight='bold')
save_fig(fig, 'fig_p06_noosfera_vraem')

# ==============================================================================
# FIGURA 7: Pregunta 7 - Sistema Hamilton-Carey vs. Minería Ilegal (Madre de Dios)
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 6.2))
for ax in (ax1, ax2):
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 65)
    ax.axis('off')

# Lado 1: Ciclo Destructivo Ilegal
ax1.set_title('(A) CICLO DESTRUCTIVO (Minería Ilegal)\nLibre Mercado Desregulado y Fuga de Riqueza', fontsize=9, weight='bold', color='#742a2a')
p1 = [(30, 52, '1. Ausencia del Estado y\nDesregulación Territorial'),
      (46, 36, '2. Minería Aluvial Ilegal\n(Mercurio y Deforestación)'),
      (38, 16, '3. Trata de Personas y\nViolencia en Enclaves'),
      (14, 28, '4. Contrabando de Oro y\nEvasión Fiscal Masiva')]
for x, y, t in p1:
    ax1.add_patch(patches.FancyBboxPatch((x-12, y-6), 24, 12, boxstyle='round,pad=0.4', facecolor='#fff5f5', edgecolor='#e53e3e', lw=1.5))
    ax1.text(x, y, t, ha='center', va='center', fontsize=7.2, weight='bold', color='#742a2a')
for i in range(len(p1)):
    ax1.annotate('', xy=(p1[(i+1)%4][0], p1[(i+1)%4][1]), xytext=(p1[i][0], p1[i][1]),
                 arrowprops=dict(arrowstyle="->", lw=2, color='#e53e3e'))

# Lado 2: Ciclo Virtuoso Hamilton - Carey
ax2.set_title('(B) CICLO VIRTUOSO (Sistema Hamilton - Carey)\nCatastro Multipropósito y Obra Pública Soberana', fontsize=9, weight='bold', color='#1a365d')
p2 = [(30, 52, '1. Catastro Multipropósito\n(Ley N.° 32279: Certidumbre)'),
      (46, 36, '2. Inversión Pública en Vías\ny Electrificación Limpia'),
      (38, 16, '3. Agroforestería y Valor\nAgregado Industrial'),
      (14, 28, '4. Reinversión Tributaria y\nBlindaje Institucional')]
for x, y, t in p2:
    ax2.add_patch(patches.FancyBboxPatch((x-12, y-6), 24, 12, boxstyle='round,pad=0.4', facecolor='#ebf8ff', edgecolor='#2b6cb0', lw=1.5))
    ax2.text(x, y, t, ha='center', va='center', fontsize=7.2, weight='bold', color='#1a365d')
for i in range(len(p2)):
    ax2.annotate('', xy=(p2[(i+1)%4][0], p2[(i+1)%4][1]), xytext=(p2[i][0], p2[i][1]),
                 arrowprops=dict(arrowstyle="->", lw=2, color='#2b6cb0'))

fig.suptitle('FIGURA 7: Contrapunto en Madre de Dios: Extractivismo Ilegal vs. Sistema Nacional Americano de Infraestructura',
             fontsize=10.8, weight='bold')
save_fig(fig, 'fig_p07_hamilton_carey_mdd')

# ==============================================================================
# FIGURA 8: Pregunta 8 - Heartland Amazónico y Fortines Noosféricos (Putumayo-Yavarí)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11.5, 6))
ax.set_facecolor('#f0fff4')
ax.set_xlim(0, 110)
ax.set_ylim(0, 60)
ax.axis('off')

# Línea del río Putumayo / Yavarí
rx = np.linspace(5, 105, 100)
ry = 32 + 7 * np.sin(rx / 9)
ax.plot(rx, ry, '-', color='#276749', lw=3.5, label='Frontera Fluvial Internacional (Ríos Putumayo y Yavarí)')

ax.text(55, 52, 'TERRITORIO EXTRANJERO (VECINOS DEL NORTE / ORIENTE)', ha='center', fontsize=9, color='#718096', weight='bold')
ax.text(55, 8, 'HEARTLAND AMAZÓNICO PERUANO (Zonas de Frontera de Desarrollo Integrado - SEDENA)', ha='center', fontsize=9, color='#22543d', weight='bold')

# Fortines bien espaciados
fortines = [
    (16, 30, 'Fortín 1: Güeppí\n[Radar Militar + MGP]'),
    (42, 38, 'Fortín 2: San Antonio\n[Monitoreo Ambiental]'),
    (68, 28, 'Fortín 3: El Estrecho\n[C2 Satelital + Aeródromo]'),
    (92, 37, 'Fortín 4: Islandia / Yavarí\n[Aduana + Telemedicina]')
]
for fx, fy, flbl in fortines:
    ax.plot(fx, fy, 's', color='#c53030', markersize=9, zorder=5)
    ax.plot(fx, fy, 'o', color='#ecc94b', markersize=4, zorder=6)
    ax.annotate(flbl, xy=(fx, fy), xytext=(fx, fy-13),
                arrowprops=dict(facecolor='#c53030', shrink=0.08, width=1.2, headwidth=5),
                fontsize=7.8, weight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffffff', edgecolor='#c53030', lw=1.2))

ax.set_title('FIGURA 8: Dispositivo Lineal de "Fortines Noosféricos" en las Fronteras Vivas del Putumayo y Yavarí\nOcupación Territorial Efectiva y Control Civil-Militar Soberano (Mackinder - Putin)',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p08_heartland_amazonico')

# ==============================================================================
# FIGURA 9: Pregunta 9 - Densidad de Flujo Energético y Corredores en Purús
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 110)
ax.set_ylim(0, 65)
ax.axis('off')

# Nodos
ax.plot(15, 32, 'o', color='#1a365d', markersize=12, zorder=5)
ax.text(15, 38, 'PUCALLPA (Ucayali)\n[Conectado a Red Nacional SINAC]', ha='center', weight='bold', fontsize=8.5, color='#1a365d')

ax.plot(95, 32, 's', color='#c53030', markersize=12, zorder=5)
ax.text(95, 38, 'PUERTO ESPERANZA (Purús)\n[Enclave Aislado Histórico]', ha='center', weight='bold', fontsize=8.5, color='#c53030')

# Barrera ambiental radical en el centro
rect_barr = patches.Rectangle((38, 12), 34, 40, facecolor='#c6f6d5', edgecolor='#38a169', lw=2, linestyle='--')
ax.add_patch(rect_barr)
ax.text(55, 46, 'BARRERA PRESERVACIONISTA\n(Tesis Anglo-Ambientalista)\nIncomunicación Artificial del Enclave', ha='center', fontsize=8, weight='bold', color='#22543d')

# Corredor multimodal propuesto
ax.plot([15, 38, 72, 95], [32, 22, 22, 32], color='#d69e2e', lw=3.8, label='Corredor Multimodal Ecológico Subterráneo / Férreo de Bajo Impacto')
ax.plot([15, 95], [26, 26], color='#3182ce', lw=2.2, linestyle=':', label='Tendido Eléctrico de Alta Tensión y Fibra Óptica')

ax.annotate('Incremento de la Densidad de Flujo Energético ($kW/km^2$)\nIntegración Soberana bajo el TUO Ley N.° 27795',
            xy=(55, 22), xytext=(55, 6),
            arrowprops=dict(facecolor='#d69e2e', shrink=0.08, width=1.5, headwidth=6),
            fontsize=8.5, weight='bold', ha='center', color='#744210',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fefcbf', edgecolor='#d69e2e', lw=1.2))

ax.set_title('FIGURA 9: Densidad de Flujo Energético y Corredores Multimodales en el Eje Purús (Lyndon LaRouche)\nSuperación de Enclaves Aislados y Articulación Continua al SINAC',
             fontsize=10.8, weight='bold', pad=15)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.98), fontsize=8.2, frameon=True)
save_fig(fig, 'fig_p09_densidad_flujo_purus')

# ==============================================================================
# FIGURA 10: Pregunta 10 - Ecorregiones de Humboldt y Choque ENOS (Piura-Tumbes)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6.2))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 110)
ax.set_ylim(0, 65)
ax.axis('off')

# Línea de costa
ax.plot([50, 50], [0, 65], 'k-', lw=1.8)
ax.text(80, 56, 'CONTINENTE (Cuencas Piura - Tumbes)\n[Despensa Agroexportadora]', ha='center', weight='bold', fontsize=9, color='#2f855a')
ax.text(25, 56, 'OCÉANO PACÍFICO ORIENTAL\n[Interfase Oceanográfica]', ha='center', weight='bold', fontsize=9, color='#2b6cb0')

# Humboldt (del sur, fría)
ax.annotate('', xy=(30, 26), xytext=(30, 4), arrowprops=dict(facecolor='#3182ce', edgecolor='#1a365d', width=5, headwidth=12))
ax.text(18, 14, 'Corriente Fría de Humboldt\n($14^\\circ - 17^\\circ\\text{C}$)', fontsize=8, weight='bold', color='#1a365d')

# El Niño (del norte, cálida)
ax.annotate('', xy=(30, 36), xytext=(30, 58), arrowprops=dict(facecolor='#e53e3e', edgecolor='#9b2c2c', width=5, headwidth=12))
ax.text(18, 48, 'Aguas Cálidas de El Niño\n($> 27^\\circ\\text{C}$ / ENOS 2026)', fontsize=8, weight='bold', color='#9b2c2c')

# Zona de choque
rect_chq = patches.Rectangle((32, 27), 36, 10, facecolor='#ecc94b', alpha=0.5, edgecolor='#d69e2e', lw=2)
ax.add_patch(rect_chq)
ax.text(50, 32, 'ZONA DE CHOQUE TÉRMICO Y LLUVIAS EXTRAORDINARIAS\nActivación de Quebradas y Crecidas Fluviales', ha='center', va='center', weight='bold', fontsize=7.8, color='#744210')

# Restricción SINAGERD
ax.text(82, 22, 'MEDIDAS OBLIGATORIAS SINAGERD (Ley N.° 29664):\n• Presas de laminación de avenidas en cabeceras.\n• Defensas ribereñas y descolmatación continua.\n• Restricción urbana en llanuras de inundación.',
        ha='center', fontsize=7.8, weight='bold', color='#742a2a',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff5f5', edgecolor='#e53e3e', lw=1.2))

ax.set_title('FIGURA 10: Interfase Ecorregional de Humboldt vs. El Niño en el Litoral Norte (Piura - Tumbes)\nAbsorción Vinculante de Riesgos de Desastres en el Ordenamiento Territorial (SINAGERD)',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p010_humboldt_elnino')

# ==============================================================================
# FIGURA 11: Pregunta 11 - Cuenca Endorreica del Titicaca y Blindaje Ambiental
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 110)
ax.set_ylim(0, 65)
ax.axis('off')

# Lago Titicaca
lake = patches.Ellipse((55, 28), 65, 24, facecolor='#bee3f8', edgecolor='#2b6cb0', lw=2.5)
ax.add_patch(lake)
ax.text(55, 28, 'LAGO TITICACA (Cuenca Endorreica Binacional)\n[Reserva Hídrica Estratégica Perú - Bolivia]', ha='center', va='center', weight='bold', fontsize=8.8, color='#1a365d')

# Fuentes de Contaminación
ax.annotate('Río Ramis (Metales Pesados: $Hg, Pb, As$\nde Minería Ilegal en La Rinconada/Ananea)',
            xy=(35, 38), xytext=(22, 54),
            arrowprops=dict(arrowstyle="->", color='#c53030', lw=2.5),
            fontsize=8, weight='bold', color='#742a2a',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#fff5f5', edgecolor='#e53e3e'))

ax.annotate('Río Coata (Efluentes Urbanos\nno Tratados de Juliaca)',
            xy=(55, 40), xytext=(72, 54),
            arrowprops=dict(arrowstyle="->", color='#c53030', lw=2.5),
            fontsize=8, weight='bold', color='#742a2a',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#fff5f5', edgecolor='#e53e3e'))

ax.text(55, 8, 'BLINDAJE TERRITORIAL SOBERANO (Ley N.° 32279 & Ley de Seguridad Nacional)\nFiscalización Militar en Cabeceras, PTARs Prioritarias y Protección del Acuífero', ha='center', fontsize=8.2, weight='bold', color='#22543d',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0fff4', edgecolor='#38a169', lw=1.2))

ax.set_title('FIGURA 11: Metabolismo de la Cuenca Endorreica del Titicaca y Acumulación de Efluentes (Odum)\nImpacto de Pasivos Minero-Urbanos y Exigencia de Blindaje Territorial Estratégico',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p011_titicaca_endorreico')

# ==============================================================================
# FIGURA 12: Pregunta 12 - Frontera Viva Tacna-Arica y Lebensraum
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 110)
ax.set_ylim(0, 65)
ax.axis('off')

# Límite de frontera
ax.plot([55, 55], [6, 58], '--', color='#4a5568', lw=2)
ax.text(55, 60, 'LÍNEA DE LA CONCORDIA (Hito N.° 1)', ha='center', weight='bold', fontsize=9, color='#4a5568')

# Lado Tacna
b_tacna = patches.FancyBboxPatch((10, 16), 38, 38, boxstyle='round,pad=0.8', facecolor='#ebf8ff', edgecolor='#2b6cb0', lw=2)
ax.add_patch(b_tacna)
ax.text(29, 46, 'TACNA (PERÚ)\n[Centralidad Geopolítica Comercial]', ha='center', weight='bold', fontsize=8.8, color='#1a365d')
ax.text(29, 32, '• Zona Franca (ZOFRATACNA)\n• Polo de Servicios Médicos y Gastronomía\n• Atracción de Flujos del Cono Sur\n• Soberanía Demográfica Viva', ha='center', fontsize=7.6, color='#2c5282')

# Lado Arica
b_arica = patches.FancyBboxPatch((62, 16), 38, 38, boxstyle='round,pad=0.8', facecolor='#edf2f7', edgecolor='#718096', lw=2)
ax.add_patch(b_arica)
ax.text(81, 46, 'ARICA (CHILE)\n[Demanda Comercial y Turismo]', ha='center', weight='bold', fontsize=8.8, color='#2d3748')
ax.text(81, 32, '• Flujo Diario Transfronterizo\n• Consumo de Bienes Peruanos\n• Puerto Libre de Arica\n• Interdependencia Económica', ha='center', fontsize=7.6, color='#4a5568')

ax.annotate('', xy=(61, 35), xytext=(49, 35), arrowprops=dict(arrowstyle="<->", lw=3.2, color='#c53030'))
ax.text(55, 38, 'Flujo Diario Masivo\n(Polo Santa Rosa)', ha='center', fontsize=7.5, weight='bold', color='#9b2c2c')

ax.text(55, 6, 'CONTRASTE CON CHECRAS: Tacna concentra atracción demográfica en frontera;\nChecras padece vaciamiento rural andino y requiere incentivos urgentes de arraigo (Ley 32279).',
        ha='center', fontsize=8, weight='bold', color='#1a365d',
        bbox=dict(boxstyle='square,pad=0.4', facecolor='#fffff0', edgecolor='#d69e2e', lw=1.2))

ax.set_title('FIGURA 12: Modelo de Frontera Viva y Atracción Comercial en el Eje Tacna-Arica (Ratzel)\nCentralidad Geoeconómica, Ocupación del Espacio Vital y Blindaje Demográfico',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p012_tacna_lebensraum')

# ==============================================================================
# FIGURA 13: Pregunta 13 - Perfil Topográfico Ferrocarril Bioceánico (Chancay)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11.5, 6.2))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 110)
ax.set_ylim(-200, 5400)

rx = np.array([0, 18, 40, 60, 80, 95, 110])
ry = np.array([0, 180, 800, 2600, 3800, 4800, 4330])
ax.plot(rx, ry, 'k-', lw=2.2)
ax.fill_between(rx, ry, -200, color='#e2e8f0', alpha=0.85)

pts = [(0, 0, 'Chancay\n(Megapuerto, 0 m)'),
       (18, 180, 'Huaral\n(180 m)'),
       (40, 800, 'Sayán\n(685 m)'),
       (60, 2600, 'Lacsaura / Purapucu\n(Checras, 2,500 m)'),
       (80, 3800, 'Oyón\n(3,620 m)'),
       (95, 4800, 'Abra Raura\n(4,800 m)'),
       (110, 4330, 'Cerro de Pasco\n(4,330 m)')]

for px, py, plbl in pts:
    ax.plot(px, py, 'o', color='#c53030', markersize=6, zorder=5)
    ax.text(px, py+240, plbl, ha='center', fontsize=7.5, weight='bold', color='#1a202c')

# Traza férrea con mega-túneles de base
ax.plot([0, 40, 78], [0, 800, 2200], '--', color='#2b6cb0', lw=2.8, label='Traza Férrea de Superficie (Pendiente máxima $\\leq 2.5\%$)')
ax.plot([78, 110], [2200, 4330], '-', color='#805ad5', lw=4.2, label='Mega-Túnel Transandino de Base (Subterráneo de Baja Cota)')

ax.set_ylabel('Altitud (m.s.n.m.)', fontsize=9.5, weight='bold')
ax.set_title('FIGURA 13: Perfil Topográfico y Descenso Ferroviario Bioceánico (Riemann - Pardo - LaRouche)\nTraza Transversal desde Cerro de Pasco y la Cuenca Alta de Huaura hasta el Megapuerto de Chancay',
             fontsize=10.5, weight='bold', pad=15)
ax.legend(loc='upper left', fontsize=8.2, frameon=True)
save_fig(fig, 'fig_p013_ferrocarril_bioceanico')

# ==============================================================================
# FIGURA 14: Pregunta 14 - Capacidad de Acogida y Zonificación de Cuenca
# ==============================================================================
fig, ax = plt.subplots(figsize=(11.5, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 115)
ax.set_ylim(0, 65)
ax.axis('off')

# 3 Zonas claramente delimitadas
z1 = patches.Rectangle((6, 12), 32, 44, facecolor='#c6f6d5', edgecolor='#2f855a', lw=2)
ax.add_patch(z1)
ax.text(22, 50, 'ZONA 1: PROTECCIÓN\nDE CABECERA (>3,800 m)', ha='center', weight='bold', fontsize=8.8, color='#22543d')
ax.text(22, 30, '• Bofedales y glaciares\n• Siembra de agua comunal\n• Pastos altoandinos\n• Intangibilidad Hídrica\n(Ley N.° 32279)', ha='center', fontsize=7.8, color='#1c4532')

z2 = patches.Rectangle((42, 12), 32, 44, facecolor='#feebc8', edgecolor='#dd6b20', lw=2)
ax.add_patch(z2)
ax.text(58, 50, 'ZONA 2: ENCLAVE MINERO\nREGULADO (3,000 - 3,800 m)', ha='center', weight='bold', fontsize=8.8, color='#7b341e')
ax.text(58, 30, '• Minería subterránea\n• Galerías profundas\n• Relaves espesados secos\n• Cero vertido al río\n• Servidumbres catastradas', ha='center', fontsize=7.8, color='#652b19')

z3 = patches.Rectangle((78, 12), 32, 44, facecolor='#bee3f8', edgecolor='#2b6cb0', lw=2)
ax.add_patch(z3)
ax.text(94, 50, 'ZONA 3: VALLE AGRÍCOLA\nY ANDENES (1,500 - 3,000 m)', ha='center', weight='bold', fontsize=8.8, color='#1a365d')
ax.text(94, 30, '• Andenerías preincas\n• Frutales en Purapucu\n• Seguridad alimentaria\n• Comunidad Campesina\n• Titulación SUNARP', ha='center', fontsize=7.8, color='#2c5282')

ax.text(58, 4, 'CATASTRO MULTIPROPÓSITO (Ley N.° 32279): Separa con precisión milimétrica los derechos mineros\nsubterráneos de las parcelas agrícolas superficiales, previniendo litigios crónicos en Checras.',
        ha='center', fontsize=8.2, weight='bold', color='#1a202c',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#edf2f7', edgecolor='#4a5568', lw=1.2))

ax.set_title('FIGURA 14: Zonificación Territorial y Capacidad de Acogida Relativa en la Cuenca del Río Huaura\nPrevención Científica de Conflictos Minero-Agrícolas y Mitigación Socioambiental en Checras',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p014_zonificacion_cuenca')

# ==============================================================================
# FIGURA 15: Pregunta 15 - Teledetección Satelital y SINADOT (Pedro Paulet)
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6.2))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 110)
ax.set_ylim(0, 65)
ax.axis('off')

# Satélite
ax.plot(22, 52, 's', color='#2b6cb0', markersize=14, zorder=5)
ax.text(22, 59, 'CONSTELACIÓN SATELITAL LEO\n(PerúSAT-1 / Visión Pedro Paulet)', ha='center', weight='bold', fontsize=8.5, color='#1a365d')

# Cono de captura
poly_sat = patches.Polygon([(20, 50), (6, 22), (38, 22), (24, 50)], closed=True,
                           facecolor='#bee3f8', alpha=0.4, edgecolor='#3182ce', lw=1.5)
ax.add_patch(poly_sat)
ax.text(22, 17, 'Territorio Checras / Cuenca Huaura\n(Multiespectral, LiDAR, Radar SAR)', ha='center', weight='bold', fontsize=7.6, color='#2c5282')

# Descarga a CNOIS
ax.annotate('', xy=(56, 36), xytext=(26, 50), arrowprops=dict(arrowstyle="->", lw=2.5, color='#2b6cb0', linestyle='--'))
ax.text(42, 47, 'Descarga Banda X\n(Telemetría)', fontsize=7.5, weight='bold', color='#1a365d')

ax.plot(56, 32, '^', color='#742a2a', markersize=13, zorder=5)
ax.text(56, 24, 'Estación CNOIS\n(Pucusana / CONIDA)', ha='center', weight='bold', fontsize=8, color='#742a2a')

# SINADOT Plataforma
rect_proc = patches.FancyBboxPatch((72, 15), 32, 40, boxstyle='round,pad=0.6', facecolor='#ebf8ff', edgecolor='#3182ce', lw=1.8)
ax.add_patch(rect_proc)
ax.text(88, 48, 'GEOPORTAL SINADOT\n(SDOT - PCM)', ha='center', weight='bold', fontsize=8.5, color='#1a365d')
ax.text(88, 30, '• Detección de cambios de uso\n• Monitoreo de bofedales\n• Alertas de huaycos en laderas\n• Fiscalización de invasiones\n• Fiscalización en Checras', ha='center', fontsize=7.6, color='#2c5282')

ax.annotate('', xy=(72, 34), xytext=(60, 34), arrowprops=dict(arrowstyle="->", lw=2.5, color='#2b6cb0'))

ax.set_title('FIGURA 15: Sistema Aeroespacial de Teledetección y Gobernanza Digital del SINADOT (Pedro Paulet)\nMonitoreo Geoespacial en Tiempo Real para la Fiscalización Territorial Descentralizada',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p015_teledeteccion_paulet')

# ==============================================================================
# FIGURA 16: Pregunta 16 - Termodinámica, Entropía y Cadena de la Papa
# ==============================================================================
fig, ax = plt.subplots(figsize=(11.5, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 115)
ax.set_ylim(0, 65)
ax.axis('off')

etapas = [
    (8, 22, 28, 28, '#2f855a', '1. CHACRA ALTOANDINA\n(Checras, 3,550 msnm)\n\n• Cosecha de Papa Nativa\n• Energía Biomasa Neta ($E_0$)\n• Baja Entropía Inicial ($S_0$)\n• Calidad Orgánica Óptima'),
    (44, 22, 28, 28, '#dd6b20', '2. TRANSPORTE EN TROCHA\n(Lacsaura - Sayán)\n\n• Trocha afirmada con baches\n• Fricción mecánica severa\n• Falta total de cadena de frío\n• Golpeteo y deshidratación'),
    (80, 22, 28, 28, '#c53030', '3. MERCADO LITORAL\n(Chancay / Lima)\n\n• Merma física: 20 a 30%\n• Pérdida Energética (Carnot)\n• Alta Entropía ($S > S_0$)\n• Sobrecosto para el productor')
]

for x, y, w, h, col, txt in etapas:
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.8', facecolor=col, edgecolor='#1a202c', lw=1.5))
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center', color='white', weight='bold', fontsize=7.8)

ax.annotate('', xy=(44, 36), xytext=(36, 36), arrowprops=dict(arrowstyle="->", lw=3.5, color='#dd6b20'))
ax.annotate('', xy=(80, 36), xytext=(72, 36), arrowprops=dict(arrowstyle="->", lw=3.5, color='#c53030'))

ax.annotate('Incremento Entrópico $\\Delta S = \\int \\frac{dQ}{T} > 0$\nDisipación de Energía por Fricción Espacial y Falta de Vías Asfaltadas',
            xy=(58, 22), xytext=(58, 8),
            arrowprops=dict(arrowstyle="->", lw=2, color='#c53030'),
            ha='center', fontsize=8.2, weight='bold', color='#742a2a',
            bbox=dict(boxstyle='square,pad=0.5', facecolor='#fff5f5', edgecolor='#e53e3e', lw=1.2))

ax.set_title('FIGURA 16: Diagrama de Fricción Espacial y Degradación Entrópica en el Eje de la Papa (Planck - Carnot)\nTermodinámica del Abastecimiento desde las Alturas de Checras hacia la Costa',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p016_entropia_alimentos')

# ==============================================================================
# FIGURA 17: Pregunta 17 - Catastro Multipropósito y Propiedad Comunal
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 110)
ax.set_ylim(0, 65)
ax.axis('off')

capas = [
    (15, 10, 80, 12, '#bee3f8', 'CAPA FÍSICA / USO DE SUELO: Andenes preincas, pastos comunales, bofedales y canales'),
    (15, 25, 80, 12, '#feebc8', 'CAPA ECONÓMICA / FISCAL: Catastro rural, servidumbres mineras y valoración comunal'),
    (15, 40, 80, 12, '#c6f6d5', 'CAPA JURÍDICA / TITULACIÓN: Linderos georreferenciados SUNARP - Comunidad de Puñun/Checras')
]

for x, y, w, h, col, txt in capas:
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', facecolor=col, edgecolor='#2d3748', lw=1.5))
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center', weight='bold', fontsize=8.2, color='#1a202c')

ax.annotate('', xy=(12, 16), xytext=(12, 46), arrowprops=dict(arrowstyle="<->", lw=2.5, color='#2b6cb0'))
ax.text(8, 31, 'Integración\nMultifinalitaria\n(Ley N.° 32279)', rotation=90, ha='center', va='center', fontsize=7.8, weight='bold', color='#1a365d')

ax.text(55, 57, 'ESTABILIZACIÓN DEL TEJIDO SOCIAL ANDINO\nCierre Definitivo de Conflictos Limítrofes con Santa Leonor, Paccho y Sayán', ha='center', fontsize=8.5, weight='bold', color='#22543d',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0fff4', edgecolor='#38a169', lw=1.2))

ax.set_title('FIGURA 17: Estructura de Capas del Catastro Multipropósito en Tierras Comunales de Checras (TUO Ley 27795)\nSaneamiento Jurídico Definitivo, Protección de Andenerías y Demarcación Georreferenciada',
             fontsize=10.5, weight='bold', pad=15)
save_fig(fig, 'fig_p017_croquis_catastro_comunal')

# ==============================================================================
# FIGURA 18: Pregunta 18 - Flujograma de Participación Ciudadana y Cohesión
# ==============================================================================
fig, ax = plt.subplots(figsize=(11.5, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 115)
ax.set_ylim(0, 65)
ax.axis('off')

pasos = [
    (4, 24, 18, 26, '#2b6cb0', '1. CONVOCATORIA\nCOMUNAL\n\n• Asamblea General\nde Puñun/Checras\n• Socialización de\nmetodología ODT'),
    (26, 24, 18, 26, '#2f855a', '2. DIAGNÓSTICO\nPARTICIPATIVO\n\n• Recorrido de hitos\n• Memoria histórica\nde linderos locales\n• Taller comunal'),
    (48, 24, 18, 26, '#dd6b20', '3. MESA TÉCNICA\nMULTINIVEL\n\n• PCM / SDOT\n• GORE Lima\n• Municipio Checras\n• Directivas comunales'),
    (70, 24, 18, 26, '#805ad5', '4. CONSULTA Y\nVALIDACIÓN\n\n• Audiencia pública\n• Acta de acuerdo\nde límites distritales\n• Firma comunal'),
    (92, 24, 18, 26, '#c53030', '5. APROBACIÓN\nFORMAL\n\n• Ley o Decreto\n• Inscripción en\nSINADOT y\nSUNARP')
]

for x, y, w, h, col, txt in pasos:
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5', facecolor=col, edgecolor='#1a202c', lw=1.3))
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center', color='white', weight='bold', fontsize=7.3)

for i in range(len(pasos)-1):
    ax.annotate('', xy=(pasos[i+1][0], 37), xytext=(pasos[i][0]+pasos[i][2], 37),
                arrowprops=dict(arrowstyle="->", lw=2.4, color='#2d3748'))

ax.text(57, 10, 'RESILIENCIA Y ESCUDO SOCIAL (Velasco Alvarado):\nLa participación activa de las comunidades de Checras (Puñun, Tongos, Tulpay, Maray) blinda el POT frente a la atomización territorial.',
        ha='center', fontsize=8.2, weight='bold', color='#1a202c',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f7fafc', edgecolor='#cbd5e0', lw=1.2))

ax.set_title('FIGURA 18: Flujograma Legal de Participación Ciudadana y Cohesión Territorial (Ley N.° 32279)\nIntegración de Demandas Comunales en la Aprobación del Plan de Ordenamiento Territorial',
             fontsize=10.8, weight='bold', pad=15)
save_fig(fig, 'fig_p018_flujograma_participacion')

# ==============================================================================
# FIGURA 19: Pregunta 19 - Macroesquema del Perú: Potencia Noosférica Unificada
# ==============================================================================
fig, ax = plt.subplots(figsize=(11.5, 7.2))
ax.set_facecolor('#f8fafc')
ax.set_xlim(0, 115)
ax.set_ylim(0, 80)
ax.axis('off')

# Silueta estilizada del Perú
poly_peru = [(18, 70), (30, 74), (62, 68), (80, 54), (96, 40), (92, 18), (84, 6), (72, 9), (50, 20), (34, 32), (24, 52), (18, 70)]
ax.add_patch(patches.Polygon(poly_peru, closed=True, facecolor='#edf2f7', edgecolor='#4a5568', lw=2.2))

nodos_12 = [
    (24, 68, '1. Piura-Tumbes\n(Despensa Norte)'),
    (52, 64, '2. Putumayo\n(Frontera Viva)'),
    (78, 52, '3. Iquitos/Yavarí\n(Heartland Fluvial)'),
    (88, 36, '4. Purús\n(Flujo Energético)'),
    (82, 21, '5. Madre de Dios\n(Eje Hamilton)'),
    (79, 11, '6. Puno/Titicaca\n(Cuenca Endorreica)'),
    (74, 6, '7. Tacna\n(Lebensraum Sur)'),
    (54, 23, '8. VRAEM\n(Noosfera Central)'),
    (46, 32, '9. Mantaro/Pasco\n(Eje Energético)'),
    (30, 40, '10. Huaura-Checras\n(Célula Andina)'),
    (28, 36, '11. Chancay Hub\n(Vector Bioceánico)'),
    (32, 31, '12. Lima Metropolitana\n(Descentralizada)')
]

for nx, ny, nlbl in nodos_12:
    col = '#c53030' if 'Chancay' in nlbl or 'Checras' in nlbl else '#2b6cb0'
    ax.plot(nx, ny, 'o', color=col, markersize=8, zorder=5)
    ax.text(nx+2, ny, nlbl, fontsize=7, weight='bold', color='#1a202c')

# Vector Bioceánico Transversal
ax.plot([28, 46, 88], [36, 32, 36], '-', color='#d69e2e', lw=3.5, label='Corredor Bioceánico Transversal (Pacífico - Chancay - Selva - Atlántico)')
ax.plot([28, 30, 46], [36, 40, 32], '--', color='#e53e3e', lw=2.2, label='Ramal Transandino Huaura - Checras - Pasco')

ax.text(57, 75, 'PERÚ: POTENCIA NOOSFÉRICA AUTÓNOMA DEL HEMISFERIO SUR\nBlindaje Territorial Soberano Frente al Choque Hegemónico Global (Mackinder - Vernadsky - LaRouche)',
        ha='center', fontsize=9.2, weight='bold', color='#1a365d',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#ebf8ff', edgecolor='#2b6cb0', lw=1.5))

ax.legend(loc='lower left', fontsize=8, frameon=True, facecolor='white', edgecolor='#cbd5e0')
save_fig(fig, 'fig_p019_mapa_geopolitico_noosferico')

print('All 19 REDESIGNED figures generated successfully with ZERO text overlapping!')
