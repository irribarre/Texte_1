# -*- coding: utf-8 -*-

import pickle


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
    NLTK_MODEL    = 'https://drive.google.com/file/d/1A_GKp8gTMcp9zRa-Zw0Fyjq6A5ECQ2aq/view?usp=sharing'
    NLTK_MODEL_ID = '1A_GKp8gTMcp9zRa-Zw0Fyjq6A5ECQ2aq'
    
    print("prediction_nltk, question_in =", question_in)
    
    # Chargement modèle pré-entraîné avec le modèle USE.
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    # https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
    # https://stackoverflow.com/questions/56611698/pandas-how-to-read-csv-file-from-google-drive-public    

    # https://realpython.com/urllib-request/
    from urllib.request import urlopen
    response = urlopen(NLTK_MODEL)
    ovr = response.read()
    response.close()


    # Making a prediction on the test set
    # https://github.com/automl/auto-sklearn/issues/849
    pickle.dump(ovr, open(NLTK_MODEL, 'wb'))
    loaded_model = pickle.load(NLTK_MODEL)
    y_pred = loaded_model.predict(question_in)
#    y_pred = ovr.predict(question_in)
    
    print('y_pred (NLTK) =', y_pred)
    
    return(y_pred)

