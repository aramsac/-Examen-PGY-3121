from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json
from app.models import Producto

@api_view(['GET', 'POST'])
def apiproductos(request):
    if request.method == 'GET':
        response_json = []
        productos = Producto.objects.all()       
        for producto in productos:
            json_productos = {
                'nombre'    : producto.nombre,
                'categoria' : producto.categoria,
                'precio'    : producto.precio,
            }
            response_json.append(json_productos)
        status_code = status.HTTP_200_OK
        print('response_json', response_json)
        return HttpResponse(json.dumps(response_json, ensure_ascii=False), content_type="application/json", status=status_code)  
