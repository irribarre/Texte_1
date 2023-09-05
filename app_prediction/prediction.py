# -*- coding: utf-8 -*-

import pickle
from io import StringIO

###################################################
#             PREDICTION DES DONNEES              #
###################################################

#C_GOOGLE_DRIVE_PUBLIC__APP_MODELS = 'https://drive.google.com/drive/folders/1tlUxQtNxNlXvcDL7sdJQEuJLv2LfHzbp?usp=drive_link'
    

    
###############################################
#                  NLTK                       #
###############################################    
# Prédiction avec NLTK
def prediction_nltk(question_in):
    
    print("prediction_nltk, question_in =", question_in)
        
    # Constantes
    # https://stackoverflow.com/questions/64047288/read-a-csv-file-stored-in-google-drive
    orig_url = 'https://drive.google.com/file/d/1A_GKp8gTMcp9zRa-Zw0Fyjq6A5ECQ2aq/view?usp=sharing'
    file_id  = orig_url.split('/')[-2]
    dwn_url  = 'https://drive.google.com/uc?export=download&id=' + file_id    
#    NLTK_MODEL_ID = '1A_GKp8gTMcp9zRa-Zw0Fyjq6A5ECQ2aq'
    
    print("prediction_nltk, orig_url =", orig_url)
    print("prediction_nltk, file_id =", file_id)
    print("prediction_nltk, dwn_url =", dwn_url)        
    
    url = requests.get(dwn_url).text
    csv_raw = StringIO(url)
#    dfs = pd.read_csv(csv_raw)

    # Chargement modèle pré-entraîné avec le modèle USE.
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    # https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
    # https://stackoverflow.com/questions/56611698/pandas-how-to-read-csv-file-from-google-drive-public    

    # https://realpython.com/urllib-request/
#    from urllib.request import urlopen
#    response = urlopen(NLTK_MODEL)
#    ovr = response.read()
#    response.close()


    
    # Making a prediction on the test set
    # https://github.com/automl/auto-sklearn/issues/849
    pickle.dump(ovr, open(NLTK_MODEL, 'wb'))
    loaded_model = pickle.load(NLTK_MODEL)
    y_pred = loaded_model.predict(question_in)
#    y_pred = ovr.predict(question_in)
    
    print('y_pred (NLTK) =', y_pred)
    
    return(y_pred)

===================================
mport pandas as pd
import requests


orig_url='https://drive.google.com/file/d/0B6GhBwm5vaB2ekdlZW5WZnppb28/view?usp=sharing'

file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
dfs = pd.read_csv(csv_raw)
