# TFG: Automatització del procés de penetration testing sobre les APIs REST
### Lola Barberan Baeta (NIU: 1532874)

## Resum
Una API de REST és el conjunt de definicions i protocols que es fan servir per a dissenyar i integrar el programari de les aplicacions, seguint les regles d'arquitectura específiques de REST. Aquest projecte se centrarà en el descobriment de vulnerabilitats explotables a aquest tipus d'APIs, concretament en les d'escalada de privilegis horitzontals, on l’usuari maliciós manté els privilegis que ja tenia, però aconsegueix tenir accés a dades i funcionalitats que no haurien d’estar disponibles per a aquest, i verticals, on l’usuari té pocs privilegis i passa a tenir més. Si es volgués realitzar aquest procés de forma manual a una API amb molt contingut, seria una pèrdua de temps molt costosa. Per tant, l'objectiu d'aquest TFG és el d'obtenir una eina que permeti la detecció automàtica de les vulnerabilitats d'escalada de privilegis horitzontals i verticals a qualsevol mena d'API de REST. 

## Requeriments
El codi conté els següents requeriments:

- L'eina ha de detectar totes les funcions que criden a l'API.
- L'eina identifica el mètode de login de l’API.
- L'eina ha de provar cadascun dels mètodes HTTP a tots els endpoints de l’API.
- L'eina ha de cridar cada un dels mètodes de l’API havent-se autenticat amb cadascun dels usuaris proporcionats.
- L'eina ha de guardar totes les respostes de l'API.
- L'eina ha d'analitzar els registres a la recerca d'errors de seguretat.
- L'eina ha de mostrar en quins casos el resultat no és l'esperat.

## Estructuració del codi
El programari es dividirà en 3 parts (tres arxius amb diferents propòsits), com es pot veure a la figura següent. I, pot ser cridat des d'un script, anomenat “main.py”, que crida a cadascun dels scripts mostrats: 


- **methodsGenerator.py**: crea les diferents funcions necessàries per a accedir a tots els endpoints d'una API de REST.
- **scanAPI.py**: crida a totes aquestes funcions esmentades anteriorment.
- **detection.py**: compara el resultat obtingut amb l'esperat.

Aquests scripts estan explicats amb més detall a les següents subseccions.

## Generador de Mètodes

Partim d'una base, un codi proporcionat per l'empresa Werfen i que a continuació, s'ampliarà. Aquest, té com a entrada el fitxer “openapi.json”, en format Open API i defineix els diferents enllaços endpoint de l'API, els codis de resposta que pot tenir, els textos de resposta i el tipus de variables existents, entre d'altres. I, genera automàticament l'script “ApiClientMethods.py”, en Python. Que conté totes les funcions necessàries, amb els diferents endpoints possibles per a accedir i rebre resposta per part de qualsevol API de REST.
 
L'enllaç per a accedir al codi és el següent: https://github.com/CarlesMaG/OpenApiSimpleClientGen.

## Escàner de les funcions de l'API
La segona part del programa, és l'anomenada “scanAPI.py”, que té com a input l'arxiu “ApiClientMethods.py”, generat amb el codi anterior i l'script "scanApiData.py", també en Python amb la sintaxi de JavaScript Object Notation (JSON), que mostra un llistat de tots els usuaris que poden accedir a l’aplicació, amb els seus passwords vàlids per a interactuar amb l’API i un llistat de paràmetres per a cridar a tots els endpoints de l’API. 

