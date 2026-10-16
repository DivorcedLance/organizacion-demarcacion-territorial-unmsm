import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

os.makedirs('figuras_pcd', exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

def save_fig(fig, name):
    svg_path = os.path.join('figuras_pcd', f'{name}.svg')
    pdf_path = os.path.join('figuras_pcd', f'{name}.pdf')
    fig.savefig(svg_path, format='svg', bbox_inches='tight')
    fig.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f'Saved {name} (.svg & .pdf)')

# ==============================================================================
# FIGURA 1: Pregunta 1 - Curvatura Espacio-Temporal y Flujo Chancay - Shanghái
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_facecolor('#f4f7f9')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Nodos
ax.plot([15, 85], [30, 30], 'o', color='#1a365d', markersize=10)
ax.text(12, 33, 'Shanghái (Asia Hub)\n[Mercado Central]', fontsize=10, weight='bold', color='#1a365d')
ax.text(82, 33, 'Puerto de Chancay\n[Hub Megapuerto del Pacífico]', fontsize=10, weight='bold', color='#0d6938')

# Ruta tradicional quebrada (35-42 días)
trad_x = [85, 75, 45, 25, 15]
trad_y = [30, 48, 52, 45, 30]
ax.plot(trad_x, trad_y, '--', color='#c53030', linewidth=2.5, label='Ruta Tradicional (35 - 45 días, transbordos en California / Manzanillo)')
for x, y, lbl in [(75, 48, 'Long Beach / Manzanillo'), (45, 52, 'Arco del Pacífico Norte'), (25, 45, 'Yokohama / Busan')]:
    ax.plot(x, y, 's', color='#c53030', markersize=6)
    ax.text(x, y+2, lbl, fontsize=8, color='#742a2a', ha='center')

# Vector directo geodésico no euclidiano (23 días)
direct_x = np.linspace(85, 15, 100)
direct_y = 30 - 8 * np.sin(np.pi * (direct_x - 15) / 70)
ax.plot(direct_x, direct_y, '-', color='#2b6cb0', linewidth=3.5, label='Vector Directo Chancay-Shanghái (23 días, Geodésica No-Euclidiana)')

# Anotaciones teóricas
ax.annotate('Contracción Espacio-Temporal\n(-15 a -20 días de tránsito)\nReducción drástica del tensor métrico de fricción',
            xy=(50, 22), xytext=(50, 10),
            arrowprops=dict(facecolor='#2b6cb0', shrink=0.08, width=1.5, headwidth=7),
            fontsize=9, weight='bold', ha='center', color='#1a365d',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#ebf8ff', edgecolor='#3182ce'))

ax.set_title('FIGURA 1: Geometría No Euclidiana y Contracción Espacio-Temporal en el Eje Chancay-Shanghái\n(Ruptura de la Fricción de Distancia y Vector Geodésico Directo)', fontsize=11, weight='bold', pad=15)
ax.legend(loc='upper center', frameon=True, facecolor='white', edgecolor='#cbd5e0', fontsize=8.5)
save_fig(fig, 'fig_p01_chancay_geometria')

# ==============================================================================
# FIGURA 2: Pregunta 2 - Metabolismo Territorial y Balance Hídrico de Cuencas
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Bloques del metabolismo
blocks = [
    (5, 20, 22, 28, '#2b6cb0', '1. CABECERA ANDINA\n(Checras / Oyón)\n\n• Glaciares y lagunas\n• Bofedales altoandinos\n• Siembra / Cosecha agua\nEntrada Neta ($Q_{in}$)', 'white'),
    (38, 20, 24, 28, '#2f855a', '2. VALLE INTERMEDIO\n(Sayán / Huaura)\n\n• Andenerías y frutales\n• Consumo agrícola\n• Evapotranspiración\nUso Metabólico Biomasa', 'white'),
    (73, 20, 23, 28, '#c53030', '3. NODO LITORAL\n(Chancay / Complejo)\n\n• Demanda megapuerto\n• Parque industrial/urbano\n• Descarga al océano\nDisipación Antrópica', 'white')
]

for x, y, w, h, col, text, tcol in blocks:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=1', facecolor=col, edgecolor='#1a202c', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', color=tcol, fontsize=8.5, weight='bold')

# Flechas de flujo
ax.annotate('', xy=(38, 34), xytext=(27, 34), arrowprops=dict(arrowstyle="->", color='#2b6cb0', lw=3.5))
ax.text(32.5, 37, 'Flujo Fluvial\n$Q_{trans}$', ha='center', fontsize=8, color='#2b6cb0', weight='bold')

ax.annotate('', xy=(73, 34), xytext=(62, 34), arrowprops=dict(arrowstyle="->", color='#2f855a', lw=3.5))
ax.text(67.5, 37, 'Agua Sobrante\n$Q_{neto}$', ha='center', fontsize=8, color='#2f855a', weight='bold')

# Disipación termodinámica (Carnot / Odum)
ax.annotate('Pérdidas Termodinámicas / Polución / Salinización\nEntropía Disipada ($dS/dt > 0$)',
            xy=(84.5, 20), xytext=(84.5, 6),
            arrowprops=dict(arrowstyle="->", color='#c53030', lw=2),
            ha='center', fontsize=8, color='#9b2c2c', weight='bold',
            bbox=dict(boxstyle='square,pad=0.4', facecolor='#fff5f5', edgecolor='#e53e3e'))

ax.annotate('Regulación Hídrica Comunal\n(Ley 32279: Intangibilidad de Cabeceras)',
            xy=(16, 20), xytext=(16, 6),
            arrowprops=dict(arrowstyle="->", color='#2b6cb0', lw=2),
            ha='center', fontsize=8, color='#2c5282', weight='bold',
            bbox=dict(boxstyle='square,pad=0.4', facecolor='#ebf8ff', edgecolor='#3182ce'))

ax.set_title('FIGURA 2: Modelo de Metabolismo Territorial y Balance Termodinámico (Odum - Carnot)\nCuenca del Río Huaura: Desde las Cumbres de Checras al Megapuerto de Chancay', fontsize=10.5, weight='bold', pad=15)
save_fig(fig, 'fig_p02_metabolismo_hidrico')

# ==============================================================================
# FIGURA 3: Pregunta 3 - Corte Estratigráfico Geotécnico (Terzaghi / SINAGERD)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(-35, 25)

# Perfil del terreno
ax.fill_between([0, 100], [0, 0], [-6, -6], color='#f6e05e', alpha=0.8, label='Arena eólica no cohesiva suelta ($N_{SPT} < 10$, riesgo licuefacción)')
ax.fill_between([0, 100], [-6, -6], [-18, -18], color='#cbd5e0', alpha=0.9, label='Grava y arena aluvial semi-densa / arcillas marinas intermedias')
ax.fill_between([0, 100], [-18, -18], [-35, -35], color='#718096', alpha=0.9, label='Basamento rocoso / formación volcano-sedimentaria estable')

# Nivel Freático
ax.plot([0, 100], [-3, -3], 'b--', lw=2, label='Nivel Freático ($NF = -3.00\\text{ m}$, alta saturación)')

# Estructura portuaria sobre pilotes
ax.plot([25, 75], [0, 0], 'k-', lw=3)
rect_super = patches.Rectangle((30, 0), 40, 12, facecolor='#4a5568', edgecolor='black', lw=1.5)
ax.add_patch(rect_super)
ax.text(50, 6, 'MEGAPLATAFORMA LOGÍSTICA / GRÚAS PORTUARIAS\nCarga Admisible Exigida: $q_{adm} > 4.5\\text{ kg/cm}^2$', ha='center', va='center', color='white', weight='bold', fontsize=8.5)

# Pilotes de cimentación profunda
for px in [33, 42, 50, 58, 67]:
    ax.plot([px, px], [0, -22], color='#2d3748', lw=3.5)
    ax.annotate('', xy=(px, -23), xytext=(px, 0), arrowprops=dict(arrowstyle="->", color='#1a202c', lw=2))

ax.text(50, -24, 'Pilotes de Gran Diámetro empotrados en Roca Sana ($> 20\\text{ m}$)\nExigencia Geotécnica Terzaghi - Restricción SINAGERD', ha='center', fontsize=8, weight='bold', color='#1a202c',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#edf2f7', edgecolor='#4a5568'))

ax.set_ylabel('Profundidad Estratigráfica (m)', fontsize=9, weight='bold')
ax.set_title('FIGURA 3: Corte Estratigráfico Geotécnico Sumario del Litoral Chancay-Ancón (Terzaghi)\nRestricciones Físicas y Vulnerabilidad Geológica ante Cargas de Alta Competencia', fontsize=10.5, weight='bold', pad=12)
ax.legend(loc='upper right', fontsize=8, frameon=True)
save_fig(fig, 'fig_p03_corte_suelos_terzaghi')

# ==============================================================================
# FIGURA 4: Pregunta 4 - Autoridad Autónoma Regional de Seguridad Territorial
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 6))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 65)
ax.axis('off')

