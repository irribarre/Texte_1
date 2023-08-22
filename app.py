#####################################################################
#   PROJET 5 - Catégorisez automatiquement des questions            #
#-------------------------------------------------------------------#
#   POINT D'ENTREE D'UNE API POUR LE TEST.                          #
#####################################################################

# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
import json
import requests

#import nbimporter     # Pour importer d'autre jupyter notebooks

# Import common functions
# >>>>>>> fonctions de préparation
from data_preparation import preparation_NLTK
from data_preparation import preparation_USE
# >>>>>>> fonctions de prédiction
from data_prediction import prediction_NLTK
from data_prediction import prediction_USE

app = Flask(__name__)

#API_URL = 'https://kind-dune-0b12b7203.3.azurestaticapps.net/'  # Azure
#API_URL = 'https://app-texte-1-3ed8a3f34c3b.herokuapp.com/'
    
question = 'peux-tu me prédire le tag de cette phrase : vvvv vvvvv ggffgfggf gfgfgfgfgfg ytnfvmf kfkfkfk ooooooo ooooogogogogg'


@app.route("/")
def hello():
    return "Bonjour, merci de taper NLTK ou USE"



###############################################
#                  NLTK                       #
###############################################    
@app.route('/NLTK/')
def nltk():
    # Préparation données
    question_NLTK = preparation_NLTK(question_in = question)
    
    # Prédiction tag  
    pred_NLTK = prediction_NLTK(question_in = question_NLTK)
   
    # Affichage résultat 
    return jsonify({'status'   : 'ok',
                    'message'  : pred_NLTK
                   })    

    

###############################################
#                  USE                        #
###############################################    
@app.route('/USE')
def use():
    # Préparation données
    question_USE = preparation_USE(question_in = question)
    
    # Prédiction tag  
    pred_USE = prediction_USE(question_in = question_USE)
   
    # Affichage résultat 
    return jsonify({'status'   : 'ok',
                    'message'  : pred_USE
                   })    



if __name__ == "__main__":
    app.run(debug=True)    
