class CarritoCompra:


    """
    inicializador de carrito de compra
    """
    def __init__(self , request):
        self.request = request
        self.session = request.session
        carritoCompra = self.session["carritoCompra"]
        if not carritoCompra:
            self.session["carritoCompra"]={}
            self.carritoCompra = self.session["carritoCompra"]
        else:
            self.carritoCompra = carritoCompra


    def agregarProducto(self,producto):
        id = str(producto.id)

        # si el producto no esta en el carrito
        if id not in self.carritoCompra.keys():
            self.carritoCompra[id]  = {
                "producto_id"       : producto.id,
                "nombre_producto"   : producto.nombre,
                "acumulado"         : producto.precio,
                "cantidad"          : 1,
            }
        else:
            self.carritoCompra[id]["cantidada"]+=1
            self.carritoCompra[id]["acumulado"]+=producto.precio
        self.guardar_carritoCompra()
    
    def guardar_carritoCompra(self):
        self.session["carritoCompra"]=self.carritoCompra
        self.session.modified = True
    
    
    def eliminar(self,producto):
        id = str(producto.id)
        if id in self.carritoCompra:
            del self.CarritoCompra[id]
            self.guardar_carritoCompra()
    
    
    def restar(self,producto):
        id = str(producto.id)
        if id in self.carritoCompra.keys():
            self.CarritoCompra[id]["cantidad"] -=1
            self.carritoCompra[id]["acumulado"]-= producto.precio
            if self.carritoCompra[id]["cantidad"] <=0:
                self.eliminar(producto)
            self.guardar_carritoCompra()
    
    def limpiar(self):
        self.session["carritoCompra"]={}
        self.session.modified = {True}