# -*- coding: utf-8 -*-
"""
Created on Thu May  4 13:58:44 2017

@author: ihassan1
"""

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'PUT KEY HERE',
}

params = urllib.parse.urlencode({})

body = {
   "documents": [
         {
             "language": "en",
             "id": "1",
             "text": "I love my wife"
         },
         {
          "language": "en",
          "id": "2",
          "text": "I hate my wife"
          }
     ]
 }

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    

#convert the byte returned from Azure to a dictionary
data_str = data.decode("utf-8")
data_dict = eval(data_str)
####################################
