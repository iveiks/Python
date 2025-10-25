# Kasutatakse 3. ülesande jaoks
import random

# 1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# kood mis teavitab paaris või paaritust arvust - 1p
# kuvatakse programmi pealkiri - 1p
# kood kommenteeritud - 1p

# Programmi pealkiri
print(20*"-","Paaris | Paaritu",20*"-")
try:
  # Kasutaja sisestab arvu
  arv = int(input("Sisesta arv: "))

# Juhuks kui kasutaja sisestas midagi muud kui numbri
except:
  print("Sisesta arv!")

else:

  # Arvutab jäägi. Paaris arvu jääk on 0
  vastus = arv % 2

  # Kuna "vastus" muutujat enam vaja ei lähe siis kasutan seda kokkuhoiu ja lihtsuse huvides ära ning
  # salvestan vastuse sinna.
  if vastus == 0:
    vastus = "paaris"
  else:
    vastus = "paaritu"

  # Prindin konsooli vastuse.
  if arv == 0:
    print("Null pole number!")
  else:
    print(f"Sinu sisestatud arv on {vastus}.")


# 2. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# küsitakse valuuta kogust ja tehakse arvutused - 2p
# kood kommenteeritud - 1p

# Euro kurss
kurss = 15.6466

# Programmi pealkiri
print(20*"-","EUROKALKULAATOR",20*"-")

# Valikuvariandid
print("Tee valik:")
print("1. EUR->EEK")
print("2. EEK->EUR")


valik = int(input("Sinu valik (1/2): "))
if valik == 1:
  print("EUR->EEK")
elif valik == 2:
  print("EEK->EUR")
# Ütleb kui valid valesti
elif valik < 1 or valik > 2:
  print("Oled teinud kummalise valiku!")

# Küsib raha kogust
summa = float(input("Raha kogus: "))

# Teeb arvutused
if valik == 1:
  loppSumma = summa * kurss
  valuuta = "EEK"
elif valik == 2:
  loppSumma = summa / kurss
  valuuta = "€"

# Prindib ilusa vastuse
print(f"{loppSumma:0.2f} {valuuta}")



# 3. Täringud
# kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# kasutaja võistleb kahe täringuga arvuti vastu - 1p
# kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# kood kommenteeritud - 1p

# Programmi pealkiri ja mängu seletus
print(20*"-","TÄRINGUMÄNG",20*"-")
print("Veeretad kahte täringut, seega võimalik veeretada 2 - 12.")
print("Tee oma panus vastavalt!")

try:
  # Veeretab kasutajale ja arvutile suvalised numbrid kahe täringuga, ehk siis 2 - 12
  kasutaja = random.randint(2,12)
  arvuti = random.randint(2,12)

  # Ütleb kasutajale mis ta veeretas ning küsib mis summa peale ta mängida tahab ja korrutab selle kahega (arvuti panus kah otsa,
  # oletame et ta "callib")
  print(f"Sinu täringud teevad kokku {kasutaja}")
  pot = int(input("Tee oma panus: ")) * 2

  # Kui kasutaja veeretas suurema summa, siis ta võitis
  if kasutaja > arvuti:
    print(f"Arvuti veeretas {arvuti}. Sina võitsid. Saad {pot}€")
  # Kui arvuti veeretas suurema summa, siis tema võitis
  elif kasutaja < arvuti:
    print(f"Arvuti veeretas {arvuti}, sina kaotasid. Jäid rahast ilma.")
  # Kui ei ole üks ega teine suurem, on nad järelikult samad = tekkis viik ja soovitatakse uut mängu
  else:
    print("Viik. Uued panused ja uus mäng!")

# Kui peaks mingi error olema, tuleb errori asemel ilus kiri (hetkel ei näe mis errori põhjustas)
except:
  print("Pekki läks")



# 4. Emaili kontroll
# kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
# programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’ - 1p
# kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
# kood kommenteeritud - 1p

# Küsib kasutajalt emaili
email = input('Sisesta email kujul "enimi.pnimi@server.com": ')

# Kontrollib @ olemasolu
at = email.find("@")

# Kui leitakse @, tehakse järgmised toimingud
if at != -1:
  # @ asendatakse punktiga ning seejärel tükeldatakse kogu joru punktide koha pealt 'nimekiri' arraysse
  nimekiri = email.replace("@", ".").split(".")

  # Arusaadavuse nimel teen eraldi muutujad nimede jne jaoks, kuigi sellise väikse asja jaoks
  # võiks konsooli printimisel asjad ka otse arrayst võtta.
  enimi = nimekiri[0].capitalize()
  pnimi = nimekiri[1].capitalize()
  server = nimekiri[2]
  domeen = nimekiri[3]

  # Prindin ilusa vastuse
  print(f"Tere {enimi}, sinu email on {server} serveris ja domeeniks on sul {domeen}")

# Kui .find() tulemus on -1, ei leitud kasutaja sisestatud emailist @ märki
# ning tal palutakse sisestada korrektne email
elif at == -1:
  print("Sisesta korrektne email!")



# 5. Kaugushüpe
# kasutaja sisestab 3 kaugushüppe tulemust - 1p
# sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
# programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
# kood kommenteeritud - 1p

# Loob "tulemused" array
tulemused = []

# Küsib järjest kolm tulemust ning lisab need enne loodud arraysse
tulemused.append(float(input("Sisesta esimese kaugushüppe tulemus: ")))
tulemused.append(float(input("Sisesta teise kaugushüppe tulemus: ")))
tulemused.append(float(input("Sisesta kolmanda kaugushüppe tulemus: ")))

# Teeb muutujad parima ning keskmisele tulemusele ning vastavad tehted nendele
parim = max(tulemused)
keskmine = sum(tulemused) / len(tulemused)

# Prindib jällegi ilusa tulemuse
print(f"parim: {parim:0.2f}m")
print(f"keskmine: {keskmine:0.2f}m")



# 6. Salakeel
# sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
# kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
# kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
# kood kommenteeritud - 1p