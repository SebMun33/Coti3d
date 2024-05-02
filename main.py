import modulo_materiales
import modulo_impresoras
import modulo_cotizaciones
import modulo_ventas
import sys
import os

mat = modulo_materiales.Material()
imp = modulo_impresoras.Impresora()
cot = modulo_cotizaciones.Cotizaciones()
ventas = modulo_ventas.Ventas()

class App: #aplicacion
    def __init__(self) -> None:
        pass
    
    def Menu_Principal(self): #funcion menú principal, se encarga de preguntar al usuario que desea hacer y desplegar el menú necesario para ello
        os.system('cls')
        print(
            "\nPrincipio:\n\n"+
            "1. Impresoras\n"+
            "2. Materiales\n"+
            "3. Operaciones\n"+
            "4. Salir\n"
        )
        while True: #ciclo de menúes, cada opción es un menú diferente
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1": 
                os.system('cls')
                app.Menu_Impresoras()
                break
                    
            elif opcion == "2":
                os.system('cls')
                app.Menu_Materiales()
                break
                
            elif opcion == "3":
                os.system('cls')
                app.Menu_Operaciones()
                break
                
            elif opcion == "4":
                sys.exit()
                
            else:
                print("Opción no válida. Intente nuevamente.")
     
     
     
    def Menu_Impresoras(self): #seccion dedicada a operaciones de impresoras
        print(
            "\nImpresoras:\n"+
            "1. Mostrar lista de Impresoras\n"+
            "2. Agregar Impresora nueva\n"+
            "3. Modificar Impresora existente\n"+
            "4. Eliminar Impresora de la lista\n"+
            "5. Volver al Menú anterior\n"
        )
        while True: #selector de funciones
            opcion=input("Sellecione una opción: ")
            if opcion=="1":
                os.system('cls')
                print("\n")
                imp.Mostrar_Impresoras()
                print("\n\n")
                self.Menu_Impresoras()
                break
            
            elif opcion=="2":
                os.system('cls')
                self.Agregar_Impresora()
                break
            
            elif opcion=="3":
                os.system('cls')
                self.Modificar_Impresora()
                break
                
            elif opcion=="4":
                os.system('cls')
                self.Eliminar_Impresora()
                break
                
            elif opcion=="5":
                os.system('cls')
                self.Menu_Principal()
                break
                                
                
    def Agregar_Impresora(self) -> None: #opción 2 de menu impresoras, se encarga de agregar una impresora nueva al json
        alias=input("Determine un alias con el cual referirse a la impresora o cancelar para volver atrás: ")
        
        if alias=="cancelar": #chequea por posibles selecciones accidentales
            self.Menu_Impresoras()
            
        modelo=input("Que modelo es la impresora?: ") #recolector de información
        costo=input("Cual fue el costo de compra?: ")
        hora=input("Cual es el costo por hora de la impresora?: ")
        tipo=input("Que tipo de impresora es?: ")
        
        impresoras=imp.Obtener_Impresoras() #controla que no se intente cargar una impresora duplicada
        for impre in impresoras:
            if alias in impre["alias"]:
                input("Ya existe una impresora con ese Alias en la lista. Presione enter para volver a intentarlo.")
                self.Menu_Impresoras()
        
        imp.Agregar_Impresora(alias,modelo,costo,hora,tipo) #función del modulo de impresoras
        
        print("\nse guardó la impresora de la siguiente manera:\n")
        imp.Mostrar_Una_Impresora(alias)
        input("presione enter para volver al menú anterior.")                
        self.Menu_Impresoras()
    
    def Modificar_Impresora(self) -> None: #opcion 3 del menú impresoras, se encarga de editar una impresora de la lista
        
        lista=input("Desea ver la lista de materiales? (Y/N): ") #chequea si el usuario necesita una lista
        if lista=="Y":
            imp.Mostrar_Impresoras()
        
        impresora=input("\nEscriba el alias de la impresora a modificar o cancelar para volver atrás: ")
        
        if impresora=="cancelar": #revisa en caso de selecciones accidentales
            self.Menu_Impresoras()
            
        imp.Mostrar_Una_Impresora(impresora) #pide al usuario la información para realizar la operacion
        
        atributo=input("que parametro se quiere modificar? (el parametro es la palabra de la izquierda, escribirlo tal cual aparece): ")
        if atributo not in {"alias","modelo","costo_compra","costo_hora","tipo_maquina"}: #revisa que el atributo exista
            input("Ese atributo no existe. Presione enter para volver atras.")
            
        nuevo=input("cual es el nuevo valor que se le quiere dar? (escribirlo sin espacios al principio o al final): ")
        
        impresoras=imp.Obtener_Impresoras() #revisa que la impresora a modificar exista
        encontrado=False
        for impres in impresoras:
            if impresora==impres["alias"]:
                encontrado=True
        if encontrado==False:
            input("Ese material no existe en la lista. Presione enter para volver al menú anterior")
        
        imp.Modificar_Impresora(impresora,atributo,nuevo)
        
        print("\nse modificó la impresorsa: "+impresora+" quedó así:\n")
        
        if atributo=="alias": #imprime los nuevos valores, teniendo en cuenta que si se modicio el alias hay que llamar a la impresora por su nuevo nombre
            imp.Mostrar_Una_Impresora(nuevo)
        else:
            imp.Mostrar_Una_Impresora(impresora)
    
        input("\npresione enter para volver al menú anterior.")
        os.system('cls')
        self.Menu_Impresoras()

    def Eliminar_Impresora(self) -> None: #opción 4 del menu impresoras, elimina una impresora de la lista
        
        seguridad=input("\nse va a eliminar una impresora de la lista, está seguro? (Y/N):") #chequeo de seguridad
        if seguridad == "N":
            print("\nvolviendo al menú anterior.\n\n")
            self.Menu_Impresoras()
        elif seguridad == "Y":
            print("Entendido, seguimos con la eliminación de una impresora de la lista.\n")
        else:
            print("tiene que responder con Y o con N, cualquier otra respuesta será tomada invalida\n\n")
            self.Eliminar_Impresora()
        
        lista=input("Desea mostrar la lista de impresoras? (Y/N): ")  
        if lista=="Y": 
            imp.Mostrar_Impresoras #muestra las impresoras y ejecuta la orden
            
        alias=input("\n\nQue impresora se quiere eliminar de la lista? (escriba el alias) o cancelar para cancelar la operación: ")
        
        if alias=="cancelar":
            self.Menu_Impresoras
            
        imp.Eliminar_Impresora(alias)
        print(alias+" fue eliminada de la lista de impresoras.\n")
        input("presione enter para volver al menú anterior.")
        os.system('cls')
        self.Menu_Impresoras()


    
    def Menu_Materiales(self): #Menu de operaciones sobre materiales
        print(
            "Materiales:\n"+
            "1. Mostrar lista de Materiales\n"+
            "2. Agregar nuevo Material\n"+
            "3. Modificar Material existente\n"+
            "4. Eliminar Material existente\n"+
            "5. Volver al Menú anterior\n"
        )
        
        while True: #selector de funciones
            opcion=input("Sellecione una opción: ")
            
            if opcion=="1": #muestra la lista de materiales
                os.system('cls')
                print("\n")
                mat.Mostrar_Materiales()
                print("\n\n")
                self.Menu_Materiales()
                break
                
            if opcion=="2":
                os.system('cls')
                self.Agregar_Nuevo_Material()
                break
            
            if opcion=="3":
                os.system('cls')
                self.Modificar_Material()
                break
                
            if opcion=="4":
                os.system('cls')
                self.Eliminar_Material()
                
            if opcion=="5":
                os.system('cls')
                self.Menu_Principal()
            
                    
    
    def Agregar_Nuevo_Material(self) -> None:
        
        nombre=input("Determine el nombre del material o escriba cancelar para cancelar: ")
        
        if nombre=="cancelar":
            self.Menu_Impresoras()
            
        costo=input("\nCuanto cuesta por kg?: ")
        tipo=input("\nQue tipo de material es?: ")
        detalle=input("\nAgregue una descripción del material:\n")
        
        materiales=mat.Obtener_Materiales()
        for mate in materiales:
            if nombre==mate["nombre"]:
                input("ya existe en la lista un material con ese nombre. Presione enter para volver a intentarlo")
                self.Menu_Materiales()
        
        mat.Agregar_Material(nombre,costo,tipo,detalle)
        print("\nse agrego el material "+nombre+" de la siguiente manera:\n")
        
        mat.Mostrar_Una_materiale(nombre)
        input("presione enter para volver al menú anterior.")
        os.system('cls')
        self.Menu_Materiales()
    
    def Modificar_Material(self) -> None: #opcion 3 del menu de materiales, se encarga de editar un material de los guardados
        
        seguridad = input("Desea ver la lista de materiales antes de modificar alguno? (Y/N): ") #pregunta al usuario si quiere ver la lista de materiales
        if seguridad=="Y":
            print("\n\n")
            mat.Mostrar_Materiales()
            print("\n\n")
            
        nombre=input("Escriba el nombre del material a modificar o Cancelar para volver atras: ")
        if nombre=="cancelar": #permite al usuario cancelar la operacion
            self.Menu_Materiales()
            
        os.system('cls')
            
        mat.Mostrar_Una_materiale(nombre) #muestra los valores del material
            
        atributo=input("\nque atributo desea modificar? (escriba exactamente el nombre del atributo): ") #solicita al usuario los valores a modificar
        if atributo not in {"nombre","costo_kg","tipo_material"}: #revisa que el atributo exista
            input("\nEse atributo no existe. Presione enter para volver atras.")
            
        nuevo_valor=input("\nque nuevo valor desea asignarle?: ")
        
        materiales=mat.Obtener_Materiales() #revisa que el material exista en la lista
        encontrado=False
        for mate in materiales:
            if nombre==mate["nombre"]:
                encontrado=True
        if encontrado==False:
            input("\nEse material no existe en la lista. Presione enter para volver al menú anterior")
        
        mat.Modificar_Material(nombre,atributo,nuevo_valor)
        
        print("\n")
        print("se ha modificado el material "+nombre+" quedó guardado de la siguiente manera:\n")
        if atributo=="nombre":
            mat.Mostrar_Una_materiale(nuevo_valor)
        else:
            mat.Mostrar_Una_materiale(nombre)
        
        os.system('cls')
        self.Menu_Materiales()
            
    def Eliminar_Material(self) -> None:
        
        seguridad=input("\nse va a eliminar un Material de la lista, está seguro? (Y/N):") #chequeo de seguridad
        if seguridad == "N":
            input("\nvolviendo al menú anterior.\n\n")
            self.Menu_Materiales()
        elif seguridad == "Y":
            print("\nEntendido, seguimos con la eliminación del Material de la lista.\n")
        else:
            print("\ntiene que responder con Y o con N, cualquier otra respuesta será tomada invalida\n\n")
            self.Eliminar_Impresora()
        
        lista=input("\nDesea mostrar la lista de materiales? (Y/N): ")  
        if lista=="Y": 
            mat.Mostrar_Materiales() #muestra los materiales y ejecuta la orden
        
        nombre=input("\nQue material va a eliminar? (escriba el nombre tal cual aparece en la lista o cancelar): ")
        
        if nombre == "cancelar":
            os.system('cls')
            self.Menu_Materiales()
        
        materiales=mat.Obtener_Materiales() #revisa que el material exista en la lista
        encontrado=False
        for mate in materiales:
            if nombre==mate["nombre"]:
                encontrado=True
        if encontrado==False:
            input("\nEse material no existe en la lista. Presione enter para volver al menú anterior")
            self.Menu_Materiales()
        
        
        mat.Eliminar_Material(nombre)
        
        print("\n\n"+nombre+" fue eliminado de la lista correctamente")
        input("presione enter para continuar.")
        os.system('cls')
        self.Menu_Materiales()
    
    
    def Menu_Operaciones(self):
        print(
            "Operaciones:\n"+
            "1. Hacer una cotización\n"+
            "2. Historial de cotizaciones\n"+
            "3. Buscar una cotización\n"+
            "4. Ventas\n"+
            "5. Volver al Menú anterior\n"
        )
        pass
    
    def Menu_cotizaciones(self):
        pass

    def Menu_Ventas(self):
        pass
    
    
app=App()

if __name__ == "__main__":
    app.Menu_Principal()