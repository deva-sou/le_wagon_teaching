# Join query
* Qu1
```sql
SELECT
  p.pdt_name
  ,sgt.pdt_segment
FROM `green_catalog.green_product` p
INNER JOIN `green_catalog.green_pdt_segment` sgt ON p.products_id = sgt.products_id
```
* Qu2
```sql
SELECT
  -- product table --
  p.products_id
  ,p.pdt_name
  ,p.products_status
  ,p.categories_id
  ,p.promo_id
  -- stock table
  ,st.stock
  ,st.stock_forecast
FROM `green_catalog.green_product` p
INNER JOIN `green_catalog.green_stock` st ON p.products_id = st.pdt_id
```
* Qu3
```sql
SELECT
  -- product table --
  p.products_id
  ,p.pdt_name
  -- promo table
  ,pr.promo_name
  ,pr.promo_pourcent
FROM `green_catalog.green_product` p
LEFT JOIN `green_catalog.green_promo` pr ON p.promo_id = pr.promo_id
```
* Qu4
```sql
SELECT
-- product table --
p.products_id
,p.pdt_name
-- promo table
,pr.promo_name
,pr.promo_pourcent
FROM `green_catalog.green_promo` pr
RIGHT JOIN `green_catalog.green_product` p ON p.promo_id = pr.promo_id
```
* Qu5
```sql
SELECT
  -- product table --
  p.products_id
  ,p.pdt_name
  ,p.products_status
  ,p.categories_id
  ,p.promo_id
  -- price table
  ,pr.pd_cat
  ,pr.pd_cat
FROM `green_catalog.green_product` p
INNER JOIN `green_catalog.green_price` pr USING (products_id)
```

* Qu6
```sql
SELECT
  -- product table --
  p.products_id
  ,p.pdt_name
  ,p.categories_id
  -- price table
  ,c.category_1
  ,c.category_2
  ,c.category_3
FROM `green_catalog.green_product` p
INNER JOIN `green_catalog.green_categories` c USING (categories_id)
```

* Qu7
```sql
SELECT
-- product table --
p.products_id
,p.pdt_name
-- price table
,IFNULL(s.qty,0) AS qty
FROM `green_catalog.green_product` p
LEFT JOIN `green_catalog.green_sales` s ON p.products_id = s.pdt_id
```

* Qu8
```sql
SELECT
  -- product table --
  p.products_id
  ,p.pdt_name
  -- price table
  ,s.qty
FROM `green_catalog.green_sales` s
RIGHT JOIN `green_catalog.green_product` p ON p.products_id = s.pdt_id
```

