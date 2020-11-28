print("CALCULATOR")
operation=int(input("please enter your coice:"))
              
if operation == 1:
    a=int(input("please enter first number:"))
    b=int(input("please enter second number:"))
    print("ADDITON OF TWO NUMBERS",a,"AND",b,"IS",a+b)
elif operation == 2:
    a=int(input("please enter first number:"))
    b=int(input("please enter second number:"))
    print("SUBTRACTION OF TWO NUMBERS",a,"AND",b,"IS",a-b)
elif operation == 3:
    a=int(input("please enter first number:"))
    b=int(input("please enter second number:"))
    print("MULTIPLICATION OF TWO NUMBERS",a,"AND",b,"IS",a*b)
elif operation == 4:
    a=int(input("please enter first number:"))
    b=int(input("please enter second number:"))
    print("DIVISION OF TWO NUMBERS",a,"AND",b,"IS",a/b)
else:
    print("please make vaild choice from 1 to 4")
