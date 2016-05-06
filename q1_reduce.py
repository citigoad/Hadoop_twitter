#!/usr/bin/env python
import sys
import string

tweets_in_hour = 24 * [0]
for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  s = val.split(':')
  tweets_in_hour[int(key)] += int(s[1])

for i in range(24):
  if tweets_in_hour[i] != 0:
    print '%s\ttweet_Count is %s\t Average is %s' % (i,tweets_in_hour[i], (float)(tweets_in_hour[i]) / 365 )
  else:
    print '%s\ttweet_Count is %s' % (i,tweets_in_hour[i])

val = tweets_in_hour.index(max(tweets_in_hour))
print 'The maximum tweets by PrezOno are during the hour %s to %s' % (val,val+1)