# Nivel 1: Presidencia / Comando Conjunto
b1 = patches.FancyBboxPatch((25, 48), 50, 12, boxstyle='round,pad=0.8', facecolor='#742a2a', edgecolor='black', lw=1.5)
ax.add_patch(b1)
ax.text(50, 54, 'AUTORIDAD AUTÓNOMA DE INFRAESTRUCTURA CRÍTICA (AAIC)\nComando de Seguridad Territorial Integrado (Civil - Militar)\n[Marco: Ley del Sistema de Seguridad y Defensa Nacional]', ha='center', va='center', color='white', weight='bold', fontsize=8.5)

# Nivel 2: Operador Logístico y Inteligencia
b2 = patches.FancyBboxPatch((8, 26), 38, 12, boxstyle='round,pad=0.8', facecolor='#2b6cb0', edgecolor='black', lw=1.5)
ax.add_patch(b2)
ax.text(27, 32, 'OPERADOR LOGÍSTICO REGIONAL\n(Gestión Portuaria, Aduanas, ZED,\nParque Industrial y Conectividad SINAC)', ha='center', va='center', color='white', weight='bold', fontsize=8)

b3 = patches.FancyBboxPatch((54, 26), 38, 12, boxstyle='round,pad=0.8', facecolor='#2c5282', edgecolor='black', lw=1.5)
ax.add_patch(b3)
ax.text(73, 32, 'DIVISIÓN DE CONTRAINTELIGENCIA Y DEFENSA\n(Monitoreo Radar, Ciberseguridad, Control de\nInversiones Estratégicas y Soberanía Territorial)', ha='center', va='center', color='white', weight='bold', fontsize=8)

# Nivel 3: Gobiernos Locales Subordinados
b4 = patches.FancyBboxPatch((15, 4), 70, 12, boxstyle='round,pad=0.8', facecolor='#2f855a', edgecolor='black', lw=1.5)
ax.add_patch(b4)
ax.text(50, 10, 'GOBIERNOS LOCALES Y COMUNIDADES SUBORDINADAS\n(Sub-zona Litoral: Chancay / Huaral / Huacho | Sub-zona Cuenca Alta: Oyón / Checras)\nGestión de Uso del Suelo, Protección de Andenerías, Agua y Servidumbres', ha='center', va='center', color='white', weight='bold', fontsize=8.2)

# Conexiones jerárquicas
ax.annotate('', xy=(27, 38), xytext=(40, 48), arrowprops=dict(arrowstyle="->", lw=2, color='#742a2a'))
ax.annotate('', xy=(73, 38), xytext=(60, 48), arrowprops=dict(arrowstyle="->", lw=2, color='#742a2a'))
ax.annotate('', xy=(40, 16), xytext=(27, 26), arrowprops=dict(arrowstyle="->", lw=2, color='#2b6cb0'))
ax.annotate('', xy=(60, 16), xytext=(73, 26), arrowprops=dict(arrowstyle="->", lw=2, color='#2c5282'))

ax.set_title('FIGURA 4: Organigrama Espacial de la Autoridad Autónoma Civil-Militar (TVA - Marcas Carolingias)\nEstructura de Gobernanza de Infraestructura Crítica y Blindaje Estratégico', fontsize=10.5, weight='bold', pad=12)
save_fig(fig, 'fig_p04_autoridad_autonoma')

# ==============================================================================
# FIGURA 5: Pregunta 5 - Fuerzas Centrífugas y Ruptura de la Macrocefalia de Lima
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#f7fafc')
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis('off')

# Núcleo Lima
circle_lima = patches.Circle((35, 18), 12, facecolor='#e53e3e', alpha=0.35, edgecolor='#9b2c2c', lw=2)
ax.add_patch(circle_lima)
ax.plot(35, 18, 'o', color='#9b2c2c', markersize=10)
ax.text(35, 18, 'LIMA METROPOLITANA\n(Macrocefalia Histórica\n43 distritos, 10M hab.)', ha='center', va='center', weight='bold', fontsize=8.5, color='#742a2a')

