# -*- coding: utf-8 -*-

import pickle


###################################################
#             PREDICTION DES DONNEES              #
###################################################
  

    
###############################################
#                  NLTK                       #
###############################################    
# Prédiction avec NLTK
def prediction_nltk(df_question_in):
    
    print("prediction_nltk, df_question_in =\n", df_question_in)
            
    NLTK_MODEL_NAME = './app_models/model_LinearSVC_NLTK_stemmer.pkl'
    print("prediction_nltk, NLTK_MODEL_NAME =", NLTK_MODEL_NAME)
    
    # Loading model to compare the results
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    loaded_model = pickle.load(open(NLTK_MODEL_NAME, 'rb'))
    print("prediction_nltk, loaded_model")
        
    y_pred = loaded_model.predict(df_question_in)
    
    print('y_pred (NLTK) =', y_pred)
    
    return(y_pred)
