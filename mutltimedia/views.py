# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render
import vimeo


def group(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


def requestvimeo(request, channel=None, name=None):
    if request.method == 'GET':
        v = vimeo.VimeoClient(settings.TOKEN, settings.KEY, settings.SECRET)
        channel = v.get('/channels/'+channel+'/videos')
        mydict = channel.json()
        # liste des videos dans la chaine
        maliste = []
        mydata_list = mydict['data']
        for i in mydata_list:
            print(i['uri'])
            myuri = i['uri'].replace('videos', 'video')
            video = [myuri, i['name']]
            if (video[0] == '/video/162966396') | (video[0] == '/video/162972218') | (video[0] == '/video/166008992'):
                maliste.insert(0, video)
            else:
                maliste.append(video)
        return render(request, 'video.html',
                      {
                          'name': name,
                          "grouppar3": group(maliste, 3),
                      }
                      )

# Physique du sport : 162966396, 162972218, 166008992
# maliste : [['/video/162952313', 'Stabilité de vol'], ..]



