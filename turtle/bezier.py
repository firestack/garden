#!python3
# 2013-Jan-21 Mon 07:15
import turtle, random, time

def turtle_cubic_bezier(p0,p1,p2,p3, n=1000*50):

    x0, y0 = p0[0], p0[1]
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    turtle.penup()
    turtle.goto(x0,y0)
    turtle.pendown()
    for i in range(n+1):
        t = i / n
        a = (1. - t)**3
        b = 3. * t * (1. - t)**2
        c = 3.0 * t**2 * (1.0 - t)
        d = t**3
 
        x = int(a * x0 + b * x1 + c * x2 + d * x3)
        y = int(a * y0 + b * y1 + c * y2 + d * y3)
        turtle.goto(x,y)
    turtle.goto(x3,y3)

def r01(): return random.random()
def r(): return int(r01()*200-100)
def rr(): return(r(),r())
def rmid(x1,x2): return int(x1+x2+r()/2)/2

def add_point(x, y):
    try:
        add_point.new_points.append([x,y])
    except AttributeError:
        add_point.new_points = [[x,y]]
    print(add_point.new_points)
    print("Mouse click")
    if len(add_point.new_points) >= 4:
        turtle_cubic_bezier(*add_point.new_points)
        add_point.new_points = []

def clearScreen(x ,y):
    print("please clear")
    turtle.getscreen().clear()




def random_color():
    def t(i): return time.clock() * i % 1
    rbg =  [t(1), t(3), t(5)]
    print("rbg=(%3.2f,%3.2f,%3.2f)" % (rbg[0],rbg[1],rbg[2]))
    turtle.color(*rbg)

def main():
    #turtle.ht()

    turtle.speed(0)
    turtle.delay(0)
    turtle.colormode(1.)

    turtle.onscreenclick(add_point)
    turtle.onscreenclick(clearScreen, btn=2)
    turtle.done()

 
   
if __name__ == "__main__":
    main() 