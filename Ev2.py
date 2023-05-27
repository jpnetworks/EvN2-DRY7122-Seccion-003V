import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "f6Mz7x0zt8Tcqm4NAEC0pHk0Z9aCnlQE"

while True:
    orig = input("Ubicacion Inicial: ")
    if orig == "z":
        break
    dest = input("Destino: ")
    if dest == "z":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print ("URL: " + (url))
    json_data = requests.get (url) .json()
    json_status = json_data ["info"] ["statuscode"]
    if json_status == 0:
        print ("Hola, estimado usuario.")
        print ("Estado de API: " + str(json_status) + " = Route Call exitoso.\n")
        print ("=============================================")
        print ("Direcciones de  " + (orig) + " to " + (dest))
        print ("Duracion viaje    " + (json_data["route"] ["formattedTime"]))
        print ("Distancia            " + str(json_data["route"] ["distance"]))
        print ("=============================================")