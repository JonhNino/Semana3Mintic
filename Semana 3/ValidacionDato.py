#Validar Datos Enteros///
while True:
    try:
        N=int(input("Cantidad de Usuarios "))
        break
    except ValueError:
        print("La Cantidad de Usuarios debe ser un dato entero")

print(N)