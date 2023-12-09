matriz=[]# MATRIZ ES UNA LISTA DE LISTAS
FILAS= 4
COLUMNAS= 6
for i in range(FILAS):
    fila=[0]*COLUMNAS
    matriz.append(fila)
print(matriz)

# CON MAS FILAS
pbi=[[1.2,2.4],[3.2,3.6],[3.2,3.8],[3.2,3.6],[3.2,3.6],[3.2,3.6],
     [2.2,2.6],[4.2,4.6],[5.2,6.6],[7.2,7.6],[8.2,9.6],[10.2,12.6]
     ,[3.2,3.6]]
FILA=11
COLUMNAS=2
for i in range(FILAS):
    for j in range(COLUMNAS):
        print(pbi[i][j],end=" ")
    print()
    
item=pbi[2][1]
print(item)
matriz=[]
ALUMNOS=4
NOTAS=3

for i in range(ALUMNOS):
    notas= []
    print("ALUMNO {}: ".format(i+1))
    for j in range(NOTAS):
        nota=float(input("nota: {}: ".format(j+1)))
        notas.append(nota)
        
    matriz.append(notas)

print("recorrido de matriz por medio de for")

for i in range (ALUMNOS):
    for j in range (NOTAS):
        print(matriz[i][j], end=" ")
    print()
