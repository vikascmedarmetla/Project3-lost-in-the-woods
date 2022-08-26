
import turtle

from tkinter import *
from tkinter import messagebox

import random

random.seed()

wn = turtle. Screen() 
wn.title("Lost in the woods")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 5
score_b = 5
score_c = 5
score_d = 5



#player 1
paddle_a = turtle. Turtle() 
paddle_a.speed(0) 
paddle_a.shape("square") 
paddle_a.color("black") 
paddle_a.shapesize(stretch_wid=1, stretch_len=1)
paddle_a.penup() 
paddle_a.goto(-370, 260)
paddle_a.dx=0
paddle_a.dy=0


#player 2
paddle_b = turtle. Turtle() 
paddle_b.speed(0) 
paddle_b.shape("square") 
paddle_b.color("black") 
paddle_b.shapesize(stretch_wid=1, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(370, -260)
paddle_b.dx=0
paddle_b.dy=0


#player 3
paddle_c = turtle. Turtle() 
paddle_c.speed(0) 
paddle_c.shape("square") 
paddle_c.color("black") 
paddle_c.shapesize(stretch_wid=1, stretch_len=1)
paddle_c.penup() 
paddle_c.goto(370, 260)
paddle_c.dx=0
paddle_c.dy=0


#player 4
paddle_d = turtle. Turtle() 
paddle_d.speed(0) 
paddle_d.shape("square") 
paddle_d.color("black") 
paddle_d.shapesize(stretch_wid=1, stretch_len=1)
paddle_d.penup() 
paddle_d.goto(-370, -260)
paddle_d.dx=0
paddle_d.dy=0



#------------------------------------------------------------------------------------------------

# Pen 
pen = turtle. Turtle() 
pen.speed (0) 
pen.color("white") 
pen.penup() 
pen.hideturtle() 
pen.goto(0, 260) 
pen.write("Player A: 5 Player B: 5 Player C: 5 Player D: 5 ", align="center", font=("Courier", 24, "normal"))

# Function 
#paddle a move
def paddle_a_up ():
	y = paddle_a.ycor() 
	y += 20
	paddle_a.sety(y)


def paddle_a_down ():
	y = paddle_a.ycor() 
	y -= 20 
	paddle_a.sety(y)

def paddle_a_right ():
	x = paddle_a.xcor() 
	x += 20 
	paddle_a.setx(x)

def paddle_a_left ():
	x = paddle_a.xcor() 
	x -= 20 
	paddle_a.setx(x)
	
# Keyboard binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_right, "d")
wn.onkeypress(paddle_a_left, "a")
	
#paddle b move	
	
def paddle_b_up ():
	y = paddle_b.ycor() 
	y += 20 
	paddle_b.sety(y)
	
def paddle_b_right ():
	x = paddle_b.xcor() 
	x += 20 
	paddle_b.setx(x)

def paddle_b_left ():
	x = paddle_b.xcor() 
	x -= 20 
	paddle_b.setx(x)

def paddle_b_down ():
	y = paddle_b.ycor() 
	y -= 20 
	paddle_b.sety(y)

# Keyboard binding for b
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_right, "Right")
wn.onkeypress(paddle_b_left, "Left")


#paddle c move	
	
def paddle_c_up ():
	y = paddle_c.ycor() 
	y += 20 
	paddle_c.sety(y)
	
def paddle_c_right ():
	x = paddle_c.xcor() 
	x += 20 
	paddle_c.setx(x)

def paddle_c_left ():
	x = paddle_c.xcor() 
	x -= 20 
	paddle_c.setx(x)

def paddle_c_down ():
	y = paddle_c.ycor() 
	y -= 20 
	paddle_c.sety(y)

# Keyboard binding for c
wn.listen()
wn.onkeypress(paddle_c_up, "y")
wn.onkeypress(paddle_c_down, "h")
wn.onkeypress(paddle_c_right, "j")
wn.onkeypress(paddle_c_left, "g")


# Function 
#paddle d move
def paddle_d_up ():
	y = paddle_d.ycor() 
	y += 20
	paddle_d.sety(y)


def paddle_d_down ():
	y = paddle_d.ycor() 
	y -= 20 
	paddle_d.sety(y)

