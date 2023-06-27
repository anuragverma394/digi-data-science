from turtle import*
speed('fastest')
size =10
angle =60 
colors=['red','purple','blue']

while True:
    pencolor(colors[size%2])
    fd(size)
    lt(angle)
    size +=1
    