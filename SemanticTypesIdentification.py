# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:15:21 2022

@author: Brune
"""


import MmlRestClient as rest 
import json


filteredSources = ["HPO", "AOD", "MSH", "CSP"]
#Creates a dict of semantic types associated with their abbreviation
def getSemanticTypesDefinition():
    f = open("SemanticTypes.txt", "r")
    semTypesDef = {}
    fileText = f.read() 
    for el in fileText.split('\n'):
        formattedEl = el.split('|')
        if len(formattedEl) == 3:
            semTypesDef[formattedEl[0]] = formattedEl[2]
    return semTypesDef

def jsonResToConcepts(jsonRes):
    data = json.loads(jsonRes)
    dictCui = {}
    dictSemType = {}
    concepts = {}
    semTypesDef = getSemanticTypesDefinition()
    for el in data:
        listConcept = el["evlist"]
        sources = listConcept[0]["conceptinfo"]["sources"]
        for source in sources:
            if source in filteredSources:
                concept = listConcept[0]["conceptinfo"]["conceptstring"]
                cui = listConcept[0]["conceptinfo"]["cui"]
                semanticType = listConcept[0]["conceptinfo"]["semantictypes"][0]
                concepts[el["matchedtext"]] = concept
                dictCui[el["matchedtext"]] = cui
                dictSemType[el["matchedtext"]] = semTypesDef[semanticType]  
    return dictSemType, concepts

def searchSemTypesFromText(text):
    res= rest.process(text)
    #json result to dictionary of each word mapped with their semantic types
    semTypes, concepts = jsonResToConcepts(res.text)
    return semTypes, concepts
    

