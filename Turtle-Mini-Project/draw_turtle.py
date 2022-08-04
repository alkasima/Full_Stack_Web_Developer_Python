import turtle

def draw_turtle():
    window = turtle.Screen()
    window.bgcolor("red")

    ttl = turtle.Turtle()  

    ttl.forward(120)  
    ttl.left(90)  
    ttl.forward(80)  
    ttl.left(90)  
    ttl.forward(120)  
    ttl.left(90)  
    ttl.forward(80)  
    ttl.left(90)  
    

    window.exitonclick()

draw_turtle()