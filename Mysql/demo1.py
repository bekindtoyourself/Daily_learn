import pymysql

find_name = input('input something:')

conn = pymysql.connect(host='localhost', port=3306, database='jing_dong', user='root', password='root', charset='utf8')
cs1 = conn.cursor()

# count = cs1.execute('insert into goods_cates(name) values("abs")')
# count = cs1.execute('select * from goods_cates')
# count = cs1.execute('select id, name from goods where id<=4')

#safety
# count = cs1.execute('select * from goods where name=%s', [find_name])

count = cs1.execute('select * from goods where name="%s"' % find_name)

print(count)
print(cs1.fetchall())

cs1.close()
conn.close()