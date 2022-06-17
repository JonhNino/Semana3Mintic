#Validar  Categoria (Entero y valor 1 2 o 3)
while True:
    try:
        Estrato=int(input("Estrato (1 2 3 4 5 o 6) "))
        if Estrato<1 or Estrato>6:
            print("El Estrato debe ser 1, 2, 3, 4, 5 y 6")
            continue
        break
    except ValueError:
        print("El Estrato debe ser numerico")
print("La Persona es estrato",Estrato)