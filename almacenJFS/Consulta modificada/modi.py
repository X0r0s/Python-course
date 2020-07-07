import sys
import sqlite3

def creaalmacen(micon, cur):
    micon = sqlite3.connect("ALMACEN.db")
    cur = micon.cursor()
    print (" PRODUCTOS ".center(50, "-")," MEDIDAS DE PESO POR KILOGRAMO ".center(50, "-"))
    print (" café      yerba      arroz      azucar      sal ".center(50, " "),
     " 0.25      0.5      1      2 ".center(50, " "))
   
    st = input("Desea abrir el Stock (S/N): ")
    if st.upper() == "S":
       
        cur.execute(""" CREATE TABLE IF NOT EXISTS PRODUCTOS(
            ID_ST INTEGER PRIMARY KEY AUTOINCREMENT,
            AT_ST VARCHAR(20) NOT NULL,
            DT_ST VARCHAR(100) NOT NULL,
            PS_ST REAL NOT NULL,
            CN_ST INTEGER NOT NULL,
            VL_ST REAL NOT NULL) """)
        cur.execute("DELETE FROM PRODUCTOS")
        micon.commit()
    input("Esperá Carlo...")
    micon.close()



def inserta_producto_inicial(mic, c):
    insertar = """INSERT INTO PRODUCTOS (ID_ST, AT_ST, DT_ST, PS_ST, CN_ST, VL_ST) VALUES
	(NULL,"café","Exprés",0.25,0,0),(NULL,"café","Capuchino",0.5,0,0),
    (NULL,"café","Moka",1,0,0),(NULL,"café","Filtrado",2,0,0),
	(NULL,"yerba","Elaborada con palo",0.25,0,0),(NULL,"yerba","Elaborada sin palo",0.5,0,0),
    (NULL,"yerba","Caaminí",1,0,0),(NULL,"yerba","Testada",2,0,0),
	(NULL,"arroz","Blanco",0.25,0,0),(NULL,"arroz","Amarillo",0.5,0,0),
    (NULL,"arroz","Yamani",1,0,0),(NULL,"arroz","Integral" ,2,0,0),
	(NULL,"azucar","Blanco",0.25,0,0),(NULL,"azucar","Moreno",0.5,0,0),
    (NULL,"azucar","Refinado",1,0,0),(NULL,"azucar","Integral",2,0,0),
	(NULL,"sal","Marino",0.25,0,0),(NULL,"sal","Común",0.5,0,0),
    (NULL,"sal","Kosher",1,0,0),(NULL,"sal","Himalaya",2,0,0)"""
    c.execute(insertar)
    mic.commit()

def modifica_almacen():
		micon = sqlite3.connect("ALMACEN.db")
		cur = micon.cursor()
		ar1=[]
		ar2=[]


		try:
			muestra_productos(micon,cur)
		except:   
			print ("Tabla no existe")
	
		input("Esperá Carlo...")
		print (" MODIFICA PRODUCTOS ")
   
		print (" Producto a modificar ")
   
		artviejo=input("   Artículo: ")
		desviejo=input("Descripción: ")

		artnuevo=input("   Artículo nuevo: ")
		desnuevo=input("Descripción nueva: ")
	

   
		ar1.append(artnuevo)
		ar1.append(desnuevo)
		ar1.append(artviejo)
		ar1.append(desviejo)
	
		peso=    input("    Peso nuevo: ")
		cant=    input("Unidades nuevo: ")
		valor=   input("   Valor nuevo: ")
		ar2.append(peso)
		ar2.append(cant)
		ar2.append(valor)
		ar2.append(artnuevo)
		ar2.append(desnuevo)


		print (ar1)
		print (ar2)
		input()

		
		modif1="""UPDATE PRODUCTOS 
		SET AT_ST=?, DT_ST=?
		WHERE AT_ST=? AND DT_ST=?"""

		modif2="""UPDATE PRODUCTOS 
		SET PS_ST=?, CN_ST=?, VL_ST=?
		WHERE AT_ST=? AND DT_ST=?"""
	   
		cur.execute(modif1,ar1)      
		micon.commit()
		cur.execute(modif2,ar2)      
		micon.commit()

		input("Esperá Carlo...")
		micon.close()	


micon = sqlite3.connect("ALMACEN.db")
cur = micon.cursor()

creaalmacen(micon, cur)
inserta_producto_inicial(micon,cur)
modifica_almacen()		