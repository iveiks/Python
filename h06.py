import turtle
import math

# Kasuta Python Turtles’i, et joonistada stseen, kus redel toetub majale 53° nurga all. Redeli ülemine ots peaks ulatuma 4,4 meetri kõrgusele maja seinal virtuaalses mõõtkavas.
# Muuda nurgad radiaanideks (radian)
# Redeli kaugus seinast: kasuta tangensfunktsiooni (tan) ja antud nurka, et leida, kui kaugele redeli alumine ots on seinast.
# Valem:
# Kaugus=Kõrgus seinaltan⁡(Nurk) 
# Redeli pikkus: kasuta Pythagorase teoreemi, et leida redeli pikkus, kui tead redeli kõrgust seinal ja kaugust seinast. Valem:
# Pikkus=(Kõrgus seinal)2+(Kaugus seinast)2 
# Ümarda vastus 2 komakohta
# Kuva vastused konsoolid

nurk = 53
korgus = 4.4
radiaanid = math.radians(nurk)
kaugus = korgus / math.tan(radiaanid)
#c = math.sqrt(korgus**2 + kaugus**2)
c = math.hypot(korgus,kaugus)

koef = 50
turtle.fd(kaugus*koef)
turtle.lt(90)
turtle.fd(korgus*koef)
turtle.lt(143)
turtle.fd(c*koef)

turtle.done()