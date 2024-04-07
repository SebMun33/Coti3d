import modulo_utilidades
import modulo_cotizaciones

cot = modulo_cotizaciones.Cotizaciones()
ruta = modulo_utilidades.Ruta_De_Archivo()

class Ventas():
    def __init__(self) -> None:
        pass
    
    def Obtener_Cotizaciones(self) -> list:
        cotizaciones = cot.Obtener_Historial
        return cotizaciones
    
    def Obtener_Ventas(self) -> list:
        ventas = ruta.Obtener_Elementos("historial_ventas.json","ventas")
        return ventas
    
    def Actualizar_Ventas(self,lista_ventas:list) -> None:
        ruta.Guardar_Elementos("historial_ventas.json","ventas",lista_ventas)
        pass
    
    def Concretar_Venta(self,cliente:str,impresion:str) -> None:
        nueva_venta = cot.Seleccionar_Cotizacion(cliente,impresion)
        historial = self.Obtener_Ventas()
        historial.append(nueva_venta)
        self.Actualizar_Ventas(historial)
        pass
    
    def Seleccionar_Venta(self,cliente:str,impresion:str) -> list:
        historial = self.Obtener_Ventas()
        for vta in historial:
            if vta["cliente"]==cliente and vta["impresion"]==impresion:
                return vta
    
    def eliminar_venta(self,cliente:str,impresion:str) -> list:
        historial = self.Obtener_Ventas()
        seleccion=self.Seleccionar_Venta(cliente,impresion)
        historial.remove(seleccion)
        self.Actualizar_Ventas()
        pass
        