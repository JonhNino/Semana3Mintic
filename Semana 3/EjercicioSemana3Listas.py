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


#Listas del ejercicio
lista_nombre=[]
lista_tipo=[]
lista_ventas=[]
lista_comision=[]

N=int(input("Cantidad de Vendedores"))
total_Comision=0
for i in range(N):
    nombre=input("Nombre vendedor")
    tipo=int(input("Tipo (1: Puerta 2:Telemercadeo, 3:Ejecutivo)"))
    ventas=float(input("Ventas del mes:"))
    lista_nombre.append(nombre)
    lista_tipo.append(tipo)
    lista_ventas.append(ventas)
print(len(lista_nombre))
print(len(lista_tipo))
print(len(lista_ventas))

#Proceso

for x in range(N):

    #valor_porducto=CANTIDAD*valor_UNITORAIO
    #valor_producto=lista_cantidad[x]*lista_valor[x]
    #lista_valor_producto.append(valor_producto)
    if lista_tipo[x] ==1:
        comision=ventas*0.2
        
    elif lista_tipo[x]==2:
        comision=ventas*0.15
        
    elif lista_tipo[x]==3:
        comision=ventas*0.25
         
    lista_comision.append(comision)
    total_Comision+=comision
    print("Comision Vendedor",comision)
print("Total Comisiones",total_Comision)