# Nodo Norte Chico (Chancay - Huaral - Huacho - Barranca)
rect_nc = patches.FancyBboxPatch((20, 42), 60, 22, boxstyle='round,pad=1', facecolor='#3182ce', alpha=0.25, edgecolor='#2b6cb0', lw=2)
ax.add_patch(rect_nc)
ax.text(50, 59, 'POLO DESCENTRALIZADO DEL NORTE CHICO\n(Chancay - Huaral - Sayán - Huacho - Barranca)', ha='center', weight='bold', fontsize=9.5, color='#1a365d')

# Nodos del Norte Chico
nodos_nc = [(28, 48, 'Chancay\n(Megapuerto)'), (45, 48, 'Huaral\n(Agro)'), (62, 50, 'Huacho\n(Capital Prov.)'), (72, 52, 'Barranca\n(Pativilca)')]
for x, y, lbl in nodos_nc:
    ax.plot(x, y, 'o', color='#2b6cb0', markersize=8)
    ax.text(x, y-4, lbl, ha='center', fontsize=8, weight='bold', color='#2c5282')

# Eje Cuenca Alta / Checras
ax.plot(58, 62, '^', color='#2f855a', markersize=9)
ax.text(66, 62, 'Checras / Oyón\n(Cabecera)', fontsize=8, weight='bold', color='#22543d')

# Vectores centrífugos de desplazamiento económico
ax.annotate('', xy=(32, 44), xytext=(35, 28), arrowprops=dict(facecolor='#c53030', edgecolor='#9b2c2c', width=3, headwidth=10))
ax.annotate('', xy=(48, 44), xytext=(38, 28), arrowprops=dict(facecolor='#c53030', edgecolor='#9b2c2c', width=2.5, headwidth=9))
ax.annotate('', xy=(62, 44), xytext=(42, 26), arrowprops=dict(facecolor='#c53030', edgecolor='#9b2c2c', width=2, headwidth=8))

ax.text(26, 34, 'Fuerza Centrífuga Logística\n(Ruptura de Centralismo)', rotation=70, fontsize=8, weight='bold', color='#9b2c2c')

ax.set_title('FIGURA 5: Dinámica Centrífuga y Descentralización Espacial (Ratzel - Velasco Alvarado)\nDesplazamiento del Peso Productivo hacia el Eje Litoral Norte Chico y Cuenca de Huaura', fontsize=10.5, weight='bold', pad=12)
save_fig(fig, 'fig_p05_fuerzas_centrifugas')

# ==============================================================================
# FIGURA 6: Pregunta 6 - Transición de Biosfera a Noosfera en el VRAEM
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
for ax in (ax1, ax2):
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.axis('off')

# Panel 1: Biosfera Desordenada
ax1.set_title('(A) BIOSFERA DESORDENADA (VRAEM Estado Inicial)\nEconomía Ilegal y Entropía Social', fontsize=9, weight='bold', color='#742a2a')
np.random.seed(42)
cx = np.random.uniform(5, 45, 18)
cy = np.random.uniform(5, 45, 18)
ax1.scatter(cx, cy, s=80, color='#e53e3e', marker='x', label='Parcelas de coca ilegal')
for i in range(12):
    ax1.plot([cx[i], cx[(i+3)%18]], [cy[i], cy[(i+3)%18]], ':', color='#cbd5e0', lw=1)
ax1.text(25, 3, 'Fragmentación, Aislamiento, Narcotráfico y Violencia', ha='center', fontsize=8, color='#742a2a', weight='bold')

# Panel 2: Noosfera Organizada
ax2.set_title('(B) NOOSFERA ORGANIZADA (Vernadsky - Antúnez de Mayolo)\nCorredores Industriales y Alta Densidad Energética', fontsize=9, weight='bold', color='#22543d')
# Red troncal de transporte
ax2.plot([10, 40], [10, 40], '-', color='#2b6cb0', lw=4, label='Eje Vial Asfaltado')
ax2.plot([10, 40], [40, 10], '-', color='#2f855a', lw=3, label='Red Eléctrica / Línea Transmisión')
# Nodos agroindustriales
for nx, ny, name in [(15, 15, 'Hub Cacao'), (25, 25, 'C.H. Antúnez de Mayolo\n[Potencia MW]'), (35, 35, 'Parque Agroindustrial')]:
    ax2.plot(nx, ny, 's', color='#1a365d', markersize=9)
    ax2.text(nx+2, ny-1, name, fontsize=7.5, weight='bold', color='#1a365d')
ax2.text(25, 3, 'Integración Energética, Soberanía y Seguridad Nacional', ha='center', fontsize=8, color='#22543d', weight='bold')

fig.suptitle('FIGURA 6: Transformación Territorial en el VRAEM: De la Biosfera Ilícita a la Noosfera Energética', fontsize=10.5, weight='bold')
save_fig(fig, 'fig_p06_noosfera_vraem')

# ==============================================================================
# FIGURA 7: Pregunta 7 - Sistema Hamilton-Carey vs. Minería Ilegal (Madre de Dios)
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.2))
for ax in (ax1, ax2):
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 60)
    ax.axis('off')

# Lado 1: Ciclo Vicioso Libre Mercado Desregulado
ax1.set_title('CICLO DESTRUCTIVO (Minería Ilegal)\nLibre Mercado Desregulado', fontsize=9, weight='bold', color='#9b2c2c')
steps1 = [(25, 50, 'Ausencia Estatal /\nDesregulación'),
          (40, 36, 'Minería Aluvial Ilegal\n(Uso masivo de Mercurio)'),
          (34, 18, 'Deforestación y Trata\nDestrucción Ecosistémica'),
          (14, 26, 'Contrabando y Fuga de Capital\nPérdida de Soberanía')]
for x, y, txt in steps1:
    rect = patches.FancyBboxPatch((x-10, y-5), 20, 10, boxstyle='round,pad=0.3', facecolor='#fff5f5', edgecolor='#e53e3e', lw=1.2)
    ax1.add_patch(rect)
    ax1.text(x, y, txt, ha='center', va='center', fontsize=7.5, weight='bold', color='#742a2a')
for i in range(len(steps1)):
    p1 = steps1[i]
    p2 = steps1[(i+1)%len(steps1)]
    ax1.annotate('', xy=(p2[0], p2[1]), xytext=(p1[0], p1[1]), arrowprops=dict(arrowstyle="->", lw=1.8, color='#e53e3e'))

