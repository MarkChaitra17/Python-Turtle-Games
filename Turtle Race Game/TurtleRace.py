import turtle  
import time     #To have delay in movement
import random   #To have random food placements
import csv

#Setup screen
window = turtle.Screen()
window.title("Turtle race by @MarkChaitra")
window.bgcolor("green")
window.setup(width=800, height=200)
window.tracer(0)

#First turtle
Tblack = turtle.Turtle()
Tblack.speed(0)
Tblack.shape("turtle")
Tblack.color("black")
Tblack.penup()
Tblack.goto(-350, 0)
Tblack.direction = "right"

#Second turtle
Tred = turtle.Turtle()
Tred.speed(0)
Tred.shape("turtle")
Tred.color("red")
Tred.penup()
Tred.goto(-350, -30)
Tred.direction = "right"

#Third turtle
Torange = turtle.Turtle()
Torange.speed(0)
Torange.shape("turtle")
Torange.color("orange")
Torange.penup()
Torange.goto(-350, 30)
Torange.direction = "right"

#Finish line
Finish_line = turtle.Turtle()
Finish_line.color("black")
Finish_line.penup()
Finish_line.goto(300, -100)
Finish_line.right
Finish_line.pendown()
Finish_line.goto(300,100)
Finish_line.penup()
Finish_line.hideturtle()

#Start button
StartBtn = turtle.Turtle()
StartBtn.penup()
StartBtn.speed(0)
StartBtn.color("grey")
StartBtn.shape("square")
StartBtn.goto(-220, 65)

#Reset button
ResetBtn = turtle.Turtle()
ResetBtn.penup()
ResetBtn.speed(0)
ResetBtn.color("grey")
ResetBtn.shape("square")
ResetBtn.goto(-170, 65)

#Winner board
winBoard = turtle.Turtle()
winBoard.speed(0)
winBoard.color("white")
winBoard.penup()
winBoard.hideturtle()
winBoard.goto(0, 70)
winBoard.write("Winner: ", align="center", font=("Courier", 18, "normal"))

#Buttons
BtnLabel = turtle.Turtle()
BtnLabel.speed(0)
BtnLabel.color("white")
BtnLabel.penup()
BtnLabel.hideturtle()
BtnLabel.goto(-195, 75)
BtnLabel.write("Start  Reset", align="center", font=("Courier", 12, "normal"))

#Turtle bet on
betScreen = turtle.Turtle()
betScreen.speed(0)
betScreen.color("white")
betScreen.penup()
betScreen.hideturtle()
betScreen.goto(-380, 75)
betScreen.write("Bet $10 on:", align="left", font=("Courier", 12, "normal"))

money = 0
with open('Turtle Race Game/money_val.csv', mode='r') as file:
    val = csv.reader(file)
    money = int(next(val)[0])

#Money
moneyAMT = turtle.Turtle()
moneyAMT.speed(0)
moneyAMT.color("white")
moneyAMT.penup()
moneyAMT.hideturtle()
moneyAMT.goto(-380, 55)
moneyAMT.write("${}".format(money), align="left", font=("Courier", 15, "normal"))

continue_race = False
winner = ""
bet = ""

def click(x,y):

    global continue_race, winner, bet, money

    #Click on any turtle to bet on
    if x > -360 and x < -340 and y > -10 and y < 10 and continue_race != True:
        bet = "Black"
        betScreen.clear()
        betScreen.write("Bet $10 on: {}".format(bet), align="left", font=("Courier", 12, "normal"))
    elif x > -360 and x < -340 and y > -40 and y < -20 and continue_race != True:
        bet = "Red"
        betScreen.clear()
        betScreen.write("Bet $10 on: {}".format(bet), align="left", font=("Courier", 12, "normal"))
    elif x > -360 and x < -340 and y > 20 and y < 40 and continue_race != True:
        bet = "Orange"
        betScreen.clear()
        betScreen.write("Bet $10 on: {}".format(bet), align="left", font=("Courier", 12, "normal"))

    #Start Button
    if x > -230 and x < -210 and y < 75 and y > 55 and len(winner) < 1:
        if len(bet) > 1 and continue_race != True:
            money-=10
            moneyAMT.clear()    
            moneyAMT.write("${}".format(money), align="left", font=("Courier", 15, "normal"))
        continue_race = True

    #Reset Button
    if x > -180 and x < -160 and y < 75 and y > 55 and continue_race != True:
        Tblack.goto(-350, 0)
        Tblack.speed(0)
        Tred.goto(-350, -30)
        Tred.speed(0)
        Torange.goto(-350, 30)
        Torange.speed(0)
        winner = ""
        winBoard.clear()
        winBoard.write("Winner: {}".format(winner), align="center", font=("Courier", 18, "normal"))

def past_line(turtle):

    global continue_race, winner, bet, money

    x = turtle.xcor()

    if (x+6) > 300:
        continue_race = False

        if turtle.ycor() == 0:
            winner = "Black"
        elif turtle.ycor() == -30:
            winner = "Red"
        else:
            winner = "Orange"

        if (bet == winner):
            money+= 40
            winBoard.clear()
            winBoard.write("Winner: {}, you WON!!".format(winner), align="center", font=("Courier", 18, "normal"))

            moneyAMT.clear()    
            moneyAMT.write("${}".format(money), align="left", font=("Courier", 15, "normal"))
        else:
            winBoard.clear()
            winBoard.write("Winner: {}".format(winner), align="center", font=("Courier", 18, "normal"))


def move():

    x = Tblack.xcor()
    y = Tblack.ycor()
    Tblack.goto(x+random.randint(4, 15), y)
    past_line(Tblack)
    x = Tred.xcor()
    y = Tred.ycor()
    Tred.goto(x+random.randint(4, 15), y)
    past_line(Tred)
    x = Torange.xcor()
    y = Torange.ycor()
    Torange.goto(x+random.randint(4, 15), y)
    past_line(Torange)

def on_close():
    with open("Turtle Race Game/money_val.csv", "w") as file:
        file.write(str(money))
        turtle.bye()

window.listen()
window.onclick(click)
window._root.protocol("WM_DELETE_WINDOW", on_close)

while True:

    window.update()

    if continue_race == True:
        move()
    
    time.sleep(0.1)
