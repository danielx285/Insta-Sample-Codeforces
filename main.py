import requests
from bs4 import BeautifulSoup
import lxml
import subprocess
import sys

mode = sys.args[2]
file_arg = sys.args[3]

if mode == "contest":
	code = int(raw_input("Code contest: "))
	r = requests.get("http://codeforces.com/contest/code/E" % (ord(code)))
	

	
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
