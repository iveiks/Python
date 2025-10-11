import random
# Matemaatika test (randint)

# Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
# Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”. Kasutaja peab sisestama vastuse.
# Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”, kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
# Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.

arv1 = random.randint(1,10)
arv2 = random.randint(1,10)
tehe = arv1 * arv2
vastus = int(input(f"{arv1} x {arv2} = "))
if vastus == tehe :
    print("Õige vastus!")
else :
    print("Vale vastus!")




# Vanusepiiranguga üritus

# Sa oled loomas programmi, mis aitab kontrollida, kas inimesed vastavad vanusepiirangu nõuetele üritusel osalemiseks.
# Programm palub kasutajal sisestada oma vanuse.
# Kui vanus on vähemalt 18 aastat, siis programm annab teada, et kasutaja võib üritusele siseneda.
# Kui vanus on alla 18, siis programm teatab, et üritusele sisenemiseks ei ole piisavalt vana.
# Kasuta if ja else lauseid, et luua see vanusekontrolli programm.

vanus = int(input("Vanus: "))

if vanus >= 18 :
    print("Võid siseneda")
else :
    print("Ei ole piisavalt vana")
    
    
    
