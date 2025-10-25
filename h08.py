# Harjutus 08

# 8.2

tooted = {
'piim': {'kogus': 20, 'hind': 1.19},
'küpsised': {'kogus': 20, 'hind': 4.99},
'või': {'kogus': 20, 'hind': 2.29},
'juust': {'kogus': 15, 'hind': 1.9},
'leib': {'kogus': 15, 'hind': 2.59},
'jogurt': {'kogus': 18, 'hind': 3.65},
'õunad': {'kogus': 35, 'hind': 3.15},
'apelsinid': {'kogus': 40, 'hind': 0.99},
'banaanid': {'kogus': 23, 'hind': 1.29}
}

try:
    toode = input("Mida otsid: ").lower()
    kogus = int(input("Palju tahad: "))

    if toode in tooted.keys():
        if kogus <= tooted[toode]["kogus"] and kogus > 0:
          print("---- ARVE ----")
          summa = kogus * tooted[toode]['hind']
          print(f"{round(summa,2)} eur")
          tooted[toode]["kogus"] -= kogus
          print(tooted)

        else:
          print("Kogust ei ole!")

    else:
       print(f"Toode {toode} ei ole")

    
except:
    print("Ole ikka!")





# 8.1

telefonid={
'Mari': '5957503',
'Toomas': '5719979',
'Kertu': '5201750',
'Siim': '5580027',
'Piret': '5960799',
'Jaan': '5160415',
'Lea': '5760164',
'Mart': '5337951',
'Anni': '5004818',
'Tõnu': '5721873',
'Kai': '5811884',
'Rasmus': '5859489',
'Eva': '5039393',
'Oskar': '5635812',
'Liina': '5696114',
'Peeter': '5560756',
'Sandra': '5257415',
'Heiki': '5207248',
'Kristi': '5703338',
'Urmas': '5400549'
}

print(telefonid['Rasmus'])
telefonid["Mario"] = "5623483"
popitud_asi = telefonid.pop('Kristi')
telefonid["Eva"] = "55555555"
print(telefonid['Eva'])
print(telefonid)
for i in telefonid:
 print(telefonid[i])

nimi = input("Sisesta nimi: ").capitalize()
print(telefonid[nimi])