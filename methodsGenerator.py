import re
import json
import sys
import os

#SAVE TO PYTHON FILE
filename = 'ApiClientMethods.py'
path = 'C:/Users/Lola/OneDrive/Documentos/TFG/VulnerableREST'
file_path = os.path.join(path, filename)
sys.stdout = open(file_path, "w")
print("import requests")
print("")

#PROGRAM STARTED
apiDescriptionFile = open('openapi.json')
apiDescription = json.load(apiDescriptionFile)

def createMethodDef(httpMethod, path, param):
    apiPath = path.replace("/", "_")
    apiPath = apiPath.replace("{", "")
    apiPath = apiPath.replace("}", "")
    apiPath = apiPath.replace("-", "_")
    s = "def " + httpMethod + apiPath + "(jwt='', " + param + "=None"

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


def createRequest(httpMethod, param):
    print("     req = requests." + httpMethod + "(url, headers=headers, json=" + param + ")")


def createReturn():
    print("     return req.status_code, req.text")


def createClientMethod(httpMethod, path, param):
    createMethodDef(httpMethod, path, param)
    createUrl(path)
    createHeaders()
    createRequest(httpMethod, param)
    createReturn()
    print("")
    print("")


# Paths

baseUrl = "http://127.0.0.1:5000"

for path in apiDescription['paths']:
    #print(path)

    for httpMethod in apiDescription['paths'][path]:
        #print(httpMethod)

        if 'requestBody' in apiDescription['paths'][path][httpMethod]:
            params = str(apiDescription['paths'][path][httpMethod]['requestBody']['content']['application/json']['schema']['$ref'])
            params = params.split('/')
            param = params[-1]
            param = param.replace("InUpdate", "").lower()
            createClientMethod(httpMethod, path, param)
        else:
            createClientMethod(httpMethod, path, 'body')




