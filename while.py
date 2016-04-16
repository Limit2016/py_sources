#count the sum of odd numbers from 1 to 100
sum = 0
i= 1
while i<=100:
    r= i%2
    i+=1
    if r==0 :
        continue
    sum = sum + (i-1)

print sum



"""
#look for the prime numbers from 1 to 100

i=1
while i<100 :
    j=2
    while j<=(i-1) :
        r=i%j
        if r==0 :
            break
        j+=1

    if j==i :
        print i ,"is a prime number"

    i+=1
"""    

#count a factorial  
"""
fac=1
i=1
while i<5 :
    fac = fac * i
    i+=1

print fac 
"""
