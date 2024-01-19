import turtle as t
t.speed(1)
t.bgcolor("sky blue")

def draw_circle(color,radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
def draw_eye(color,radius,x,y):
    draw_circle("white",radius,x,y)
    draw_circle(color,radius/2 , x, y)

draw_circle("grey",40,0 ,-40)

draw_eye("black", 8, -10, 0)
draw_eye("black", 8, 10, 0)

draw_circle("pink", 5, 0, -10)

t.penup()
t.goto(0,-10)
t.pendown()
t.right(80)
t.circle(12,180)
t.penup()
t.goto(0,0)

t.goto(0,-10)
t.pendown()
t.left(-80)
t.circle(-12,180)

t.hideturtle()

t.exitonclick()





    
    