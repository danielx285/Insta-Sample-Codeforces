#!/usr/bin/env python2.7
#coding: utf-8

import requests
from bs4 import BeautifulSoup
import argparse
import lxml
import subprocess
import sys

parser = argparse.ArgumentParser(description='Executa seu arquivo python ou cpp testando os samples do codeforces')
parser.add_argument('mode', type=str, help='Modo de execução podendo ser:\n C(Contest)\nG(Gym)\nN(Execução Normal)\nGN(Problemas de Gym)')
parser.add_argument('code', type=str, help='Código do contest pode ser encontrado facilmente na barra de endereços')
parser.add_argument('file_arg', type=str, help='Nome do arquivo podendo ter a extensão .py ou ponto .cpp')
args = parser.parse_args()

if "__name__" == "__main__":
	try :
		#Pegando argumentos
		mode = args.mode
		file_arg, ext = args.file_arg.split(".")
		code = args.code

	except :
		print "Argumentos invalidos ou não reconhecidos"
		print "Digite: insta {modo de execução} {Nome_do_arquivo.extensão} {Código do contest}"
		exit()

	#Se o usuario entrar em modo contestante
	if mode == "c":
		#Exemplo de endereço
		#https://codeforces.com/contest/102323/problem/A
		r = requests.get("http://codeforces.com/contest/%s/problem/%s" %( code, file_arg))
	
	#Se o usuario entrar em modo for gym
	elif mode == "g":
		# Exemplo de endereço
		# https://codeforces.com/gym/102323/problem/A
		r = requests.get("http://codeforces.com/gym/%s/E" % code)
	
	#Se o usuario entrar em modo normal
	elif mode == "n":
		# Exemplo de endereço
		# https://codeforces.com/problemset/problem/1214/C
		r = requests.get("http://codeforces.com/problemset/problem/%s/%s" % (code, file_arg))
	
	#Se o usuario entrar em modo para problemas de gym
	elif mode == "gn":
		# Exemplo de endereço
		# https://codeforces.com/gym/102323/problem/A
		r = requests.get("http://codeforces.com/gym/%s/problem/%s" % (code, file_arg))
	
	else:
		print "Argumentos invalidos ou não reconhecidos"
		print "Digite: insta {modo de execução} {Nome_do_arquivo.extensão} {Código do contest}"
		exit()

	search = BeautifulSoup(r.content, 'lxml')
	statments = [ str(ans).replace("<br/>", "\n").strip("<pre>").strip("</pre>").strip() for ans in search.find_all("pre")]

	in_out = {}

	for s in xrange(0, len(statments), 2):
		in_out[statments[s]] = statments[s+1]

	for k in in_out:
		print "Input: "
		print k

		print "Output: "
		print in_out[k]

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
