
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



#player 1
paddle_a = turtle. Turtle() 
paddle_a.speed(0) 
paddle_a.shape("square") 
paddle_a.color("black") 
paddle_a.shapesize(stretch_wid=1, stretch_len=1)
paddle_a.penup() 
paddle_a.goto(350, 0)
paddle_a.dx=0
paddle_a.dy=0


#final 2
paddle_b = turtle. Turtle() 
paddle_b.speed(0) 
paddle_b.shape("square") 
paddle_b.color("blue") 
paddle_b.shapesize(stretch_wid=1, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(-370, 260)
paddle_b.dx=0
paddle_b.dy=0



#------------------------------------------------------------------------------------------------

# Pen 
pen = turtle. Turtle() 
pen.speed (0) 
pen.color("white") 
pen.penup() 
pen.hideturtle() 
pen.goto(0, 260) 
pen.write("Player's life: 5", align="center", font=("Courier", 24, "normal"))

# Function 

	
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
	global score_a,score_b
	if paddle_b.ycor() == y and paddle_b.xcor() == x :
		paddle_b.goto(-370, 260)
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
			pen.write("Player's life: {}".format(score_b), align="center", font=("Courier", 24, "normal"))	
	


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
		blockarea(150, 80)
		

			
			
		if paddle_b.ycor() == paddle_a.ycor() and paddle_b.xcor() == paddle_a.xcor():
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
			
			
			
			


if __name__ == "__main__":
	fun()


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
