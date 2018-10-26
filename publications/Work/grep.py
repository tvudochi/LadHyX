#!/home/toai/Developpement/LadHyX/bin/python

import re
import sys
import csv

with open(sys.argv[2], "r", encoding="iso8859-15") as infofile:
    reg = "^"+sys.argv[1]
    mylist = []
    for line in infofile:
        if re.search(reg, line):

            mylist.append(line.rstrip('\n'))

mycsv = csv.DictReader(mylist, delimiter='|',
                       fieldnames=[
                           'code',
                           'Nom_C',
                           'Nom_D',
                       ])


maliste = list(mycsv)
print(maliste)