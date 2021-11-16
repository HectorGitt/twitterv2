
import tweepy


consumer_key = "VHyvPRXLIucBR0lL4qcT6lhBf"
consumer_secret = "FLpvaQB8frXNFxO2UimZg0YAQJ5mpJ1tj68knJz4My3ohjgk0l"
access_token = "3314774051-8iP8wKlP5tljwOMs6QRyhNn7UfFeBCZYAf5Pqy3"
access_token_secret = ""

# Subclass Stream to print IDs of Tweets received
class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)

# Initialize instance of the subclass
printer = IDPrinter(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)

# Filter realtime Tweets by keyword
printer.filter(track=["Twitter"])