def paddle_d_right ():
	x = paddle_d.xcor() 
	x += 20 
	paddle_d.setx(x)

def paddle_d_left ():
	x = paddle_d.xcor() 
	x -= 20 
	paddle_d.setx(x)
	
# Keyboard binding 
wn.listen()
wn.onkeypress(paddle_d_up, "f")
wn.onkeypress(paddle_d_down, "v")
wn.onkeypress(paddle_d_right, "b")
wn.onkeypress(paddle_d_left,"c")
	



#gameover

def gameover():
	pen.clear()
	pen.write("over", align="center", font=("curier",24,"normal"))
	#messagebox.showerror("showerror", "GameOver")
	canvas = screen.getcanvas()
	button = Button(canvas.master, text="Exit", command=do_something)				
	button.pack()
	button.place(x=300, y=100)
	# place the button anywhere on the screen
	screen.exitonclick()	
	







def blockarea(x,y):
	global score_a,score_b,score_c,score_d
	if paddle_b.ycor() == y and paddle_b.xcor() == x :
		paddle_b.goto(370, -260)
		score_b -=1
		if (score_b == 0):
			pen.clear()
			pen.write("over", align="center", font=("curier",24,"normal"))
			#messagebox.showerror("showerror", "GameOver")
			canvas = screen.getcanvas()
			button = Button(canvas.master, text="Exit", command=do_something)
			button.pack()
			button.place(x=300, y=100)  # place the button anywhere on the screen
			screen.exitonclick()
		
		else:
			pen.clear()
			pen.write("Player A: {} Player B: {} Player C: {} Player D: {}".format(score_a, score_b, score_c, score_d),align="center", font=("Courier", 20, "normal"))	
	elif paddle_a.ycor() == y and paddle_a.xcor() == x :
		paddle_a.goto(-370, 260)
		score_a -=1
		if (score_a == 0):
			pen.clear()
			pen.write("over", align="center", font=("curier",24,"normal"))
			#messagebox.showerror("showerror", "GameOver")
			canvas = screen.getcanvas()
			button = Button(canvas.master, text="Exit", command=do_something)
			button.pack()
			button.place(x=300, y=100)  # place the button anywhere on the screen
			screen.exitonclick()
		
		else:
			pen.clear()
			pen.write("Player A: {} Player B: {} Player C: {} Player D: {}".format(score_a, score_b, score_c, score_d), align="center", font=("Courier", 20, "normal"))
			
	elif paddle_c.ycor() == y and paddle_c.xcor() == x :
		paddle_c.goto(370, 260)
		score_c -=1
		if (score_c == 0):
			pen.clear()
			pen.write("over", align="center", font=("curier",24,"normal"))
			#messagebox.showerror("showerror", "GameOver")
			canvas = screen.getcanvas()
			button = Button(canvas.master, text="Exit", command=do_something)
			button.pack()
			button.place(x=300, y=100)  # place the button anywhere on the screen
			screen.exitonclick()
		
		else:
			pen.clear()
			pen.write("Player A: {} Player B: {} Player C: {} Player D: {}".format(score_a, score_b, score_c, score_d), align="center", font=("Courier", 20, "normal"))	
	elif paddle_d.ycor() == y and paddle_d.xcor() == x :
		paddle_d.goto(-370, -260)
		score_d -=1
		if (score_d == 0):
			pen.clear()
			pen.write("over", align="center", font=("curier",24,"normal"))
			#messagebox.showerror("showerror", "GameOver")
			canvas = screen.getcanvas()
			button = Button(canvas.master, text="Exit", command=do_something)
			button.pack()
			button.place(x=300, y=100)  # place the button anywhere on the screen
			screen.exitonclick()
		
		else:
			pen.clear()
			pen.write("Player A: {} Player B: {} Player C: {} Player D: {}".format(score_a, score_b, score_c, score_d), align="center", font=("Courier", 20, "normal"))





