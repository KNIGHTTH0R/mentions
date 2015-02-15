import karma


# total_count,like_count,comment_count,share_count,click_count


URL = 'http://mashable.com'


print "total count: " + str(karma.facebook_total_count(URL))
print "like count: " + str(karma.facebook_like_count(URL))
print "comment count: " + str(karma.facebook_comment_count(URL))
print "share count: " + str(karma.facebook_share_count(URL))
print "tweets: " + str(karma.tweets(URL))
print "1+: " + str(karma.google_plus_one(URL))
print "linkedin: " + str(karma.linkedin_mentions(URL))
print "pinterest: " + str(karma.pinterest_shares(URL))
print "stumbleupon: " + str(karma.stumbleupon_views(URL))
# print "delicious: " + str(karma.delicious_count(URL))
print "reddit: " + str(karma.reddit_mentions(URL))
