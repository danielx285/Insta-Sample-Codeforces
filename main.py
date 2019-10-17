#!/usr/bin/env python2.7
#coding: utf-8

import requests
from bs4 import BeautifulSoup
from os import system, path

import argparse
import lxml
import commands
import sys

parser = argparse.ArgumentParser(description='Executa seu arquivo executável ou .py testando os samples do codeforces')
parser.add_argument('mode', type=str, help='Modo de execução podendo ser:\n C(Contest)\nG(Gym)\nN(Execução Normal)\nGN(Problemas de Gym)')
parser.add_argument('code', type=str, help='Código do contest pode ser encontrado facilmente na barra de endereços do codeforces')
parser.add_argument('file_arg', type=str, help='Nome do arquivo podendo ter a extensão .py ou ser um executável qualquer já compilado')
args = parser.parse_args()

if __name__ == "__main__":
	#O uso do getoutput é pra evitar o runtime caso eu crie um cache mas o diretório já existe
	commands.getoutput('mkdir cache')
	
	try :
		#Pegando argumentos
		mode = args.mode.lower()
		file_arg = args.file_arg.split(".")
		code = args.code
		file_arg[0].upper()

	except :
		print "Argumentos invalidos ou não reconhecidos"
		print "Digite: insta {modo de execução} {Nome_do_arquivo.extensão} {Código do contest}"
		exit()
	
	'''
	A requisição será feita por meio do endereço em formato string. Sendo assim criarei primeiro a
 	a string requisição e depois verei se a mesma é valida...
	'''
	#Se o usuario entrar em modo contestante
	if mode == "c":
		#Exemplo de endereço
		#https://codeforces.com/contest/102323/problem/A
		requisicao = ("https://codeforces.com/contest/%s/problem/%s" %( code, file_arg[0]))
	
	#Se o usuario entrar em modo for gym
	elif mode == "g":
		# Exemplo de endereço
		# https://codeforces.com/gym/102323/problem/A
		requisicao = ("https://codeforces.com/gym/%s/%s" % (code, file_arg[0]))
	
	#Se o usuario entrar em modo normal
	elif mode == "n":
		# Exemplo de endereço
		# https://codeforces.com/problemset/problem/1214/C
		requisicao = ("https://codeforces.com/problemset/problem/%s/%s" % (code, file_arg[0]))
	
	#Se o usuario entrar em modo para problemas de gym
	elif mode == "gn":
		# Exemplo de endereço
		# https://codeforces.com/gym/102323/problem/A
		requisicao = ("https://codeforces.com/gym/%s/problem/%s" % (code, file_arg[0]))
	
	else:
		print "Argumentos invalidos ou não reconhecidos"
		print "Digite: insta {modo de execução} {Nome_do_arquivo} {Código do contest}"
		exit()

    #Tratando códigos de contests errados ou questões inexistentes...
	try :
		request = requests.get(requisicao)
	except :
			
		print "Argumentos invalidos"
		print "Certifique-se de que o código do contest foi inserido corretamente e na ordem correta"
		print "Certifique-se também se há uma questão com o identificada pelo nome do seu arquivo de código"
		print "Certifique-se de que o site do codeforces n está congestionado..."
		exit()

	if len(file_arg) > 2 or (len(file_arg) == 2 and file_arg[1] != 'py'):
		print "Extensões de arquivos suportados: .py ou executável sem extensão já compilado"
		exit()

	search = BeautifulSoup(request.content, 'lxml')
	statments = [ str(ans).replace("<br/>", "\n").strip("<pre>").strip("</pre>").strip() for ans in search.find_all("pre")]

	in_out = []
	
	for s in xrange(0, len(statments), 2):
		in_out.append((statments[s], statments[s+1]))
			
	test_case = 1
	
	save_path = '%s/cache' % (commands.getoutput('pwd'))

	for case in xrange(len(in_out)):

		input_id = '%s%d.txt' % (file_arg[0], test_case)
		complete_path_in = path.join(save_path, input_id)
		input_file = open(complete_path_in, 'w')
		input_file.write(in_out[case][0])
		input_file.close()
		print "Input: "
		print in_out[case][0]
		
		output_id = '%s%d_correct_out.txt' % (file_arg[0], test_case)
		complete_path_out = path.join(save_path, output_id)
		output_file = open(complete_path_out, 'w')
		output_file.write(in_out[case][1])
		output_file.close()
		print "Output: "
		print in_out[case][1]

		if len(file_arg) == 2:
			system("python whatchdog.py %s.py %s" % (file_arg[0], case + 1) )
		else:
			system("python whatchdog.py %s.py %s" % (file_arg[0], case + 1) )
		
		test_case += 1

	'''
	import requests
	from bs4 import BeautifulSoup
	import lxml
	
	def GetMyOutput(ID, Input):
		entrada = open("Answers/Input.txt", "w")
		entrada.write(Input + "\n")
		entrada.close()
		cmd = "cat Answers/Input.txt | python Answers/%i.py" % ID
		return subprocess.Popen(
			cmd, shell=True, stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT, universal_newlines=True).communicate()[0]
	
	def Assert(Expected, Recive):
		if Expected != Recive:
			print("\033[1;31m" +
				  subprocess.Popen("cat Answers/Input.txt" if system() == "Linux" else "type Answers\Input.txt", shell=True,
								   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
								   universal_newlines=True).communicate()[0] + '\x1b[0m')
	
			print("Expected:\n" + Expected)
			print("Recive:\n" + Recive)
			print("\033[0;31m" + '.' + '\x1b[0m')
			return False
		print("\033[0;32m" + '. ' + '\x1b[0m')
		return True
	
	#r = requests.get("http://codeforces.com/problemset/problem/1208/E")
	r = requests.get(input("site: "))
	soup = BeautifulSoup(r.content, 'lxml')
	
	l = [str(name).replace("<br/>","\n").strip("<pre>").strip("</pre>").strip() for name in soup.find_all("pre")]
	
	flag = True
	q = {}
	
	i = 0
	while i < len(l):
		q[l[i]] = q[l[i+1]]
		i += 2
	
	for i in q:
		Assert(q[i],GetMyOutput(ID, i))
	'''
