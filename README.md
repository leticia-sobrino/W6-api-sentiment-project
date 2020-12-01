# API tweets realdonaldtrump

### INDICE:
#### 1. PROYECTO
#### 2. ESTRUCTURA DEL PROYECTO
#### 3. DOCUMENTACION DE LA API
#### 4. RECURSOS UTILIZADOS 

![fotodeportada](https://github.com/leticia-sobrino/W6-api-sentiment-project/blob/main/images/donald-trump-twitter.jpg)


#### 1. PROYECTO
El fin de este proyecto es construir una API (application programming interfacecon) con diferentes endpoints que propocionen al cliente, con un llamada directa, una serie de datos.
Esta API ha sido creada a través de una importación de un dataset de kaggle.com sobre tweets de realdonaldtrump.
Este dataset ha sido limpiado y analaizando en python con la herramienta de pandas y, al conseguir la información necesaria ha sido importado a MongoDB Compass para empezar a hacer las funciones necesarias para crear las llamadas a la API.
La API ha sido creada mediante la herramienta de Flask y se han utilizado dos métodos para su desarrollo: el método GET y el método POST.
   - Método GET: mediante este método hemos conseguido realizar cuatro diferentes endpoints para nuestra  API, para que el cliente pueda extraer los datos que corresponden a cada uno de esos enpoints de manera inmediata; solamente con una llamada.
  
    
   - Método POST: mediante este método lo que hemos realizado ha sido importar información nueva a nuestro base de datos en MongoDB Compass de una manera eficaz y rápida; con tan solo una llamada.

Ademas de cumplir la finalidad y los objetivos de este proyecto, también se ha realizado un análisis de polaridad del contenido que hemos utilizado. Con este último análisis hemos podido observar el grado de positividad de los tweets publicados anualmente. 



#### 2. ESTRUCTURA DEL PROYECTO
El proyecto está estructurado de la siguiente manera para su mejor comprensión, mediante una estricta limpieza y organización. 
  * Carpetas:
    - Images: la foto de portada
    - Data: en dónde podrás encontrar el dataset limpio y un archivo .json de nuestro dataset.
    - confing: en esta carpeta encontrás una un archivo llamado configuration creado únicamente para la conexión de python con mi usuario de MongoDB Compass, con la finalidad de poder trabajar con mis datos.
    - tools: en esta carpeta podrás encontrar tres diferentes archivos de herramientas (cuyo nombre de cada archivo de dará una pista sobre lo que contiene). Los archivos son los siguientes:
      - init.py --> Este archivo ha sido creado para la conexión entre las carpeta de config (en donde nos conectábamos con mongo) y la de tools, para evistar posibles errores entre la conexión entre estas dos carpetas.
      - getdata.py --> este archivo contiene funciones para extraer la información que queremos que nuestro enpoint devuelva al ser llamdo por un cliente futuro.
      - postdata.py --> archivo en donde se encuentra la función necesaria para importar nuevos datos en el database de Mongo.
    - notebooks: en esta carpeta se proporcionan 3 notebooks explicativos y sencillos en dónde se encuentra de una manera más visual, paso a paso, el desarrollo del proyecto.
      - 1.Tweets dataset: este notebook encontrarás la importación del dataset de kaggle, la limpieza y el análisis mediante pandas, la importación del dataset final a Mongo y la conexión de python con Mongo para poder realizar las 4 diferentes querys necesarias para crear nuestros endpoints.
      - 2.Análisis de polaridad: en este notebook preparamos como va a ser la función que tendremos que tilizar en el archivo getdata.py para poder conseguir la media de positivismo anual de nuestros tweets.
      - 3. Llamadas a la API. Este notebook es el noebook final del proyecto en dónde se muestra mediante llamadas con los cuatro diferentes enpoints creados que la API funciona correctamente. 
  
  - Archivos:
    - main.py: Este es el archivo principal de todo el poyecto en dónde podrás ver todas las funciones importadas de las demás carpetas para que todo nuestro trabajo cobre vida. Este archivo es el que se ejecuta finalmente para que nuestra API funcione correctamente. 
  

#### 3. DOCUMENTACION DE LA API
La API consta de dos métodos el método POST y el método GET. Usted como cliente solo deberá de tener encuenta el método GET ya que ahí encontrará la explicaciión de lo que devuelve cada enpoint y cómo utilizarlo.

+ Método GET
  Mediante este método podrá llamar a la url padre: "http://127.0.0.1:5000 " añadiédole el endpoint que le parezca útil para conseguir su información. 
  + Enpoints:
    + "/"  --> si añade este endpoint a la url padre podrá acceder a este README y portanto a esta documentación de la API para su fácil utilización.
    + "/tweetspopulares/<numero>" --> Este endpoint lo que nos proporcionará será la información de los tweets que tengan más de x retweets. El número de retweets es de libre elección es decir, lo elige TÚ. ¡OJO! este número lo deberás de meter en tipo string para que no te de ningún problema. Por lo tanto la llamada final será: request.get (url padre) + (enpoint con tu numero en string) y para que te devuelva la información no te olvides de añadirle el .json().
    + "/favoritos/<numero>" --> Este endpoint lo que nos proporcionará será la información de los tweets que tengan más de x favoritos. El número de favoritos es de libre elección es decir, lo elige TÚ. ¡OJO! este número lo deberás de meter en tipo string para que no te de ningún problema. Por lo tanto la llamada final será: request.get (url padre) + (enpoint con tu numero en string) y para que te devuelva la información no te olvides de añadirle el .json().
    + "/yeartweets/<rango>" --> Este endpoint lo que nos proporcionará será los tweets publicados en el año o años  que tu quieras. El año/años que tu quierás es de libre elección, es decir los deberás de elegir TÚ. ¡OJO! los años  los deberás de meter en tipo string con un ESPACIO entre ellos para que no te de ningún problema. Por lo tanto la llamada final será: request.get (url padre) + (enpoint con tus años en tipo string y con un ESPACIO entre medias) y para que te devuelva la información no te olvides de añadirle el .json().
    + "/polaridad/<year>" --> Este último endpoint te proporcionará la media anual del grado de positividad de los tweets, es decir un análisis de polaridad de los tweets de cada año. El año lo deberás de elegir TÚ. ¡OJO! El año lo debrás de meter en tipo string para que la llamada no te de ningún tipo de error. Por lo tanto la llamada final será: request.get (url padre) + (enpoint con tu año en tipo string) y para que te devuelva la información no te olvides de añadirle el .json(). 
    Este último endpoint me parece muy curioso ya que podrás ver como cambia la positividad de los tweets durante durante la política de Donald Trump. 

#### 4. RECURSOS UTILIZADOS 
Los links, materiales, páginas y documentación utilizada para el desarrollo del proyecto has sido los siguientes:
+ Markdown y Readme
    1. https://python-markdown.github.io/extensions/fenced_code_blocks/
    2. https://code.visualstudio.com/docs/languages/markdown

    Conclusion: En HTML hay que poner fenced_code entre corchetes para que funcione
    --> markdown.markdown(some_text, extensions=['fenced_code'])
+ Mongo
  1. https://docs.mongodb.com/manual/reference/operator/aggregation/convert/#convert-to-int
  2. https://docs.mongodb.com/manual/reference/method/db.collection.insert/
+ Flask
  1. https://flask.palletsprojects.com/en/1.1.x/
+ Dataset
  1. https://www.kaggle.com/austinreese/trump-tweets
+ Apuntes
  1. https://github.com/leticia-sobrino/teaching-ironhack-data-madrid-2020
  2. https://github.com/leticia-sobrino/datamad1020-rev 

