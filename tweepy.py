import tweepy
auth = tweepy.OAuthHandler("CONSUMER KEY HERE", "CONSUMER KEY SECRET HERE") 
auth.set_access_token("ACCESS TOKEN HERE", "ACCESS TOKEN SECRET HERE") 
api = tweepy.API(auth)
print ("Tweet From Terminal, Made By @iCrazeiOS On Twitter!")
print ("Twitter For........")
tweet = input("What Would You Like To Tweet? ")
api.update_status(status =(tweet))
print ("Done!")