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
        
    def Mostrar_Impresoras(self) -> None:
        impresoras=self.Obtener_Impresoras()
        numero_impresoras=len(impresoras)-1
        print("actualmente hay cargadas "+str(numero_impresoras)+" impresora/s")
        if numero_impresoras != 0:
            for impre in impresoras:
                if impre["id"] != 0:
                        print("-"+str(impre["alias"])+", una "+ str(impre["modelo"])+", que costó "+str(impre["costo_compra"])+" y que por hora cuesta "+str(impre["costo_hora"]))
        else:
            print("todavía no hay impresoras cargadas")
            
    def Buscar_Una_Impresora(self,impresora) -> str:
        impresoras=self.Obtener_Impresoras()
        for impre in impresoras:
            if impresora==impre["alias"]:
                return impre
        else: raise TypeError("no se encontró una impresora con ese alias, prueba de nuevo. Recuerda revisar las ma0yusculas")
    
    def Mostrar_Una_Impresora(self,impresora):
        muestra=self.Buscar_Una_Impresora(impresora)
        if muestra["id"]==0:
            raise TypeError("esa impresora no existe")
        print(str(muestra["alias"])+", una "+str(muestra["modelo"])+" que costó "+str(muestra["costo_compra"])+" y que por hora cuesta"+str(muestra["costo_hora"]))
    
    def Modificar_Impresora(self,impresora,atributo,nuevo) -> None:
        impresoras=self.Obtener_Impresoras()
        impre_a_modificar=self.Buscar_Una_Impresora(impresora)
        impre_a_modificar[atributo]=nuevo
        if impre_a_modificar["id"]==0:
            raise TypeError("esa impresora no existe")
        if atributo=="id":
            raise TypeError("por temas de funcionamiento no se puede modificar el id de las impresoras")
        print("se ha modificado la impresora: "+str(impre_a_modificar["alias"])+"\n"+"los nuevos valores son:\n-modelo: "+str(impre_a_modificar["modelo"])+"\n-costo de compra: "+str(impre_a_modificar["costo_compra"])+"\n-costo por hora: "+str(impre_a_modificar["costo_hora"]))
        for i,impre in enumerate(impresoras):
            if impre["id"]==impre_a_modificar["id"]:
                impresoras[i]=impre_a_modificar
        self.Guardar_Impresoras(impresoras)
        