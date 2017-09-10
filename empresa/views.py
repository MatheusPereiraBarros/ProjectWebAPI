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

# Create your views here.
