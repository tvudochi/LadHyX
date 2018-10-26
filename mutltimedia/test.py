#!/home/toai/Developpement/LadHyX/bin/python

import vimeo
import pprint

token = "12691339049ae2a9fa802cfc48a44d3e"
key = "4154291421c99e630e0bc3c3a1ba7d1102e76269"
secret = "tddAX7IrrZ2tOSWmZdcxfbKdH0+YjtBvPuzjZYUP6C6+t9KLyCha7dzH9YnavjWtmPb2/o73FsuHtuDSiWtDaLHJ2D5odEiWrmr8yNbhcOB1iQY4K0/w9rV4X8q8SrKZ"

v = vimeo.VimeoClient(token, key, secret)

#allchannels = v.get('/channels/aeroelasticite/videos')
allchannels = v.get('/channels/1271458/videos')
#
# assert about_me.status_code == 200
mydict = allchannels.json()
mydata_list = mydict['data']
nb_videos = len(mydata_list)
pprint.pprint(mydata_list,indent=1)
maliste = []
for i in mydata_list:
    myuri = i['uri'].replace('videos', 'video')
    # print(myuri, i['name'])
    maliste.append([myuri, i['name']])

print(maliste)
