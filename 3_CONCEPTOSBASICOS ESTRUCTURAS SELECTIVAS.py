# condicional simple
EDAD =int(input("ingresar edad:")) # conversion para convertir de str a int
if EDAD >= 18:
    print("mayor de edad")
#condicional doble
else:
     print("menor de edad ")    

# estructuras de control selectivas multiples y anidadas

n=int (input("ingrese numero:"))
if n> 0:
    print("ingreso un numero positivo")
elif n< 0:
    print("ingreso un numero negativo")
else:
    print("ingreso cero")


EDAD2 =int(input("ingresar edad:")) # conversion para convertir de str a int
if EDAD2 >= 18:
    print("mayor de edad")
#condicional doble y selectiva simple doble y anidada
else:
    if EDAD2>0:
     print("menor de edad ")    
    else:
     print("edad no correcta ") 
