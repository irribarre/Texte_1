# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from string import punctuation
import re
from bs4 import BeautifulSoup
import nltk
#nltk.download('wordnet')
#from nltk.tokenize import RegexpTokenizer
#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer, PorterStemmer
import emoji

from sklearn.feature_extraction.text import CountVectorizer
import tensorflow_hub as hub



###################################################
#             PREPARATION DES DONNEES             #
###################################################

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ 1) NLTK                                                                        @
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#####################################################################################
# Lecture d'un fichier .txt pour maj variables                                      #
#####################################################################################
def lecture_fichier(file_name_in):

    words = []
    print('lecture fichier', file_name_in)
    
    with open('./app_preparation/' + file_name_in) as f:
        for word in f.readlines():
            words.append(word[:-1])
    return words



# Maj des variables pour différentes fonctions :
# >>>>>>> fonction cleaning_mot
stop_words    = lecture_fichier(file_name_in = 'stop_words.txt')
english_words = lecture_fichier(file_name_in = 'english_words.txt')
token_tags    = lecture_fichier(file_name_in = 'token_tags.txt')

# >>>>>>> fonction cleaning_complément
liste_rare_words = lecture_fichier(file_name_in = 'rare_words.txt')
doublons         = lecture_fichier(file_name_in = 'doublons.txt')
    
# >>>>>>> fonction cleaning_complement_normalisation
liste_rare_words_stemmer = lecture_fichier(file_name_in = 'rare_words_stemmer.txt')
liste_rare_words_lemma   = lecture_fichier(file_name_in = 'rare_words_lemma.txt')




#####################################################################################
# Nettoyage au niveau des chaînes de caractères :                                   #
#  - Suppression des balises HTML                                                   #
#  - Passage en minuscules                                                          #
#  - Tokenization                                                                   #
#  - Suppressions : ponctuation, caractères 'blancs', mots alphanumeriques, nombres #
#  - Transform emojis to characters                                                 #
#####################################################################################
def cleaning_chaine(texte_in):
    
    print('\n\n\n')    
    print('@' * 30, ' cleaning_chaine ', '@' * 30)
    print('cleaning_chaine, texte_in =', texte_in)
        
        
    # Suppression des balises HTML
    soup = BeautifulSoup(texte_in, "html.parser")
    soup_text = soup.get_text()
    print('cleaning_chaine, soup_text =', soup_text)

    
    # Passage en minuscules
    soup_text_min = soup_text.lower()
    print('cleaning_chaine, soup_text_min =', soup_text_min)

    
    # Suppression ponctuation (remplacement par un caractère blanc)
    # Ponctuation =  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
    doc_sans_ponctuation = re.sub(f"[{re.escape(punctuation)}]", " ", soup_text_min)
    print('cleaning_chaine, doc_sans_ponctuation =', doc_sans_ponctuation)
    
    
    # Initialisation RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    # Tokenization : liste de tokens bruts    
    tokens = tokenizer.tokenize(doc_sans_ponctuation)
    print('cleaning_chaine, tokens =', tokens)
    
    
    # Suppression de tous les caractères "blanc" (\s) i.e. équivalent à la classe [ \t\n\r\f\v].
    # https://docs.python.org/fr/3/howto/regex.html
    tokens_no_blanc = [w for w in tokens if not (bool(re.search(r'\s', w)))]
    print('cleaning_chaine, tokens_no_blanc =', tokens_no_blanc)
    
        
    # Suppression des mots alphanumeriques (exemple : 4cb9df79467b3eb5d6787a98dcf8665)
    # https://www.delftstack.com/fr/howto/python/how-to-check-a-string-contains-a-number-or-not-in-python/
    # <=> on regarde si la chaîne de caractère contient un nombre.
    # Suppression de tous les caractères numériques (\d) i.e. équivalent à la classe [0-9].
    # https://docs.python.org/fr/3/howto/regex.html        
    tokens_no_alphanum = [w for w in tokens_no_blanc if not (bool(re.search(r'\d', w)))]
    print('cleaning_chaine, tokens_no_alphanum =', tokens_no_alphanum)
    
        
    # Suppression des nombres    
    tokens_no_nombre = [w for w in tokens_no_alphanum if not (w.isdigit())]
    print('cleaning_chaine, tokens_no_nombre =', tokens_no_nombre)
    
        
    # Conversion liste de tokens de type str --> une chaîne de caractères.        
    # https://www.delftstack.com/fr/howto/python/how-to-convert-a-list-to-string/
    text_clean = ' '.join(tokens_no_nombre)
    print('cleaning_chaine, text_clean =', text_clean)
    

    # Transform emojis to characters
    text_no_emojis = emoji.demojize(text_clean)  
    print('cleaning_chaine, text_no_emojis =', text_no_emojis)
    
    return(text_no_emojis)

    

    
