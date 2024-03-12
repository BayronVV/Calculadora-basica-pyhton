print("ingrese el primer numero: ")
n1= float (input())
print("ingrese el segundo numero: ")
n2= float (input())
print("ingrese el caracter correspondiente a la operacion(+,-,*,/): ")
c1 = input()
if c1 == "+":
    print(n1 + n2)
elif c1 == "-":
    print(n1 - n2)
elif c1 == "*":
    print(n1 * n2)
elif c1 == "/":
    print(n1/n2)