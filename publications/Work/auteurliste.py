#!/home/toai/Developpement/LadHyX/bin/python

import sys
import csv

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|',
                       fieldnames=[
                           'Code',
                           'Auteur',
                           'Auteurs1'
                            ]
                            )
    Liste = []
    for row in reader:
        # print(row['Code'], row['Auteur'])
        person = (row['Code'], row['Auteur'])
        Liste.append(person)

    mytuple = tuple(Liste)
