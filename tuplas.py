#tupla vacia 
x=()
print(x)
#tuplas con elementos - modo1
x=(1,2,3,5,10,"hola",10.4)
print(x)

x=1,2,3,7
print(x)

print("tupla cona acceso de lista")
tupla=1,2,('a','b'),3 # no permite la modificacion
print(tupla)
print(tupla[2][1])

print("tuple funcion")
lista={1,2,4}
tupla=tuple(lista)
print(type(tupla))
print(tupla)

print("asignacion")
l=(1,2,3,"pruebamela cabronazo")
x,y,z,p=l
print(x,y,z,p)

print("recorrido")
tupla=1,2,3,"yo soy tu padre sting cabron",5,10.5
for i in tupla:
 print(i)
 
 print("tupla count")
 l=(1,1,1,3,5)
 print(l.count(10))# elemento a buscar o contabilizar si no esta es igual a cero
 
 print("index")
 l=[7,7,7,3,5]
 print(l.index(5))
 
 l=[7,7,7,3,5]
 print(l.index(7,2))# busca el 7 mas desde que posicion sera el 2 