create table goods_cates(
    id int unsigned primary key auto_increment not null,
    name varchar(40) not null
);

desc goods_cates;

alter table goods_cates add abbreviation varchar(5);

alter table goods_cates modify abbreviation varchar(3);

alter table goods_cates change abbreviation 简称 varchar(3);

alter table goods_cates drop 简称;

insert into goods_cates values (0, '台式机');

load data local infile "F:\Code\Python3\Daily_learn\Ecommerce_website_dev\goods_cates.txt" into table goods_cates;

update goods_cates set name='手机' where id=2;

delete from goods_cates where id=2;

mysqldump –uroot –p goods_cates > python.sql;

select name from goods_cates;

select distinct name from goods_cates;

select * from goods_cates where id=1;

select * from goods_cates where id>1;

select * from goods_cates where name like "%机";

select * from goods_cates where id in (3, 4);


create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(40) default '',
    cate_name varchar(10) default '',
    brand_name varchar(10) default '',
    price decimal(10,3),
    is_show bit default 1,
    is_saleoff bit default 0
);

alter table goods modify price decimal(10,2);

select count(*) from goods;

select max(price) from goods where cate_name="笔记本";

select sum(price) from goods where cate_name="台式机";

select cate_name, group_concat(id) from goods group by cate_name;

select cate_name, count(*) from goods group by cate_name;

select cate_name, group_concat(id) from goods group by cate_name having count(*) > 3;

select cate_name, group_concat(id) from goods group by cate_name with rollup having count(*) > 3;

select * from goods limit 1, 10;

select * from goods left join goods_cates on goods.cate_name=goods_cates.name;

select * from goods inner join goods_cates on goods.cate_name=goods_cates.name;

create table goods_1(
    id smallint primary key auto_increment,
    name varchar(20) not null,
    cate_name varchar(20)
);

select goods_cates_1.cate_name, goods_1.cate_name, goods_1.name from goods_1 left join goods_cates_1 on goods_1.cate_name=goods_cates_1.cate_name;

select name, cate_name from goods where cate_name in (select name from goods_cates where id < 3);

select name, cate_name from (select * from goods where id < 5) as t where t.cate_name = "笔记本";