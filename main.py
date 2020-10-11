"""
programa para cadastrar, buscar, deletar e listar veículos de lava a jato.
"""
from funcoes import *

bd_path = "file.txt"

while (True):
	# imprimindo o menu principal
	print("\n[1] Cadastrar \n[2] Buscar \n[3] Listar \n[0] Sair \n")
	# capturando entrada do usuário
	op = input("Informe a opção desejada: ")
	
	# realizando operação de acordo com a entrada do usuário
	if (op == "1"):
		while(True):
			# chamando a função de cadastrar veículo e imprimindo mensagens de confirmação
			if cadastrar_veiculo(bd_path):
				limpar_tela()
				print("### VEÍCULO CADASTRADO COM SUCESSO! ###")
				op1 = input("\n[Enter Para Voltar] ")
			else:
				limpar_tela()
				print("### VEÍCULO JÁ EXISTE NA BASE DE DADOS! ###")
				op1 = input("\n[Enter Para Voltar] ")
			if op1 == "":
				break

	# buscar veículo
	elif (op == "2"):
		limpar_tela()
		placa = input("\nInformar placa do veículo (abc1234): ")	# informando a placa a ser buscada
		while(True):
			car = buscar_veiculo(bd_path, placa.upper())						# buscando veículo
			if car:																									# se o veículo for encontrado ele será retornado
				print(car.replace(",","\t"))													# as vírgulas da string serão substituídas por tabulações
			else:																										# se o veículo buscado não existir na BD
				print("\n### VEÍCULO NÃO ENCONTRADO! ###")

			print("\n[0] Voltar \t[1] Deletar \t[2] Editar")				# será exibido um submenu
			op2 = input("\nEscolher opção: ")													# a entrada do usuário é capturada
			if op2 == "0":																					# volta ao menu principal
				limpar_tela()
				break
			elif op2 == "1":
				limpar_tela()
				# chama buscar_veiculo() com opCod para deletar_veiculo()
				buscar_veiculo(bd_path,placa.upper(),3)
				break						
			elif op2 == "2":
				limpar_tela()
				# chama buscar_veiculo() com opCod para editar_veiculo()
				buscar_veiculo(bd_path, placa.upper(),2)
				break
			else:
				pass			

	# realizando operação de listar todos os veículos
	elif (op == "3"):
		while(True):
			listar_veiculos(bd_path)
			# submenu para voltar
			op2 = input("\n[Enter Para Voltar] ")
			if op2 == "":
				limpar_tela()
				break
	
	# realizando operação de finaliação
	elif (op == "0"):
		limpar_tela()
		# exibindo mensagem de finalização para o usuário
		print("\n### APLICAÇÃO FINALIZADA! ###\n")
		break
	# tratando situação de entrada do usuário inválida
	elif not op.isnumeric():
		# limpando a tela
		limpar_tela()
		# exibindo opções válidas
		print("\n### AS OPÇÕES VÁLIDAS SÃO: 0, 1, 2, 3 ###")