numero_1 = int(input("Ingresa el primer numero: "))
numero_2 = int(input("Ingresa el segundo numero: "))
numero_3 = int(input("Ingresa el tercer numero: "))

mayor = numero_1

if mayor < numero_2:
    mayor = numero_2
elif mayor < numero_3:
    mayor = numero_3

print(f"El numero mayor es: {mayor}")