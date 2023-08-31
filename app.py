#####################################################################
#   PROJET 5 - Catégorisez automatiquement des questions            #
#-------------------------------------------------------------------#
#   POINT D'ENTREE D'UNE API POUR LE TEST.                          #
#####################################################################

# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, jsonify
#import os

#import nbimporter     # Pour importer d'autre jupyter notebooks

# Import common functions
#from app_preparation import preparation # fonctions de préparation
#from app_prediction import prediction # fonctions de prédiction

app = Flask(__name__)


#os.environ.get('PORT', 5000)
#print('os =', os)


#API_URL = 'https://app-texte-1-3ed8a3f34c3b.herokuapp.com/'

# https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python
#question_python_1 = "Best online resource to learn Python? <br/> I am new to any scripting language. But, Still I worked on scripting a bit like tailoring other scripts to work for my purpose. For me, What is the best online resource to learn Python? <br/> Some Online Resources: <br/> http://docs.python.org/tut/tut.html - Beginners <br/> http://diveintopython3.ep.io/ - Intermediate <br/> http://www.pythonchallenge.com/ - Expert Skills <br/>http://docs.python.org/ - collection of all knowledge<br/>Some more: A Byte of Python. <br/>Python 2.5 Quick Reference<br/>Python Side bar<br/>A Nice blog for beginners<br/>Think Python: An Introduction to Software Design"    


###############################################
#                  Accueil                    #
###############################################    
@app.route("/")
def accueil():

    texte = "Bonjour titi."
    #texte = "Bonjour,<br/><br/>La prédiction du tag se trouve sur le endPoint de la méthode utilisée (NLTK / USE).<br/><br/><br/>Merci de vous rendre sur le endPoint choisi pour saisir votre question :<br/><br/>1) Méthode NLTK -------> endPoint <b>/nltk</b>.<br/>2) Méthode USE  ---------> endPoint <b>/use</b>."    
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



if __name__ == "__main__":
    app.run(debug=True)    
