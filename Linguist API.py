body = ({"language" : "en",
      "analyzerIds":["22a6b758-420f-4745-8a3c-46835a67c0d2", "4fa79af1-f22c-408d-98bb-b7d7aeef7f04", "08ea174b-bfdb-4e64-987e-602f85da7f72"], #use these codes to choose what features you want
      "text" : "Hi, Tom! How are you today?"})
   
#analyzerIds are used for either "part of speech tagging", "Constituency parsing", "Tokenizing"

#08ea174b-bfdb-4e64-987e-602f85da7f72 = Tokenizing
#4fa79af1-f22c-408d-98bb-b7d7aeef7f04 = POS tagging
#22a6b758-420f-4745-8a3c-46835a67c0d2 = Constituency_Tree

#reference page 'https://westus.dev.cognitive.microsoft.com/docs/services/56ea598f778daf01942505ff/operations/56ea59bfca73071fd4b102ba'
 
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'PUT YOUR KEY HERE',
}


params = urllib.parse.urlencode({
})


try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/linguistics/v1.0/analyze?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))