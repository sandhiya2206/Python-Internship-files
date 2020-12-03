Number1=[10,11,12,13,14,15,17,19]
even_number=lambda x:x%2==0
Number2=list(filter(even_number,Number1))
print(Number2)
