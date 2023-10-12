import json
from tweepy import OAuthHandler, Stream, StreamListener 
from datetime import datetime

# Cadastrar as chaves de acesso
consumer_key = "bBH2JAfbBG68EoL8CYn5kt16l"
consumer_secret = "456zxph8gpUQfuY3wWSF3PqPoGZVlBHE3P2hXwEHX35i2PaVO4"

access_token = "1659282121138094080-Er1fuirPoI6OTz8Ec3nKWReMiIF6Li" 
access_secret = "NLFaONFZvdCqjMrp4OYtMtVlrC9wmYlJ7BHS0CpJBuIPO"

# Um arquivo de saída para armazenar os tweets coletados
out = open("collected_tweets.text", "w")

# Implementar uma classe para conexão com o Twitter
class MyListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True
    
    def on_error(self, status):
        print(status)
                 