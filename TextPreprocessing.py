# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:56:52 2022

@author: Brune
"""
from nltk.tokenize import PunktSentenceTokenizer
import nltk
import re


keywords = ['preoperative', 'characteristics', 'impairment', 'age', 'indicators', 'mortality', 'asa', 'charlson', 'ecg', 'cognitive', 'resident', 'care', 'fracture', 'mobility', 'type', 'high', 'score', 'admission', 'cochrane', 'library', 'years', 'pre', 'intra', 'capsular', 'comorbidity', 'score', 'common', 'condition', 'reviewers', 'independently', 'appropriate', 'management', 'embase', 'medline', 'undertaken', 'identify', 'characteristics', 'participants', 'benefit', 'comprehensive']

def removeVerbs(sent):
    filteredTags = ['VBG', 'VBZ', 'VBN', 'VBD', 'VB', 'MD', 'IN']
    filteredList = []
    tagged = nltk.pos_tag(sent)
    for el in tagged:
        if el[1] not in filteredTags:
            filteredList.append(el[0])
    return filteredList

def removeNumber(rlist):
    listq=[]
    for a in rlist:
        if len(a) >0:
            if (re.search('[a-zA-Z]', a)):
                listq.append(a)
    return listq

def removeStopwords(word_tokens):
    stop_words = nltk.corpus.stopwords.words('english')
    new_stopwords = ["hip", "fracture", "fractures", "pre-fracture", "hip-fracture", "patient", "patients", "surgery", "ci", "rr", "risk", "objective", "studies",  "statistically", "significant", "systematic", "review", "meta-analysis", "study", "design", "methods", "results", "conclusions", "confidence", "interval", "intervals"]
    stop_words.extend(new_stopwords)
    filter_sentence=[]
    for w in word_tokens:
        if w !='':
            if w not in stop_words:
                filter_sentence.append(w)
    return filter_sentence

def ngramReturner(ngramString, keywords):
    bigram_vector=[]
    for i in range(1,4):
        for item in nltk.ngrams(ngramString,i):
            for el in item:
                if el in keywords:
                    bigram_vector.append(' '.join(item))
    #remove duplicate
    bigram_vector = list(dict.fromkeys(bigram_vector))
    return bigram_vector

def readTextFile(path):
    with open(path, 'r', encoding='utf8') as f:
        data = f.read().replace('Â', ' ').replace('»','').replace('¿','').replace('ï','') 
    return data

def removeDuplicate(tokenlist):
    order_tokens = set()
    result=[]
    for word in tokenlist:
        if word not in order_tokens:
            order_tokens.add(word)
            result.append(word)
    return result

#Text preprocessing function
def processContent(text):
    #Create a list of sentences
    text = re.sub(r"[\(\)\[\]\%\<\>\{\}\=\:\;\,\"]",'',text)
    custom_sent_tokenizer = PunktSentenceTokenizer()
    sents = custom_sent_tokenizer.tokenize(text)  
    content = []    
    for i in sents:
        #For each sentence, create a list of words
        tokenizer = nltk.RegexpTokenizer(r"\w+(?:-\w+)*|\$[\d.]+|\S+")
        words = tokenizer.tokenize(i)
        words= removeStopwords(words)
        words=removeNumber(words)
        words = removeVerbs(words)
        tagged=removeDuplicate(words)     
        #words = ngramReturner(tagged, keywords)
        content.append(tagged)
    return content
