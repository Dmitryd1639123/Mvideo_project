CREATE TABLE mvideo_products (
	prd_id int4 NULL,					--Id товара
	load_dttm timestamp NULL,			--Дата/время загрузки
	load_dt date NULL,					--Дата загрузки
	main_cat_id int4 NULL,				--Id основной категории 
	main_cat_name varchar(100) NULL,	--Наименование основной категории
	sec_cat_name varchar(100) NULL,		--Наименование подкатегории
	prd_name varchar(180) NULL,			--Наименование товара
	base_price int4 NULL,				--Старая цена
	sale_price int4 NULL,				--Новая цена
	cashback int4 NULL,					--Начисляемые баллы
	prd_stars numeric NULL,				--Оценка товара
	manufacturer varchar(100) NULL,		--Производитель товара
	prd_url varchar(100) null			--Ссылка на товар
);