import time
import tweepy
from tweepy.api import API
# Perform OS Actons

# Set the Keys and tokens to the environemntal variable
API_KEY = "c6trv1ovCx37seB8LnKab3l87"
SECRET_KEY = "8oBtQBPuamgoMK62ImWVR64LPE8D0K6gWcRwHocZJrKPpZsRlW"
ACCESS_TOKEN = "1281228204523454464-ayOCJc3p2vIKWDwhDUeFRVm1jYxpXB"
ACCESS_TOKEN_SECRET = "hDzOFI3ObN7gCcqVriB6TRe3dyno7S0Q60PCBmB20mjw9"

# Connect to the tweepy Auth
auth = tweepy.OAuthHandler(API_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
search_words = "$Dwac"
date_since = "2021-11-16"
# Create a listener object
search_words = "$Dwac"
date_since = "2021-11-16"

go = tweepy.Client(auth, wait_on_rate_limit=True)
tweets = go.search_all_tweets(query=search_words, max_results=1, until_id=1461456950231801861)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
    try:
       
        message = " hey, Did you see this $LMACA rumor? Could be a similar play https://twitter.com/Spacul8r/status/1455624133908238343?s=20"
        #api.update_status(status=message, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    except:
        print("Already Commented")
