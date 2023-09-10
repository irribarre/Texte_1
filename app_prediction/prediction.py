# -*- coding: utf-8 -*-

import pickle
import pandas as pd


###################################################
#             PREDICTION DES DONNEES              #
###################################################
  

    
###############################################
#                  NLTK                       #
###############################################    
# Prédiction avec NLTK
def prediction_nltk(df_question_in):
    
    print('prediction_nltk, df_question_in =\n', df_question_in)
            
    NLTK_MODEL_NAME = './app_models/model_LinearSVC_NLTK_stemmer.pkl'
    print('prediction_nltk, NLTK_MODEL_NAME =', NLTK_MODEL_NAME)
    
    
    
    # Intégration df_question_in dans les colonnes des données entraînées
    df_stemmer_columns = pd.read_csv('./app_prediction/df_stemmer_columns.csv', sep = '\t')
    print('prediction_nltk, df_stemmer_columns.shape =', df_stemmer_columns.shape)
    print('prediction_nltk, df_stemmer_columns =\n', df_stemmer_columns)
    
    # Boucle sur les colonnes
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.items.html   
    ind_ligne      = 0 # initialisation de la ligne correspondant à la question écrite depuis postman.
    liste_question = []

    for col in df_stemmer_columns.columns:
        if (col in df_question_in):
            value = df_question_in[ind_ligne, col]
        else:
            value = 0
        print('prediction_nltk, col =', col, ':', value)
        liste_question.append(value)
        
#    print('prediction_nltk, liste_question =', liste_question)
    df_stemmer_columns.loc[ind_ligne] = liste_question


   
    # Vérification mise à jour : affichage des colonnes non vides
    print('prediction_nltk, df_stemmer_columns.shape =', df_stemmer_columns.shape)
    for col in df_stemmer_columns.columns:
        if (df_stemmer_columns[ind_ligne, col] != 0):
            print('prediction_nltk, colonne', col, '\t=', df_stemmer_columns[ind_ligne, col])
        
    
    # Loading model to compare the results
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    loaded_model = pickle.load(open(NLTK_MODEL_NAME, 'rb'))
    print('prediction_nltk, loaded_model')
        
    y_pred = loaded_model.predict(df_stemmer_columns)
    
    print('y_pred (NLTK) =', y_pred)
    
    return(y_pred)




###############################################
#                  USE                        #
###############################################    
# Prédiction avec USE
def prediction_use(df_question_in):

    print('prediction_use, df_question_in =\n', df_question_in)
            
    USE_MODEL_NAME = './app_models/model_LinearSVC_USE.pkl'
    print('prediction_use, USE_MODEL_NAME =', USE_MODEL_NAME)
    
        
    
    # Loading model to compare the results
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    loaded_model = pickle.load(open(USE_MODEL_NAME, 'rb'))
    print('prediction_use, loaded_model')
        
    y_pred = loaded_model.predict(df_stemmer_columns)
    
    print('y_pred (USE) =', y_pred)
    
    return(y_pred)    
    
