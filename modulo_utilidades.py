import os
import json

class Ruta_De_Archivo:
    
    def __init__(self) -> None:
        pass
    
    def Obtener_Cantidad(self,archivo:str,tabla:str):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__)) #estas tres lineas son para obtener la ruta dinamica del archivo de data, de seguro se puede optimizar un poco, debería hacerlo
            data_dir = os.path.join(current_dir, "data")
            with open(os.path.join(data_dir, archivo),"r") as file:
                data=json.load(file)
                return len(data[tabla])
        except FileNotFoundError:
            raise ValueError("no se encontró el archivo")
        
    def Obtener_Elementos(self,archivo:str,tabla:str):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__)) #estas tres lineas son para obtener la ruta dinamica del archivo de data, de seguro se puede optimizar un poco, debería hacerlo
            data_dir = os.path.join(current_dir, "data")
            with open(os.path.join(data_dir, archivo),"r") as file:
                data=json.load(file)
                return data[tabla]
        except FileNotFoundError:
            raise ValueError("no se encontró el archivo")
        
    def Guardar_Elementos(self,archivo:str,tabla:str,diccionario:dict):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(current_dir, "data")
            with open(os.path.join(data_dir, archivo), "w") as file:
                json.dump({tabla:diccionario},file,indent=4)
        except FileNotFoundError:
            raise ValueError("no se encontró el archivo")
        
    def Obtener_Valor(self,archivo:str,tabla:str,indice:int,valor:str) -> int:
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__)) #estas tres lineas son para obtener la ruta dinamica del archivo de data, de seguro se puede optimizar un poco, debería hacerlo
            data_dir = os.path.join(current_dir, "data")
            with open(os.path.join(data_dir, archivo),"r") as file:
                data=json.load(file)
                diccionario = data[tabla]
                return diccionario[indice][valor]
        except FileNotFoundError:
            raise ValueError("no se encontró el archivo")
        
ruta=Ruta_De_Archivo()
print(ruta.Obtener_Elementos("impresoras.json","impresoras"))