import os

# função para limpar a tela
def limpar_tela():
	os.system("cls" if os.name == "nt" else "clear")

# função para calcular valor do serviço
def calcular_valor(nRodas):
	valor = 1
	for i in range(1,nRodas+1):
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
	nPneus = input("Quantidade de pneus do veículo (padrão:4): ")
	nPneus = 4 if nPneus == "" else int(nPneus)

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
			print("\n### LISTA VAZIA! ###")

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
	#opCod=2: chama editar_veiculo()
	#opCod=3: chama deletar_veiculo (0)
	
	limpar_tela()

	try:
		# abrindo conexão com a BD
		bd = open(bd_path)
		# passando as informações da BD para uma lista
		veiculos = bd.readlines()

		# verificando se existem veículos na BD
		if len(veiculos) == 0 and opCod != 1:
			print("\n### LISTA VAZIA! ###")
			return False

		print("\nBuscando placa {}".format(placa))
		# iterando sobre os veículos em busca do match
		for veiculo in veiculos:
			if placa in veiculo:
				while True:
					if opCod == 0 or opCod == 1:
						return veiculo
					elif opCod == 2:
						veiculo_editado = editar_veiculo()
						index = veiculos.index(veiculo)
						veiculos[index] = veiculo_editado
						print("\n### VEÍCULO EDITADO ###")
						op = input("\n[Aperte qualquer techa para voltar] ")
						break
					elif opCod == 3:
						veiculos = deletar_veiculo(veiculos,placa)
						print("\n### VEÍCULO DELETADO ###")
						op = input("\n[Aperte qualquer techa para voltar] ")
						break
	except FileNotFoundError:
		print("### BASE DE DADOS NÃO ENCONTRADA! ###")
		bd = open(bd_path,"w")
		print("### BASE DE DADOS CRIADA! ###")
	finally:
		# granvando novas informações na BD se foi feita alguma alteração
		if opCod == 2 or opCod == 3:
			bd.close()
			bd = open(bd_path,"w")
			for v in veiculos:
				bd.write(v)
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
	nPneus = input("Quantidade de pneus do veículo (padrão:4): ")
	nPneus = 4 if nPneus == "" else int(nPneus)
	return "{},{},{},{},{}\n".format(marca.upper(),modelo.upper(),ano,placa.upper(),calcular_valor(nPneus))

# função para deletar veículos
def deletar_veiculo(veiculos, placa):
		# iterando sobre a lista
		for v in veiculos:
			# verificando match da placa
			if placa in v:
				# removendo veículo encontrado
				veiculos.remove(v)
				return veiculos
		return False