#####################################################################
#   PROJET 5 - Catégorisez automatiquement des questions            #
#-------------------------------------------------------------------#
#   POINT D'ENTREE D'UNE API POUR LE TEST.                          #
#####################################################################

# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, jsonify


#import nbimporter     # Pour importer d'autre jupyter notebooks

# Import common functions
from app_preparation import preparation # fonctions de préparation
from app_prediction import prediction # fonctions de prédiction


app = Flask(__name__)


#API_URL = 'https://app-texte-1-3ed8a3f34c3b.herokuapp.com/'

# https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python
question_python_1 = "Best online resource to learn Python? <br/> I am new to any scripting language. But, Still I worked on scripting a bit like tailoring other scripts to work for my purpose. For me, What is the best online resource to learn Python? <br/> Some Online Resources: <br/> http://docs.python.org/tut/tut.html - Beginners <br/> http://diveintopython3.ep.io/ - Intermediate <br/> http://www.pythonchallenge.com/ - Expert Skills <br/>http://docs.python.org/ - collection of all knowledge<br/>Some more: A Byte of Python. <br/>Python 2.5 Quick Reference<br/>Python Side bar<br/>A Nice blog for beginners<br/>Think Python: An Introduction to Software Design"    


###############################################
#                  Accueil                    #
###############################################    
@app.route("/")
def accueil():

    texte = "Bonjour,<br/><br/>La prédiction du tag se trouve sur le endPoint de la méthode utilisée (NLTK / USE).<br/><br/><br/>Merci de vous rendre sur le endPoint choisi pour saisir votre question :<br/><br/>1) Méthode NLTK -------> endPoint <b>/nltk</b>.<br/>2) Méthode USE  ---------> endPoint <b>/use</b>."
    return texte



###############################################
#                  Question                   #
###############################################    
# handle a POST request
#@app.route('/question', methods=['POST'])
#def endpoint_question():
#
##    data = question_python_1
#    data = request.form
#
#    # handle the POST request
#    language = request.form.get('question')
#    framework = request.form.get('framework')
#    return '''<h1>The language value is: {}</h1>
#              <h1>The framework value is: {}</h1>'''.format(language, framework)
##               <h1>The language value is: {}</h1>'''.format(question)
#    
#    # Traiter la requête
#    return data
#
# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr
# allow both GET and POST requests
#@app.route('/form-example', methods=['GET', 'POST'])
#def form_example():
#    # handle the POST request
#    if request.method == 'POST':
#        question = request.form.get('question')
#        algorithme = request.form.get('algorithme (NLTK / USE)')
#        
#        
#        # Préparation données
#        question_nltk = preparation.preparation_nltk(question_in = question)
#    
#        # Prédiction tag  
#        pred_nltk = prediction.prediction_nltk(question_in = question_nltk)
#    
##        return '''
##                  <h1>La question est : {}</h1>
##                  <h1>L'algorithme est : {}</h1>'''.format(question, pred_nltk)
#        # Affichage résultat 
#        return jsonify({'status'   : 'ok',
#                        'message'  : pred_nltk
#                       })    
#    
#    
#    # otherwise handle the GET request
#    return '''
#           <form method="POST">
#               <div><label>Question: <input type="text" name="question"></label></div>
#               <div><label>Algorithme: <input type="text" name="algorithme"></label></div>
#               <input type="submit" value="Submit">
#           </form>'''


@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)



###############################################
#                  NLTK                       #
###############################################    
@app.route('/nltk', methods=['POST'])
def endpoint_nltk():
    
    # Question (clé = 'question', valeur = reçue par l'utilisateur via une requête postman)
    # https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr    
#    question = request.params   
    question = request.args['question']

    # Préparation données
    question_nltk = preparation.preparation_nltk(question_in = question)
    
    # Prédiction tag  
    pred_nltk = prediction.prediction_nltk(question_in = question_nltk)
   
    # Affichage résultat 
    return jsonify({'status'   : 'ok',
                    'message'  : pred_nltk
                   })    

    

###############################################
#                  USE                        #
###############################################    
@app.route('/use', methods=['POST'])
def endpoint_use():

    # Question (clé = 'question', valeur = reçue par l'utilisateur via une requête postman)
    # https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr    
#    question = request.params   
    question = request.args['question']
    
    # Préparation données
    question_use = preparation.preparation_use(question_in = question)
    
    # Prédiction tag  
    pred_use = prediction.prediction_use(question_in = question_use)
   
    # Affichage résultat 
    return jsonify({'status'   : 'ok',
                    'message'  : pred_use
                   })    


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ exemple (begin)
# https://flask-request-params.readthedocs.io/en/latest/
#from flask import Flask, request, render_template, jsonify
#from flask_request_params import bind_request_params
#
#
#app = Flask(__name__)
#app.secret_key = 'secret'
## bind rails like params to request.params
#app.before_request(bind_request_params)
#
## just return request.params
#@app.route('/echo/<path>', methods=['GET', 'POST'])
#def echo(path):
#    return jsonify(request.params)
#
#@app.route('/user', methods=['POST'])
#def create_user():
#    user = request.params.require('user').permit('name', 'password')
#    # do something
#    return jsonify(user)
#
## serve at localhost:5000
#app.run(debug=True)
#
#--------------------------------------------------------
#
#@app.route('/api/meteo')
#def meteo():
#    response = requests.get(METEO_API_URL)
#    content = json.loads(response.content.decode('utf-8'))
#
#    if response.status_code != 200:
#        return jsonify({
#            'status': 'error',
#            'message': 'La requête à l\'API météo n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
#        }), 500
#
#    data = []
#
#    for prev in content["list"]:
#        datetime = prev['dt'] * 1000 # conversion du timestamp en millisecondes
#        temperature = prev['main']['temp'] - 273.15 # Conversion de Kelvin en °c
#        temperature = round(temperature, 2) # Arrondi
#        data.append([datetime, temperature])
#
#    return jsonify({
#      'status': 'ok', 
#      'data': data
#    })
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ exemple (end)


if __name__ == "__main__":
    app.run(debug=True)    
