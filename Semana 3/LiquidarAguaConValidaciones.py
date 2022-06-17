# Programa para liquidar servicios Agua a N Usuarios
# Jonh Niño 
# 02/06/2022

while True:
    try:
        N=int(input("Cantidad de Usuarios"))
        break
    except ValueError:
        print("La Cantidad de Usuarios debe sru un dato entero")
total_servicio=0
for i in range(N):
    while True:
        try:
            codigo=int(input("Codigo Usuario: "))
            break
        except ValueError:
            print("El Codigo del Usuario debe ser un dato entero")

    nombre=input("Nombre Usuario")

    while True:
        estado=input("Estado (V=Vigente, S=Suspendido)")
        if estado!="V" and estado!="S":
            print("El estado debe ser V=Vigente o S=Suspendido")
            continue
        break

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

    while True:
        try:
            consumo=float(input("Consumo del mes :"))
            break
        except ValueError:
            print("El Consumo debe ser un dato Flotante")

    if (estado=="V"):
        if Estrato==1:
            tarifa_Basica=10000
        elif Estrato==2:
            tarifa_Basica=20000
        elif Estrato==3:
            tarifa_Basica=30000
        elif Estrato==4:
            tarifa_Basica=45000
        elif Estrato==5:
            tarifa_Basica=60000
        else:
            tarifa_Basica=70000
        valor_consumo=consumo*200
        valor_pagar=tarifa_Basica+valor_consumo
        print("Nombre Usuario",nombre)
        print("Tarifa Basica: ","{:,.2f}".format(tarifa_Basica))
        print("Valor Consumo","{:,.2f}".format(valor_consumo))
        print("Valor a Pagar","{:,.2f}".format(valor_pagar))
    print("Total Servicio Agua","{:,.2f}".format(total_servicio))
        
