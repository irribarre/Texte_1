#####################################################################
#   PROJET 5 - Catégorisez automatiquement des questions            #
#-------------------------------------------------------------------#
#   POINT D'ENTREE D'UNE API POUR LE TEST.                          #
#####################################################################

# -*- coding: utf-8 -*-
# Maj Procfile : 
#  --> https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524
#  --> https://devcenter.heroku.com/articles/python-gunicorn

from flask import Flask, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json


# Import common functions
from app_preparation import preparation # fonctions de préparation
from app_prediction import prediction # fonctions de prédiction


app = Flask(__name__)
json = FlaskJSON(app)


json.init_app(app)


###############################################
#                  Accueil                    #
###############################################    
@app.route("/")
def accueil():

    texte = "Bonjour,<br/><br/>La prédiction du tag se trouve sur le endPoint de la méthode utilisée (NLTK / USE).<br/><br/><br/>Merci de vous rendre sur le endPoint choisi pour saisir votre question :<br/><br/>1) Méthode NLTK -------> endPoint <b>/nltk</b>.<br/>2) Méthode USE  ---------> endPoint <b>/use</b>."    
    return texte



# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr
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


# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr
# GET requests will be blocked
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)



###############################################
#                  NLTK                       #
###############################################    
#@app.route('/nltk', methods=['POST'])
#def endpoint_nltk():
#    
#    print('endpoint_nltk')
#    
#    # Question (clé = 'question', valeur = reçue par l'utilisateur via une requête postman)
#    # https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr    
##    question = request.params   
#    question = request.args['question']
#    print('endpoint_nltk, question =', question)
#    
#    # Préparation données
#    question_nltk = preparation.preparation_nltk(question_in = question)
#    print('endpoint_nltk, question_nltk =', question_nltk)
#    
#    # Prédiction tag  
#    pred_nltk = prediction.prediction_nltk(question_in = question_nltk)
#    print('endpoint_nltk, pred_nltk =', pred_nltk)
#    
#    # Affichage résultat 
#    return jsonify({'status'   : 'ok',
#                    'message'  : pred_nltk
#                   })    

# https://flask-json.readthedocs.io/en/latest/#examples
@app.route('/nltk', methods=['POST'])
def endpoint_nltk():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    print('increment_value, data =', data)
       
    try:
        value = int(data['value'])
        print('increment_value, value =', value)        
           
        # Préparation données
        question_nltk = preparation.preparation_nltk(question_in = value)
        print('endpoint_nltk, question_nltk =', question_nltk)
    
        # Prédiction tag  
        pred_nltk = prediction.prediction_nltk(question_in = question_nltk)
        print('endpoint_nltk, pred_nltk =', pred_nltk)
    
       
    except (KeyError, TypeError, ValueError):
        raise JsonError(description = 'Invalid value.')
    return json_response(value = value + 1)



if __name__ == "__main__":
    app.run(debug=True)    
