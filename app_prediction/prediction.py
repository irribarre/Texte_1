# -*- coding: utf-8 -*-

import pickle
import pandas as pd
import numpy as np


###################################################
#             PREDICTION DES DONNEES              #
###################################################
  
y_classes = ['.net', 'android', 'asp.net', 'c', 'c#', 'c++', 'css', 'html', 'ios', 'iphone', 'java', 'javascript', 'jquery', 'json',
             'linux', 'mysql', 'node.js', 'objective-c', 'performance', 'php', 'python', 'reactjs', 'ruby-on-rails', 'spring',
             'sql', 'swift', 'windows', 'xcode'] 

    
###############################################
#                  NLTK                       #
###############################################    
# Prédiction avec NLTK
def prediction_nltk(df_question_in):
    
    # Initialisation
    y_pred_str = ''
    
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
            value = df_question_in.loc[ind_ligne, col]
            print('prediction_nltk, col =', col, ':', value)            
        else:
            value = 0
        liste_question.append(value)
        
#    print('prediction_nltk, liste_question =', liste_question)
    df_stemmer_columns.loc[ind_ligne] = liste_question


   
    # Vérification mise à jour : affichage des colonnes non vides
    print('prediction_nltk, df_stemmer_columns.shape =', df_stemmer_columns.shape)
    print('prediction_nltk, affichage colonnes non vides :')
    for col in df_stemmer_columns.columns:
        value = df_stemmer_columns.loc[ind_ligne, col]
        if (value != 0):
            print('\t- prediction_nltk, colonne', col, '=', value)
        
    
    # Loading model to compare the results
    # https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
    loaded_model = pickle.load(open(NLTK_MODEL_NAME, 'rb'))
    print('prediction_nltk, loaded_model')
        
    y_pred = loaded_model.predict(df_stemmer_columns)
    
    print('prediction_nltk, y_pred\t\t=', y_pred)
    print('prediction_nltk, y_pred.shape\t=', y_pred.shape)    
    print('prediction_nltk, type(y_pred)\t=', type(y_pred))    
    
    # Transformation ndarray 2D --> ndarray 1D
    y_pred_1D = np.hstack(y_pred)
    print('prediction_nltk, y_pred_1D\t\t=', y_pred_1D)
    print('prediction_nltk, type(y_pred_1D)\t=', type(y_pred_1D))
    
    
    # Transformation ndarray --> liste
    y_pred_list = y_pred_1D.tolist()
    print('prediction_nltk, y_pred_list\t\t=', y_pred_list)
    print('prediction_nltk, type(y_pred_list)\t=', type(y_pred_list))
    
    
    # Recherche classe(s) prédite(s)
    # https://www.freecodecamp.org/french/news/trouver-dans-une-liste-python-comment-trouver-iindex-dun-element-dans-une-liste/    
#    y_classes.index('android')

    y_pred_indices  = [index for (index, item) in enumerate(y_pred_list) if (item == 1)]
    print('prediction_nltk, y_pred_indices =', y_pred_indices)

    for ind in y_pred_indices:
        y_pred_str = y_pred_str + y_classes[ind]
        
    print('prediction_nltk, y_pred_str =', y_pred_str)
        
    return(y_pred_str)




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
    
