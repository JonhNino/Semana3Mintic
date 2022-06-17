# Programa Listas – Ejercicio
# Se desea liquidar la comisión de N vendedores, de los cuales se conoce el nombre, tipo de vendedor(1: Puerta a Puerta,
# 2:Telemercadeo, 3: Ejecutivo de ventas) y el valor de las ventas del mes. También se suministra el porcentaje de comisión que
# gana el vendedor de acuerdo con el tipo, que se la aplica al valor de las ventas del mes:
# (Tipo vendedor - % comisión): ( 1-Puerta a Puerta: 20%, 2-Telemercadeo:15%, 3-Ejecutivo de ventas: 25%)
# Con base en la anterior información, se desea calcular e imprimir:
#  Valor comisión a pagar a cada vendedor.
#  Valor total a pagar por comisiones(Todos los vendedores)
# NOTA: Se debe almacenar la información de entrada y la de salida en listas (Similar al reto 3)

# Jonh Niño
# Fecha 09/06/2022

N=int(input("Cantidad de Vendedores"))
total_Comision=0
for i in range(N):
    nombre=input("Nombre vendedor")
    tipo=int(input("Tipo (1: Puerta 2:Telemercadeo, 3:Ejecutivo)"))
    ventas=float(input("Ventas del mes:"))
    if tipo==1:
        comision=ventas*0.2
    elif tipo==2:
        comision=ventas*0.15
    elif tipo==3:
        comision=ventas*0.25
    total_Comision+=comision
    print("Comision Vendedor",comision)
print("Total Comisiones",total_Comision)
