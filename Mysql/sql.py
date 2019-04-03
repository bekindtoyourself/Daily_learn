insert into students values('wang', 'boy', '1993')

insert into addressList select name from Students

delete from a where name='wang'

truncate table addressList

update addressList set born =18 where name='wang'

select * from addressList

select i,j, k from a where f = 5

select name as 姓名 from a where gender='boy'

select name from a where email is null

select top 6 name from addressList

select name from a where grade >=60 order by desc

select * from a where name like "zhaoA%"

select * from a where age between 18 and 20

select name from a where address in ('beijing, nanjing')

select a.name, b.mark from a, b where a.name = b.name