#################################################################################################
# Nettoyage au niveau des mots :                                                                #
#  - Suppressions : stop words, mots qui ne sont pas dans le dictionnaire anglais, short tokens #
#################################################################################################
def cleaning_mot(texte_in, min_len_word_in = 3):
    
    print('\n\n\n')        
    print('@' * 30, ' cleaning_mot ', '@' * 30)
    print('cleaning_mot, texte_in =', texte_in)

    
    # Découpage en tokens
    tokens = texte_in.split()
    print('cleaning_mot, tokens =', tokens)
    
        
    # Suppression stop_words
    tokens_no_stop_words = [w for w in tokens if w not in stop_words] 
    print('cleaning_mot, tokens_no_stop_words =', tokens_no_stop_words)
    
        
    # Suppression des mots qui ne sont pas dans le dictionnaire anglais 
    tokens_english = [w for w in tokens_no_stop_words if w in english_words]
    print('cleaning_mot, tokens_english =', tokens_english)
    
        
    # Suppression short tokens (taille >= min_len_word_in) s'il n'est pas dans les token_tags 
    # (les termes techniques sont indispensables à garder pour les algos).
    # Autrement dit, les tokens longs prennnent en compte les tags.
    tokens_long = [w for w in tokens_english if (len(w) >= min_len_word_in) |  
                                                    (w in token_tags)]
    print('cleaning_mot, tokens_long =', tokens_long)
    

    # Conversion liste de tokens de type str --> une chaîne de caractères.     
    # https://www.delftstack.com/fr/howto/python/how-to-convert-a-list-to-string/
    text_clean = ' '.join(tokens_long)
    print('cleaning_mot, text_clean =', text_clean)
    
    return(text_clean)
        
    


#################################################################################################
# Complément nettoyage :                                                                        #
#  - Suppressions : rare words, doublons.                                                       #
#  - Normalisation (lemmatisation & stemming).                                                  #
#################################################################################################
def cleaning_complement(texte_in):    
    
    print('\n\n\n')
    print('@' * 30, ' cleaning_complement ', '@' * 30)
    print('cleaning_complement, texte_in =', texte_in)

    
    # Découpage en tokens
    tokens = texte_in.split()
    print('cleaning_complement, tokens =', tokens)
    
    
    # Suppression rare tokens présents peu de fois
    # Les tokens rares sur l'ensemble du corpus ne sont pas très utiles.
    # Nous les supprimons pour diminuer la liste de tokens du corpus (la taille du vocabulaire) et accélérer nos calculs.
    tokens_non_rare = [w for w in tokens if w not in liste_rare_words]
    print('cleaning_complement, tokens_non_rare =', tokens_non_rare)
    
    
    # Suppression doublons
    tokens_sans_doublons = [w for w in tokens_non_rare if w not in doublons]
    print('cleaning_complement, tokens_sans_doublons =', tokens_sans_doublons)
    
        
    # Normalisation : lemmatisation et stemming
    # Initialisation
    stemmer = PorterStemmer()
    lemma   = WordNetLemmatizer()    

    # >>>>>>> stemming   
    tokens_stemmer = [stemmer.stem(i) for i in tokens_sans_doublons]   
    print('cleaning_complement, tokens_stemmer =', tokens_stemmer)
    
    # >>>>>>> lemmatisation
    tokens_lemma = [lemma.lemmatize(i) for i in tokens_sans_doublons]
    print('cleaning_complement, tokens_lemma =', tokens_lemma)
    
        
    # Suppression short tokens (taille >= 3)
    tokens_stemmer_long = [w for w in tokens_stemmer if len(w) >= 3]
    tokens_lemma_long   = [w for w in tokens_lemma if len(w) >= 3]
    print('cleaning_complement, tokens_stemmer_long =', tokens_stemmer_long)
    print('cleaning_complement, tokens_lemma_long =', tokens_lemma_long)    
    
    
    # Conversion liste d'éléments de type str --> une chaîne de caractères.        
    # https://www.delftstack.com/fr/howto/python/how-to-convert-a-list-to-string/
    stemmer_clean = ' '.join(tokens_stemmer_long)
    lemma_clean   = ' '.join(tokens_lemma_long)
    print('cleaning_complement, stemmer_clean =', stemmer_clean)
    print('cleaning_complement, lemma_clean =', lemma_clean)
    
    return stemmer_clean, lemma_clean
    
    


