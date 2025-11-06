# Harjutus 10

# 1 Arvude keskmine
# Koostage Pythoni programm, mis küsib kasutajalt arve ükshaaval.
# Programm peaks jätkama arvude küsimist ja nende vastuvõtmist seni,
# kuni kasutaja jätab sisestuse tühjaks (st vajutab sisestusklahvi ilma midagi kirjutamata).
# Programm peab kasutama while-tsüklit arvude küsimiseks ja nende salvestamiseks.
# Pärast seda, kui kasutaja lõpetab arvude sisestamise peab programm arvutama ja väljastama kõikide sisestatud arvude keskmise väärtuse.

loop = 1
counter = 0
sum = 0

while loop:
    arv = input("Lisa arv: ")
    if arv == "":
        break
    counter += 1
    sum += int(arv)

print(f"Keskmine: {sum/counter}")

