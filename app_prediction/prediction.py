# -*- coding: utf-8 -*-

import pickle


###################################################
#             PREDICTION DES DONNEES              #
###################################################

C_GOOGLE_DRIVE_PUBLIC__APP_MODELS = 'https://drive.google.com/drive/folders/1tlUxQtNxNlXvcDL7sdJQEuJLv2LfHzbp?usp=drive_link'
    
# https://inside-machinelearning.com/charger-fichiers-depuis-un-drive-public-sur-google-colab/

    
###############################################
#                  NLTK                       #
###############################################    
# Prédiction avec NLTK
def prediction_nltk(question_in):
    
    # Constantes
#    NLTK_MODEL = 'model_RandomForestClassifier_NLTK_stemmer.pkl'
    NLTK_MODEL    = 'https://drive.google.com/file/d/1A_GKp8gTMcp9zRa-Zw0Fyjq6A5ECQ2aq/view?usp=sharing'
    NLTK_MODEL_ID = '1A_GKp8gTMcp9zRa-Zw0Fyjq6A5ECQ2aq'
#    NLTK_MODEL = 'model_RandomForestClassifier_NLTK_stemmer.sav'    
    
    print("prediction_nltk, question_in =", question_in)
    
    # Chargement modèle pré-entraîné avec le modèle USE.
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    # https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
    # https://stackoverflow.com/questions/56611698/pandas-how-to-read-csv-file-from-google-drive-public    
#    ovr = pickle.load(open(C_GOOGLE_DRIVE_PUBLIC__APP_MODELS + '/' + NLTK_MODEL, 'rb'))  
#    NLTK_MODEL = 'https://drive.google.com/uc?id=' + NLTK_MODEL.split('/')[-2]

#    path = 'https://drive.google.com/uc?export=download&id=' + NLTK_MODEL.split('/')[-2]

#    NLTK_MODEL = 'https://drive.google.com/uc?id=' + NLTK_MODEL_ID
#    print('NLTK_MODEL =', path)

#------------------------
    # https://realpython.com/urllib-request/
    from urllib.request import urlopen
    response = urlopen(NLTK_MODEL)
    ovr = response.read()
    response.close()
#-------------------------
#    ovr = pickle.load(open(path, 'rb'))       
#    ovr = pickle.load(open(NLTK_MODEL, 'rb'))   
#    ovr = joblib.load(NLTK_MODEL)


    # Making a prediction on the test set
    # https://github.com/automl/auto-sklearn/issues/849
    pickle.dump(ovr, open(NLTK_MODEL, 'wb'))
    loaded_model = pickle.load(NLTK_MODEL)
    y_pred = loaded_model.predict(question_in)
#    y_pred = ovr.predict(question_in)
    
    print('y_pred (NLTK) =', y_pred)
    
    return(y_pred)




###############################################
#                  Word2Vec                   #
###############################################    
# Prédiction avec Word2Vec
#def prediction_w2v(question_in):
#    
#    # Constantes
#    W2V_MODEL    = "https://drive.google.com/file/d/1AfUXjCoejbSxhHGSblQHxNiGCh5vw_nK/view?usp=sharing"
#    W2V_MODEL_ID = '1AfUXjCoejbSxhHGSblQHxNiGCh5vw_nK'
#        
#    print("prediction_w2v, question_in =", question_in)
#    
#    # Chargement modèle pré-entraîné avec le modèle USE.
#    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
#    print('W2V_MODEL =', W2V_MODEL)
#    
#    path = 'https://drive.google.com/uc?export=download&id=' + W2V_MODEL.split('/')[-2]
#    
#    # https://realpython.com/urllib-request/
#    from urllib.request import urlopen
#    response = urlopen(W2V_MODEL)
#    ovr = response.read()
#    response.close()
#    
#    
#    # Making a prediction on the test set
#    # https://github.com/automl/auto-sklearn/issues/849
#    pickle.dump(ovr, open(W2V_MODEL, 'wb'))
#    loaded_model = pickle.load(W2V_MODEL)
#    y_pred = loaded_model.predict(question_in)    
#    y_pred = ovr.predict(question_in)
#    print('y_pred (w2v) =', y_pred)
#    
#    return(y_pred)




###############################################
#                  USE                        #
###############################################    
## Prédiction avec USE
#def prediction_use(question_in):
#    
#    # Constantes
##    USE_MODEL = 'model_RandomForestClassifier_USE.pkl'
#    USE_MODEL    = "https://drive.google.com/file/d/1AfUXjCoejbSxhHGSblQHxNiGCh5vw_nK/view?usp=sharing"
#    USE_MODEL_ID = '1AfUXjCoejbSxhHGSblQHxNiGCh5vw_nK'
##    USE_MODEL = 'app_models/model_RandomForestClassifier_USE.sav'    
#        
#    print("prediction_use, question_in =", question_in)
#    
#    # Chargement modèle pré-entraîné avec le modèle USE.
#    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
##    ovr = pickle.load(open(C_GOOGLE_DRIVE_PUBLIC__APP_MODELS + '/' + USE_MODEL, 'rb'))
##    USE_MODEL = 'https://drive.google.com/uc?id=' + USE_MODEL.split('/')[-2]
##    USE_MODEL = 'https://drive.google.com/uc?id=' + USE_MODEL_ID    
#    print('USE_MODEL =', USE_MODEL)
#    
#    path = 'https://drive.google.com/uc?export=download&id=' + USE_MODEL.split('/')[-2]
#    
#    # https://realpython.com/urllib-request/
#    from urllib.request import urlopen
#    response = urlopen(NLTK_MODEL)
#    ovr = response.read()
#    response.close()
#    
##    ovr = pickle.load(open(USE_MODEL, 'rb'))
##    ovr = pickle.load(open(path, 'rb'))
##    ovr = joblib.load(USE_MODEL)
#    
#    # Making a prediction on the test set
#    # https://github.com/automl/auto-sklearn/issues/849
#    pickle.dump(ovr, open(NLTK_MODEL, 'wb'))
#    loaded_model = pickle.load(NLTK_MODEL)
#    y_pred = loaded_model.predict(question_in)    
#    y_pred = ovr.predict(question_in)
##    print('y_pred (USE) =', y_pred)
#    
#    return(y_pred)
 