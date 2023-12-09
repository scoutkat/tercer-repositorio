print("modo 1")
diccionario=dict()
print(diccionario)

print("modo 2")
d1={
    "nombre":"jorge",
    "edad": 25,
    "documento":10203040
}
print(d1)
print("modo3")
d2={
   ( 'nombre','jorge'),
    ('edad',25),
    ('documento',10203040)
}
print(d2)

print("modo4")
d3=dict(Nombre='jorge',
        edad=25,Documento=10203040)
print(d3)
print("acceso")

d1={
    "nombre":"jorge",
    "edad":25,
    "documento":10203040
}
print(d1["nombre"])
print(d1["edad"])
print(d1["documento"])

print("modificacion")
d1={
    "nombre":"jorge",
    "edad":25,
    "documento":10203040
}
print("nombre antes de modificar: {}".format(d1["nombre"]))
d1["nombre"]="david pantoja"
print("nombre despues de modificar: {}".format(d1["nombre"]))


print("agragar elementos a un diccionario")
d1={
    "nombre":"jorge",
    "edad":25,
    "documento":10203040
}
d1["apellido"]="villacabron"
d1[90]="horario viejo cabron"
print(d1)

print("iteracion")

d1={
    "nombre":"jorge",
    "edad":25,
    "documento":10203040
}
print("m1")
for x in d1:
    print(x)
#imprime los valores del diccionario
print("m2")
for x in d1:
    print(d1[x])

print("m3")
#imprime los keys  value del diccionario
for x,y in d1.items():
    print(x,y)

print("clear")
d={'a':1,'b':2}
print(d.get('a'))
print(d.get('z',"no encontrado"))

print("items")
d={'a':1,'b':2}
it=d.items()
print(it)
print(list(it))
print(list(it)[0][0])

print("keys")
d={'a':1,'b':2}
print(list(d.values()))

print("diccionario anidado")

dic1={"nombre": "casiheuvon", "edad":26, "nota":12}
dic2={"nombre": "omar", "edad":26, "nota":12}

d={
    1:dic1,
    2:dic2
}
print(d)