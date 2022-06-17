#Programa que cuenta la cantidad de vocales 
# Jonh 
# 08/06/2022

#Iniciar lista como vaciias
lista_letras=[]
N=int(input("Cantidad de Letras: "))
cantidad_a=0
cantidad_e=0
cantidad_i=0
cantidad_o=0
cantidad_u=0
#llenar Lista
for i in range(N):
    letra=input("letra: ")
    lista_letras.append(letra)
print("Lista Letras : ",lista_letras)
#Procesar lista
for x in range(N):
    if lista_letras[x]=="a" or lista_letras[x]=="A":
        cantidad_a+=1
    elif lista_letras[x]=="e" or lista_letras[x]=="E":
        cantidad_e+=1
    elif lista_letras[x]=="i" or lista_letras[x]=="I":
        cantidad_i+=1
    elif lista_letras[x]=="o" or lista_letras[x]=="O":
        cantidad_o+=1
    elif lista_letras[x]=="u" or lista_letras[x]=="U":
        cantidad_u+=1
print("Cantidad de letras a :",cantidad_a)
print("Cantidad de letras e :",cantidad_e)
print("Cantidad de letras i :",cantidad_i)
print("Cantidad de letras o :",cantidad_o)
print("Cantidad de letras u :",cantidad_u)