from django.shortcuts import render
from api.serializers import Todoserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Todo
import requests 

# Create your views here.
def index(request):
    url = requests.get('http://localhost:8000/api/v1/alltodos')
    data = url.json()
    return render(request, 'page/index.html', {'data': data})

@api_view(['POST'])
def createtodo(request):
    record = Todoserializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['GET'])
def alltodos(request):
    record = Todo.objects.all()
    info = Todoserializer(record, many=True)
    return Response(info.data)

@api_view(['DELETE'])
def delete(request, id):
    record = Todo.objects.get(id=id)
    record.delete()
    return Response('Record Deleted')

@api_view(['PUT'])
def edittodos(request, id):
    record = Todo.objects.get(id=id)
    info = Todoserializer(data = request.data, instance=record)
    if info.is_valid():
        info.save()
        return Response('Record Editted')

def index(request):
    url = requests.get('http://localhost:8000/api/v1/alltodos')
    data = url.json()
    return render(request, 'page/index.html', {'data': data})