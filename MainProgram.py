# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:35:17 2022

@author: Brune
"""

import TextPreprocessing as text
import SemanticTypesIdentification as sem 
import LabelExtraction as lab
import spacy

def listToString(listOfSents):
    txtFinal = []
    for el in listOfSents:
        txtFinal.append(" ".join(el))
    txtFinal = " ".join(txtFinal)
    return txtFinal


fullText= text.readTextFile("Clinical Notes/Corpus/Doc13.txt").lower()
#Text preprocessing
preprocessedText = text.processContent(fullText)
#Get a string from the list of sentences
txt = listToString(preprocessedText)
semTypes, conceptsList = sem.searchSemTypesFromText(txt)
dictLabels = lab.extractConcept(semTypes)

#Named-entity recognition with the labels found
nlp = spacy.blank("en") 
#Ruler definition to define a label for the words found in the abstract with the labels
ruler = nlp.add_pipe("entity_ruler")
patterns = []
for label in dictLabels:
    if dictLabels[label] == 'RISK FACTOR' or dictLabels[label] == 'OUTCOME' :
        pattern = {"label": dictLabels[label], "pattern": label}
        patterns.append(pattern)
ruler.add_patterns(patterns)

doc = nlp(fullText)
for ent in doc.ents:
    print (ent, ", ", ent.label_)