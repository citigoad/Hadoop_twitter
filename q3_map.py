#!/usr/bin/env python

import sys
import string
import json

po_length_sum = 0
po_tweet_count = 0
all_others_length_sum = 0
all_others_tweet_count = 0

for line in sys.stdin:
        tweet = json.loads(line)
        try:
                user = tweet['user']
                screenname = user['screen_name']
                tweet_length = len(tweet['text'])

                if screenname == 'PrezOno':
                    po_length_sum += tweet_length
                    po_tweet_count += 1
                else:
                    all_others_length_sum += tweet_length
                    all_others_tweet_count += 1
        except:
                continue

print 'PrezOno\t%s\t%s' % (po_length_sum, po_tweet_count)
print 'Other\t%s\t%s' % (all_others_length_sum, all_others_tweet_count)
