import sqlite3
import tweepy
import json
import demoji

"""
class TweetsListener(tweepy.StreamListener):

    def on_connect(self):
        print("Estoy conectado!")

    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            conn = sqlite3.connect('datosclean.csv')
            c = conn.cursor()
            text = demoji.replace(status.text, "")
            rts = status.retweeted_status.retweet_count
            favs = status.retweeted_status.favorite_count
            replys = status.retweeted_status.reply_count
            quotes = status.retweeted_status.quote_count
            print("Tweet: ", text)
            print("RTs: ", rts)
            print("FAVs: ", favs)
            print("Replys: ", replys)
            print("Quotes: ", quotes)

            c.execute("INSERT INTO ETH VALUES (:text, :rts, :favs, :replys, :quotes)",
                      {'text': text, 'rts': rts, 'favs': favs, 'replys': replys, 'quotes': quotes})

            conn.commit()

            conn.close()
        elif hasattr(status, 'quoted_status'):
            conn = sqlite3.connect('datosclean.csv')

            c = conn.cursor()
            text = demoji.replace(status.text, "")
            rts = status.quoted_status.retweet_count
            favs = status.quoted_status.favorite_count
            replys = status.quoted_status.reply_count
            quotes = status.quoted_status.quote_count
            print("Tweet: ", text)
            print("RTs: ", rts)
            print("FAVs: ", favs)
            print("Replys: ", replys)
            print("Quotes: ", quotes)

            c.execute("INSERT INTO ETH VALUES (:text, :rts, :favs, :replys, :quotes)",
                      {'text': text, 'rts': rts, 'favs': favs, 'replys': replys, 'quotes': quotes})

            conn.commit()

            conn.close()

    def on_error(self, status_code):
        print("Error", status_code)

consumer_key = "Snk14eAh0czMNo8O3nmoXQOTP"
consumer_secret = "bUukIpA0uJXahnrSjlwB1toiVBIsSzk2jiZsbfpo0PPrmaDaML"
access_token = "1030741939363164161-TkUJLpdNb8QOLiSFgwBBlyLSKe9aUO"
access_token_secret = "djuo5cQ2m0VVGs8FJTZf2TWPbul6yJmSraB3yEDiVZOxH"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
streamingApi.filter(
    track=["Ethereum", "ETH"],
    #locations=[-9.5057561994,35.6739929002,4.97862041,43.8048232407] #España
)

"""

#c.execute("""CREATE TABLE ETH (
#              text text,
#              rts integer,
#              favs integer,
#              replys integer,
#              quotes integer
#        )""")



conn = sqlite3.connect('datosclean.csv')

c = conn.cursor()

c.execute("SELECT * FROM ETH WHERE rts=379")

print(c.fetchall())

conn.commit()

conn.close()