def haddel(n):
	for i in range(n):
		haddel_1 = turtle. Turtle() 
		haddel_1.speed(0) 
		haddel_1.shape("square") 
		haddel_1.color("#954f22") 
		haddel_1.shapesize(stretch_wid=4, stretch_len=2)
		haddel_1.penup()
		m = random.randrange(-340, 340,80)
		n = random.randrange(-280, 280,120)
		haddel_1.goto( m, n)
		j=0
		k=0
		j=n-40
		k=n+60
		for i in range(j,k,10):
			blockarea(0,i)
		

haddel(90)
		




def fun():
	global score_a,score_b
		 
	while True:
		wn.update()
		
		
		#haedel-------------------------------------------------------------------------

		
		blockarea(-350,0)
		blockarea(110,260)
		blockarea(10,0)
		blockarea(-150,200)
		blockarea(190,-220)
		blockarea(-290,80)
		blockarea(-30,20)
		blockarea(-130,140)
		blockarea(-150,140)
		blockarea(350,0)
		blockarea(-110,-260)
		blockarea(-10,0)
		blockarea(-150,-200)
		blockarea(-190,220)
		blockarea(290,-80)
		blockarea(30,-20)
		blockarea(-130,-140)
		blockarea(-150,-140)		

			
			
		if paddle_b.ycor() == paddle_a.ycor() and paddle_b.xcor() == paddle_a.xcor() and paddle_a.ycor() == paddle_c.ycor() and paddle_a.xcor() == paddle_c.xcor() and paddle_b.ycor() == paddle_d.ycor() and paddle_b.xcor() == paddle_d.xcor():
				launch = messagebox.askquestion("You win","Play again?")
				if launch == "yes":
					print(launch)
					fun()
				else:
					exit()
	

		paddle_b.setx(paddle_b.xcor() + paddle_b.dx)
		paddle_b.sety(paddle_b.ycor() + paddle_b.dy)
			
			# Border checking 
		if paddle_b.ycor() > 290:
			paddle_b.sety (290) 
			paddle_b.dy *= -1
	
		if paddle_b.ycor() < -290:
			paddle_b.sety(-290) 
			paddle_b.dy *= -1
		
		if paddle_b.xcor() > 390:
			paddle_b.setx (390) 
			paddle_b.dx *= -1
		
		if paddle_b.xcor() < -380:
			paddle_b.setx(-380) 
			paddle_b.dx *= -1
	
	
		paddle_a.setx(paddle_a.xcor() + paddle_a.dx)
		paddle_a.sety(paddle_a.ycor() + paddle_a.dy)
		
			# Border checking 
		if paddle_a.ycor() > 290:
			paddle_a.sety (290) 
			paddle_a.dy *= -1
		
		if paddle_a.ycor() < -290:
			paddle_a.sety(-290) 
			paddle_a.dy *= -1
		
		if paddle_a.xcor() > 390:
			paddle_a.setx (390) 
			paddle_a.dx *= -1
		
		if paddle_a.xcor() < -390:
			paddle_a.setx(-390) 
			paddle_a.dx *= -1
			
			
		paddle_d.setx(paddle_d.xcor() + paddle_d.dx)
		paddle_d.sety(paddle_d.ycor() + paddle_d.dy)
			
			# Border checking 
		if paddle_d.ycor() > 290:
			paddle_d.sety (290) 
			paddle_d.dy *= -1
	
		if paddle_d.ycor() < -290:
			paddle_d.sety(-290) 
			paddle_d.dy *= -1
		
		if paddle_d.xcor() > 390:
			paddle_d.setx (390) 
			paddle_d.dx *= -1
		
		if paddle_d.xcor() < -380:
			paddle_d.setx(-380) 
			paddle_d.dx *= -1
	
	
		paddle_c.setx(paddle_c.xcor() + paddle_c.dx)
		paddle_c.sety(paddle_c.ycor() + paddle_c.dy)
		
			# Border checking 
		if paddle_c.ycor() > 290:
			paddle_c.sety (290) 
			paddle_c.dy *= -1
		
		if paddle_c.ycor() < -290:
			paddle_c.sety(-290) 
			paddle_c.dy *= -1
		
		if paddle_c.xcor() > 390:
			paddle_c.setx (390) 
			paddle_c.dx *= -1
		
		if paddle_c.xcor() < -390:
			paddle_c.setx(-390) 
			paddle_c.dx *= -1
			
			


if __name__ == "__main__":
	fun()


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
