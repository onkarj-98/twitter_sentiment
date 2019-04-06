from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import tweepy
import csv


access_token = "2922469548-z4Gojre31l0nYNri89z49XD0XMx6IZ6PNZ4ZQGV"
access_token_secret = "3gpDtba3YkGKXJdlP3exmtHm3S3DCaY9kt7A22CAw2Fwf"
consumer_key = "5Kq7fg615uFk9ugTMLK92Uo9F"
consumer_key_secret = "S5bh8bXfmDUMmbRWTqEhNk9DXAhF7Ot7yBwwVaCfVwT6SJElRQ"

class stdOutListener(StreamListener):
	def on_data(self,data):
		print(data)
		return True
	
		
		
	def on_error(self,status):
		print(status)




if __name__ == '__main__':
	l = stdOutListener()
	auth = OAuthHandler(consumer_key,consumer_key_secret)
	auth.set_access_token(access_token,access_token_secret)
	stream = Stream(auth,l)
	stream.filter(track=['#MIvsSRH'])
#	api = tweepy.API(auth,wait_on_rate_limit=True)
  
