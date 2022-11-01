import turtle

def coreFill():
    owl_core = turtle.Turtle()
    owl_core.shape("turtle")
    owl_core.color('yellow', 'black') # Изменяем цвет линии и цвет заливки
    owl_core.begin_fill()
    owl_core.pensize(3) #Изменяем толщину линии
    owl_core.left(90)
    owl_core.forward(100)
    owl_core.left(45)
    owl_core.circle(140, 90)
    owl_core.left(45)
    owl_core.forward(180)
    owl_core.circle(198, 90)
    owl_core.left(90)
    owl_core.forward(290)
    owl_core.end_fill()
    owl_core.hideturtle()

def maskFill():
    owl_mask = turtle.Turtle()
    owl_mask.shape("turtle")
    owl_mask.pensize(3) #Изменяем толщину линии
    owl_mask.setpos(-20, 0)
    owl_mask.color('yellow', 'white') # Изменяем цвет линии и цвет заливки
    owl_mask.begin_fill()
    owl_mask.left(90)
    owl_mask.forward(90)

    angle = 90
    for i in range(2):
        owl_mask.left(angle * (i + 1))
        owl_mask.circle(80, 90)

    owl_mask.left(90)
    owl_mask.forward(90)
    owl_mask.left(45)
    owl_mask.circle(113, 90)
    owl_mask.end_fill()
    owl_mask.hideturtle()

def owlEyes():
    owl_eyes = turtle.Turtle()
    owl_eyes.shape("turtle")
    owl_eyes.pensize(3) #Изменяем толщину линии

    eyes_x = [-55, -145]

    for i in range(2):
        owl_eyes.pencolor("")  # Изменяем цвет линии
        owl_eyes.setpos(eyes_x[i], 35)
        owl_eyes.pencolor("cyan") # Изменяем цвет линии
        owl_eyes.dot(35)

    owl_eyes.hideturtle()

def owlWing():
    owl_wing = turtle.Turtle()
    owl_wing.shape("turtle")
    owl_wing.pensize(3) #Изменяем толщину линии

    def wingCore():
        owl_wing.pencolor("")  # Изменяем цвет линии
        owl_wing.setpos(50, -20)
        owl_wing.color('yellow', 'black') # Изменяем цвет линии и цвет заливки
        owl_wing.begin_fill()
        owl_wing.left(180)
        owl_wing.circle(110, 270)
        owl_wing.forward(110)
        owl_wing.left(90)
        owl_wing.forward(110)
        owl_wing.end_fill()

    def wingCircle():
        owl_wing.pencolor("")  # Изменяем цвет линии
        owl_wing.setpos(50, -80)
        owl_wing.color('yellow', 'violet') # Изменяем цвет линии и цвет заливки
        owl_wing.begin_fill()
        owl_wing.circle(50)
        owl_wing.end_fill()

    def wingLines():
        owl_wing.pencolor("")  # Изменяем цвет линии
        owl_wing.setpos(50, -100)
        owl_wing.pensize(7) #Изменяем толщину линии

        owl_wing.pencolor("palegreen")  # Изменяем цвет линии
        owl_wing.circle(30, 80)

        owl_lines = [[30, 20, 50], [40, 90, 30]]

        for i in range(3):
            not_fill_line = owl_lines[0]
            fill_line = owl_lines[1]
            owl_wing.pencolor("")  # Изменяем цвет линии
            owl_wing.circle(30, not_fill_line[i])
            owl_wing.pencolor("palegreen")  # Изменяем цвет линии
            owl_wing.circle(30, fill_line[i])

    wingCore()
    wingCircle()
    wingLines()
    owl_wing.hideturtle()

def cheese():
    cheese = turtle.Turtle()
    cheese.shape("turtle")
    cheese.pencolor("")
    cheese.setpos(-300, -120)
    cheese.color('goldenrod', 'goldenrod') # Изменяем цвет линии и цвет заливки

    cheese.begin_fill()

    cheese_right = [90, 105, 75]
    cheese_forward = [100, 300, 100]
    for i in range(3):
        cheese.right(cheese_right[i])
        cheese.forward(cheese_forward[i])

    cheese.end_fill()

    cheese.color('gold', 'gold') # Изменяем цвет линии и цвет заливки

    cheese.begin_fill()
    cheese.right(105)
    cheese.forward(300)
    cheese.left(165)
    cheese.forward(250)
    cheese.left(18)
    cheese.circle(62, 90)
    cheese.end_fill()

    cheese_position = [[-550, -360, -410, -300], [-115, -140, -150, -160]]
    cheese_dot = [45, 30, 38, 42]
    cheese_color = ["gold", "white"]
    for i in range(4):
        cheese_position_x = cheese_position[0]
        cheese_position_y = cheese_position[1]
        cheese.pencolor("")
        cheese.setpos(cheese_position_x[i], cheese_position_y[i])
        if i < 3:
            cheese.pencolor(cheese_color[0]) # Изменяем цвет линии
        else: 
            cheese.pencolor(cheese_color[1]) # Изменяем цвет линии
        cheese.dot(cheese_dot[i])

    cheese.hideturtle()


coreFill()
maskFill()
owlEyes()
owlWing()
cheese()

turtle.exitonclick()