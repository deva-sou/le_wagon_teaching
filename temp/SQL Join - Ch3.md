### Challenge 3

* QU 2
```sql
SELECT
  s.date_date
  ### Key ###
  ,s.orders_id
  ,s.products_id
  ###########
  -- sales columns --
  ,s.turnover
  ,s.qty
  -- product column --
  ,p.purchase_price
FROM `course16.gwz_sales` s
LEFT JOIN `course16.gwz_product` p ON s.products_id=p.products_id -- USING (products_id)
```

* QU 3
```sql
SELECT 
  ### Key ###
  orders_id
  ,products_id
  ###########
  ,COUNT(*) AS nb
FROM `course16.gwz_sales_margin`
GROUP BY
  orders_id
  ,products_id
HAVING nb>=2
ORDER BY nb DESC
```

* QU 4
```sql
SELECT
  s.date_date
  ### Key ###
  ,s.orders_id
  ,s.products_id
  ###########
  -- qty --
  ,s.qty
  -- revenue --
  ,s.turnover
  -- cost --
  ,p.purchase_price
  ,ROUND(s.qty*p.purchase_price,2) AS purchase_cost
  -- margin --
  ,s.turnover - ROUND(s.qty*p.purchase_price,2) AS margin
FROM `course16.gwz_sales` s
LEFT JOIN `course16.gwz_product` p ON s.products_id = p.products_id
```

* QU 5
```sql
SELECT
  s.date_date
  ### Key ###
  ,s.orders_id
  ,s.products_id
  ###########
  -- qty --
  ,s.qty
  -- revenue --
  ,s.turnover
  -- cost --
  ,p.purchase_price
  ,ROUND(s.qty*p.purchase_price,2) AS purchase_cost
  -- margin --
  ,s.turnover - ROUND(s.qty*p.purchase_price,2) AS margin
FROM `course16.gwz_sales` s
RIGHT JOIN `course16.gwz_product` p ON s.products_id = p.products_id
```

* QU 8
```sql
 SELECT 
   ### Key ###
   orders_id
   ,products_id
   ###########
   ,purchase_price
 FROM `course16.gwz_sales_margin`
 WHERE purchase_price IS NULL
```

* QU 10
```sql
 SELECT
   date_date
   ### Key ###
   ,orders_id
   ###########
   ,ROUND(SUM(qty),2) AS qty
   ,ROUND(SUM(turnover),2) AS turnover
   ,ROUND(SUM(purchase_cost),2) AS purchase_cost
   ,ROUND(SUM(margin),2) AS margin
 FROM `course16.gwz_sales_margin`
 GROUP BY 
   date_date
   ,orders_id
 ORDER BY
   date_date
   ,orders_id
```

* QU 11
```sql
SELECT
   ### Key ###
   orders_id
   ###########
   ,COUNT(*) AS nb
 FROM `course16.gwz_orders`
 GROUP BY
   orders_id
 HAVING nb>=2
 ORDER BY nb DESC
```

* QU 12
```sql
 SELECT
   o.date_date
   ### Key ###
   ,o.orders_id
   ###########
   -- orders infos --
   ,o.qty
   ,o.turnover
   ,o.purchase_cost
   ,o.margin
   -- ship infos --
   ,s.shipping_fee
   ,s.log_cost
   ,s.ship_cost
 FROM `course16.gwz_orders` o
 LEFT JOIN `course16.gwz_ship` s ON o.orders_id = s.orders_id
 ORDER BY
   date_date
   ,orders_id
```

* QU 13
```sql
-- Test 1
SELECT
  ### Key ###
  orders_id
  ###########
  ,COUNT(*) AS nb
FROM `course16.gwz_orders_operational`
GROUP BY
  orders_id
HAVING nb>=2
ORDER BY nb DESC
-- Test 2
SELECT
   ### Key ###
   orders_id
   ###########
   ,shipping_fee
   ,log_cost
   ,ship_cost
FROM `course16.gwz_orders_operationnal`
WHERE TRUE
   AND shipping_fee IS NULL
   OR log_cost IS NULL
   OR ship_cost IS NULL
ORDER BY orders_id
```

* QU 14
```sql
SELECT
 o.date_date
  ### Key ###
  ,o.orders_id
  ###########
  -- orders infos --
  ,o.qty
  ,o.turnover
  ,o.purchase_cost
  ,o.margin
  -- ship infos --
  ,s.shipping_fee
  ,s.log_cost
  ,s.ship_cost
  -- operationnal margin --
  ,o.margin + s.shipping_fee - (s.log_cost + s.ship_cost) AS operational_margin 
FROM `course16.gwz_orders` o
LEFT JOIN `course16.gwz_ship` s ON o.orders_id = s.orders_id
ORDER BY
  date_date
  ,orders_id
```

* QU 15
```sql
SELECT
  ### Key ###
  date_date
  ###########
  -- orders infos --
  ,SUM(qty) AS qty 
  ,ROUND(SUM(turnover),0) AS turnover 
  ,ROUND(SUM(purchase_cost),0) AS purchase_cost 
  ,ROUND(SUM(margin),0) AS margin 
  -- ship infos --
  ,ROUND(SUM(shipping_fee),0) AS shipping_fee 
  ,ROUND(SUM(log_cost),0) AS log_cost 
  ,ROUND(SUM(ship_cost),0) AS ship_cost 
  -- operationnal margin --
 ,ROUND(SUM(operational_margin),0) AS operational_margin  
FROM `course16.gwz_orders_operational`
GROUP BY
  date_date
ORDER BY
  date_date DESC
```

* QU 16
```sql
SELECT
### Key ###
date_date
###########
-- orders infos --
,COUNT(orders_id) AS nb_transaction
,SUM(qty) AS qty 
,ROUND(SUM(turnover),0) AS turnover 
,ROUND(AVG(turnover),1) AS average_basket
,ROUND(SUM(turnover)/COUNT(orders_id),1) AS average_basket_bis
,ROUND(SUM(purchase_cost),0) AS purchase_cost 
,ROUND(SUM(margin),0) AS margin 
-- ship infos --
,ROUND(SUM(shipping_fee),0) AS shipping_fee 
,ROUND(SUM(log_cost),0) AS log_cost 
,ROUND(SUM(ship_cost),0) AS ship_cost 
-- operationnal margin --
,ROUND(SUM(operational_margin),0) AS operational_margin  
FROM `course16.gwz_orders_operationnal`
GROUP BY
date_date
ORDER BY
date_date DESC
```
