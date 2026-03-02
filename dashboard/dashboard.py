# ============================================
# KPI E-COMMERCE DASHBOARD
# Author: [Ton Prénom]
# Stack: Python, Pandas, Plotly, MySQL
# ============================================

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# ============================================
# DATA — Simulation des résultats SQL
# (à remplacer par une connexion MySQL réelle)
# ============================================

# KPI 2 — CA Mensuel
df_ca = pd.DataFrame({
    'mois': ['2024-01','2024-02','2024-03','2024-04','2024-05',
             '2024-06','2024-07','2024-08','2024-09','2024-10',
             '2024-11','2024-12'],
    'nb_commandes': [19, 19, 20, 20, 20, 10, 20, 10, 10, 10, 16, 20],
    'CA_mensuel': [8543.51, 7823.42, 9124.63, 7234.51, 8932.45,
                   5123.32, 9823.45, 6234.12, 5823.41, 7234.52,
                   11234.63, 14823.54],
    'panier_moyen': [449.66, 411.76, 456.23, 361.73, 446.62,
                     512.33, 491.17, 623.41, 582.34, 723.45,
                     702.16, 741.18]
})

# KPI 4 — Taux de conversion
df_conv = pd.DataFrame({
    'mois': ['2024-01','2024-02','2024-03','2024-04','2024-05',
             '2024-06','2024-07','2024-08','2024-09','2024-10',
             '2024-11','2024-12'],
    'taux_conversion': [0.74, 0.82, 0.89, 0.91, 0.95,
                        0.88, 0.86, 0.83, 0.79, 0.85,
                        1.12, 1.38]
})

# KPI 5 — Top produits
df_top = pd.DataFrame({
    'produit': ['Laptop UltraSlim 15', 'Smartphone X12', 'Chaise Ergonomique',
                'Montre Sport GPS', 'Veste Winter', 'Écouteurs Bluetooth Pro',
                'Jean Slim Fit', 'Parfum Élégance', 'Lampe Design LED', 'Tapis de Yoga'],
    'CA': [13199.89, 7799.87, 3299.89, 2499.90, 1319.89,
           989.89, 659.89, 559.93, 549.89, 439.89]
})

# KPI 6 — Statuts commandes
df_status = pd.DataFrame({
    'status': ['paid', 'shipped', 'cancelled', 'pending'],
    'nb': [155, 32, 13, 0],
    'pct': [77.5, 16.0, 6.5, 0.0]
})

# KPI 8 — CA par catégorie
df_cat = pd.DataFrame({
    'categorie': ['Électronique', 'Maison & Jardin', 'Mode', 'Sport', 'Beauté', 'Livres'],
    'CA': [21989.65, 3299.89, 2979.67, 2939.79, 1109.82, 549.87]
})

# ============================================
# DASHBOARD — Layout Plotly
# ============================================

colors = {
    'bg': '#0f1117',
    'card': '#1a1d2e',
    'accent1': '#00d4ff',
    'accent2': '#7c3aed',
    'accent3': '#10b981',
    'accent4': '#f59e0b',
    'text': '#e2e8f0',
    'subtext': '#94a3b8'
}

fig = make_subplots(
    rows=3, cols=3,
    subplot_titles=(
        '📈 CA Mensuel 2024 (€)',
        '🛒 Panier Moyen Mensuel (€)',
        '🎯 Taux de Conversion (%)',
        '🏆 Top 10 Produits par CA (€)',
        '📊 Répartition CA par Catégorie',
        '✅ Statut des Commandes',
        '', '', ''
    ),
    specs=[
        [{"type": "xy"}, {"type": "xy"}, {"type": "xy"}],
        [{"type": "xy"}, {"type": "domain"}, {"type": "domain"}],
        [{"type": "xy", "colspan": 3}, None, None]
    ],
    vertical_spacing=0.12,
    horizontal_spacing=0.08
)

# --- Row 1, Col 1 : CA Mensuel (Bar)
fig.add_trace(go.Bar(
    x=df_ca['mois'],
    y=df_ca['CA_mensuel'],
    name='CA Mensuel',
    marker_color=colors['accent1'],
    marker_line_color='rgba(0,0,0,0)',
    hovertemplate='%{x}<br>CA: %{y:,.0f} €<extra></extra>'
), row=1, col=1)

# --- Row 1, Col 2 : Panier Moyen (Line)
fig.add_trace(go.Scatter(
    x=df_ca['mois'],
    y=df_ca['panier_moyen'],
    name='Panier Moyen',
    mode='lines+markers',
    line=dict(color=colors['accent3'], width=3),
    marker=dict(size=8),
    hovertemplate='%{x}<br>Panier: %{y:.2f} €<extra></extra>'
), row=1, col=2)

