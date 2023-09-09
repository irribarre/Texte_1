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
from app_prediction import prediction   # fonctions de prédiction


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




###############################################
#                  NLTK                       #
###############################################    
# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask-fr
# https://flask-json.readthedocs.io/en/latest/#examples
# https://github.com/skozlovf/flask-json/blob/master/examples/example2.py
@app.route('/nltk', methods = ['POST'])
def endpoint_nltk():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force = True)
    print('endpoint_nltk, data =', data)
       
    try:
        question = data['question']
        print('endpoint_nltk, question =', question)        
           
        # Préparation données
        df_question_nltk = preparation.preparation_nltk(question_in = question)
        print('endpoint_nltk, df_question_nltk =\n', df_question_nltk)
    
        # Prédiction tag  
        pred_nltk = prediction.prediction_nltk(df_question_in = df_question_nltk)
        print('endpoint_nltk, pred_nltk =', pred_nltk)
       
    except (KeyError, TypeError, ValueError):
        raise JsonError(description = 'Invalid value.')
    return json_response(value = value + 1)




###############################################
#                  USE                        #
###############################################    
@app.route('/use', methods = ['POST'])
def endpoint_use():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force = True)
    print('endpoint_use, data =', data)
       
    try:
        question = data['question']
        print('endpoint_use, question =', question)        
           
        # Préparation données
        df_question_use = preparation.preparation_use(question_in = question)
        print('endpoint_use, df_question_use =\n', df_question_use)
    
        # Prédiction tag  
        pred_use = prediction.prediction_use(df_question_in = df_question_use)
        print('endpoint_use, pred_use =', pred_use)
       
    except (KeyError, TypeError, ValueError):
        raise JsonError(description = 'Invalid value.')
    return json_response(value = value + 1)




if __name__ == "__main__":
    app.run(debug=True)    
