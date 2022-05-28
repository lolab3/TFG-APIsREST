import json
import webbrowser

from example import *

f = open('website.html','w')

mensaje = """<html>
<head><link rel="stylesheet" type="text/css" href="estilo.css"></head>
<body><table class="detection" id="detection">
  <tr>
    <th>USER</th>
    <th>FUNCTION</th>
    <th>PARAMETERS</th>
    <th>EXPECTED CODE</th>
    <th>RESULT CODE </th>
    <th>CHECK IF BODY CONTAINS</th>
    <th>DOES IT CONTAIN IT?</th>
    <th>RESULT</th>
  </tr> """




with open('data.json') as json_file:
    data = json.load(json_file)

for u in users_detection:
    x = globals()[u]
    for info in data:
        if info["username"] == u:
            for inside in x:
                for par,c in inside.items():
                    for b in c:
                        if par == info['function']:
                            if info["parameters"] == b["parameters"]:
                                if info["code"] == b["response"]:
                                    if "message" in b and "body" in info:
                                        if b["message"] in info["body"]:
                                            mensaje = mensaje + """
                                            <tr>
                                                <td>""" + u + """</td>
                                                <td>""" + info["function"] + """</td>
                                                <td>""" + str(info["parameters"]) + """</td>
                                                <td>""" + b["response"] + """</td>
                                                <td>""" + info["code"] + """</td>
                                                <td>""" + b["message"] + """</td>
                                                <td>True</td>
                                                <td id="green">GOOD</td>
                                            </tr>"""
                                        else:
                                            mensaje = mensaje + """
                                            <tr>
                                                <td>""" + u + """</td>
                                                <td>""" + info["function"] + """</td>
                                                <td>""" + str(info["parameters"]) + """</td>
                                                <td>""" + b["response"] + """</td>
                                                <td>""" + info["code"] + """</td>
                                                <td>""" + b["message"] + """</td>
                                                <td>False</td>
                                                <td id="red">BAD</td>
                                            </tr>"""
                                    else:
                                        mensaje = mensaje + """
                                        <tr>
                                            <td>""" + u + """</td>
                                            <td>""" + info["function"] + """</td>
                                            <td>""" + str(info["parameters"]) + """</td>
                                            <td>""" + b["response"] + """</td>
                                            <td>""" + info["code"] + """</td>
                                            <td>---</td>
                                            <td>---</td>
                                            <td id="green">GOOD</td>
                                        </tr>"""
                                else:
                                    if "message" in b and "body" in info:
                                        if b["message"] in info["body"]:
                                            mensaje = mensaje + """
                                            <tr>
                                                <td>""" + u + """</td>
                                                <td>""" + info["function"] + """</td>
                                                <td>""" + str(info["parameters"]) + """</td>
                                                <td>""" + b["response"] + """</td>
                                                <td>""" + info["code"] + """</td>
                                                <td>""" + b["message"] + """</td>
                                                <td>True</td>
                                                <td id="red">BAD</td>
                                            </tr>"""
                                        else:
                                            mensaje = mensaje + """
                                            <tr>
                                                <td>""" + u + """</td>
                                                <td>""" + info["function"] + """</td>
                                                <td>""" + str(info["parameters"]) + """</td>
                                                <td>""" + b["response"] + """</td>
                                                <td>""" + info["code"] + """</td>
                                                <td>""" + b["message"] + """</td>
                                                <td>False</td>
                                                <td id="red">BAD</td>
                                            </tr>"""
                                    else:
                                        mensaje = mensaje + """
                                        <tr>
                                            <td>""" + u + """</td>
                                            <td>""" + info["function"] + """</td>
                                            <td>""" + str(info["parameters"]) + """</td>
                                            <td>""" + b["response"] + """</td>
                                            <td>""" + info["code"] + """</td>
                                            <td>---</td>
                                            <td>---</td>
                                            <td id="red">BAD</td>
                                        </tr>"""
                                break

mensaje = mensaje + """ </table> </body>
</html> """
f.write(mensaje)
f.close()

webbrowser.open_new_tab('website.html')
