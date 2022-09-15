CREATE TABLE public.user_clicks (
	load_dttm timestamp NULL,			--Дата/время загрузки
	load_dt date NULL,					--Дата загрузки
	button_name varchar(50) NULL,		--Имя кнопки / введенного текста пользователя
	user_id varchar(50) NULL,			--Id пользователя
	nickname varchar(50) NULL,			--Никнейм пользователя
	first_name varchar(50) NULL,		--Имя пользователя
	last_name varchar(50) null			--Фамилия пользователя
);