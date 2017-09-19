#from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.utils import timezone
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

'''from .serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
'''

@api_view(['GET', 'POST'])
def viagens_list(request):
	if request.method == 'GET':
		viagens = Viagem.objects.all()
		viagens_serializer = ViagemSerializer(viagens, many=True)
		return Response(viagens_serializer.data)

	elif request.method == 'POST':
		viagens_serializer = ViagemSerializer(data=request.data)
		if viagens_serializer.is_valid():
			viagens_serializer.save()
			return Response(viagens_serializer.data, status=status.HTTP_201_CREATED)
			return Response(viagens_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def viagens_detail(request, pk):
	try:
		viagem = Viagem.objects.get(pk=pk)
	except Viagem.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		viagens_serializer = ViagemSerializer(viagem)
		return Response(viagens_serializer.data) 
	elif request.method == 'PUT':
		viagens_serializer = ViagemSerializer(viagem, data=request.data)
		if viagens_serializer.is_valid():
			viagens_serializer.save()
			return Response(viagens_serializer.data)
		return Response(viagens_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		viagem.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
@api_view(['GET', 'POST'])
def funcionarios_list(request):
	if request.method == 'GET':
		funcionarios = Funcionario.objects.all()
		funcionarios_serializer = FuncionarioSerializer(funcionarios, many=True)
		return Response(funcionarios_serializer.data)

	elif request.method == 'POST':
		funcionarios_serializer = FuncionarioSerializer(data=request.data)
		if funcionarios_serializer.is_valid():
			funcionarios_serializer.save()
			return Response(funcionarios_serializer.data, status=status.HTTP_201_CREATED)
			return Response(funcionarios_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def funcoes_list(request):
	if request.method == 'GET':
		funcoes = Funcao.objects.all()
		funcoes_serializer = FuncaoSerializer(funcoes, many=True)
		return Response(funcoes_serializer.data)

	elif request.method == 'POST':
		funcoes_serializer = FuncaoSerializer(data=request.data)
		if funcoes_serializer.is_valid():
			funcoes_serializer.save()
			return Response(funcoes_serializer.data, status=status.HTTP_201_CREATED)
			return Response(funcoes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def rotas_list(request):
	if request.method == 'GET':
		rotas = Rota.objects.all()
		rotas_serializer = RotaSerializer(rotas, many=True)
		return Response(rotas_serializer.data)

	elif request.method == 'POST':
		rotas_serializer = RotaSerializer(data=request.data)
		if rotas_serializer.is_valid():
			rotas_serializer.save()
			return Response(rotas_serializer.data, status=status.HTTP_201_CREATED)
			return Response(rotas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def onibus_list(request):
	if request.method == 'GET':
		onibus = Onibus.objects.all()
		onibus_serializer = OnibusSerializer(onibus, many=True)
		return Response(onibus_serializer.data)

	elif request.method == 'POST':
		onibus_serializer = OnibusSerializer(data=request.data)
		if onibus_serializer.is_valid():
			onibus_serializer.save()
			return Response(onibus_serializer.data, status=status.HTTP_201_CREATED)
			return Response(onibus_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def garagens_list(request):
	if request.method == 'GET':
		garagens = Garagem.objects.all()
		garagens_serializer = GaragemSerializer(garagens, many=True)
		return Response(garagens_serializer.data)

	elif request.method == 'POST':
		garagens_serializer = GaragemSerializer(data=request.data)
		if garagens_serializer.is_valid():
			garagens_serializer.save()
			return Response(garagens_serializer.data, status=status.HTTP_201_CREATED)
			return Response(garagens_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
  """
  get: Return a list of all the existing users.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-list'
  permission_classes = (permissions.IsAuthenticated,)