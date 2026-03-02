-- ============================================
-- KPI QUERIES — E-Commerce Dashboard
-- ============================================
USE ecommerce_kpi;

-- -------------------------
-- KPI 1 : Chiffre d'Affaires Total (commandes payées)
-- -------------------------
SELECT
    ROUND(SUM(total_amount), 2) AS CA_total_EUR
FROM orders
WHERE status = 'paid';

-- -------------------------
-- KPI 2 : CA Mensuel 2024
-- -------------------------
SELECT
    DATE_FORMAT(created_at, '%Y-%m') AS mois,
    COUNT(id_order)                  AS nb_commandes,
    ROUND(SUM(total_amount), 2)      AS CA_mensuel_EUR,
    ROUND(AVG(total_amount), 2)      AS panier_moyen_EUR
FROM orders
WHERE status = 'paid'
GROUP BY mois
ORDER BY mois;

-- -------------------------
-- KPI 3 : Panier Moyen Global
-- -------------------------
SELECT
    ROUND(AVG(total_amount), 2) AS panier_moyen_EUR
FROM orders
WHERE status = 'paid';

-- -------------------------
-- KPI 4 : Taux de Conversion par Mois
-- (Commandes payées / Visiteurs totaux)
-- -------------------------
SELECT
    o.mois,
    o.nb_commandes_payees,
    v.total_visitors,
    ROUND((o.nb_commandes_payees / v.total_visitors) * 100, 2) AS taux_conversion_pct
FROM (
    SELECT
        DATE_FORMAT(created_at, '%Y-%m') AS mois,
        COUNT(*) AS nb_commandes_payees
    FROM orders
    WHERE status = 'paid'
    GROUP BY mois
) o
JOIN (
    SELECT
        DATE_FORMAT(visit_date, '%Y-%m') AS mois,
        SUM(total_visitors) AS total_visitors
    FROM site_visits
    GROUP BY mois
) v ON o.mois = v.mois
ORDER BY o.mois;

-- -------------------------
-- KPI 5 : Top 10 Produits par CA
-- -------------------------
SELECT
    p.name AS produit,
    c.name AS categorie,
    SUM(oi.quantity)                        AS unites_vendues,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS CA_produit_EUR
FROM order_items oi
JOIN products p  ON oi.id_product = p.id_product
JOIN categories c ON p.id_category = c.id_category
JOIN orders o    ON oi.id_order = o.id_order
WHERE o.status = 'paid'
GROUP BY p.id_product, p.name, c.name
ORDER BY CA_produit_EUR DESC
LIMIT 10;

-- -------------------------
-- KPI 6 : Taux d'annulation
-- -------------------------
SELECT
    status,
    COUNT(*) AS nb_commandes,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS pourcentage
FROM orders
GROUP BY status
ORDER BY nb_commandes DESC;

-- -------------------------
-- KPI 7 : Clients les plus actifs (Top 10)
-- -------------------------
SELECT
    cl.email,
    cl.city,
    COUNT(o.id_order)              AS nb_commandes,
    ROUND(SUM(o.total_amount), 2)  AS CA_client_EUR
FROM clients cl
JOIN orders o ON cl.id_client = o.id_client
WHERE o.status = 'paid'
GROUP BY cl.id_client, cl.email, cl.city
ORDER BY CA_client_EUR DESC
LIMIT 10;

-- -------------------------
-- KPI 8 : Répartition CA par catégorie
-- -------------------------
SELECT
    c.name AS categorie,
    SUM(oi.quantity)                           AS unites_vendues,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS CA_categorie_EUR
FROM order_items oi
JOIN products p   ON oi.id_product = p.id_product
JOIN categories c ON p.id_category = c.id_category
JOIN orders o     ON oi.id_order = o.id_order
WHERE o.status = 'paid'
GROUP BY c.id_category, c.name
ORDER BY CA_categorie_EUR DESC;

-- -------------------------
-- KPI 9 : Périodes fortes (jour de la semaine)
-- -------------------------
SELECT
    DAYNAME(created_at) AS jour_semaine,
    COUNT(*)            AS nb_commandes,
    ROUND(SUM(total_amount), 2) AS CA_EUR
FROM orders
WHERE status = 'paid'
GROUP BY DAYNAME(created_at), DAYOFWEEK(created_at)
ORDER BY DAYOFWEEK(created_at);

-- -------------------------
-- KPI 10 : Nouveaux clients par mois
-- -------------------------
SELECT
    DATE_FORMAT(created_at, '%Y-%m') AS mois,
    COUNT(*)                         AS nouveaux_clients
FROM clients
GROUP BY mois
ORDER BY mois;
