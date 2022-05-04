import inspect
import re
import json
#import OpenApi as OpenApi

from ApiClientMethods import *
from sampleData import *

from itertools import combinations

Functions = []
allFunctions = []
listofDelete = []
finalList = []
allUsers = []

data = {"functions": []}
data_holder = data["functions"]


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
    code, body = funcioLogin(user=u)
    token = json.loads(body)

    for i, function in enumerate(finalList):
        if i != indexofLogin:
            params = []
            diffpam2 = []
            final = []
            combor = []
            funcio = globals()[function]
            args = inspect.getfullargspec(funcio)
            total_args_id = args[0].__len__() - 2
            if "id" in function:
                for i in args[0]:
                    if "id" in i:
                        p = i.replace("_id", "") + "s"
                        params.append(p)
                for i, x in enumerate(params):
                    y = globals()[x]
                    for h in y:
                        diffpam2.append(h['id'])

                for combo in combinations(diffpam2, total_args_id):
                    combor = []
                    for x in combo:
                        combor.append(''.join([i for i in x if not i.isdigit()]))
                    if len(combor) == len(set(combor)):
                        code, body = funcio(token['token'], None, *combo)
                        data_holder.append({'function': function,
                                            'username': u['username'],
                                            'parameters': combo,
                                            'token': token['token'],
                                            'code': str(code),
                                            'body': body})
            else:
                if (args[0].__len__() == 2) and (args[0][1] == "body"):
                    code, body = funcio(token['token'])
                    data_holder.append({'function': function,
                                        'username': u['username'],
                                        'parameters': None,
                                        'token': token['token'],
                                        'code': str(code),
                                        'body': body})
                else:
                    param = args[0][1] + "s"
                    params = globals()[param]
                    for p in params:
                        code, body = funcio(token['token'], p)
                        data_holder.append({'function': function,
                                            'username': u['username'],
                                            'parameters': p['id'],
                                            'token': token['token'],
                                            'code': str(code),
                                            'body': body})

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data_holder, f, ensure_ascii=False, indent=4)