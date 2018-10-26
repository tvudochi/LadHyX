#!/home/toai/Developpement/LadHyX/bin/python
# -*- coding: utf-8 -*-
import subprocess
import csv

prog = '/home/toai/Developpement/LadHyX/LadHyX/publications/Prog/\
search-pub-rp-stdin'

result = subprocess.Popen(
    [prog, '2017', '0', '0'],
    stdout=subprocess.PIPE,
    shell=False, bufsize=1400000)

stdout_value = result.communicate()[0].decode("iso8859-15")

l = stdout_value.splitlines()
mycsv = csv.DictReader(l, delimiter='+',
                       fieldnames=[
                           'date',
                           'auteurs',
                           'titre',
                           'journal',
                           'index',
                           'abstract',
                           'preprint'
                       ])

# for dict in list(mycsv):
#    print(dict)
print(list(mycsv))

