from datetime import date
import modulo_utilidades
import modulo_impresoras
import modulo_materiales

ruta = modulo_utilidades.Ruta_De_Archivo()
imp = modulo_impresoras.Impresora()
mat = modulo_materiales.Material()

class Cotizaciones:
    def __init__(self) -> None:
        pass
    
    def Obtener_Historial(self)-> int: #obtiene el historial de cotizaciones guardado en el json
        return ruta.Obtener_Elementos("historial_cotizaciones.json","cotizaciones")
    
    def Actualizar_Historial(self,historial:list) -> None: #actualiza el historial del json con los nuevos cambios
        return ruta.Guardar_Elementos("historial_cotizaciones.json","cotizaciones",historial)
    
    def Cotizar_Impresion(self,impresora:str,material:str,peso:int,horas:int,minutos:int) -> int: #esta función se encarga de calcular el precio de costo
        id_imp = imp.Obtener_Id_Impresora(impresora)
        id_mat = mat.Obtener_Id_Material(material)
        costo_kg = ruta.Obtener_Valor("materiales.json","materiales",id_mat,"costo_kg")
        costo_h = ruta.Obtener_Valor("impresoras.json","impresoras",id_imp,"costo_hora")
        costo_impresion = costo_h*horas + (costo_h/60)*minutos + (costo_kg/1000)*peso 
        return costo_impresion
    
    def Cotizar_Venta(self,impresora:str,material:str,peso:int,horas:int,minutos:int,ganancia:int) -> int: #acá se calcula teniendo en cuenta la ganancia
        precio_costo = self.Cotizar_Impresion(impresora,material,peso,horas,minutos)
        precio_venta = precio_costo + precio_costo*(ganancia/100)
        return precio_venta
    
    def Guardar_Cotizacion(self,impresion,cliente:str,impresora:str,material:str,peso:int,horas:int,minutos:int,ganancia:int,costo_imp:int,costo_venta:int) -> None: #esta función se encarga de guardar la cotización en el historial
        historial = self.Obtener_Historial()
        hoy = date.today()
        fecha= hoy.strftime("%d/%m/%Y")
        datos_cotizacion= {
            "impresion":impresion,
            "cliente": cliente,
            "fecha": fecha,
            "maquina": imp.Obtener_Id_Impresora(impresora),
            "material": mat.Obtener_Id_Material(material),
            "horas_impresion": horas,
            "minutos_impresion": minutos,
            "peso_impresion":peso,
            "porcentaje_ganancia":ganancia,
            "costo_impresion":costo_imp,
            "precio_venta":costo_venta
            }
        for coti in historial:
         if coti["cliente"]==cliente and coti["impresion"]==impresion:
             raise ValueError("ese cliente ya tiene esa cotización hecha")
        historial.append(datos_cotizacion)
        self.Actualizar_Historial(historial) 
        pass
    
    def Cargar_Cotización(self,cliente:str,impresion:str) -> list: #esta función se encarga de cargar alguna cotización guardada
        if cliente=="ejemplo" and impresion == "ejemplo":
            raise ValueError("Esa cotización no existe, pruebe de nuevo")
        historial=self.Obtener_Historial()
        for coti in historial:
         if coti["cliente"]==cliente and coti["impresion"]==impresion:
             seleccion=coti
        return seleccion
        
    def Modificar_Cotizacion(self,cliente:str,impresion:str,atributo:str,nuevo_valor:str)->None: #esta función se encarga de modificar la última cotización cargada
        seleccion = self.Cargar_Cotización(cliente,impresion)
        seleccion[atributo]=nuevo_valor
        self.Actualizar_Historial()
        print("se ha modificado la cotización de la impresión: " + impresion + " del cliente: " + cliente + "\nPara más información revise el historial")