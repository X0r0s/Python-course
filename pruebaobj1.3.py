'''Documentación del Programa 
Nombre:				pruebadeobjetos.py
clase:				
Autor: 				JFS
Fecha de Creación:		12-04-2020 
Versión:			1.3
Tema:				POO ejercitacion
'''
from os import system

# Se crea la clase empleado con sus metodos
class Empleado():
	def __init__(self,nombre,apellido):
		self.nombre=nombre
		self.apellido=apellido
		
# Se crea una variable de control para los datos a ingresar
	def __control(self):
		while True:
			try:
				edad=int(input("ingrese edad:"))
				self.edad=edad
				if 18<=self.edad<=60 :
					return edad
				else:
					print("La edad no es acorde a los parametros que estamos contratando")
			except:
				break

		
		
		
# Se crea una variable que imprima los datos del objeto
	def imprime(self):
		ctrl=self.__control()
		print("Nombre",self.nombre)
		print("Apellido:",self.apellido)
		print("Edad:",self.edad)
		
		
# 2° Prueba de objetos esta vez utlizando la herencia
# Se crea la clase madre (objeto principal) del cual derivaran sus atributos a otras clases (hijas/os)
class Mercaderia():
	
	def __init__(self,tipo,marca,origen):
		self.tipo=tipo
		self.marca=marca
		self.origen=origen

	def imprime(self):
		print("Producto:",self.tipo)
		print("Producto marca:",self.marca)		
		print("Producto origen:",self.origen)

#clase hija/o que deriva de la clase madre Mercarderia
class Almacen(Mercaderia):
	def __init__(self,tipo,marca,origen):
		super().__init__(tipo,marca,origen)
# la funcion super() es la encargada de indicar lo que se debe heredar de la clase madre
	def imprime(self):
		super().imprime()

class Lacteos(Mercaderia):
	def __init__(self,tipo,marca,origen,vencimiento):
		self.vencimiento=vencimiento
		super().__init__(tipo,marca,origen)
# la funcion super() es la encargada de indicar lo que se debe heredar de la clase madre
	def imprime(self):
		super().imprime()
		print("La fecha de vencimiento es:",self.vencimiento)

print("*****Trabajando la orientacion a objetos en python*****".center(50))

ingreso=input("Ingrese nombre:")
ingreso2=input("Ingrese apellido:")
recruit=Empleado(ingreso,ingreso2)
recruit.imprime()

print("*****Herencia de objetos en python*****".center(50))
print()

print(" Almacen ".center(50,"*"))
print()

prod=input("Ingrese el producto:")
marc=input("Ingrese la marca:")
org=input("Ingrese el origen del producto:")


almacen=Almacen(prod,marc,org)

almacen.imprime()
print()
print(" Lacteos ".center(50,"*"))

prod2=input("Ingrese el producto:")
marc2=input("Ingrese la marca:")
org2=input("Ingrese el origen del producto:")
venc2=input("Ingrese el vencimiento del producto:")

lacteo=Lacteos(prod2,marc2,org2,venc2)
lacteo.imprime()