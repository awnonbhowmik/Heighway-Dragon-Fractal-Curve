import turtle
turtle.speed(10000)
turtle.hideturtle()
wn=turtle.Screen()
wn.bgcolor("black")
turtle.pencolor("green")
 
def dragoncurve(l,n):
  def x(n):
    if n==0:
      return
    x(n-1)
    turtle.right(90)
    y(n-1)
    turtle.forward(l)
  def y(n):
    if n==0:
      return
    turtle.forward(l)
    x(n-1)
    turtle.left(90)
    y(n-1)
  turtle.fd(l)
  x(n)
dragoncurve(5,15)