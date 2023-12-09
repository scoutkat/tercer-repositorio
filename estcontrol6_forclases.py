#for con lista
##elementlist=[1,2,3,4,5]
##for item in elementlist:
  ##  print("este es el elemento de la lista",item)

#for con string
#texto= " hola mundo"
#for x in texto:
 #   print(x)

#for con range desde el cero hasta el 50 
##for element in range(50):
  ##  print(element)
  
#range desde ciertos numeros con valor inicial o valor final
#for element in range(5,10):
 # print(element)

# con range de tres terminos  con inicio, termino, de cuanto en cuanto se suma
##for element in range(5,100,3):
  ## print(element)
  
# for con nombres 
#N=int(input("ingresar numero de alumnos: "))
#for i in range(N):#i=0,1,2,3,4,5,6
 #   nombre= input("nombre {}:".format(i))

#for anidado for dentrode for
#N=int(input("ingresar numero de alumnos: "))
#for i in range(N):#i=0,1,2,3,4,5,6
 #   nombre=input("ALUMNO{}: ".format(i))
  #  M=int(input("ingresar numero de CURSOS: "))
   # for j in range(M):
    #    CURSOnombre= input("nombre {}:".format(j+1))

# estrucutra for con break and continue 
#i=1
#while i<100:
 #   print(i)

#    if i==5:
 #       break  
  #  i+=1
# break rompe bucle
 
#for con break como anterior ejemplo solo imprime el uno 
#for element in range(1,100):
 #   print (element)
  #  break
for element in range(1,11,2):
    #if element==5:
     #   continue## hace continue en elemento cinco lo salta
    print(element)