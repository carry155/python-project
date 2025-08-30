def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a, b):
        return a / b
    
while True:
    print("\n....simple calculator program....")
    print("chose the chioce")
    print(" 1. add")
    print(" 2. sub")
    print(" 3. multipy")
    print(" 4. divide")
    print(" 5. exit")

    choice=input("enter your choice (1-5) ")

    if choice == '5':
      print("exit....thank you")
      break

    num1=float(input("enter frist num = "))
    num2=float(input("enter second num = "))

    if choice == '1':
        print(f"output {add(num1,num2)}")
    elif choice == '2':
        print(f"output {sub(num1,num2)}")
    elif choice == '3':
        print(f"output {multiply(num1,num2)}")
    elif choice == '4':
        print(f"output {divide(num1,num2)}")
    else:
        print("invalid, input ")




















