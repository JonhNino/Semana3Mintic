#Validar Datos Flotatantes
while True:
    try:
        Dato_Float=float(input("Cantidad de Usuarios "))
        break
    except ValueError:
        print("La Cantidad de Usuarios debe ser un dato Flotante")

print(Dato_Float)