# Lado 2: Ciclo Virtuoso Hamilton - Carey
ax2.set_title('CICLO VIRTUOSO NACIONAL (Hamilton - Carey)\nProteccionismo, Catastro y Obra Pública', fontsize=9, weight='bold', color='#1a365d')
steps2 = [(25, 50, 'Catastro Multipropósito\n(Ley 32279: Seguridad Jurídica)'),
          (40, 36, 'Inversión en Infraestructura\n(Carreteras, Energía Limpia)'),
          (34, 18, 'Industrialización Local\n(Agroforestería, Valor Agregado)'),
          (14, 26, 'Reinversión y Blindaje Territorial\nSoberanía Económica')]
for x, y, txt in steps2:
    rect = patches.FancyBboxPatch((x-10, y-5), 20, 10, boxstyle='round,pad=0.3', facecolor='#ebf8ff', edgecolor='#3182ce', lw=1.2)
    ax2.add_patch(rect)
    ax2.text(x, y, txt, ha='center', va='center', fontsize=7.5, weight='bold', color='#1a365d')
for i in range(len(steps2)):
    p1 = steps2[i]
    p2 = steps2[(i+1)%len(steps2)]
    ax2.annotate('', xy=(p2[0], p2[1]), xytext=(p1[0], p1[1]), arrowprops=dict(arrowstyle="->", lw=1.8, color='#3182ce'))

fig.suptitle('FIGURA 7: Contrapunto Geoeconómico en Madre de Dios: Extractivismo Ilegal vs. Sistema Nacional Americano', fontsize=10.5, weight='bold')
save_fig(fig, 'fig_p07_hamilton_carey_mdd')

# ==============================================================================
# FIGURA 8: Pregunta 8 - Heartland Amazónico y Fortines Noosféricos (Putumayo-Yavarí)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 5.5))
ax.set_facecolor('#f0fff4')
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.axis('off')

# Línea de frontera fluvial
t = np.linspace(5, 95, 100)
f_y = 25 + 6 * np.sin(t / 8)
ax.plot(t, f_y, '-', color='#276749', lw=3, label='Frontera Fluvial Internacional (Río Putumayo / Yavarí)')

# Zonas
ax.text(50, 43, 'TERRITORIO EXTRANJERO (VECINOS DEL NORTE / ORIENTE)', ha='center', fontsize=9, color='#718096', weight='bold')
ax.text(50, 7, 'HEARTLAND AMAZÓNICO PERUANO (ZONAS DE DESARROLLO INTEGRADO)', ha='center', fontsize=9, color='#22543d', weight='bold')

# Fortines Noosféricos a lo largo de la línea
fortines = [(15, 23, 'Fortín 1: Güeppí\n[Radar + Base Fluvial]'),
            (40, 28, 'Fortín 2: San Antonio\n[Monitoreo + Telemedicina]'),
            (65, 21, 'Fortín 3: El Estrecho\n[C2 Satelital + Aeródromo]'),
            (88, 29, 'Fortín 4: Islandia/Yavarí\n[Aduana + Control Dual]')]

