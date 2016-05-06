#!/usr/bin/env python
import sys
import json


tweets_in_day=7*[0]
w={'Mon':0,'Tue':1,'Wed':2,"Thu":3,'Fri':4,'Sat':5,'Sun':6}

for line in sys.stdin:
    line_object = json.loads(line)
    name=line_object['user']['screen_name']
    if name=='PrezOno':
        date=line_object['created_at'].split()
        day=str(date[0])
        tweets_in_day[w[day]]+=1

for i in range(len(tweets_in_day)):
        print '%s\tcount:%s' % (i, tweets_in_day[i])

