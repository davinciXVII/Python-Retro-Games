import turtle
import time
import random as rnd

with open("snake/records.txt","r",encoding="utf-8")as file:
    record=file.read()
    record=int(record)
score=0
colors=["DarkOliveGreen","DarkOliveGreen1","DarkOliveGreen2","DarkOliveGreen3","DarkOliveGreen4"]    
def move_snake():
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    if head.direction=="right":
        head.setx(head.xcor()+10)

    if head.direction=="left":
        head.setx(head.xcor()-10)

    if head.direction=="up":
        head.sety(head.ycor()+10)

    if head.direction=="down":
        head.sety(head.ycor()-10)
    for segment in segments:
        if segment.distance(head)<10:
            colision()
        

    
def colision():
    global segments
    global score
    global record
    global delay
    for segment in segments:
        segment.hideturtle()
    
    segments.clear()
    move(head,0,0)
    head.up()
    head.direction="stop"
    if score>record:
        record=score
        with open("snake/records.txt","w",encoding="utf-8")as file:
            file.write(str(record))
    score=0
    update_score()
    delay=0.2
    
        

def update_score():
    global score
    global record
    pen.clear()
    pen.write(f"Score:{score} High Score:{record}",align="center",font=("Courier",24,"normal"))
    

    

def square(t,n):
    for i in range(4):
        t.forward(n)
        t.left(90)


def move(t,x,y):
    t.up()
    t.goto(x,y)
    t.down()

def go_right():
    if head.direction!="left":
        head.direction="right"
        
        
def go_left():
    if head.direction!="right":
        head.direction="left"
        
def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"
        

window=turtle.Screen()
window.title("snake")
window.tracer(0)
window.bgcolor("lime")
window.setup(width=700,height=700)

boarding=turtle.Turtle()
boarding.speed(0)
boarding.color("black")
boarding.hideturtle()
move(boarding,-310,-310)
square(boarding,620)

head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.direction="stop"
move(head,0,0)
head.up()

food=turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("square")
move(food,100,0)

pen=turtle.Turtle()
score=0
pen.speed(0)
pen.color("black")
pen.hideturtle()
move(pen,0,310)
update_score()

window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")

segments=[]

delay=0.2
while True:
    window.update()
    if head.xcor()<-290 or head.xcor()>290 or head.ycor()<-290 or head.ycor()>290:
        colision()
    if head.distance(food)<20:
        score=score+10
        update_score()
        move(food,rnd.randint(-280,280),rnd.randint(-280,280))
        delay=delay-(delay/10)
        segment=turtle.Turtle()
        segment.speed(0)
        segment.shape("circle")
        segment.color(rnd.choice(colors))
        segment.up()
        segments.append(segment)
        
        
        
    move_snake()
    
    time.sleep(delay)
    





window.mainloop()
    
