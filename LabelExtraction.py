# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:54:23 2022

@author: Brune
"""

from collections import defaultdict


dicRiskFactors = ["Biologically Active Substance", "Finding", "Organism Attribute", "Qualitative Concept", "Clinical Attribute", "Mental or Behavioral Dysfunction", "Therapeutic or Preventive Procedure", "Disease or Syndrome", "Daily or Recreational Activity", "Amino Acid, Peptide, or Protein"]
dicOutcomes = ["Quantitative Concept", "Functional Concept", "Health Care Activity"]

def extractConcept(dicSemanticType):
    dicLabel=defaultdict(list)
    for w in dicSemanticType:
        if dicSemanticType[w] in dicRiskFactors:
            dicLabel[w]="RISK FACTOR"
        elif dicSemanticType[w] in dicOutcomes:
            dicLabel[w]="OUTCOME"
        else:
            dicLabel[w]="NONE"
    return dicLabel