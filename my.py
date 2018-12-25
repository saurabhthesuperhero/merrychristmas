import turtle

screen=turtle.Screen()
screen.setup(1000,600)


x=[0,-30,0,30,-60,-30,0,30,60,-60,-30,0,30,60,-90,-60,-30,0,30,60,90,-120,-90,-60,-30,0,30,60,90,120,-150,-120,-90,-60,-30,0,30,60,90,120,150,]
#-90,-60,-30,0,30,60,90,-120,-90,-60,-30,0,30,60,90,120
y=[270,240,240,240,210,210,210,210,210,170,170,170,170,170,140,140,140,140,140,140,140,110,110,110,110,110,110,110,110,110,]
#50,50,50,50,50,50,50,20,20,20,20,20,20,20,20,20

square=turtle.Turtle()
circle=turtle.Turtle()
square.shape("square")
circle.shape("circle")
square.color("green")
circle.color("yellow")
circle.up()
square.up()
square.speed("fast")
circle.speed("fastest")
for i,j  in zip(x,y):
	square.goto(i,j)
	square.stamp()

square.goto(0,0)
x=[-60,-30,0,30,60,-90,-60,-30,0,30,60,90,-120,-90,-60,-30,0,30,60,90,120,-150,-120,-90,-60,-30,0,30,60,90,120,150]
y=[80,80,80,80,80,50,50,50,50,50,50,50,20,20,20,20,20,20,20,20,20,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10]
for i,j  in zip(x,y):
	square.goto(i,j)
	square.stamp()

square.color("brown")
x=[-30,0,30,-30,0,30,-30,0,30]
y=[-40,-40,-40,-80,-80,-80,-110,-110,-110]

for i,j  in zip(x,y):
	square.goto(i,j)
	square.stamp()


circle.goto(0,280)
circle.stamp()
x=[-90,90,-110,110,-140,140,-90,90,-110,110,-140,140,-170,170,-200,200]
y=[170,170,140,140,110,110,90,90,60,60,30,30,0,0]
for i,j  in zip(x,y):
	circle.goto(i,j)
	circle.stamp()

turtle.up()
turtle.goto(-250,-160)
turtle.down()
turtle.color("RED")
turtle.write("Merry Christmas 2018",font=("Comic Sans MS", 28, "bold"))
turtle.up()
turtle.goto(-220,-190)
turtle.down()
turtle.color("RED")
turtle.write("By Saurabh Jadhav",font=("Comic Sans MS", 28, "bold"))
turtle.up()

screen.bgpic("Ohhappiness.jpg")



turtle.exitonclick()

