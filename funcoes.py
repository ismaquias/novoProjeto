import os

# função para limpar a tela
def limpar_tela():
	os.system("cls" if os.name == "nt" else "clear")

# função para calcular valor do serviço
def calcular_valor(nRodas):
	valor = 1
	for i in range(nRodas):
		valor *= i
	return valor

# função para cadastrar veículos
def cadastrar_veiculo(bd_path):
	limpar_tela()
	print("Informações do Cadastro \n")
	# coletando as informações do veículo
	marca = input("Marca do veículo: ")
	modelo = input("Modelo do veídulo: ")
	ano = input("Ano do veículo: ")
	placa = input("Placa do veículo (ABC1234): ")

	# verificando se o veículo já existe na BD
	if buscar_veiculo(bd_path,placa.upper(), opCod=0):	#opCod=0 desativa msg de lista vazia
		return False

	try:
		# abrindo conexão com a BD
		bd = open(bd_path, "a+")
		# montando o registro que será salvo na BD
		registro = "{},{},{},{}\n".format(marca.upper(),modelo.upper(),ano,placa.upper())
		# gravando o registro na BD
		bd.write(registro)
		return True
	finally:
		# fechando conexão com a BD
		bd.close()

def buscar_veiculo(bd_path, placa, opCod=1):
	try:
		# abrindo conexão com a BD
		bd = open(bd_path)
		# passando as informações da BD para uma lista
		carros = bd.readlines()

		# verificando se existem veículos na BD
		if len(carros) == 0 and opCod == 0:
			print("###  LISTA VAZIA!  ###")
			return False

		# iterando sobre os veículos em busca do match
		for car in carros:
			if placa in car:
				return car

	except FileNotFoundError:
		print("###  BASE DE DADOS NÃO ENCONTRADA  ###")
	finally:
		# fechando conexão com a BD
		bd.close()

# funcão para listar todos os veículos
def listar_veiculos(bd_path):
	try:
		# abrindo conexão com a BD
		bd = open(bd_path, "a+")
		# passando as informações da BD para uma lista
		carros = bd.readlines()

		# verificando se existem veículos na BD
		if len(carros) == 0:
			print("###  LISTA VAZIA!  ###")

		# imprimindo o cabeçalho da tabela
		if (len(carros) != 0):
		print("{}{}{}{}".format("MARCA".ljust(15,"_"), "MODELO".ljust(15,"_"), "ANO".ljust(8,"_"), "PLACA".ljust(8,"_")))
		
		# iterando sobre os veículos imprimindo-os
		for car in carros:
			# transformando a string em lista
			c = car.split(",")
			# imprimindo as informações formatadas
			print("{}{}{}{}".format(c[0].ljust(15), c[1].ljust(15), c[2].ljust(8), (c[3])[:7]))
	except FileNotFoundError as f:
		print("### BASE DE DADOS NÃO ENCONTRADA! ###")
	finally:
		# fechando conexão com a BD
		bd.close()

# função para deletar veículos
def deletar_veiculo(bd_path,placa):
	try:
		# abrindo conexão com a BD
		bd = open(bd_path,"r+")
		# passando as informações da BD para uma lista
		carros = bd.readlines()

		# iterando sobre a lista
		for i in range(len(carros)):
			# verificando match da placa
			if placa in carros[i]:
				# removendo veículo encontrado
				carros.pop(i)
				# fechando conexão com a BD
				bd.close()
				# abrindo conexão para sobrescrever a BD antiga
				bd = open(bd_path,"w")
				# inserindo veículos na BD
				for c in carros:
					bd.write(c)
				return True
		return False
	except FileNotFoundError:
		print("### BASE DE DADOS NÃO ENCONTRADA! ###")
	finally:
		# fechando conexão com a BD
		bd.close()