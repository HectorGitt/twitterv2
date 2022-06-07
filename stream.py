import time
import tweepy
# Perform OS Actons
import os as _os
# Import the environmental vaiables
import dotenv as _dotenv
# load the environmental variables
_dotenv.load_dotenv()

# Set the Keys and tokens to the environemntal variables
API_KEY = _os.environ["TWITTER_API_KEY"]
SECRET_KEY = _os.environ["TWITTER_API_SECRET_KEY"]
ACCESS_TOKEN = _os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = _os.environ["ACCESS_TOKEN_SECRET"]
BEARER = _os.environ["BEARER_TOKEN"]

# Connect to the tweepy Auth
auth = tweepy.OAuthHandler(API_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create a listener object
class MyStreamListener(tweepy.StreamingClient):
    #number of times bot replied since startup
    replied = 0
    #get called when a tweet is recieved
    def on_tweet(self, tweet):
        #recieved the tweet text in a variable
        print(tweet.id)
        call = tweet.text
        print(tweet.text)
        #check if string has initially not being liked 
        if (tweet.favorited == False and tweet.author_id == 3314774051):
            #This string will contain the message to be replied
            message =" hi "
            #send the message in the string as a reply
            api.update_status(status=message,in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)
            #like the tweet
            api.create_favorite(tweet.id)
            #increase the number of replied status by 1
            self.replied += 1
            print(self.replied , " tweets replied")
            print("Waiting for stream")
            
    #get called when the stream is disconnected
    def disconnect(self):
        return super().disconnect()
        print("disconnected")
    #gets called when the string is connected
    def on_connect(self):
        print("Connected")
        print("Waiting for stream")

    #gets called when an error is detected in the stream
    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.
    #gets called when an exception is being handled
    def on_exception(self, exception):
        print(exception)
        return
# Create API object
def main():
    #keeps the stream in a loop to avoid shutting down
    while True:
        print("connecting")
        global api
        #create an api instance with the keys
        api = tweepy.API(auth, wait_on_rate_limit=True)
        
        #create a stream instance with the keys
        myStreamListener = MyStreamListener(BEARER)
        myStreamListener.add_rules(tweepy.StreamRule("tweepy"))
        
        #create a tweet filter for the stream
        myStreamListener.filter()
        
    
#dont run script when imported as a module
if __name__ == '__main__':
    main()
    """
    I am Planning to use the twitter API to target and check the use of a particular keyword on twitter, replying the tweet with a comment that is quoting another tweet relaying to the profile user more and further description about the keyword target
    
    
    The app will only be able to like, and tweet an already defined post under the tweet that the keyword was used in
    
    The elevated access can be applied for by going to the developers dashboard and navigating to the product button at the sidebar, then click on twitter api v2 then youll see elevated access, click on it the apply for the access
    
    
    """
    

