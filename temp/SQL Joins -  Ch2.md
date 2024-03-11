### Challenge 2

* Question 1: 

Faites une query: 
SELECT * FROM `course15.circle_stock` 

Et enregistrez la table dans votre projet perso :) 

* Question 2 
```sql
SELECT 
  ### Key ###
  product_id
  ###########
  ,count(*) AS nb
FROM `course15.circle_stock_cat`
GROUP BY
  product_id
HAVING nb>=2
ORDER BY nb DESC;
```

* Question 3 
```sql
SELECT 
  ### Key ###
  model
  ,color
  ,size
  ###########
  ,count(*) AS nb
FROM `course15.circle_stock`
GROUP BY
  model
  ,color
  ,size
HAVING nb>=2
ORDER BY nb DESC
```

* Question 4 
```sql
SELECT 
  ### Key ###
  product_id
  ###########
  ,model_type
FROM `course15.circle_stock_kpi`
WHERE
  model_type IS NULL
ORDER BY product_id
```

* Question 5 
```sql
-- Créer une nouvelle table: cc_stock_model_type 
SELECT
  ### Key ###  
  model_type
  ###########
  ,COUNT(in_stock) AS nb_products
  ,SUM(in_stock) AS nb_products_in_stock
  ,ROUND(AVG(1-in_stock),3) AS shortage_rate
  ,SUM(stock_value) AS total_stock_value
FROM `course15.circle_stock_kpi`
GROUP BY model_type
ORDER BY model_type
;
-- Test pour la clef primaire: à sauvegarder comme cc_stock_model_type_pk dans les queries sauvegardées
SELECT 
  ### Key ###
  model_type
  ###########
  ,count(*) AS nb
FROM `course15.cc_stock_model_type`
GROUP BY
  model_type
HAVING nb>=2
ORDER BY nb DESC;
```

* Question 6 
```sql
SELECT 
  ### Key ###
  product_id
  ###########
  ,count(*) AS nb
FROM `course15.cc_sales_daily`
GROUP BY
  product_id
HAVING nb>=2
ORDER BY nb DESC
```

* Question 7 
```sql
SELECT 
  ### Key ###
  product_id
  ###########
  ,product_name
FROM `course15.circle_stock_kpi`
WHERE
  product_name IS NULL
ORDER BY product_id
```

* Question 8 
```sql
-- Test stock_value column
SELECT 
### Key ###
product_id
###########
,stock_value
FROM `course15.circle_stock_kpi`
WHERE
stock_value < 0
ORDER BY product_id;

-- New circle_stock_kpi
SELECT
### Key ###
CONCAT(model,"_",color,"_",IFNULL(size,"no-size")) AS product_id 
###########
,model
,color
,size
-- category
,CASE
  WHEN REGEXP_CONTAINS(LOWER(model_name),'t-shirt') THEN 'T-shirt'
  WHEN REGEXP_CONTAINS(LOWER(model_name),'short') THEN 'Short'
  WHEN REGEXP_CONTAINS(LOWER(model_name),'legging') THEN 'Legging'
  WHEN REGEXP_CONTAINS(LOWER(REPLACE(model_name,"è","e")),'brassiere|crop-top') THEN 'Crop-top'
  WHEN REGEXP_CONTAINS(LOWER(model_name),'débardeur|haut') THEN 'Top'
  WHEN REGEXP_CONTAINS(LOWER(model_name),'tour de cou|tapis|gourde') THEN 'Accessories'
  ELSE NULL
END AS model_type
-- name
,model_name
,color_name
,CONCAT(model_name," ",color_name,IF(size IS NULL,"",CONCAT(" - Taille ",size))) AS product_name
-- product info --
,t.new AS pdt_new
-- stock metrics --
,forecast_stock
,stock
,IF(stock>0,1,0) AS in_stock
-- value
,price
,IF(stock<0,NULL,ROUND(stock*price,2)) AS stock_value
FROM `course15.circle_stock` t
WHERE TRUE
ORDER BY product_id
```