for x, y, name in fortines:
    ax.plot(x, y, 's', color='#c53030', markersize=9)
    ax.plot(x, y, 'o', color='#ecc94b', markersize=4)
    ax.annotate(name, xy=(x, y), xytext=(x, y-10),
                arrowprops=dict(facecolor='#c53030', shrink=0.08, width=1, headwidth=5),
                fontsize=7.5, weight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#c53030'))

ax.set_title('FIGURA 8: Dispositivo Lineal de "Fortines Noosféricos" en las Fronteras Vivas del Putumayo y Yavarí\n(Ocupación Efectiva y Administración Estratégica Civil-Militar según Mackinder y Putin)', fontsize=10.5, weight='bold', pad=12)
save_fig(fig, 'fig_p08_heartland_amazonico')

# ==============================================================================
# FIGURA 9: Pregunta 9 - Densidad de Flujo Energético y Corredores en Purús
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Nodos
ax.plot(15, 30, 'o', color='#1a365d', markersize=10)
ax.text(15, 33, 'Pucallpa (Ucayali)\n[Conexión Red Nacional SINAC]', ha='center', weight='bold', fontsize=8.5, color='#1a365d')

ax.plot(85, 30, 's', color='#c53030', markersize=10)
ax.text(85, 33, 'Puerto Esperanza (Purús)\n[Enclave Aislado Histórico]', ha='center', weight='bold', fontsize=8.5, color='#c53030')

# Barrera verde (reserva estricta preservacionista)
rect_res = patches.Rectangle((35, 10), 30, 40, facecolor='#c6f6d5', edgecolor='#38a169', lw=2, linestyle='--')
ax.add_patch(rect_res)
ax.text(50, 44, 'BARRERA AMBIENTAL RADICAL\n(Tesis Anglo-Ambientalista:\nAislamiento Artificial del Enclave)', ha='center', fontsize=8, weight='bold', color='#22543d')

# Corredor multimodal propuesto (LaRouche / TUO Ley 27795)
ax.plot([15, 35, 65, 85], [30, 22, 22, 30], color='#d69e2e', lw=3.5, linestyle='-', label='Corredor Multimodal Ecológico Subterráneo / Férreo de Bajo Impacto')
ax.plot([15, 85], [26, 26], color='#3182ce', lw=2, linestyle=':', label='Línea de Alta Densidad Energética y Fibra Óptica')

ax.annotate('Incremento de la Densidad de Flujo Energético por $km^2$\n(Integración a la Economía Física Soberana)',
            xy=(50, 22), xytext=(50, 8),
            arrowprops=dict(facecolor='#d69e2e', shrink=0.08, width=1.5, headwidth=6),
            fontsize=8.5, weight='bold', ha='center', color='#744210',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fefcbf', edgecolor='#d69e2e'))

ax.set_title('FIGURA 9: Densidad de Flujo Energético y Corredores Multimodales en el Aislamiento de Purús\nSuperación de Enclaves y Articulación Territorial de Alta Tecnología (Lyndon LaRouche)', fontsize=10, weight='bold', pad=12)
ax.legend(loc='upper left', fontsize=8)
save_fig(fig, 'fig_p09_densidad_flujo_purus')

# ==============================================================================
# FIGURA 10: Pregunta 10 - Ecorregiones de Humboldt y Choque ENOS (Piura-Tumbes)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Litoral Norte y Masas Oceánicas
ax.plot([50, 50], [0, 60], 'k-', lw=1.5) # Línea de costa esquemática
ax.text(75, 52, 'CONTINENTE (Cuencas Piura - Tumbes)\n[Despensa Agroexportadora]', ha='center', weight='bold', fontsize=9, color='#2f855a')
ax.text(25, 52, 'OCÉANO PACÍFICO ORIENTAL\n[Interfase Oceanográfica]', ha='center', weight='bold', fontsize=9, color='#2b6cb0')

# Flecha Corriente de Humboldt (Fría, del Sur)
ax.annotate('', xy=(30, 28), xytext=(30, 5), arrowprops=dict(facecolor='#3182ce', edgecolor='#1a365d', width=5, headwidth=12))
ax.text(18, 15, 'Corriente Fría\nde Humboldt\n($14^\\circ - 17^\\circ\\text{C}$)', fontsize=8, weight='bold', color='#1a365d')

# Flecha Masa El Niño (Cálida, del Norte)
ax.annotate('', xy=(30, 32), xytext=(30, 55), arrowprops=dict(facecolor='#e53e3e', edgecolor='#9b2c2c', width=5, headwidth=12))
ax.text(18, 45, 'Ondas Kelvin / El Niño\nAguas Cálidas\n($> 26^\\circ - 29^\\circ\\text{C}$)', fontsize=8, weight='bold', color='#9b2c2c')

# Zona de Choque y Lluvias
rect_choque = patches.Rectangle((32, 25), 35, 10, facecolor='#ecc94b', alpha=0.5, edgecolor='#d69e2e', lw=2)
ax.add_patch(rect_choque)
ax.text(49.5, 30, 'ZONA DE CONVERGENCIA INTERTROPICAL / CHOQUE TÉRMICO\nLluvias Torrenciales Excepcionales (ENOS 2026-2027)\nActivación de Quebradas y Ruptura de Presas', ha='center', va='center', weight='bold', fontsize=8, color='#744210')

# Impacto en Cuenca y Gestión SINAGERD
ax.annotate('Restricción SINAGERD:\nDiques, Defensas Ribereñas y Drenaje Pluvial',
            xy=(67, 30), xytext=(75, 18),
            arrowprops=dict(arrowstyle="->", color='#c53030', lw=2),
            fontsize=8, weight='bold', color='#742a2a',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff5f5', edgecolor='#e53e3e'))

ax.set_title('FIGURA 10: Choque Ecorregional de Humboldt vs. El Niño en el Litoral Norte (Piura - Tumbes)\nInterdependencia Hídrica y Absorción Obligatoria de Riesgos (SINAGERD - Ley 32279)', fontsize=10, weight='bold', pad=12)
save_fig(fig, 'fig_p010_humboldt_elnino')

# ==============================================================================
# FIGURA 11: Pregunta 11 - Cuenca Endorreica del Titicaca y Blindaje Ambiental
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Cubeta del lago
lake = patches.Ellipse((50, 25), 55, 20, facecolor='#63b3ed', edgecolor='#2b6cb0', lw=2.5)
ax.add_patch(lake)
ax.text(50, 25, 'LAGO TITICACA (Cuenca Endorreica Cerrada)\n[Recurso Hídrico Binacional Estratégico Perú - Bolivia]', ha='center', va='center', weight='bold', fontsize=8.5, color='#1a365d')

# Fuentes de Contaminación
# Río Ramis (Minería La Rinconada)
ax.annotate('Río Ramis / Crucero\n(Metales Pesados: $Hg, As, Pb$\nde Minería La Rinconada/Ananea)',
            xy=(35, 33), xytext=(15, 48),
            arrowprops=dict(arrowstyle="->", color='#c53030', lw=2.5),
            fontsize=8, weight='bold', color='#742a2a',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#fff5f5', edgecolor='#e53e3e'))

# Río Coata (Efluentes Urbanos Juliaca)
ax.annotate('Río Coata\n(Aguas residuales no tratadas de Juliaca)',
            xy=(45, 33), xytext=(55, 48),
            arrowprops=dict(arrowstyle="->", color='#c53030', lw=2.5),
            fontsize=8, weight='bold', color='#742a2a',
            bbox=dict(boxstyle='square,pad=0.3', facecolor='#fff5f5', edgecolor='#e53e3e'))

# Desaguadero (Salida única y taponamiento)
ax.plot([72, 90], [20, 12], '-', color='#2b6cb0', lw=3)
ax.text(90, 12, 'Río Desaguadero\n(Salida mínima, acumulación de contaminantes)', fontsize=7.5, weight='bold', color='#2c5282')

# Blindaje Territorial
ax.text(50, 7, 'BLINDAJE TERRITORIAL SOBERANO (Ley 32279 y Ley de Seguridad Nacional)\nTratamiento en Cabeceras, Fiscalización Militar-Ambiental y Preservación del Acuífero', ha='center', fontsize=8.5, weight='bold', color='#22543d',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0fff4', edgecolor='#38a169'))

ax.set_title('FIGURA 11: Metabolismo de la Cuenca Endorreica del Titicaca y Vulnerabilidad Ecosistémica (Odum)\nPuntos Críticos de Contaminación Minero-Urbana y Necesidad de Blindaje Territorial', fontsize=10, weight='bold', pad=12)
save_fig(fig, 'fig_p011_titicaca_endorreico')

# ==============================================================================
# FIGURA 12: Pregunta 12 - Frontera Viva Tacna-Arica y Dinámica de Lebensraum
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Línea divisoria de frontera
ax.plot([50, 50], [5, 55], '--', color='#4a5568', lw=2)
ax.text(50, 57, 'LÍNEA DE LA CONCORDIA (Hito N° 1)', ha='center', weight='bold', fontsize=9, color='#4a5568')

# Lado Tacna
rect_tacna = patches.FancyBboxPatch((8, 15), 35, 35, boxstyle='round,pad=0.8', facecolor='#ebf8ff', edgecolor='#2b6cb0', lw=2)
ax.add_patch(rect_tacna)
ax.text(25.5, 43, 'TACNA (PERÚ)\n[Centralidad Geopolítica Comercial]', ha='center', weight='bold', fontsize=9, color='#1a365d')
ax.text(25.5, 30, '• Zona Franca (ZOFRATACNA)\n• Mercados y Servicios Médicos\n• Polo de Atracción Fronteriza\n• Blindaje de Soberanía Comercial', ha='center', fontsize=7.5, color='#2c5282')

# Lado Arica
rect_arica = patches.FancyBboxPatch((57, 15), 35, 35, boxstyle='round,pad=0.8', facecolor='#edf2f7', edgecolor='#718096', lw=2)
ax.add_patch(rect_arica)
ax.text(74.5, 43, 'ARICA (CHILE)\n[Nodo Portuario e Inversión Externa]', ha='center', weight='bold', fontsize=9, color='#2d3748')
ax.text(74.5, 30, '• Consumo de Bienes Peruanos\n• Flujo Turístico / Comercio Diario\n• Presión de Capitales del Cono Sur\n• Demanda de Mano de Obra y Agro', ha='center', fontsize=7.5, color='#4a5568')

# Flujos bidireccionales
ax.annotate('', xy=(56, 32), xytext=(44, 32), arrowprops=dict(arrowstyle="<->", lw=3, color='#c53030'))
ax.text(50, 35, 'Flujo Diario Masivo\n(Paso Santa Rosa)', ha='center', fontsize=7.5, weight='bold', color='#9b2c2c')

# Contraste con Checras
ax.text(50, 6, 'CONTRASTE CON CHECRAS: Tacna enfrenta presiones por flujo centrípeto fronterizo intenso;\nChecras sufre vaciamiento rural y requiere incentivos de arraigo comunal (TUO Ley 27795).', ha='center', fontsize=8, weight='bold', color='#1a365d',
        bbox=dict(boxstyle='square,pad=0.4', facecolor='#fffff0', edgecolor='#d69e2e'))

ax.set_title('FIGURA 12: Modelo de Frontera Viva y Atracción Comercial en el Eje Tacna-Arica (Ratzel)\nDemarcación, Densificación Poblacional e Inexpugnabilidad Geoeconómica', fontsize=10, weight='bold', pad=12)
save_fig(fig, 'fig_p012_tacna_lebensraum')

# ==============================================================================
# FIGURA 13: Pregunta 13 - Perfil Topográfico Ferrocarril Bioceánico (Chancay)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(-200, 5200)

# Relieve Cordillerano
x_relieve = np.array([0, 15, 35, 55, 75, 90, 100])
y_relieve = np.array([0, 150, 800, 2600, 3800, 4800, 4300])
ax.plot(x_relieve, y_relieve, 'k-', lw=2)
ax.fill_between(x_relieve, y_relieve, -200, color='#e2e8f0', alpha=0.8)

# Localidades sobre el relieve
puntos = [(0, 0, 'Chancay\n(Megapuerto, 0 m)'),
          (15, 150, 'Huaral\n(180 m)'),
          (35, 800, 'Sayán\n(685 m)'),
          (55, 2600, 'Lacsaura / Purapucu\n(Checras, 2500 m)'),
          (75, 3800, 'Oyón\n(3620 m)'),
          (90, 4800, 'Abra Cordillera Raura\n(Túnel Base, 4600 m)'),
          (100, 4300, 'Cerro de Pasco\n(Meseta Bombón, 4330 m)')]

for x, y, lbl in puntos:
    ax.plot(x, y, 'o', color='#c53030', markersize=6)
    ax.text(x, y+220, lbl, ha='center', fontsize=7.5, weight='bold', color='#1a202c')

# Traza Férrea con Túneles de Base (Pendiente máxima 2.5%)
ax.plot([0, 35, 75, 88], [0, 800, 2400, 3200], '--', color='#2b6cb0', lw=2.5, label='Traza Férrea de Alta Carga (Pendiente Controlada $\\leq 2.5\\%$)')
ax.plot([88, 100], [3200, 4300], '-', color='#805ad5', lw=3.5, label='Mega-Túnel Transandino de Base (Subterráneo de Baja Cota)')

ax.set_ylabel('Altitud (m.s.n.m.)', fontsize=9, weight='bold')
ax.set_title('FIGURA 13: Perfil Topográfico y Descenso Ferroviario Bioceánico (Riemann - Pardo - LaRouche)\nConexión Estratégica desde la Sierra Central / Pasco hasta el Terminal Portuario de Chancay', fontsize=10, weight='bold', pad=12)
ax.legend(loc='upper left', fontsize=8)
save_fig(fig, 'fig_p013_ferrocarril_bioceanico')

# ==============================================================================
# FIGURA 14: Pregunta 14 - Capacidad de Acogida y Zonificación de Cuenca
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Tres Zonas de la Cuenca
# Zona 1: Cabecera
z1 = patches.Rectangle((5, 10), 28, 40, facecolor='#c6f6d5', edgecolor='#2f855a', lw=2)
ax.add_patch(z1)
ax.text(19, 44, 'ZONA 1: PROTECCIÓN\nDE CABECERA\n(> 3,800 msnm)', ha='center', weight='bold', fontsize=8.5, color='#22543d')
ax.text(19, 26, '• Bofedales y Lagunas\n• Recarga de Acuíferos\n• Pastos Naturales\n• Intangibilidad Hídrica\n(Ley N° 32279)', ha='center', fontsize=7.5, color='#1c4532')

# Zona 2: Enclave Minero Subterráneo
z2 = patches.Rectangle((36, 10), 28, 40, facecolor='#feebc8', edgecolor='#dd6b20', lw=2)
ax.add_patch(z2)
ax.text(50, 44, 'ZONA 2: ENCLAVE\nMINERO REGULADO\n(3,000 - 3,800 msnm)', ha='center', weight='bold', fontsize=8.5, color='#7b341e')
ax.text(50, 26, '• Minería Polimetálica\n• Galerías Subterráneas\n• Cero Vertimiento a Ríos\n• Depósito de Relaves Secos\n• Servidumbres Catastradas', ha='center', fontsize=7.5, color='#652b19')

# Zona 3: Valle Agrícola y Andenerías
z3 = patches.Rectangle((67, 10), 28, 40, facecolor='#bee3f8', edgecolor='#2b6cb0', lw=2)
ax.add_patch(z3)
ax.text(81, 44, 'ZONA 3: VALLE AGRÍCOLA\nY ANDENERÍAS\n(1,500 - 3,000 msnm)', ha='center', weight='bold', fontsize=8.5, color='#1a365d')
ax.text(81, 26, '• Andenes Tradicionales\n• Frutales en Purapucu\n• Seguridad Alimentaria\n• Comunidad Campesina\n• Saneamiento COFOPRI', ha='center', fontsize=7.5, color='#2c5282')

# Rol del Catastro Multipropósito
ax.text(50, 4, 'CATASTRO MULTIPROPÓSITO (Ley 32279): Establece la Capacidad de Acogida Relativa y delimita\ncon precisión milimétrica los derechos mineros subterráneos frente a las parcelas agrícolas superficiales.',
        ha='center', fontsize=8, weight='bold', color='#1a202c',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#edf2f7', edgecolor='#4a5568'))

ax.set_title('FIGURA 14: Zonificación Territorial y Capacidad de Acogida en la Cuenca del Río Huaura\nPrevención Científica de Conflictos Minero-Agrícolas y Mitigación de Impactos en Checras', fontsize=10, weight='bold', pad=12)
save_fig(fig, 'fig_p014_zonificacion_cuenca')

# ==============================================================================
# FIGURA 15: Pregunta 15 - Teledetección Satelital y Gobernanza SINADOT
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# 1. Órbita Satelital
ax.plot(20, 48, 's', color='#2b6cb0', markersize=12)
ax.text(20, 54, 'SATÉLITE PERÚSAT-1 / CONSTELACIÓN LEO\n(Visión Científica Pedro Paulet)', ha='center', weight='bold', fontsize=8.5, color='#1a365d')

# 2. Cono de Captura hacia el Territorio
path_sat = [(18, 46), (5, 20), (35, 20), (22, 46)]
poly_sat = patches.Polygon(path_sat, closed=True, facecolor='#bee3f8', alpha=0.4, edgecolor='#3182ce', lw=1.5)
ax.add_patch(poly_sat)
ax.text(20, 16, 'Territorio Checras / Cuenca Huaura\n(Captura Multiespectral / LiDAR / Radar SAR)', ha='center', weight='bold', fontsize=7.5, color='#2c5282')

# 3. Descarga a Estación Terrena
ax.annotate('', xy=(55, 35), xytext=(24, 46), arrowprops=dict(arrowstyle="->", lw=2.5, color='#2b6cb0', linestyle='--'))
ax.text(40, 44, 'Enlace de Descarga\nBanda X (Telemetría)', fontsize=7.5, weight='bold', color='#1a365d')

ax.plot(55, 32, '^', color='#742a2a', markersize=12)
ax.text(55, 24, 'Estación CNOIS\n(Pucusana / CONIDA)', ha='center', weight='bold', fontsize=8, color='#742a2a')

# 4. Procesamiento SINADOT / PCM y Alertas
rect_proc = patches.FancyBboxPatch((70, 15), 26, 35, boxstyle='round,pad=0.5', facecolor='#ebf8ff', edgecolor='#3182ce', lw=1.5)
ax.add_patch(rect_proc)
ax.text(83, 44, 'PLATAFORMA SINADOT\n(SDOT - PCM / Geoportal)', ha='center', weight='bold', fontsize=8, color='#1a365d')
ax.text(83, 28, '• Mapas de Cambios de Uso\n• Alertas de Huaycos\n• Detección Invasiones Arqueol.\n• Monitoreo de Bofedales\n• Fiscalización de Checras', ha='center', fontsize=7.5, color='#2c5282')

ax.annotate('', xy=(70, 32), xytext=(58, 32), arrowprops=dict(arrowstyle="->", lw=2.5, color='#2b6cb0'))

ax.set_title('FIGURA 15: Arquitectura Aeroespacial de Teledetección y Gobernanza Digital del SINADOT\nMonitoreo en Tiempo Real de Riesgos, Bofedales y Usos del Suelo (Legado de Pedro Paulet)', fontsize=10, weight='bold', pad=12)
save_fig(fig, 'fig_p015_teledeteccion_paulet')

# ==============================================================================
# FIGURA 16: Pregunta 16 - Termodinámica, Entropía y Cadena de la Papa
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Tres Estaciones de la Cadena
etapas = [
    (8, 20, 24, 25, '#2f855a', 'PARCELA ALTOANDINA\n(Checras, 3,550 msnm)\n\n• Cosecha de Papa Nativa\n• Energía Biomasa Máxima ($E_0$)\n• Baja Entropía ($S_0$)'),
    (38, 20, 25, 25, '#dd6b20', 'TRANSPORTE EN TROCHA\n(Lacsaura - Sayán)\n\n• Vía no asfaltada afirmada\n• Fricción mecánica severa\n• Falta de Cadena de Frío\n• Golpeteo y Deshidratación'),
    (70, 20, 24, 25, '#c53030', 'MERCADO LITORAL\n(Chancay / Lima)\n\n• Merma física: 20 - 30%\n• Pérdida Energética (Carnot)\n• Alta Entropía ($S > S_0$)\n• Incremento del Precio')
]

for x, y, w, h, col, txt in etapas:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.8', facecolor=col, edgecolor='black', lw=1.5)
    ax.add_patch(rect)
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center', color='white', weight='bold', fontsize=7.8)

# Flechas de degradación entrópica
ax.annotate('', xy=(38, 32.5), xytext=(32, 32.5), arrowprops=dict(arrowstyle="->", lw=3.5, color='#dd6b20'))
ax.annotate('', xy=(70, 32.5), xytext=(63, 32.5), arrowprops=dict(arrowstyle="->", lw=3.5, color='#c53030'))

# Disipación Térmica y Pérdidas de Energía (Planck / Carnot)
ax.annotate('Incremento Entrópico $\\Delta S = \\int \\frac{dQ}{T} > 0$\nDisipación de Biomasa por Fricción Espacial',
            xy=(50.5, 20), xytext=(50.5, 6),
            arrowprops=dict(arrowstyle="->", lw=2, color='#c53030'),
            ha='center', fontsize=8, weight='bold', color='#742a2a',
            bbox=dict(boxstyle='square,pad=0.4', facecolor='#fff5f5', edgecolor='#e53e3e'))

ax.set_title('FIGURA 16: Diagrama de Fricción Espacial y Degradación Entrópica en el Eje de la Papa\nTermodinámica del Abastecimiento desde los Andes de Checras hacia la Costa (Planck - Carnot)', fontsize=10, weight='bold', pad=12)
save_fig(fig, 'fig_p016_entropia_alimentos')

# ==============================================================================
# FIGURA 17: Pregunta 17 - Catastro Multipropósito y Propiedad Comunal
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Capas superpuestas de Catastro Multipropósito (Perspectiva Isométrica conceptual)
capas = [
    (15, 8, 70, 12, '#bee3f8', 'CAPA FÍSICA / USO DE SUELO: Andenes, Pastos, Bofedales y Bosques Comunales'),
    (15, 22, 70, 12, '#feebc8', 'CAPA ECONÓMICA / VALORATIVA: Catastro Rural, Servidumbres, Riego y Valuación Fiscal'),
    (15, 36, 70, 12, '#c6f6d5', 'CAPA JURÍDICA / TITULACIÓN: Linderos Georreferenciados SUNARP - Comunidad Puñun/Checras')
]

for x, y, w, h, col, txt in capas:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5', facecolor=col, edgecolor='#2d3748', lw=1.5)
    ax.add_patch(rect)
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center', weight='bold', fontsize=8.2, color='#1a202c')

# Vínculo integrador
ax.annotate('', xy=(12, 14), xytext=(12, 42), arrowprops=dict(arrowstyle="<->", lw=2.5, color='#2b6cb0'))
ax.text(8, 28, 'Integración\nMultifinalitaria\n(Ley N° 32279)', rotation=90, ha='center', va='center', fontsize=8, weight='bold', color='#1a365d')

ax.text(50, 53, 'ESTABILIZACIÓN DEL TEJIDO SOCIAL ANDINO\nCierre Definitivo de Conflictos Limítrofes con Santa Leonor, Paccho y Sayán', ha='center', fontsize=8.5, weight='bold', color='#22543d',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0fff4', edgecolor='#38a169'))

ax.set_title('FIGURA 17: Estructura de Capas del Catastro Multipropósito en Tierras Comunales de Checras\nSaneamiento Jurídico, Protección de Andenerías y Demarcación Definitiva (TUO Ley 27795)', fontsize=10, weight='bold', pad=12)
save_fig(fig, 'fig_p017_croquis_catastro_comunal')

# ==============================================================================
# FIGURA 18: Pregunta 18 - Flujograma de Participación Ciudadana y Cohesión
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 5.5))
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Pasos del Flujograma Legal
pasos = [
    (4, 22, 17, 24, '#2b6cb0', '1. CONVOCATORIA\nCOMUNAL\n\n• Asamblea General\nde Comuneros\n• Socialización de\nmetodología ODT'),
    (24, 22, 17, 24, '#2f855a', '2. DIAGNÓSTICO\nPARTICIPATIVO\n\n• Recorrido de hitos\n• Memoria histórica\nde linderos locales\n• Taller comunal'),
    (44, 22, 17, 24, '#dd6b20', '3. MESA TÉCNICA\nMULTINIVEL\n\n• PCM / SDOT\n• GORE Lima\n• Municipio Checras\n• Autoridades comunales'),
    (64, 22, 17, 24, '#805ad5', '4. CONSULTA Y\nVALIDACIÓN\n\n• Audiencia pública\n• Acta de acuerdo\nde límites distritales\n• Firma comunal'),
    (84, 22, 14, 24, '#c53030', '5. APROBACIÓN\nFORMAL\n\n• Ley o Decreto\n• Inscripción en\nSINADOT y\nSUNARP')
]

for x, y, w, h, col, txt in pasos:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5', facecolor=col, edgecolor='black', lw=1.2)
    ax.add_patch(rect)
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center', color='white', weight='bold', fontsize=7.2)

# Flechas conectivas
for i in range(len(pasos)-1):
    x_end = pasos[i][0] + pasos[i][2]
    x_next = pasos[i+1][0]
    ax.annotate('', xy=(x_next, 34), xytext=(x_end, 34), arrowprops=dict(arrowstyle="->", lw=2.2, color='#2d3748'))

ax.text(50, 8, 'RESILIENCIA Y ESCUDO SOCIAL (Velasco Alvarado):\nLa participación activa de las comunidades de Checras (Puñun, Tongos, Tulpay, Maray) blinda el POT frente a la atomización territorial.',
        ha='center', fontsize=8, weight='bold', color='#1a202c',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f7fafc', edgecolor='#cbd5e0'))

ax.set_title('FIGURA 18: Flujograma Legal de Participación Ciudadana y Cohesión Territorial (Ley N° 32279)\nIntegración de Demandas Comunales en la Aprobación del Plan de Ordenamiento Territorial', fontsize=10, weight='bold', pad=12)
save_fig(fig, 'fig_p018_flujograma_participacion')

# ==============================================================================
# FIGURA 19: Pregunta 19 - Macroesquema del Perú: Potencia Noosférica Unificada
# ==============================================================================
fig, ax = plt.subplots(figsize=(10.5, 6))
ax.set_facecolor('#f8fafc')
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis('off')

# Silueta esquemática del territorio peruano
poly_peru = [(15, 62), (25, 65), (55, 60), (70, 48), (85, 35), (82, 15), (75, 5), (65, 8), (45, 18), (30, 28), (20, 45), (15, 62)]
ax.add_patch(patches.Polygon(poly_peru, closed=True, facecolor='#edf2f7', edgecolor='#4a5568', lw=2))

# 12 Nodos Estratégicos Nacionales
nodos_12 = [
    (20, 60, '1. Piura-Tumbes\n(Despensa Norte)'),
    (45, 56, '2. Putumayo\n(Frontera Viva)'),
    (68, 46, '3. Iquitos/Yavarí\n(Heartland Fluvial)'),
    (78, 32, '4. Purús\n(Flujo Energético)'),
    (72, 18, '5. Madre de Dios\n(Eje Hamilton)'),
    (70, 9, '6. Puno/Titicaca\n(Cuenca Endorreica)'),
    (65, 5, '7. Tacna\n(Lebensraum Sur)'),
    (48, 20, '8. VRAEM\n(Noosfera Central)'),
    (40, 28, '9. Mantaro/Pasco\n(Eje Energético)'),
    (26, 35, '10. Huaura-Checras\n(Célula Andina)'),
    (24, 32, '11. Chancay Hub\n(Vector Bioceánico)'),
    (28, 27, '12. Lima Metropolitana\n(Descentralizada)')
]

for x, y, name in nodos_12:
    ax.plot(x, y, 'o', color='#c53030' if 'Chancay' in name or 'Checras' in name else '#2b6cb0', markersize=7)
    ax.text(x+1.5, y, name, fontsize=6.8, weight='bold', color='#1a202c')

# Vectores Bioceánicos Transversales
ax.plot([24, 40, 78], [32, 28, 32], '-', color='#d69e2e', lw=3, label='Corredor Bioceánico Transversal (Pacífico - Chancay - Selva - Atlántico)')
ax.plot([24, 26, 40], [32, 35, 28], '--', color='#e53e3e', lw=2, label='Ramal Huaura - Checras - Pasco')

# Anotación Geopolítica Soberana
ax.text(50, 65, 'PERÚ: POTENCIA NOOSFÉRICA AUTÓNOMA DEL HEMISFERIO SUR\nBlindaje Territorial Frente al Choque Hegemónico Global (Mackinder - Vernadsky - LaRouche)',
        ha='center', fontsize=9, weight='bold', color='#1a365d',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#ebf8ff', edgecolor='#2b6cb0'))

ax.legend(loc='lower left', fontsize=7.5, frameon=True)
save_fig(fig, 'fig_p019_mapa_geopolitico_noosferico')

print('All 19 figures generated successfully!')
