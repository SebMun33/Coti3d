import modulo_materiales
import modulo_impresoras
import modulo_cotizaciones
import modulo_ventas
import sys

mat = modulo_materiales.Material()
imp = modulo_impresoras.Impresora()
cot = modulo_cotizaciones.Cotizaciones()
ventas = modulo_ventas.Ventas()

class App:
    def __init__(self) -> None:
        pass
    
    def Menu_Principal(self):
        print(
            "\nPrincipio:\n\n"+
            "1. Impresoras\n"+
            "2. Materiales\n"+
            "3. Operaciones\n"+
            "4. Salir\n"
        )
        while True:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                while True:
                    app.Menu_Impresoras()
                    
            elif opcion == "2":
                while True:
                    app.Menu_Materiales()
            elif opcion == "3":
                while True:
                    app.Menu_Operaciones()
            elif opcion == "4":
                sys.exit()
            else:
                print("Opción no válida. Intente nuevamente.")
     
     
     
    def Menu_Impresoras(self):
        print(
            "\nImpresoras:\n"+
            "1. Mostrar lista de Impresoras\n"+
            "2. Agregar Impresora nueva\n"+
            "3. Modificar Impresora existente\n"+
            "4. Eliminar Impresora de la lista\n"+
            "5. Volver al Menú anterior\n"
        )
        while True:
            opcion=input("Sellecione una opción: ")
            if opcion=="1":
                print("\n")
                imp.Mostrar_Impresoras()
                print("\n\n")
                self.Menu_Impresoras()
            
            elif opcion=="2":
                self.Agregar_Impresora()
                print("\n\n")
                self.Menu_Impresoras()
            
            elif opcion=="3":
                self.Modificar_Impresora()
                print("\n\n")
                self.Menu_Impresoras()
                
            elif opcion=="4":
                self.Eliminar_Impresora()
                print("\n\n")
                self.Menu_Impresoras()
                
            elif opcion=="5":
                self.Menu_Principal()
                print("\n\n")
                self.Menu_Impresoras()
                                
                
    def Agregar_Impresora(self) -> None:
        alias=input("Determine un alias con el cual referirse a la impresora: ")
        modelo=input("Que modelo es la impresora?: ")
        costo=input("Cual fue el costo de compra?: ")
        hora=input("Cual es el costo por hora de la impresora?: ")
        tipo=input("Que tipo de impresora es?: ")
        imp.Agregar_Impresora(alias,modelo,costo,hora,tipo)
        print("\nse guardó la impresora de la siguiente manera:\n")
        imp.Mostrar_Una_Impresora(alias)
        print("\n volviendo al menú anterior.\n\n")                
        self.Menu_Impresoras()
    
    def Modificar_Impresora(self) -> None:
        impresora=input("\nEscriba el alias de la impresora a modificar: ")
        imp.Mostrar_Una_Impresora(impresora)
        atributo=input("que parametro se quiere modificar? (el parametro es la palabra de la izquierda, escribirlo tal cual aparece): ")
        nuevo=input("cual es el nuevo valor que se le quiere dar? (escribirlo sin espacios al principio o al final): ")
        imp.Modificar_Impresora(impresora,atributo,nuevo)
        print("\nse modificó la impresorsa: "+impresora+" quedó así:\n")
        imp.Mostrar_Una_Impresora(impresora)
        print("\nvolviendo al menú anterior\n\n")
        self.Menu_Impresoras()

    def Eliminar_Impresora(self) -> None:
        seguridad=input("\nse va a eliminar una impresora de la lista, está seguro? (Y/N):")
        if seguridad == "N":
            print("\nvolviendo al menú anterior.\n\n")
            self.Menu_Impresoras()
        elif seguridad == "Y":
            print("Entendido, seguimos con la eliminación de una impresora de la lista.\n")
        else:
            print("tiene que responder con Y o con N, cualquier otra respuesta será tomada invalida\n\n")
            self.Eliminar_Impresora()
                
        imp.Mostrar_Impresoras
        alias=input("\n\nQue impresora se quiere eliminar de la lista? (escriba el alias): ")    
        imp.Eliminar_Impresora(alias)
        print(alias+" fue eliminada de la lista de impresoras.\n")
        print("\n\n")
        self.Menu_Impresoras()

    
    def Menu_Materiales(self):
        print(
            "Materiales:\n"+
            "1. Mostrar lista de Materiales\n"+
            "2. Agregar nuevo Material\n"+
            "3. Modificar Material existente\n"+
            "4. Eliminar Material existente"+
            "5. Volver al Menú anterior\n"
        )
        pass
    
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

'''
if __name__ == "__main__":
    # Coloca aquí tu lógica principal, como un menú interactivo o la ejecución de una función específica
    print("Bienvenido al sistema de gestión.")
    # Ejemplo de un menú interactivo
    while True:
        app.Menu_Principal
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            while True:
                app.Menu_Impresoras()
        elif opcion == "2":
            while True:
                app.Menu_Materiales()
        elif opcion == "3":
            while True:
                app.Menu_Operaciones()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")'''
            

app.Menu_Principal()