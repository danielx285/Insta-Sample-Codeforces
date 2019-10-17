#!/usr/bin/env python2.7
#coding: utf-8
from os import path
import thread
import commands
import time
import argparse

parser = argparse.ArgumentParser(description="A função deste é arquivo é ser o cão de guarda validador")
parser.add_argument('arg_file', type=str, help="Nome do arquivo")
parser.add_argument('case_number', type=str, help="Numero do caso de teste que está sendo testado")
args = parser.parse_args()

print "aaaa"

arg_file = args.arg_file.split(".")

tle = 2.0
ar = []
def run():
    if len(arg_file) == 2 and arg_file[1] == "py":
        out = commands.getoutput("./pyrunner.sh %s %s" % (args.arg_file, args.case_number))

    else:
        out = commands.getoutput("./runner.sh %s %s" % (args.arg_file, args.case_number))
    print out
    ar.append(out.split("real")[1])
    print ar
    print len(ar)

thread.start_new_thread(run, ())

time.sleep((tle + 0.1))

#Se houve modificação na lista então a execução foi conforme planejada...
if len(ar) >= 1:
    print "Time", ar[0].strip().split("\n")[0]

#Se a lista não foi modificada é porque o processo ainda está sendo executado e precisa morrer...
else:    
    cmd = "ps -ef | grep prog.py"
    kill = commands.getoutput(cmd).split("\n")[0].split()[1]
    commands.getoutput("kill -9 %s" % kill)
    print "TLE case #" % (args.case_number + 1), tle, "ms"
