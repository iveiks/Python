import turtle
import random

# Iseseisev töö 03
# Kilpkonn
# Kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu.
# Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib
# programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Kõik kujundite joonistamise käsud peavad olema kirjutatud eraldi funktsioonidesse. Näiteks funktsioon
# joonista_ruut() või joonista_viisnurk().
# Pärast joonistamist peab programm pakkuma võimalust sisestada uued väärtused või väljuda programmist,
# jättes sisendi tühjaks.

# Näiteks:
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Soovid jätkata?



# Viisnurga funktsioon
def joonista_viisnurk(arv):
  for i in range(arv):
    turtle.penup()
    turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle.pendown()
    for j in range(5):
      turtle.lt(72)
      turtle.fd(50)
    turtle.penup()

# Ringi funktsioon
def joonista_ring(arv):
  for i in range(arv):
    turtle.penup()
    turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()

# Ruudu funktsioon
def joonista_ruut(arv):
  for i in range(arv):
    turtle.penup()
    turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle.pendown()
    for j in range(4):
      turtle.fd(50)
      turtle.lt(90)
    turtle.penup()

# Suvalise kujundi funktsioon
def joonista_suvaline(arv):

  # Kujude massiiv
  funktsiooni_massiiv = [joonista_viisnurk, joonista_ring, joonista_ruut]

  # Salvestan suvaliselt joonistatud kujud massiivi
  kuju_massiiv = []

  for i in range(arv):
    # Massiivist suvaline joonistamisfunktsioon
    suvaline = random.choice(funktsiooni_massiiv)
    # Siia tekivad siis suvalised joonistamis funktsioonid mis kordamööda joonistavadd suvalised kujud
    kuju_massiiv.append(suvaline(1))
  # Lisab selle ilusa pildi "lõuendile"
  return kuju_massiiv

# Küsib kujundi ja arvu
kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline): ")
arv = int(input("Mitu kujundit soovid joonistada? "))

# Alustab "mängu" loogika
while True:

  # Otsustab mida teha, vastavalt soovitud kujundile
  if kujund == "viisnurk":
    joonista_viisnurk(arv)
    kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline): ")
    # Kui sisend on tühi, sulgeb kilpkonna akna ja väljub while loopist
    if kujund == "":
      turtle.bye()
      break
    # Kui pole tühi, küsib kujundite arvu ning seejärel algab while loop algusest, niikaua kuni kujundi sisend jäetakse tühjaks
    # Sama jutt järgmiste if'de kohta, ei hakka sama juttu dubleerima 
    else:
      arv = int(input("Mitu kujundit soovid joonistada? "))
      continue
  elif kujund == "ring":
    joonista_ring(arv)
    kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline): ")
    if kujund == "":
      turtle.bye()
      break   
    else:
      arv = int(input("Mitu kujundit soovid joonistada? "))
      continue
  elif kujund == "ruut":
    joonista_ruut(arv)
    kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline): ")
    if kujund == "":
      turtle.bye()
      break   
    else:
      arv = int(input("Mitu kujundit soovid joonistada? "))
      continue
  elif kujund == "suvaline":
    joonista_suvaline(arv)
    kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline): ")
    if kujund == "":
      turtle.bye()
      break   
    else:
      arv = int(input("Mitu kujundit soovid joonistada? "))
      continue

