from funcoes import *

bd_path = "file.txt"

while (True):
	# imprimindo o menu principal
	print("\n[1] Cadastrar \n[2] Buscar \n[3] Listar \n[0] Sair \n")
	# capturando entrada do usuário
	op = input("Informe a opção desejada: ")
	
	# realizando operação de acordo com a entrada do usuário
	if (op == "1"):
		# chamando a função de cadastrar veículo e imprimindo mensagens de confirmação
		if cadastrar_veiculo(bd_path):
			print("\n###  VEÍCULO CADASTRADO COM SUCESSO!  ###")
		else:
			print("\n###  VEÍCULO JÁ CADASTRADO!  ###")

	# buscar veículo
	elif (op == "2"):
		# passando a placa a ser buscada
		placa = input("Informe a placa do veículo (abc1234): ")
		car = buscar_veiculo(bd_path, placa.upper())

		# se o veículo for encontrado ele será retornado
		if car:
			# as vírgulas da string serão substituídas por tabulações
			print(car.replace(",","\t"))
			# será exibido um submenu com opção de deleção do veículo
			print("\n[1] Deletar \t[2] Voltar\n")
			# a entrada do usuário é capturada
			op2 = input("Escolher opção: ")
			if op2 == "2":		# volta ao menu principal
				pass
			elif op2 == "1":	# chama a função deletar_veiculo() para este veículo
				if deletar_veiculo(bd_path,placa.upper()):
					print("\n###  VEÍCULO DELETADO  ###\n")	# exibe mensagem de confirmação
		# se o veículo buscado não existir na BD
		else:
			print("\n### VEÍCULO NÃO ENCONTRADO! ###")

	# realizando operação de listar todos os veículos
	elif (op == "3"):
		listar_veiculos(bd_path)
	
	# realizando operação de finaliação
	elif (op == "0"):
		# exibindo mensagem de finalização para o usuário
		print("###  APLICAÇÃO FINALIZADA!  ###")
		break
	# tratando situação de entrada do usuário inválida
	elif not op.isnumeric():
		# limpando a tela
		limpar_tela()
		# exibindo opções válidas
		print("\n###  AS OPÇÕES VÁLIDAS SÃO: 0, 1, 2, 3  ###")

