import re
import json
import sys
import os

#SAVE TO PYTHON FILE
filename = 'ApiClientMethods1.py'
path = 'C:/Users/Lola/OneDrive/Documentos/TFG/VulnerableREST/TFG-APIsREST'
file_path = os.path.join(path, filename)
sys.stdout = open(file_path, "w")
print("import requests")
print("")

#PROGRAM STARTED
apiDescriptionFile = open('openapi.json')
apiDescription = json.load(apiDescriptionFile)

def createMethodDef(httpMethod, path):
    apiPath = path.replace("/", "_")
    apiPath = apiPath.replace("{", "")
    apiPath = apiPath.replace("}", "")
    s = "def " + httpMethod + apiPath + "(jwt='', body=None"

    for arg in re.findall(r'\{\w*\}', path):
        s += ", " + arg.replace("{", "").replace("}", "") + '=None'
    s += "):"

    print(s)


def createHeaders():
    print("     headers = {'Authorization': 'Bearer ' + jwt}")


def createUrl(path):
    apiPath = path.replace("{", "' + ")
    apiPath = apiPath.replace("}", " + '")
    print("     url = '" + baseUrl + apiPath + "'")


def createRequest(httpMethod):
    print("     req = requests." + httpMethod + "(url, headers=headers, json=body)")


def createReturn():
    print("     return req.status_code, req.text")


def createClientMethod(httpMethod, path):
    createMethodDef(httpMethod, path)
    createUrl(path)
    createHeaders()
    createRequest(httpMethod)
    createReturn()
    print("")
    print("")


# Paths

baseUrl = "http://127.0.0.1:5000"

for path in apiDescription['paths']:
    #print(path)

    for httpMethod in apiDescription['paths'][path]:
        #print(httpMethod)

        createClientMethod(httpMethod, path)




