def number():
    num1 = int(input("Ingrese un numero"))
    num2 = int(input("Ingrese otro numero"))
    if num1 > num2: 
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

print(number())
