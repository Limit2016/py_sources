# -*- coding: utf-8 -*-
#函数的定义和调用
def fac( x ):
    i = 1
    result = 1
    while i <=x :
        result = result * i
        i+=1
    return result

print ( fac(3) )
print ( fac(8) )

