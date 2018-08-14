import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import operator
import random
from time import sleep


ACCESS_TOKEN = '997031551-Vb9kPenCDJjXZNxrGwcQoP2p2PpDKwiFWwTXcXyj'
ACCESS_SECRET = 'Agjo3m0QhzGve4pwDIlSVExFuwN6eVT3cuvkHS2qHzoYE'
CONSUMER_KEY = 'SL0CgC416q05wuXJX5eDFWY14'
CONSUMER_SECRET = 'THEJFqCNw9yMewj8kaROcUzOkjhFYxQ3xndgZRKqi06AXSXBsW'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.sample()

tweets = []
tweet_count = 100
s= 100
counter=0

for newtweet in iterator:
    
    counter+=1
   
    if(tweet_count>0):
        tweets.append(newtweet)
 
    tweet_count -= 1

    if tweet_count <= -1:
        
        print ("\n\nThe number of twitter from beginning: "+ str(counter) )

        tweet_count=0

        dtweet = {}
        tweetlength=0

        for tweet in tweets:
            
            try:
                if 'text' in tweet: 
                    
                    tweet_msg = tweet['text']
                    tweetlength += len(tweet_msg)    
                    hashtags = []
                    
                    for hashtag in tweet['entities']['hashtags']:
                        hashtags.append(hashtag['text'])
                        if hashtag['text'] not in dtweet :
                            dtweet[hashtag['text']] = 1
                        else:
                            dtweet[hashtag['text']] += 1
                
            except:
                continue
         
        tweetlist = sorted(dtweet.items(),key=operator.itemgetter(1),reverse=True)
        # print tweetlist

        print "Top 5 hot hashtags: "
        maxlen = len(tweetlist)
        if maxlen >= 5:
            maxlen = 5
         
        for x in range(0,maxlen):
            t = tweetlist[x]
            print ((t[0]) + " " + str(t[1]))

        print ("The average length of the twitter is: " + str(tweetlength/100.0))

        del dtweet

        r = random.randint(1,counter)
        
        if ( r <= s ):
            random.shuffle(tweets)
            y = tweets.pop()
            tweets.append(newtweet)

        # time gap to get next entries
        sleep(2)
