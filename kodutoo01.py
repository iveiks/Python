# 1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# kood mis teavitab paaris või paaritust arvust - 1p
# kuvatakse programmi pealkiri - 1p
# kood kommenteeritud - 1p

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
# 3. Täringud
# kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# kasutaja võistleb kahe täringuga arvuti vastu - 1p
# kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# kood kommenteeritud - 1p
# 4. Emaili kontroll
# kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
# programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’ - 1p
# kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
# kood kommenteeritud - 1p
# 5. Kaugushüpe
# kasutaja sisestab 3 kaugushüppe tulemust - 1p
# sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
# programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
# kood kommenteeritud - 1p
# 6. Salakeel
# sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
# kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
# kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
# kood kommenteeritud - 1p