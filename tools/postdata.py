
from config.configuration import db,collection

def insertnuevotweet(tweet, retweet, favoritos, año):
    """
    #funcion que inserta los datos en mongo es el momento de revisar
    #que todos los datos esten como queramos. 
    """

    dict_insert = {"content" : f"{tweet}",
    "retweets" : f"{retweet}",
    "favorites" : f"{favoritos}",
    "year" : f"{año}"
    }

    collection.insert_one(dict_insert)
