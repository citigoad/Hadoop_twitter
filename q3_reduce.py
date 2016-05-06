#!/usr/bin/env python

import sys
import string


po_length_sum = 0
po_tweet_count = 0
all_others_length_sum = 0
all_others_tweet_count = 0

for line in sys.stdin:
    try:
        (key, length_sum, tweet_count) = line.strip().split('\t')
        if key == 'PrezOno':
            po_length_sum += int(length_sum)
            po_tweet_count += int(tweet_count)
        elif key == 'Other':
            all_others_length_sum += int(length_sum)
            all_others_tweet_count += int(tweet_count)
    except:
        continue

if (po_length_sum or po_tweet_count) == 0:
    print "There are no tweets from prezono"
else:
    prezono_avg_length = float(po_length_sum) / float(po_tweet_count)
    print "PrezOno's Average Tweet Length: %s" % prezono_avg_length

others_avg_length = float(all_others_length_sum) / float(all_others_tweet_count)
print "Others' Average Tweet Length: %s" % others_avg_length
