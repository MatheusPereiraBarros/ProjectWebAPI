#from django.contrib.auth.models import User, Group

from rest_framework import serializers
from empresa.models import Viagem


class ViagemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Viagem
		fields = ('idViagem', 'horario', 'quantPassageiros', 'idRota', 'idOnibus', 'idFuncionario')

"""class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

"""

