SYNTAX ERROR:
name= input("please enter your name:")
if name== "sandhiya":
print("welcome sandhiya")

OUTPUT:
    EXPECTED AN INDENTED OUTPUT

    
name= input("please enter your name:")
if name== "sandhiya":
    print("welcome sandhiya")

OUTPUT:
please enter your name:sandhiya
welcome sandhiya

RUNTIME ERROR:
age= input("HOW OLD ARE YOU?")

if age<50:
    print("wow you are old")
    
HOW OLD ARE YOU?50
Traceback (most recent call last):
  File "D:/python files/runtime error.py", line 3, in <module>
    if age<50:
TypeError: '<' not supported between instances of 'str' and 'int'

age= input("HOW OLD ARE YOU?")
age=int(age)
if age<50:
    print("wow you are young")

HOW OLD ARE YOU?40
wow you are young