#################################################################################################
# Complément nettoyage après normalisation :                                                    #
#  - Suppressions : rare words données normalisées.                                             #
#################################################################################################
def cleaning_complement_normalisation(texte_stemmer_in, texte_lemma_in):
    
    print('\n\n\n')
    print('@' * 30, ' cleaning_complement_normalisation ', '@' * 30)
    print('cleaning_complement_normalisation, texte_stemmer_in =', texte_stemmer_in)
    print('cleaning_complement_normalisation, texte_lemma_in =', texte_lemma_in)    

    
    # Découpage en tokens
    tokens_stemmer = texte_stemmer_in.split()
    tokens_lemma   = texte_lemma_in.split()
    print('cleaning_complement_normalisation, tokens_stemmer =', tokens_stemmer)
    print('cleaning_complement_normalisation, tokens_lemma =', tokens_lemma)
    
    
    # Suppression rare tokens présents peu de fois
    # Les tokens rares sur l'ensemble du corpus ne sont pas très utiles.
    # Nous les supprimons pour diminuer la liste de tokens du corpus (la taille du vocabulaire) et accélérer nos calculs.
    tokens_non_rare_stemmer = [w for w in tokens_stemmer if w not in liste_rare_words_stemmer]
    tokens_non_rare_lemma   = [w for w in tokens_lemma   if w not in liste_rare_words_lemma]
    print('cleaning_complement_normalisation, tokens_non_rare_stemmer =', tokens_non_rare_stemmer)
    print('cleaning_complement_normalisation, tokens_non_rare_lemma =', tokens_non_rare_lemma)
    
        
    # Conversion liste d'éléments de type str --> une chaîne de caractères.        
    # https://www.delftstack.com/fr/howto/python/how-to-convert-a-list-to-string/
    stemmer_clean_final = ' '.join(tokens_non_rare_stemmer)
    lemma_clean_final   = ' '.join(tokens_non_rare_lemma)
    print('cleaning_complement_normalisation, stemmer_clean_final =', stemmer_clean_final)
    print('cleaning_complement_normalisation, lemma_clean_final =', lemma_clean_final)
    
    return stemmer_clean_final, lemma_clean_final
        
    
    

