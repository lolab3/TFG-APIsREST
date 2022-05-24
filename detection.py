import json

from example import *

with open('data.json') as json_file:
    data = json.load(json_file)

for u in users:
    x = globals()[u]
    for info in data:
        if info["username"] == u:
            for inside in x:
                for par,c in inside.items():
                    for b in c:
                        if par == info['function']:
                            if info["parameters"] == b["parameters"]:
                                if info["code"] == b["response"]:
                                    print("Entering with " + u + ": the function " + info["function"] + " with parameters " + str(info["parameters"]) + " has the correct code: " + b["response"] + ".")
                                else: print("Entering with " + u + ": the function " + info["function"] + " with parameters " + str(info["parameters"]) + " has the code " + info["code"] + " and it had to be a " + b["response"] + ".")
                                break