import datetime as dtime;
import json;
import os;


class Impresora:
    def __init__(self) -> None:
        pass

    def obtener_num(self) -> None: #funcion para obtener el indice de la lista de impresoras
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__)) #estas tres lineas son para obtener la ruta dinamica del archivo de data, de seguro se puede optimizar un poco, debería hacerlo
            data_dir = os.path.join(current_dir, "data")
            with open(os.path.join(data_dir, "impresoras.json"),"r") as file:
                data=json.load(file)
                return len(data["impresoras"])
        except FileNotFoundError:
            return 0

    def Obtener_Impresoras(self) -> None:  #esta funcion es para recuperar el diccionario de impresoras del json
        current_dir=os.path.dirname(os.path.abspath(__file__))
        data_dir=os.path.join(current_dir,"data")
        with open(os.path.join(data_dir,"impresoras.json"),"r") as file:
            data=json.load(file)
            return data["impresoras"]

    def Guardar_Impresoras(self,impresoras:dict) -> None: #esta función es para actualizar el diccionario del json
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        with open(os.path.join(data_dir, "impresoras.json"), "w") as file:
            json.dump({"impresoras":impresoras},file,indent=4)

    def Agregar_Impresora(self,alias,modelo,costo_compra,costo_hora,tipo) -> None: #esta funcion es la que le permite al usuario agragar nuevas impresoras a al json de impresoras
        impresoras=self.Obtener_Impresoras()
        id = self.obtener_num()
        datos_impresora={
            "id": id,
            "alias": alias,
            "modelo": modelo,
            "costo_compra": costo_compra,
            "costo_hora": costo_hora,
            "tipo_maquina": tipo
        }
        for impre in impresoras:
            if alias in impre["alias"]:
                raise ValueError("Ya existe una impresora con ese Alias, pruebe otro")
        impresoras.append(datos_impresora)
        self.Guardar_Impresoras(impresoras)
        
    def Eliminar_Impresora(self,alias) -> None: #con este se debería poder eliminar impresoras de la lista
        impresoras = self.Obtener_Impresoras()
        impresoras_nueva=[]
        counter=0
        for impre in impresoras:
            if alias!=impre["alias"]:
                impre["id"]=counter
                counter+=1
                impresoras_nueva.append(impre)
        self.Guardar_Impresoras(impresoras_nueva)

print(os.path.abspath(os.path.join("data", "impresoras.json")))

nueva_impresora = Impresora()
nueva_impresora.Agregar_Impresora("Marta2", "Modelo Z", 1200, 11, "Filamento")
nueva_impresora.Eliminar_Impresora("jesus")