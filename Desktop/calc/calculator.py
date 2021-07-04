print("Welcome to the simple calculator!!")
num1 = float(input("Enter 1st no:"))
num2 = float(input("Enter 2nd no:"))
operation = input("which  operation do you want to perform?")

def additon1():
    result=num1+num2
    print(result)

def subtraction():
    result=num1-num2
    print(result)

def multiplicaton():
    result=num1*num2
    print(result)

def division():
    result=num1/num2
    print(result)

if operation in ['add','ADD','addition','ADDITION','+']:
    additon1()

elif operation in ['sub','SUB','SUBTRACTION','-','subtraction']:
    subtraction()

elif operation in['mul','MUL','Multiplication','MULTIPLICATION','*']:
    multiplicaton()

elif operation in['div','DIV','Division','DIVISION','/']:
    division()
