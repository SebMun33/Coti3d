import modulo_utilidades;

ruta = modulo_utilidades.Ruta_De_Archivo()

class Material:
    def __init__(self) -> None:
        pass

    def obtener_num(self) -> None: #funcion para obtener el indice de la lista de materiales
        return ruta.Obtener_Cantidad("materiales.json","materiales")

    def Obtener_Materiales(self) -> None:  #esta funcion es para recuperar el diccionario de materiales del json
        return ruta.Obtener_Elementos("materiales.json", "materiales")

    def Guardar_Materiales(self,materiales:dict) -> None: #esta función es para actualizar el diccionario del json
        ruta.Guardar_Elementos("materiales.json","materiales",materiales)

    def Agregar_Material(self,nombre,costo,tipo,detalle) -> None: #esta funcion es la que le permite al usuario agragar nuevas materiales a al json de materiales
        materiales=self.Obtener_Materiales()
        id = self.obtener_num()
        datos_material={
            "id": id,
            "nombre": nombre,
            "costo_kg": costo,
            "tipo": tipo,
            "detalle": detalle
            }
        for material in materiales:
            if nombre in material["nombre"]:
                raise ValueError("Ya existe una material con ese nombre, pruebe otro")
        materiales.append(datos_material)
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
        
    def Mostrar_Materiales(self) -> None: #esta función muestra la lista de materiales
        materiales=self.Obtener_Materiales()
        numero_materiales=len(materiales)-1
        print("actualmente hay cargados "+str(numero_materiales)+" material/es:\n")
        if numero_materiales != 0:
            for material in materiales:
                if material["id"] != 0:
                        print("  nombre: "+str(material["nombre"])+"\ncosto_kg: "+str(material["costo_kg"])+"\ntipo: "+str(material["tipo"])+"\ndescripcion: "+str(material["detalle"])+"\n")
        else:
            print("todavía no hay materiales cargados")
            
    def Buscar_Un_material(self,material) -> str: #esta busca un material especifico de la lista
        materiales=self.Obtener_Materiales()
        for impre in materiales:
            if material==impre["nombre"]:
                return impre
        else: raise TypeError("no se encontró una materiale con ese nombre, prueba de nuevo. Recuerda revisar las ma0yusculas")
    
    def Mostrar_Una_materiale(self,materiale): #muestra un solo material de la lista
        muestra=self.Buscar_Un_material(materiale)
        if muestra["id"]==0:
            raise TypeError("esa material no existe")
        print("nombre: "+str(muestra["nombre"])+"\ncosto_kg: "+str(muestra["costo_kg"])+"\ntipo: "+str(muestra["tipo"])+"\nDescripcion: "+str(muestra["detalle"]))
    
    def Modificar_Material(self,material,atributo,nuevo) -> None: #modifica un material de la lista de guardados
        materiales=self.Obtener_Materiales()
        mat_a_modificar=self.Buscar_Un_material(material)
        mat_a_modificar[atributo]=nuevo
        if mat_a_modificar["id"]==0:
            raise TypeError("ese material no existe")
        if atributo=="id":
            raise TypeError("por temas de funcionamiento no se puede modificar el id de los materiales")
        print("se ha modificado el material: "+str(mat_a_modificar["nombre"])+"\n"+"los nuevos valores son:\n-costo por kg: "+str(mat_a_modificar["costo_kg"])+"\n-tipo: "+str(mat_a_modificar["tipo"])+"\nDescripcion: "+str(mat_a_modificar["detalle"]))
        for i,impre in enumerate(materiales):
            if impre["id"]==mat_a_modificar["id"]:
                materiales[i]=mat_a_modificar
        self.Guardar_Materiales(materiales)
        
    def Obtener_Id_Material(self,material) -> int:
        impresoras=self.Obtener_Materiales()
        for imp in impresoras:
            if imp["nombre"]==material:
                return imp["id"]
        