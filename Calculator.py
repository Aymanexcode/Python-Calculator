while True:
    x = input("Enter The First Number (or 'exit' to close): ")
    if x.lower() == 'exit':
        break
    if not x.replace('.', '').isdigit():
        print("invalid input. Please Enter a valid Number !.")
        continue
    opr = input("Enter The operator: ")
    if opr not in ('+', '-' , '*' , '/'):
        print("invalid operator. Please Enter +, -, * or / :")
        continue
    y = input("Enter The Second Number : ")
    if not y.replace('.', '').isdigit():
        print("invalid input. Please Enter a valid Number !.")
        continue
    x = float(x)
    y = float(y)
    if opr == "+":
        print(x + y)
    elif opr == "-":
        print(x - y)
    elif opr == "*":
        print(x * y)
    elif opr == "/":
        if y != 0:
            print(x / y)
        else:
            print("Error: Division By Zero")