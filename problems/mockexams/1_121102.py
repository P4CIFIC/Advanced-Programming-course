def power(a,b):
   if b == 0:
       return 1
   if b == 1:
       return a
   x = power(a,b//2)   # // represents integer division
   if (b % 2) == 0:
       return x*x
   else: 
    return x*x*a

for i in range(10):
    print(power(2,i))