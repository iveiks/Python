import turtle

# muutujad
nimi = "Juhan"
vanus = 58
pikkus = 1.80

print(nimi, "," , vanus, "aastat vana ja pikkus on", pikkus, "m")
print(nimi+", "+str(vanus)+" aastat vana ja pikkus on "+str(pikkus)+"m")

# Haapsalu reis
sihtkoht = "Haapsalu"
paevade_arv = 5
oobimise_hind = 100.50
kokku = paevade_arv * oobimise_hind

print(sihtkoht, "reis kestab", paevade_arv, "päeva ja maksab kokku",kokku,"€")


# Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
# Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
# Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)

kylje_pikkus = 100
nurk = 90
kujundi_varv = "red"
x = 110
for j in range(3):  
    for i in range(4):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    x *= 2


turtle.done()