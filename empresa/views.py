#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from empresa.models import Viagem
from empresa.serializers import ViagemSerializer
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
		game.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
