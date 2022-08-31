from functools import partial
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializer import Items

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def contents(request):
    if request.method == 'GET':
        data = Data.objects.all()
        serializer = Items(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = Items(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer = Items(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Data.objects.get(id = data['id'])
        serializer = Items(obj, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    else: 
        data = request.data
        obj = Data.objects.get(id = data['id'])
        obj.delete()
        return Response(200)
