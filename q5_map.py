#!/usr/bin/env python

import sys
import string
import json

total_length_sum = 0
tweet_count = 0

for line in sys.stdin:
        tweet = json.loads(line)

        screenname = tweet['user']['screen_name']
        tweet_length = len(tweet['text'])
        tweet_count = 1
        print '%s\t%s\t%s' % (screenname, tweet_length, tweet_count)

