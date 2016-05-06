#!/usr/bin/env python
import sys
import json

tweets_in_hour=24*[0]

for line in sys.stdin:
    line_object = json.loads(line)
    name=line_object['user']['screen_name']
    if name=='PrezOno':
        date=line_object['created_at'].split()
        time=date[3]
        hour=int(time.split(':')[0])
        tweets_in_hour[hour]+=1

for i in range(len(tweets_in_hour)):
        print '%s\tcount:%s' % (i, tweets_in_hour[i])


