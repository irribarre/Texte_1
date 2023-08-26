# -*- coding: utf-8 -*-

import pickle
#import joblib

###################################################
#             PREDICTION DES DONNEES              #
###################################################

C_GOOGLE_DRIVE_PUBLIC__APP_MODELS = 'https://drive.google.com/drive/folders/1tlUxQtNxNlXvcDL7sdJQEuJLv2LfHzbp?usp=drive_link'


###############################################
#                  NLTK                       #
###############################################    
# Prédiction avec NLTK
def prediction_nltk(question_in):
    
    # Constantes
    NLTK_MODEL = 'model_RandomForestClassifier_NLTK_stemmer.pkl'
#    NLTK_MODEL = 'model_RandomForestClassifier_NLTK_stemmer.sav'    
    
    print("prediction_nltk")
    
    # Chargement modèle pré-entraîné avec le modèle USE.
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    # https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
    ovr = pickle.load(open(C_GOOGLE_DRIVE_PUBLIC__APP_MODELS + '/' + NLTK_MODEL, 'rb'))   
#    ovr = joblib.load(NLTK_MODEL)

    # Making a prediction on the test set
    y_pred = ovr.predict(question_in)
    
    print('y_pred (NLTK) =', y_pred)
    
    return(y_pred)



###############################################
#                  USE                        #
###############################################    
# Prédiction avec USE
def prediction_use(question_in):
    
    # Constantes
    USE_MODEL = 'model_RandomForestClassifier_USE.pkl'
#    USE_MODEL = 'app_models/model_RandomForestClassifier_USE.sav'    
        
    print("prediction_use")
    
    # Chargement modèle pré-entraîné avec le modèle USE.
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    ovr = pickle.load(open(C_GOOGLE_DRIVE_PUBLIC__APP_MODELS + '/' + USE_MODEL, 'rb'))
#    ovr = joblib.load(USE_MODEL)
    
    # Making a prediction on the test set
    y_pred = ovr.predict(question_in)
    
    print('y_pred (USE) =', y_pred)
    
    return(y_pred)
 