#hile bucle finito
##iterator = 0
##while iterator <10:
   ## print(iterator)
    ##iterator=iterator+1
#bucle infinito
##while True:
    ##print(iterator)
    ##iterator=iterator+1
#bucle infinito con condicional
#iterator = 0
##while iterator !=10:
   ## print(iterator)
    ##iterator=iterator+2
#N = int(input("ingresar numero de estudiantes:"))
#i=1
#while N>=i:
  #  nombre= input("nombre{}:".format(i))#cambio de iteracion le hara suma al contador
  #  i += 1 

N=int(input("cantidad de estudiantes: "))
i=1

while N >=i:
    nombre= input("ALUMNO{} ".format(i) )
    M=int(input("Ingresar cantidad de cursos: "))
    j=0
    while M>j:
        curso_nombre=input("CURSO {}: ".format(j+1))
        j+=1
        
    i+=1