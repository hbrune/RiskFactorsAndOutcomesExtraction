import sys
import argparse
import requests

def package_payload(txt):
    #Generate payload parameters
    req_content_type = 'default=application/x-www-form-urlencoded'
    params = []
    params.append(('inputtext', txt))
    params.append(('docformat', 'freetext'))
    params.append(('resultformat', 'json'))
    params.append(('sourceString', 'HPO'))
    params.append(('sourceString', 'MSH'))
    params.append(('sourceString', 'AOD'))
    params.append(('sourceString', 'CSP'))
    params.append(('semanticTypeString', 'all'))
    return params

def process(txt):
    #Calls package_payload and then calls handle_request. """
    payload = package_payload(txt)
    acceptfmt = 'text/plain'
    url = 'https://ii.nlm.nih.gov/metamaplite/rest/annotate'
    return handle_request(url, acceptfmt, payload)

def handle_request(url, acceptfmt, payload):   
    headers = {'Accept' : acceptfmt}
    return requests.post(url, payload, headers=headers)