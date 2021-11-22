import time
import tweepy
# Perform OS Actons
import os as _os
# Import the environmental vaiables
import dotenv as _dotenv
# load the environmental variables
_dotenv.load_dotenv()

# Set the Keys and tokens to the environemntal variable
API_KEY = _os.environ["TWITTER_API_KEY"]
SECRET_KEY = _os.environ["TWITTER_API_SECRET_KEY"]
ACCESS_TOKEN = _os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = _os.environ["ACCESS_TOKEN_SECRET"]

# Connect to the tweepy Auth
auth = tweepy.OAuthHandler(API_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create a listener object


class MyStreamListener(tweepy.Stream):
    def on_status(self, status):
        call = status.text
        call = call.lower()
        print(status.text)
        if ("$dwac" in call and status.favorited == False):
            
            message =" hey, Did you see this $LMACA rumor? Could be a similar play https://twitter.com/Spacul8r/status/1455624133908238343?s=20"
            print(message)
            #api.update_status(status=message,in_reply_to_status_id = status.id, auto_populate_reply_metadata=True)
            api.create_favorite(status.id)
            self.disconnect()
            
    def disconnect(self):
        return super().disconnect()
        print("disconnected")
    def on_connect(self):
        print("Connected")

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.

# Create API object
def main():
    while True:
        print("connecting")
        global api
        api = tweepy.API(auth)
        myStreamListener = MyStreamListener(API_KEY, SECRET_KEY,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        myStreamListener.filter(track=['$Dwac'])
        print("done")
        
    
if __name__ == '__main__':
    main()
    """
    I am Planning to use the twitter API to target and check the use of a particular keyword on twitter, replying the tweet with a comment that is quoting another tweet relaying to the profile user more and further description about the keyword target
    
    
    The app will only be able to like, and tweet an already defined post under the tweet that the keyword was used in
    
    
    
    
    """
    

