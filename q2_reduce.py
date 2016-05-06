#!/usr/bin/env python

import sys
import string
w={'0':'Mon','1':'Tues','2':'Wednes','3':'Thurs','4':'Fri','5':'Satur','6':'Sun'}
tweets_in_day = 7 * [0]

for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  s = val.split(':')
  tweets_in_day[int(key)] += int(s[1])

for i in range(7):
  if tweets_in_day[i] != 0:
    print '%s\tCount is %s Average is %s' % (w[str(i)][:3],tweets_in_day[i], (float)(tweets_in_day[i]) /52  )
  else:
    print '%s\tCount is %s' % (w[str(i)][:3],tweets_in_day[i])

val = str(tweets_in_day.index(max(tweets_in_day)))
val= w[val]
print 'The maximum  tweets by PrezOno are on %sday ' % (val)

