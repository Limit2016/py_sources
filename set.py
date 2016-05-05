# -*- coding: utf-8 -*-

s = set ([ 3,2,3,4,4,3,5 ])                       #  set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合 ,注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。重复元素在set中自动被过滤
print(s)

s.add( 8 )                                     #通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
print(s)

s.remove(3)                     #通过remove(key)方法可以删除元素
print(s)


#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作，还可以放入变量
sd=34
s2 = set ([3,2,8,9,sd,0])
s3 = s&s2
print(s3)


#et和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
l = [32,43,435]
s4 = set ([3,34,"sd"])     #可以存字符串
print(s4)
