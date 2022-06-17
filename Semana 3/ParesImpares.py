# Programa para calcular identificiar numeros pares e impares y cuantos de cada grupo -WHILE
# Autor : Jonh niño
# 07/06/2022

numero_entero=int(input("Numero Entero:"))
cantidad_pares=0
cantidad_impares=0
while numero_entero!=-1:
    if numero_entero%2==0:
        print(numero_entero,"Es PAR")
        cantidad_pares+=1
    else:
        print(numero_entero,"Es Impar")
        cantidad_impares+=1
    numero_entero=int(input("Numero Entero:"))
print("Cantidad de Pares:",cantidad_pares)
print("Cantidad de Impares:",cantidad_impares)