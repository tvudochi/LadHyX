#!/bin/bash
#bases Publi
echo "Sync Base Publis"
rsync -ave ssh django@quasi:/srv/www/Django-publications/Data/* /home/toai/Developpement/LadHyX/LadhyX/publications/Data
#Seminaires pdf postesA
echo "Sync Séminaires pdf"
rsync -ave ssh django@quasi:/home/django/LadHyX/LadHyX/LadHyX/media/evenement/* /home/toai/Developpement/LadHyX/LadhyX/LadHyX/media/evenement
#base Mysql via Dump
echo "Sync Base Mysql"
ssh root@quasi "/usr/bin/mysqldump -u root -p'Sl,quLH20' LadHyXWeb > /tmp/LadHyXWeb.sql"
rsync -ave ssh root@quasi:/tmp/LadHyXWeb.sql /tmp
mysql -u root -p'Sl,quLH20' LadHyXWeb < /tmp/LadHyXWeb.sql
