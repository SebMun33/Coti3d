import datetime as dtime;
import json;
import os;


class material:
    def __init__(self) -> None:
        pass

    def obtener_num(self) -> None: #funcion para obtener el indice de la lista de materiales
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__)) #estas tres lineas son para obtener la ruta dinamica del archivo de data, de seguro se puede optimizar un poco, debería hacerlo
            data_dir = os.path.join(current_dir, "data")
            with open(os.path.join(data_dir, "materiales.json"),"r") as file:
                data=json.load(file)
                return len(data["materiales"])
        except FileNotFoundError:
            return 0

    def Obtener_Materiales(self) -> None:  #esta funcion es para recuperar el diccionario de materiales del json
        current_dir=os.path.dirname(os.path.abspath(__file__))
        data_dir=os.path.join(current_dir,"data")
        with open(os.path.join(data_dir,"materiales.json"),"r") as file:
            data=json.load(file)
            return data["materiales"]

    def Guardar_Materiales(self,materiales:dict) -> None: #esta función es para actualizar el diccionario del json
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        with open(os.path.join(data_dir, "materiales.json"), "w") as file:
            json.dump({"materiales":materiales},file,indent=4)

    def Agregar_Material(self,nombre,costo,tipo) -> None: #esta funcion es la que le permite al usuario agragar nuevas materiales a al json de materiales
        materiales=self.Obtener_Materiales()
        id = self.obtener_num()
        datos_materialsora={
            "id": id,
            "nombre": nombre,
            "costo_kg": costo,
            "tipo": tipo,
            }
        for material in materiales:
            if nombre in material["nombre"]:
                raise ValueError("Ya existe una materialsora con ese nombre, pruebe otro")
        materiales.append(datos_materialsora)
        self.Guardar_Materiales(materiales)
        
    def Eliminar_Material(self,nombre) -> None: #con este se debería poder eliminar materiales de la lista
        materiales = self.Obtener_Materiales()
        materiales_nueva=[]
        counter=0
        for material in materiales:
            if nombre!=material["nombre"]:
                material["id"]=counter
                counter+=1
                materiales_nueva.append(material)
        self.Guardar_Materiales(materiales_nueva)
        
    def Mostrar_Materiales(self) -> None:
        materiales=self.Obtener_Materiales()
        numero_materiales=len(materiales)-1
        print("actualmente hay cargados "+str(numero_materiales)+" material/es")
        if numero_materiales != 0:
            for material in materiales:
                if material["id"] != 0:
                        print("-"+str(material["nombre"])+", un/a "+ str(material["tipo"])+", que cuesta "+str(material["costo_kg"]))
        else:
            print("todavía no hay materiales cargados")
            
    def Buscar_Un_material(self,material) -> str:
        materiales=self.Obtener_Materiales()
        for impre in materiales:
            if material==impre["nombre"]:
                return impre
        else: raise TypeError("no se encontró una materiale con ese nombre, prueba de nuevo. Recuerda revisar las ma0yusculas")
    
    def Mostrar_Una_materiale(self,materiale):
        muestra=self.Buscar_Un_material(materiale)
        if muestra["id"]==0:
            raise TypeError("esa material no existe")
        print(str(muestra["nombre"])+", una "+str(muestra["costo_kg"])+" que costó "+str(muestra["costo_compra"])+" y que por hora cuesta"+str(muestra["costo_hora"]))
    
    def Modificar_Material(self,material,atributo,nuevo) -> None:
        materiales=self.Obtener_Materiales()
        mat_a_modificar=self.Buscar_Un_material(material)
        mat_a_modificar[atributo]=nuevo
        if mat_a_modificar["id"]==0:
            raise TypeError("ese material no existe")
        if atributo=="id":
            raise TypeError("por temas de funcionamiento no se puede modificar el id de los materiales")
        print("se ha modificado el material: "+str(mat_a_modificar["nombre"])+"\n"+"los nuevos valores son:\n-costo por kg: "+str(mat_a_modificar["costo_kg"])+"\n-tipo: "+str(mat_a_modificar["tipo"]))
        for i,impre in enumerate(materiales):
            if impre["id"]==mat_a_modificar["id"]:
                materiales[i]=mat_a_modificar
        self.Guardar_Materiales(materiales)
        