A la primera part del codi, es busquen totes les funcions del document “apiClienMethods.py”. Més tard, es troba automàticament la funció Login i, si no la troba, pregunta per quina és. A més, guarda tots els users en un array per a després fer un loop per a cada un d'ells. Per a cadascun d'aquests users, es fa un altre loop de totes les funcions menys la de login, que se separen segons si inclouen un (o més) “id” al nom de la funció o no, ja que si l'inclouen és necessari afegir un o més dels paràmetres guardats a l'arxiu "scanApiData.py". En aquesta part, s'analitza quins paràmetres necessita la funció i totes les seves possibilitats (per exemple, pot necessitar informació dels hospitals i departaments de cadascun d'aquests) i les envia, junt amb el token, a la crida de l'endpoint específic (a l'exemple anterior podria enviar l'hospital 1 amb els departaments 1 i 2 i l'hospital 2 amb els departaments 1 i 2) i es guarda la resposta rebuda. Per a les altres funcions, que no contenen “id” al nom,  hi ha dues opcions, que no es necessitin enviar paràmetres a part del token, i que s'hagin d'enviar el token i un paràmetre, que conté el nom específic a l'argument de la funció. Per a aquestes dues crides a funcions, també es guarden les respostes, que posteriorment es guardaran a l'arxiu explicat a continuació.

Aquest codi genera l'arxiu “data.json”, que conté el codi de resposta de cadascuna de les crides de l'API amb la combinació dels diferents usuaris i tots els possibles paràmetres definits, en format JSON. En aquest script es guarden les següents dades:

- Nom de la funció.
- Username utilitzat per a iniciar sessió.
- Paràmetres introduïts.
- Token utilitzat.
- Codi HTTP de retorn de cada petició. 
- Text de resposta rebut de la petició.

## Detector de vulnerabilitats
L'última part del codi, consta de comparar l'arxiu fet en Python amb format JSON, “detectionData.py”, que conté els diferents resultats desitjats de la crida a les diferents funcions de l'API que volen ser comprovades, amb el fitxer “data.json” generat anteriorment, comprovant per a cada funció amb els paràmetres concrets introduïts, si el codi de resposta és l'esperat i/o si el missatge de resposta generat conté una paraula o frase que s'esperava obtenir com a resultat. Tot generant una pàgina final anomenada “website.html” en “HyperText Markup Language” (HTML), que mostra si el resultat és l'esperat o si, pel contrari, hi ha hagut algun error, que podria ser una vulnerabilitat de l'API escanejada i causar una bretxa de la seguretat de la informació.

Ara, s'explicarà el codi pas per pas. Primerament, es guarden les dades de l'arxiu “data.json” i les que guarden el resultat desitjat. A continuació, es fa un loop perquè cadascuna d'aquestes respostes es comparin entre elles. I, quan es troben les funcions iguals entre els dos arxius, assegurant-se que són les mateixes perquè s'anomenen igual i tenen els mateixos paràmetres, es compara si el codi de resposta és el mateix (que llavors, coincidiria el resultat desitjat amb el real) i, si s'específica, es detecta si el missatge de resposta conté una paraula o frase indicada a l'arxiu “detectionData.py”. El resultat de cadascuna de les funcions, com s'ha dit abans, es guarda a l'arxiu “website.html” i s'obre una finestra del navegador web mostrant l'HTML resultant.

## Resultats

En finalitzar el codi sencer, podem veure com cadascuna de les funcions ha acabat amb un resultat correcte o no, comprovant que realment ha accedit l’usuari que havia de fer-ho o no. El resultat final en HTML, mostra una taula dividida en:

- **User**: defineix l'usuari que s'ha utilitzat en cada cas per a cridar a la funció corresponent.
- **Function**: especifica la funció analitzada en cada cas.
- **Parameters**: nomena els paràmetres que s'han introduït en cada crida a una funció.
- **Expected code**: anomena el codi que s'esperava obtenir com a resultat [17].
- **Result Code**: dona el codi resultant del script.
- **Check if body contains**: mostra la paraula o frase que s'ha volgut buscar al text resultant.
- **Does the body contain it?**: mostra una resposta de “True” o “False” segons si s'ha trobat la paraula o frase anterior al text.
- **Result**: comprovant si compleix els dos casos de manera positiva, dona un resultat de “GOOD”, en verd o de “BAD”, en vermell.