# --- Row 1, Col 3 : Taux Conversion (Line)
fig.add_trace(go.Scatter(
    x=df_conv['mois'],
    y=df_conv['taux_conversion'],
    name='Conversion %',
    mode='lines+markers',
    line=dict(color=colors['accent4'], width=3),
    marker=dict(size=8),
    fill='tozeroy',
    fillcolor='rgba(245,158,11,0.15)',
    hovertemplate='%{x}<br>Conversion: %{y:.2f}%<extra></extra>'
), row=1, col=3)

# --- Row 2, Col 1 : Top Produits (Horizontal Bar)
fig.add_trace(go.Bar(
    y=df_top['produit'],
    x=df_top['CA'],
    name='Top Produits',
    orientation='h',
    marker_color=colors['accent2'],
    hovertemplate='%{y}<br>CA: %{x:,.0f} €<extra></extra>'
), row=2, col=1)

# --- Row 2, Col 2 : CA par Catégorie (Donut)
fig.add_trace(go.Pie(
    labels=df_cat['categorie'],
    values=df_cat['CA'],
    name='Catégories',
    hole=0.55,
    marker_colors=[colors['accent1'], colors['accent2'], colors['accent3'],
                   colors['accent4'], '#ef4444', '#8b5cf6'],
    hovertemplate='%{label}<br>CA: %{value:,.0f} €<br>%{percent}<extra></extra>'
), row=2, col=2)

# --- Row 2, Col 3 : Statuts (Donut)
fig.add_trace(go.Pie(
    labels=df_status['status'],
    values=df_status['nb'],
    name='Statuts',
    hole=0.55,
    marker_colors=[colors['accent3'], colors['accent1'], '#ef4444', colors['subtext']],
    hovertemplate='%{label}<br>%{value} commandes (%{percent})<extra></extra>'
), row=2, col=3)

# --- Row 3 : KPI Summary Cards (Annotations instead)
kpis = [
    ('💰 CA Total 2024', '92 957 €'),
    ('🛒 Panier Moyen', '533 €'),
    ('📦 Commandes Payées', '155'),
    ('🎯 Taux Conversion Moy.', '0.92%'),
    ('❌ Taux Annulation', '6.5%'),
    ('👥 Clients Actifs', '50')
]

# Scatter invisible pour row 3
fig.add_trace(go.Scatter(
    x=[0], y=[0], mode='markers',
    marker=dict(opacity=0),
    showlegend=False
), row=3, col=1)

# ============================================
# LAYOUT
# ============================================

fig.update_layout(
    title=dict(
        text='🛒 Dashboard KPI E-Commerce 2024',
        font=dict(size=28, color=colors['text'], family='Inter'),
        x=0.5, xanchor='center'
    ),
    paper_bgcolor=colors['bg'],
    plot_bgcolor=colors['card'],
    font=dict(color=colors['text'], family='Inter'),
    height=1100,
    showlegend=False,
    margin=dict(t=100, b=40, l=40, r=40)
)

# Update axes styling
for i in range(1, 4):
    fig.update_xaxes(
        gridcolor='rgba(255,255,255,0.05)',
        linecolor='rgba(255,255,255,0.1)',
        tickfont=dict(size=10),
        row=1, col=i
    )
    fig.update_yaxes(
        gridcolor='rgba(255,255,255,0.05)',
        linecolor='rgba(255,255,255,0.1)',
        tickfont=dict(size=10),
        row=1, col=i
    )

fig.update_xaxes(gridcolor='rgba(255,255,255,0.05)', row=2, col=1)
fig.update_yaxes(tickfont=dict(size=9), row=2, col=1)

# Subplot titles styling
for annotation in fig['layout']['annotations']:
    annotation['font'] = dict(size=13, color=colors['accent1'])

# ============================================
# KPI CARDS via Annotations
# ============================================
card_x = [0.08, 0.25, 0.42, 0.59, 0.76, 0.93]
for idx, (label, value) in enumerate(kpis):
    fig.add_annotation(
        x=card_x[idx], y=0.05,
        xref='paper', yref='paper',
        text=f"<b>{value}</b><br><span style='font-size:10px;color:{colors['subtext']}'>{label}</span>",
        showarrow=False,
        font=dict(size=16, color=colors['accent3']),
        align='center',
        bgcolor=colors['card'],
        bordercolor=colors['accent1'],
        borderwidth=1,
        borderpad=10,
        opacity=0.95
    )

fig.write_html("dashboard/dashboard_kpi.html")
fig.write_image("dashboard/dashboard_kpi.png", width=1400, height=1100, scale=2)

print("✅ Dashboard exporté : dashboard_kpi.html & dashboard_kpi.png")
