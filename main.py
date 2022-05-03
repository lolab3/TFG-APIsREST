import inspect
import os
import re
import json
from inspect import signature
import copy
import OpenApi as OpenApi

from ApiClientMethods import *
from sampleData import *
#from ApiParameters import *

import sys
sys.stdout = open('output.txt', 'w')


Functions = []
allFunctions = []
listofDelete = []
finalList = []
allUsers = []
params = []

#Buscar totes les funcions al document apiClientMethods.py
f = open ('apiClientMethods.py','r')
message = f.read()

allFunctions = re.findall("def .*", message)
for i in allFunctions:
    Functions.append(i)

words = [w.replace("def ", "") for w in Functions]
for i in words:
    for j in i:
        boolean = j.find(str('('))
        if boolean == 0:
            listofDelete.append(i.index(j))

boolean = False
for i in words:
    a = words.index(i)
    for j in i:
        if(boolean == False):
            if i.index(j) == listofDelete[words.index(i)]:
                x = listofDelete[words.index(i)]
                boolean = True
        if boolean:
            i = i[:x] + i[x + 1:]

    finalList.append(i)
    boolean = False

#print(finalList)

#identificar funció Login
indexofLogin = -1

#intentar trobar la funció de login
for i, parameter in enumerate(finalList):
    if 'login' in parameter or 'Login' in parameter or 'LOGIN' in parameter:
        indexofLogin = i

#si no, demanar identificar-la
if indexofLogin == -1:
    print("Quina funció és la de login?")
    for i, parameter in enumerate(finalList):
        print((i+1), ". ", parameter)
    i = int(input()) - 1

funcioLogin = finalList[indexofLogin]
funcioLogin = globals()[funcioLogin]


#GetAllUsers
for user in users:
    u = {'username': user['username'], 'password': user['password']}
    allUsers.append(u)

#print(allUsers)


#Login with all Users
for u in allUsers:
    print("****************************************************************************")
    print("YOU HAVE LOGGED IN WITH " + u['username'])
    print("****************************************************************************")
    code, body = funcioLogin(user=u)
    token = json.loads(body)

    for i, function in enumerate(finalList):
        if i != indexofLogin:
            funcio = globals()[function]
            args = inspect.getfullargspec(funcio)
            if "id" in function:
                for i in args[0]:
                    if "id" in i:
                        p = i.replace("_id", "") + "s"
                        params.append(p)
                for p in params:
                    paramP = globals()[param]
                    for p in paramP:
                        print(function)
                        print(u)
                    print(p)
                    print(token['token'])
                    code, body = funcio(token['token'], None, p['id'])
                    print(str(code))
                    print(body)
                    print("-------------------------------------------------------")
            else:
                if (args[0].__len__() == 2) and (args[0][1] == "body"):
                    print(function)
                    print(u)
                    print(token['token'])
                    code, body = funcio(token['token'])
                    print(str(code))
                    print(body)
                    print("-------------------------------------------------------")
                else:
                    param = args[0][1] + "s"
                    params = globals()[param]
                    for p in params:
                        print(function)
                        print(u)
                        print(p)
                        print(token['token'])
                        code, body = funcio(token['token'], p)
                        print(str(code))
                        print(body)
                        print("-------------------------------------------------------")

sys.stdout.close()