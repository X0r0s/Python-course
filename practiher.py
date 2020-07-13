'''Documentación del Programa 
Nombre:       practiher.py
clase:        
Autor:        JFS
Fecha de Creación:    16-04-2020 
Versión:      1.2
Tema:       POO ejercitacion listas
'''


# Herencia super() veamos la función super()con las clases personas y empleados 
from os import system
def limPant():
    system("clear")


#********************Class Persona (clase padre)**************************
class Persona():
# Constructor
    def __init__(self,nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad= edad
        self.lugar_residencia= lugar_residencia
    
    

    def ingreso(self):
      listaper=[]
      nom=""
      ed=""
      dom=""
      self.nombre=nom
      self.edad=ed
      self.lugar_residencia=dom
      nom=input("ingrese el nombre:")
      nom="Nombre "+nom
      ed=input("ingrese la edad:")
      ed="Edad "+ed
      dom=input("Ingrese el domicilio:")
      dom="Domicilio: "+dom
      listaper.append(nom)
      listaper.append(ed)
      listaper.append(dom)
      return listaper
        
        
#******************Fin Clase Persona************************
#********************Class Empleado (clase hija) ************************
class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        # Con super() pasamos el método de la clase padre
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
          
    def ingreso(self):
      listaper=[]
      nom=""
      ed=""
      dom=""
      sal=""
      anti=""
      self.nombre=nom
      self.edad=ed
      self.lugar_residencia=dom
      self.salario=sal
      self.antiguedad=anti
      nom=input("ingrese el nombre:")
      nom="Nombre "+nom
      ed=input("ingrese la edad:")
      ed="Edad "+ed
      dom=input("Ingrese el domicilio:")
      dom="Domicilio "+dom
      sal=input("Ingrese el salario:")
      sal="Salario "+sal
      anti=input("Ingrese la antiguedad:")
      anti="Antiguedad "+anti
      listaper.append(nom)
      listaper.append(ed)
      listaper.append(dom)
      listaper.append(sal)
      listaper.append(anti)
      return listaper    
        

#******************Fin Clase Empleado***********************

#******************Construimos una Persona******************
limPant()
print (" Ingresar datos de la Persona ".center(50,"="))
lista_personas=[]
nom=""
edad=""
nac=""
Personas=Persona(nom,edad,nac)
lista_personas=Personas.ingreso()
print(lista_personas)
#******************Construimos un Empleado******************
print (" Ingresar datos del Empleado ".center(50,"="))
lista_emp=[]
nom=""
edad=""
res=""
sala=""
anti=""
Empleados=Empleado(nom,edad,res,sala,anti)
lista_emp=Empleados.ingreso()
print(lista_emp)

#******************Guardamos el resultado en dos archivos .txt para cada clase******************
with open('Personas.txt', 'w') as listado:
    for listitem in lista_personas:
        listado.write('%s\n' % listitem)

with open('Empleados.txt', 'w') as listado:
    for listitem in lista_emp:
        listado.write('%s\n' % listitem)

#print ("\tRealizar listas para guardar a las personas y empleados")
#print ("\tGuardar los datos en dos archivos de texto")
#print ("""\tSubir esta practica a la carpeta 
#\t'2020-04-16 Herencia Lista Archivo' y allí 
#\ten la carpera 'Practica'""")
#input()

