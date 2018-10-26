#!/home/toai/Developpement/LadHyX/bin/python

import os
import sys

proj_path = "/home/toai/Developpement/LadHyX/LadHyX"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LadHyX.settings")
sys.path.append(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.template import Template, Context
from personnel.models import Personnel

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.



if __name__ == "__main__":
	mypathsource = '/home/toai/Developpement/LadHyX/LadHyX/LadHyX/templates/'
	mypathdest = '/home/toai/Developpement/LadHyX/LadHyX/LadHyX/scripts/'
	liste = os.listdir(mypathsource)
	for i in liste:
		
		with open(mypathsource+i, "r") as myfile:
			filedata = myfile.read()
		
	
		newdata = filedata.replace('target=\"_blank\"', '')

		
		with open(mypathdest+i, 'w') as file:
			  file.write(newdata)



