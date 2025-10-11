# Loo lugudest loend (koos numbrite ja jutumärkidega)
# 1. ALIKA – “Bridges”
# 2. Anett x Fredi – “Read Between The Lines”
# 3. villemdrillem – “leekiv armastus”
# 4. Clicherik & Mäx – “PAKSUD”
# 5. nublu – “ära ärata”
# 6. NOËP – “Move Your Feet”
# 7. Trad.Attack! – “Bring It On”
# 8. Bedwetters – “It Is What It Is”
# 9. Reket – “Panama paberid”
# 10. Grete Paia – “Võluväel”
# Kuva kasutajale kõik lood massiivist
# Küsi millist lugu ta “kuulata” soovib
# Kuva kasutaja valitud lugu

laulud = ['1. ALIKA – "Bridges"','2. Anett x Fredi – "Read Between The Lines"','3. villemdrillem – "leekiv armastus"','4. Clicherik & Mäx – "PAKSUD"','5. nublu – "ära ärata"','6. NOËP – "Move Your Feet"','7. Trad.Attack! – "Bring It On"','8. Bedwetters – "It Is What It Is"','9. Reket – "Panama paberid"','10. Grete Paia – "Võluväel"']

print(20*"-","KÕIK LOOD",20*"-")
for i in laulud:
    print(i)
    
valik = int(input("Millist laulu soovid kuulata? ")) - 1

print(laulud[valik])