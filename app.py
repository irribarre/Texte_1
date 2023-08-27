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
    


###############################################
#                  Accueil                    #
###############################################    
@app.route("/")
def accueil():

    texte = "Bonjour,<br/><br/>1) Merci de saisir votre question sur le endPoint <b>/question</b>.<br/><br/>2) La prédiction du tag se trouve sur le endPoint de la méthode utilisée :<br/>>>>>>>> endPoint <b>/nltk</b> pour NLTK.<br/>>>>>>>> endPoint <b>/use</b> pour USE."
    return texte



###############################################
#                  Question                   #
###############################################    
# handle a POST request
@app.route('/question', methods=["POST"])
def endpoint_question():

    data = request.form

    # Traiter la requête
    return data



###############################################
#                  NLTK                       #
###############################################    
@app.route('/nltk')
def endpoint_nltk():

    # Préparation données
    question_nltk = preparation.preparation_nltk(question_in = data)
    
    # Prédiction tag  
    pred_nltk = prediction.prediction_nltk(question_in = question_nltk)
   
    # Affichage résultat 
    return jsonify({'status'   : 'ok',
                    'message'  : pred_nltk
                   })    

    

###############################################
#                  USE                        #
###############################################    
@app.route('/use')
def endpoint_use():

    # Préparation données
    question_use = preparation.preparation_use(question_in = data)
    
    # Prédiction tag  
    pred_use = prediction.prediction_use(question_in = question_use)
   
    # Affichage résultat 
    return jsonify({'status'   : 'ok',
                    'message'  : pred_use
                   })    



if __name__ == "__main__":
    app.run(debug=True)    
