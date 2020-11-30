from flask import Flask, request
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as pos
import json

app = Flask(__name__)


########## GET ##########

# FUNCIONA!!
# Creamos el primer enpoint que va a ser el README para quien abra mi API --> documento explicativo para en donde se va a informar de los enpoints que tiene la API y que puedes sacar con cada uno de esos endpoint
@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string

#FUNCIONA!!!
# Primer endpoint de la API --> Retweets
@app.route("/tweetspopulares/<numero>")
def mayoresretweets(numero):
    print(f"el nmero es {numero}")
    print("getting tweets")
    tweets = get.mayoresretweets(int(numero))
    return json.dumps(tweets)


# FUNCIONA!!!
# Segundo enpoint de la API --> Favoritos
@app.route("/favoritos/<numero>")
def tweetsfavoritos(numero):
    tweets_fav = get.mayores_favoritos(int(numero))
    return json.dumps(tweets_fav)

#FUNCIONA!!!!
# Tercer endpoint de la api --> tweet por año de publicacion
@app.route("/yeartweets/<rango>")
def year_tweets(rango):
    year0 = rango.split(" ")[0]
    year1= rango.split(" ")[1]
    
    year_tweets = get.year_tweets(year0, year1)
    return json.dumps(year_tweets)  


# LLORO QUE FUNCIONAA!!!!!!
#Cuarto enpoint --> Medimos la polaridad de nuestros tweets
@app.route("/polaridad/<year>")

def polaridad_media(year):
    mean_anual_polaridad = get.polaridad_media2(year)
    return json.dumps(mean_anual_polaridad)








########## POST ##########

@app.route("/newtweet/", methods=["POST"])
def insertnuevotweet():
    tweet = request.form.get('content')
    retweet = request.form.get('retweets')
    favoritos = request.form.get('favorites')
    año = request.form.get('year')
    
    pos.insertnuevotweet(tweet, retweet, favoritos, año)
    return "Mensaje introducido correctamente en la base de datos"












































app.run(debug=True)

"""
Ponemos el debug en True cuando ESTEMOS desarrollando la API, cuando la vayamos a dubir a la nube 
(hacerla publica/deploy) lo cambiamos a False

"""