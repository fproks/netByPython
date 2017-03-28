#coding:utf8
import web
db =web.database(dbn='mysql', user='root',pw='',host='192.68.4.113',db='test')
db.printing =True
ps='123456'
lists =db.query("SELECT name FROM users")
print(lists.__nonzero__())
for li in lists:
    print(li.name)
    #print(type(li))
lists =db.query("SELECT * FROM users")
for li in lists:
    print(li.age)
db._db_cursor().close()    # 关闭链接