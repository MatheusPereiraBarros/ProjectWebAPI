from django.db import models
from django.utils import timezone

class Garagem(models.Model):
	idGaragem = models.AutoField(primary_key=True)
	endereco = models.CharField(max_length=255)
	quantVagas = models.IntegerField()

	def saveModel(self):
		self.save()

	def garagem_id(self):
		return self.id

	def __str__(self):
		return 'Garagem: {0}, Endereço: {1}'.format(self.idGaragem, self.endereco)
		

class Onibus(models.Model):
	idOnibus = models.AutoField(primary_key=True)
	marcaOnibus = models.CharField(max_length=140, default='')
	modeloOnibus = models.CharField(max_length=140, default='')
	placa = models.CharField(max_length=8, default='')
	garagem = models.ForeignKey(Garagem, on_delete=models.CASCADE, related_name = 'garagem')

	def saveModel(self):
		self.save()

	def onibus_id(self):
		return self.id

	def __str__(self):
		return self.modeloOnibus

DAYS_OF_WEEK = (
    (0, 'Segunda'),
    (1, 'Terça'),
    (2, 'Quarta'),
    (3, 'Quinta'),
    (4, 'Sexta'),
    (5, 'Sábado'),
    (6, 'Domingo'),
)

class Rota(models.Model):
	idRota = models.AutoField(primary_key=True)
	nomeRota = models.CharField(max_length=140, default='')
	destino = models.CharField(max_length=140, default='')
	partida = models.CharField(max_length=140, default='')
	horario = models.TimeField()
	diaDaSemana = models.IntegerField(choices=DAYS_OF_WEEK)
	valorPassagem = models.BigIntegerField()

	def saveModel(self):
		self.save()

	def rota_id(self):
		return self.id

	def __str__(self):
		return self.nomeRota

class Funcao(models.Model):
	idFuncao = models.AutoField(primary_key=True)
	descricaoFuncao = models.CharField(max_length=140)

	def saveModel(self):
		self.save()

	def funcao_id(self):
		return self.id

	def __str__(self):
		return self.descricaoFuncao

class Funcionario(models.Model):
	idFuncionario = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=255)
	CPF = models.IntegerField()
	idFuncao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name = 'funcao')

	def saveModel(self):
		self.save()

	def funcionario_id(self):
		return self.id

	def __str__(self):
		return self.nome


class Viagem(models.Model):
	idViagem = models.AutoField(primary_key=True)
	horario = models.TimeField()
	quantPassageiros = models.IntegerField()
	idRota = models.ForeignKey(Rota, on_delete=models.CASCADE, related_name = 'rota')
	idOnibus = models.ForeignKey(Onibus, on_delete=models.CASCADE, related_name = 'onibus')
	idFuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name = 'funcionario')

	def saveModel(self):
		self.save()

	def viagem_id(self):
		return self.id

	def __str__(self):
		return 'Viagem: {0}, Rota: {1}'.format(self.idViagem, self.idRota)

