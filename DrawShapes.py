import turtle
import math
import os


def main() :
 print("Welcome to Draw Shapes!!!Here we will draw your favorite Shapes ")
 choice=input("Press 1.Circle"+os.linesep+"2.Square "+os.linesep+"3.Triangle ")   
 ttl=turtle.Turtle()
 ttl.color("Blue")   
 switch_shapes(choice, ttl)
 turtle.exitonclick()


def draw_circle(t, r):
    window = t.screen
    window.bgcolor("pink") #
    t.circle(r)
    window.exitonclick()


def draw_triangle(t,s):
    window = t.screen
    window.bgcolor("pink") #background color
    t.forward(s) 
    t.left(120)
    t.forward(s)
    t.left(120)
    t.forward(s)
    window.exitonclick()
        
def draw_square(t,w):
    window = t.screen
    window.bgcolor("pink") 
    for side in range(4):
        t.forward(w)
        t.left(90)
        
    window.exitonclick()    
         
def switch_shapes(argument,ttl):
    switcher = {
        "1" : draw_circle,
        "2" : draw_square,
        "3" : draw_triangle
        }   
    return switcher.get(argument)(ttl,140)
        
if __name__ == '__main__':
    main()


