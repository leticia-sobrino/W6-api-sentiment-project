
from config.configuration import db, collection
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# QUE ES LO QUE QUIERO QUE ME DEVUELVA MI PRIMER ENDPOINT --> VER LOS TWEETS QUE TENGAN X RETWEETS
def mayoresretweets(numero):
    """
    # Hacemos una query a la base de datos para sacar los tweets que tenga mas de 150.000 retweets

    """
    query_one = {'retweets': {"$gt": numero}}
    print(query_one)
    tweets = list(collection.find(query_one,{"content": 1, "retweets": 1, "_id" : 0}))          #.sort("date", -1))
    return tweets


# QUE ES LO QUE QUIERO QUE ME DEVUELVA MI SEGUNDO ENDPOINT --> VER LOS TWEETS QUE TENGAN X FAVORITOS
def mayores_favoritos(numero):

    query_two = {'favorites':{"$gt": numero}}
    tweets_fav = list(collection.find(query_two, {"content": 1, "favorites": 1, "_id" : 0}))
    return tweets_fav


# QUE ES LO QUE QUIERO QUE ME DEVUELVA MI TERCER ENDPOINT --> VER LOS TWEETS PUBLICADOS EN X AÑO/AÑOS
def year_tweets(year0, year1):
    query_third = {"$and":[{'year': {"$gt": year0}}, {'year': {"$lt": year1}}]}
    year_tweets = list(collection.find(query_third, {"content": 1, "year":1, "_id": 0}))
    return year_tweets


# QUE ES LO QUE QUIERO QUE ME DEVUELVA MI CUATRO ENDPOINT
def polaridad_media2(year):
    query_fourth = {'year': year}
    year = list(collection.find(query_fourth, {"content": 1, "_id" : 0}))
    
    
    sia = SentimentIntensityAnalyzer()

    
    pos = []
    for i in year:
        polarity = sia.polarity_scores(i['content'])
        pos.append(polarity['pos'])
    

    mean_anual_polaridad = sum(pos)/len(pos)
    print(mean_anual_polaridad)
    return mean_anual_polaridad








