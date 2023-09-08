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
    for (column_name, column_data) in df_stemmer_columns.items():
        if column_name in df_question_in.columns:
            df_stemmer_columns[column_name] = df_question_in[column_name]
            print('Column name\t:', column_name)
            print('Column value\t:', df_stemmer_columns[column_name]) 
        else:
            df_stemmer_columns[column_name] = 0
   
    # Vérification mise à jour : affichage des colonnes non vides
    print('prediction_nltk, df_stemmer_columns.shape =', df_stemmer_columns.shape)
    for (column_name, column_data) in df_stemmer_columns.items():
        if (column_data.values != 0):
            print('colonne', column_name, '=', column_data.values)
        
    
    # Loading model to compare the results
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    loaded_model = pickle.load(open(NLTK_MODEL_NAME, 'rb'))
    print('prediction_nltk, loaded_model')
        
    y_pred = loaded_model.predict(df_stemmer_columns)
    
    print('y_pred (NLTK) =', y_pred)
    
    return(y_pred)
