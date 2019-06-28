import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"] 

turtle.width(10) 

length = 14

turtle.speed(0)

for count in range(1000):
  color = random.choice(colors) 
  turtle.forward(length)
  turtle.right(156)
  turtle.color(color) 
  length = length + 4
