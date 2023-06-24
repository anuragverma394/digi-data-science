from turtle import*

speed('slowest')
distance =100
sides =6
for i in range(sides):
    fd(distance)
    rt(360/sides)
    circle(distance/2)
    for i in range(sides):
        fd(distance/2)
        rt(360/sides)
        dot(10)
        write(i)
hideturtle()
mainloop()