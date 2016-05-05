# -*- coding: utf-8 -*-


d={
            "adam": 100,
            "bob": 90,
            "cat": 88,
        }
d["dog"] = 77                    #把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
print ( d )

print ( d[ "bob" ] )           #只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩

caaa = d ["cat"]              #只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩
print ( caaa )

flag = "tom" in d      #要避免key不存在的错误，有两种办法，一是通过in判断key是否存在 
print ( flag )

flag = d.get  ("hehe" )        #二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print ( flag )

flag = d.get  ("hehe" , -1 )        #二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print ( flag )

d.pop("cat")                                #要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print ( d )
