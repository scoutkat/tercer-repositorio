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
