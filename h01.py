import turtle

#tõstab pliiatsi üles, viib akna nurka ja paneb maha
turtle.penup()
turtle.goto(-400,200)
turtle.pendown()

# kolmnurk
for i in range (3):
    turtle.fd(200)
    turtle.left(120)
    
turtle.penup()
turtle.goto(-100,200)
turtle.pendown()

# ruut
for i in range (4):
    turtle.fd(150)
    turtle.left(90)
    
turtle.penup()
turtle.goto(250,200)
turtle.pendown()

# V
turtle.fd(25)
turtle.left(70)
turtle.fd(200)
turtle.left(110)
turtle.fd(50)
turtle.left(70)
turtle.fd(150)
turtle.right(140)
turtle.fd(150)
turtle.left(70)
turtle.fd(50)
turtle.left(110)
turtle.fd(200)
turtle.left(70)
turtle.fd(50)

turtle.penup()
turtle.fd(100)


turtle.done()