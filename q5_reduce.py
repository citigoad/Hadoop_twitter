#!/usr/bin/env python

import sys
import string
import operator

count = 0
length = 0
old_word = None
avg_length = 0
avg={}
cnt={}

for line in sys.stdin:
  (key, tweet_length, tweet_count) = line.strip().split('\t')
  if old_word != key:
    if old_word:
      #print '%s\t%s\t%s\t%s' % (old_word,length,count,avg_length)
      avg[old_word]=avg_length
      cnt[old_word]=count
      count = 0
      length = 0
      avg_length = 0
  old_word = key

  count = count + int(tweet_count)
  length = length + int(tweet_length)
  avg_length = float(length)/float(count)

#print '%s\t%s\t%s\t%s' % (old_word,length,count,avg_length)
avg[old_word]=avg_length
cnt[old_word]=count

x=sorted(avg.items(),key=operator.itemgetter(1))
y=sorted(cnt.items(),key=operator.itemgetter(1))
print 'The user with most number of tweets is %s with %s tweets' %(y[-1][0],y[-1][1])
print '\nThe top 5 users with longest avg_tweet_length and their corresponding averages are'
x.reverse()
print x[:5]
print '\nThe bottom 5 users with longest avg_tweet_length and their corresponding averages are'
print x[-5:]
~

