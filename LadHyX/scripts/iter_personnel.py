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


def group(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

if __name__ == "__main__":
    staff = Personnel.objects.all().filter(categorie="ITA").filter(presence=True).order_by('nom')
    template = Template("{% for group in staff %}{{ group }}{%endfor%}")
    context = Context({"staff": group(staff, 7)})
    print(template.render(context))


    # nbr_doctorants = len(doctorants)
    # quotient = nbr_doctorants // 4
    # reste = nbr_doctorants % 4
    # print(quotient, reste)
    # print(type(doctorants))