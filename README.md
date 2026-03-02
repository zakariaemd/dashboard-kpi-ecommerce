# 📊 Dashboard KPI E-Commerce 2025

> **Stack :** SQL · MySQL · Python · Plotly · Pandas  
> **Type :** Data Marketing · Business Intelligence · KPI Analysis

---

## 🎯 Objectif

Suivre la performance d'une boutique en ligne (chiffre d'affaires, taux de conversion,
panier moyen) et identifier des leviers d'optimisation via un tableau de bord interactif.

---

## 🗄️ Base de données

```
ecommerce_kpi/
├── categories     (6 catégories)
├── products       (14 produits)
├── clients        (50 clients)
├── orders         (200 commandes)
├── order_items    (détail articles)
└── site_visits    (trafic mensuel)
```

---

## 📈 KPIs Analysés

| KPI | Valeur 2024 |
|-----|-------------|
| 💰 CA Total | 92 957 € |
| 🛒 Panier Moyen | 533 € |
| 🎯 Taux de Conversion | 0.92% |
| ❌ Taux d'Annulation | 6.5% |
| 📦 Commandes Payées | 155 |
| 👥 Clients Actifs | 50 |

---

## 🔍 Insights Clés

- 📅 **Périodes fortes** : Novembre–Décembre (Black Friday + Noël = +60% CA)
- 🏆 **Top produit** : Laptop UltraSlim 15 → 13 199 € de CA
- 📱 **Catégorie dominante** : Électronique → 68% du CA total
- 📉 **Friction identifiée** : Taux d'annulation à 6.5% → optimisation checkout

---

## 🚀 Lancer le projet

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Importer la base de données
mysql -u root -p < database/setup.sql

# 3. Lancer le dashboard
python dashboard/dashboard.py
```

---

## 🛠️ Stack Technique

![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
