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
    NLTK_MODEL_NAME = 'model_RandomForestClassifier_NLTK_stemmer.pkl'
    
    print("prediction_nltk, orig_url =", orig_url)
    print("prediction_nltk, file_id =", file_id)
    print("prediction_nltk, dwn_url =", dwn_url)        
    
#    url = requests.get(dwn_url).text
#    csv_raw = StringIO(url)
##    dfs = pd.read_csv(csv_raw)

    # Chargement modèle pré-entraîné avec le modèle USE.
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    # https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
    # https://stackoverflow.com/questions/56611698/pandas-how-to-read-csv-file-from-google-drive-public    
    # https://stackoverflow.com/questions/50624042/how-to-unpickle-a-file-that-has-been-hosted-in-a-web-url-in-python
    
    # https://realpython.com/urllib-request/
#    from urllib.request import urlopen
#    response = urlopen(NLTK_MODEL)
#    ovr = response.read()
#    response.close()

#    import cloudpickle as cp
#    from urllib.request import urlopen
#    loaded_model = cp.load(urlopen(dwn_url, 'rb'))

    filename = dwn_url + 'MODEL_NAME'
    print('prediction_nltk, filename =', filename)
    
    # Making a prediction on the test set
    # https://github.com/automl/auto-sklearn/issues/849
#    pickle.dump(ovr, open(filename, 'wb'))
    loaded_model = pickle.load(open(filename, 'wb'))
    y_pred = loaded_model.predict(question_in)
#    y_pred = ovr.predict(question_in)
    
    print('y_pred (NLTK) =', y_pred)
    
    return(y_pred)

