lista=["juan",2,"Andres"]
lista.append(30)#Agrega un item al final de la lista

lista.extend(["Maria", 25])#Agrega una lista al final de lista :V 
lista.insert(5, 22.23)#Permite insertar elementos en un indice especifico y luego corre los elemetos a la derecha
lista.pop(1)#Quita el elmeneto en la posicion 1
#lista.remove(3)
lista[4]="Jose andres"#Cambia le contenido de la posicion 4
print(lista)