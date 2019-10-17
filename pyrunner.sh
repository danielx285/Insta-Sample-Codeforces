#!/bin/bash
time python $1.py < ./cache/$1$2.txt > ./cache/$1_out.txt