#################################################################################################
# Nettoyage des données avec NLTK                                                               #
#################################################################################################
def nettoyage_nltk(question_in):
    
    print('\n\n\n')
    print('@' * 30, ' nettoyage_nltk ', '@' * 30)
    print('nettoyage_nltk, question_in =', question_in)
    
    
    # Nettoyage au niveau des chaînes de caractères
    question_clean_chaine = cleaning_chaine(texte_in = question_in)
    print('nettoyage_nltk, question_clean_chaine =', question_clean_chaine)
    
    
    # Nettoyage au niveau des mots
    question_clean_mot = cleaning_mot(texte_in = question_clean_chaine)
    print('nettoyage_nltk, question_clean_mot =', question_clean_mot)
    
    
    # Complément nettoyage
    question_stemmer_clean, question_lemma_clean = cleaning_complement(texte_in = question_clean_mot)
    print('nettoyage_nltk, question_stemmer_clean =', question_stemmer_clean)
    print('nettoyage_nltk, question_lemma_clean =', question_lemma_clean)    
    
    
    # Complément nettoyage après normalisation
    question_stemmer_clean_final, question_lemma_clean_final = cleaning_complement_normalisation(texte_stemmer_in = question_stemmer_clean, 
                                                                                                 texte_lemma_in   = question_lemma_clean)
    print('nettoyage_nltk, question_stemmer_clean_final =', question_stemmer_clean_final)
    print('nettoyage_nltk, question_lemma_clean_final =', question_lemma_clean_final)    
    
    return question_stemmer_clean_final, question_lemma_clean_final




#################################################################################################
# Préparation des données avec NLTK : création des features                                     #
#################################################################################################
def preparation_nltk(question_in):
    
    print('\n\n\n')
    print('@' * 30, ' preparation_nltk ', '@' * 30)
    print('preparation_nltk, question_in =', question_in)
    
    
    # Nettoyage du texte
    question_stemmer_clean_final, question_lemma_clean_final = nettoyage_nltk(question_in = question_in)
    print('preparation_nltk, question_stemmer_clean_final =', question_stemmer_clean_final)
    print('preparation_nltk, question_lemma_clean_final =', question_lemma_clean_final)    
    
    
    # On ne s'intéresse qu'aux données stemmer
    vect_stemmer = CountVectorizer()
    
    # Updating corpus list : one string for one document :
    # corpus = ['This is the first document.',
    #           'This document is the second document.',
    #           'And this is the third one.',
    #           'Is this the first document?'] 
    # Ici ion a un seul document (car une seule question).
    corpus_liste_doc_stemmer   = []
    corpus_liste_doc_stemmer.append(question_stemmer_clean_final)
    vect_stemmer.fit(corpus_liste_doc_stemmer)
    print('preparation_nltk, len(vect_stemmer.vocabulary_) =', len(vect_stemmer.vocabulary_), 'mots de vocabulaire pour stemmer')
    # Affichage des 20 premiers mots
    print('preparation_nltk, vect_stemmer.vocabulary_ =', str(dict(list(vect_stemmer.vocabulary_.items()))))
    print('preparation_nltk, vect_stemmer.get_feature_names =', len(vect_stemmer.get_feature_names()))


    # DTM (Document Term Matrix) : le corpus se répartit sur différentes features
    dtm_stemmer = vect_stemmer.transform(corpus_liste_doc_stemmer)
    print('preparation_nltk, dtm_stemmer =', dtm_stemmer)    


    # Conversion spare matrix --> dense matrix (pour gagner de la place)
    df_stemmer = pd.DataFrame(dtm_stemmer.toarray(), columns = vect_stemmer.get_feature_names())
    print('preparation_nltk, df_stemmer.columns =', df_stemmer.columns)
    print('preparation_nltk, df_stemmer.shape =', df_stemmer.shape)
    
    return(df_stemmer)




# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @ 2) USE                                                                         @
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   
# Préparation des données avec USE : création des features
def preparation_use(question_in):
          
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4") # USE (Universal Sentence Encoder)

    print('\n\n\n')
    print('@' * 30, ' preparation_use ', '@' * 30)
    print('preparation_use, question_in =', question_in)

    
    # texte brut 
    sentences   = []
    sentences.append(question_in)  
#    sentences = question_in.to_list()
    print('preparation_use, sentences =', sentences)
          
          
    batch_size = 1
    
    for step in range(len(sentences)//batch_size):
        idx = step * batch_size
              
        feat = embed(sentences[idx:idx + batch_size])

        if (step == 0):
            features = feat
        else :
            features = np.concatenate((features, feat))
    print('preparation_use, features.shape =', features.shape)          
          
    return(features)

