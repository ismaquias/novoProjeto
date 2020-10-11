import os

# função para limpar a tela
def limpar_tela():
	os.system("cls" if os.name == "nt" else "clear")

# função para calcular valor do serviço
def calcular_valor(nRodas):
	valor = 1
	for i in range(1,nRodas):
		valor *= i
	return valor

# função para cadastrar veículos
def cadastrar_veiculo(bd_path):
	limpar_tela()
	# coletando informações do veículo
	print("Informações do Cadastro \n")
	marca = input("Marca do veículo: ")
	modelo = input("Modelo do veídulo: ")
	ano = input("Ano do veículo: ")
	placa = input("Placa do veículo (ABC1234): ")
	nPneus = int(input("Quantidade de pneus do veículo: "))

	# verificando se o veículo já existe na BD
	if buscar_veiculo(bd_path,placa.upper(), opCod=1):
		return False

	try:
		# abrindo conexão com a BD
		bd = open(bd_path, "a+")
		# montando o registro que será salvo na BD
		registro = "{},{},{},{},{}\n".format(marca.upper(),modelo.upper(),ano,placa.upper(),calcular_valor(nPneus))
		# gravando o registro na BD
		bd.write(registro)
		return True
	finally:
		# fechando conexão com a BD
		bd.close()

# funcão para listar todos os veículos
def listar_veiculos(bd_path):
	limpar_tela()

	try:
		# abrindo conexão com a BD
		bd = open(bd_path)
		# passando as informações da BD para uma lista
		carros = bd.readlines()

		# verificando se existem veículos na BD
		if len(carros) == 0:
			print("### LISTA VAZIA! ###\n")

		# imprimindo o cabeçalho da tabela
		if (len(carros) != 0):
			print("{}{}{}{}{}".format("MARCA".ljust(15), "MODELO".ljust(15), "ANO".ljust(8), "PLACA".ljust(10), "VALOR(R$)"))
		
		# iterando sobre os veículos imprimindo-os
		for car in carros:
			# transformando a string em lista
			c = car.split(",")
			# imprimindo as informações formatadas
			print("{}{}{}{}{:.2f}".format(c[0].ljust(15), c[1].ljust(15), c[2].ljust(8), c[3].ljust(10), int(c[4])))
	except FileNotFoundError:
		print("### BASE DE DADOS NÃO ENCONTRADA! ###")
		bd = open(bd_path,"w")
		print("### BASE DE DADOS CRIADA! ###")
	finally:
		# fechando conexão com a BD
		bd.close()

# função de busca e manipulação de veiculos
def buscar_veiculo(bd_path, placa, opCod=0):
	#opCod=0: busca normal
	#opCod=1: desativa msg de lista vazia
	#opCod=2: chama editar_veiculo
	#opCod=3: chama deletar_veiculo 
	
	limpar_tela()
	print("Buscando placa {}\n".format(placa))

	try:
		# abrindo conexão com a BD
		bd = open(bd_path)
		# passando as informações da BD para uma lista
		carros = bd.readlines()

		# verificando se existem veículos na BD
		if len(carros) == 0 and opCod == 0:
			print("### LISTA VAZIA! ###\n")
			return False

		# iterando sobre os veículos em busca do match
		for car in carros:
			if placa in car:
				if opCod == 0 or opCod == 1:
					return car
				elif opCod == 2:
					car = editar_veiculo()
					break
				elif opCod == 3:
					carros = deletar_veiculo(carros,placa)
					bd.close()
					bd.open(bd_path,"w")
					for car in carros:
						bd.write(car)
					break

	except FileNotFoundError:
		print("### BASE DE DADOS NÃO ENCONTRADA! ###")
		bd = open(bd_path,"w")
		print("### BASE DE DADOS CRIADA! ###")
	finally:
		# fechando conexão com a BD
		bd.close()

# função para editar veículos
def editar_veiculo():
	limpar_tela()
	print("Alteração do Cadastro \n")
	# coletando novas informações
	marca = input("Marca do veículo: ")
	modelo = input("Modelo do veídulo: ")
	ano = input("Ano do veículo: ")
	placa = input("Placa do veículo (ABC1234): ")
	nPneus = int(input("Quantidade de pneus do veículo: "))
	return "{},{},{},{},{}\n".format(marca.upper(),modelo.upper(),ano,placa.upper(),calcular_valor(nPneus))

# função para deletar veículos
def deletar_veiculo(carros, placa):
		# iterando sobre a lista
		for car in carros):
			# verificando match da placa
			if placa in car:
				# removendo veículo encontrado
				carros.remove(car)
				return carros
		return False