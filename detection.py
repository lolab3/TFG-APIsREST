import json

from example import *

with open('data.json') as json_file:
    data = json.load(json_file)

for info in data:
    for func in user1:
        for inside in func:
            # for parameters --> print(func[inside][0]["parameters"])
            if inside == info['function']:
                print("Function " + info["function"] + " with parameters " + str(info["parameters"]))
                if info["code"] == func[inside][1]["response"]:
                    print("The function has ended successfully")
                else: print("The function has an error")
                break

