# TwitterStreamingAnalysis--DataMining

You will use Twitter API of streaming to implement the fixed size sampling
method (Reservoir Sampling Algorithm) and use the sampling to track the popular tags on tweets and calculate the average length of tweets.

# Detail
In this task, we assume that the memory can only save 100 Twitter in memory,
so we need to use the fixed size sampling method to only sampling part of the
Twitter in the streaming.

You need to have a list(Reservoir) has the capacity limit of 100, which can only save 100 twitters.
When the streaming of the Twitter coming, for the first 100 Twitter, we can directly save them in the list. After that, for the nth twitter, with probability 100/n , keep the nth Twitter, else discard it.
If you will keep the nth Twitter, it will replace one of the Twitter in list, you need to randomly pick one to be replaced.

After fully save the list, each time when you choose to keep an new Twitter and
replace one in the list, you need to statistic the hottest 5 tags and the average
length of the Twitter in the list. And print them out. The API tweepy can extract the tags and content of twitter.
