a=0
b=1
n=int(input("ENTER THE NUMBER OF FIBONACCI SERIES GENERATED:"))
if n<=0:
    print("NOT POSSIBLE")
elif n==1:
    print(a)
elif n>=2:
    print("{},{}".format(a,b),end= ' ')
for i in range(2,n):
          c=a+b
          print(",{}".format(c),end= ' ')
          a=b
          b=c
          
