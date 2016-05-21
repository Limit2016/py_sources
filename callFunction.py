# -*- coding: utf-8 -*-

#from function import fac                            #其实就是把两个程序合在一起运行，不只是调用fac()一个函数
import function                                      #其实就是把两个程序合在一起运行，不只是调用fac()一个函数

def sumerize ( x ):
    i = 1 ;
    result = 0
    while i<=x:
        result = result + function.fac( i )
        i+=1
    return result


print ( sumerize(3) )




import math                                                       

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny                                                                         #可以有多个返回值

x, y = move(100, 100, 60, 3.14 / 6)
print ( x  )

tup = move ( 30 , 40 , 43 , 5 )                                               #返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
print ( tup )


#parameter参数

def  myPow( x , n = 2 ):                           #因为有两个参数，调用时缺少一个参数就无法正常调用
    result  =  x                                               #定义默认参数要牢记一点：默认参数必须指向不变对象！
    while n>1 :
        result = result * x
        n -= 1

    return result

print ( myPow( 3 ,2 ) )
print ( myPow( 3 ) )                                        #但是定义函数时给了n=2,一个默认参数，当参数缺少时默认参数就会起作用

print( myPow( n=2 , x = 3 ) )                        #可以不按顺序传递参数，但此时必须注明参数名



#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def sumer1( numbers ) :
    result = 0
    for num in numbers :
        result = result + num

    return result

s = sumer1 ( [ 1,3,4,2 ] )                     #由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
print ( s )

#################################
def sumer2 ( *numbers ) :                        ###定义一个可变参数但函数
    result = 0
    for num in numbers :
        result = result + num

    return result


s = sumer2 ( 1,3,4,2 )                     #无需list或者tuple
print ( s )

#如果已经有一个list或者tuple，Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
t = { 1,2,3,4 }
s = sumer2 ( *t )
print ( s )


#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def student( name , age , ** kw ) :
    print  "name:"  , name , "age: " , age ,"others :" , kw             #

student ( "bob" , 23 )
student ( "bob" , 23 , city = "shenzhen " , gener = "man" )       #函数person除了必选参数name和age外，还接受关键字参数kw

d = { 'city':"shenzhen" , "gender" : "man" }
student( "bob" ,23 , **d )

