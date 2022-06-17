#Validar  Categoria (Entero y valor 1 2 o 3)
while True:
    try:
        Categoria=int(input("Categoria (Entero y valor 1 2 o 3)"))
        if Categoria<1 or Categoria>3:
            print("Categoria debe ser 1, 2 o 3")
            continue
        break
    except ValueError:
        print("La Categoria dede ser un dato entero")
print("Prceso Finalizado")