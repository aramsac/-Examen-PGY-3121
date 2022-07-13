from itertools import product
from django.shortcuts import redirect, render
from app.CarritoCompra import CarritoCompra

from app.models import Producto

def tienda(request):
    productos = Producto.objects.all()
    return render(request,'carrito-compra.html',{'productos':productos})

def agregar_producto(request,producto_id):
    carritoCompra = CarritoCompra(request)
    producto = Producto.objects.get(id=producto_id)
    carritoCompra.agregarProducto(producto)
    return redirect("app:tienda")

def eliminar_producto(request,producto_id):
    carritoCompra = CarritoCompra(request)
    producto = Producto.objects.get(id=producto_id)
    carritoCompra.eliminar(producto)

def restar_producto(request,producto_id):
    carritoCompra = CarritoCompra(request)
    producto = Producto.objects.get(id=producto_id)
    carritoCompra.restar(producto)

def limpiar_carritoCompra(request):
    carritoCompra = CarritoCompra(request)
    carritoCompra.limpiar()
    return redirect("app:tienda")