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