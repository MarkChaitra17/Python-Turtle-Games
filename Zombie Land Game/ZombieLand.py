import turtle
import time
import random

#Setup screen
width = 600
height = 600
window = turtle.Screen()
window.title("ZombieLand by @MarkChaitra")
window.bgcolor("green")
window.setup(width=width, height=height)
window.tracer(0)

#Player
Player = turtle.Turtle()
Player.shape("triangle")
Player.setheading(90)
Player.color("blue")
Player.shapesize(stretch_wid=1, stretch_len=1)
Player.penup()
Player.goto(0,0)

Score = 0
highScore = 0
Lives = 10

with open('ZombieLand game/highscore.csv', 'r') as f:
    highScore = int(f.readline())

#ScoreBoard
ScoreBoard = turtle.Turtle()
ScoreBoard.speed(0)
ScoreBoard.color("white")
ScoreBoard.penup()
ScoreBoard.hideturtle()
ScoreBoard.goto(0, 280)
ScoreBoard.write("Score: {}   High Score: {}    Lives: {}".format(Score, highScore, Lives), align="center", font=("Courier", 15, "normal"))

left = False
right = False
forward = False
backward = False

def go_left():
    global left
    left = True
def stop_left():
    global left
    left = False
def go_right():
    global right
    right = True
def stop_right():
    global right
    right = False
def go_forward():
    global forward
    forward = True
def stop_forward():
    global forward
    forward = False
def go_backward():
    global backward
    backward = True
def stop_backward():
    global backward
    backward = False
def move():
    global left, right, forward, backward
    if left == True:
        Player.left(3)
    elif right == True:
        Player.right(3)
    elif forward == True:
        Player.forward(4)
    elif backward == True:
        Player.backward(4)

player_bullets = []
enemy_zombies = []
def shoot():

    global player_bullets

    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.setheading(Player.heading())
    bullet.color("black")
    bullet.shapesize(stretch_wid=0.4, stretch_len=0.4)
    bullet.penup()
    bullet.goto(Player.pos())
    player_bullets.append(bullet)

def reset():

    global player_bullets, enemy_zombies, Lives, Score

    for bullet in player_bullets[:]:
            player_bullets.remove(bullet)
            bullet.goto(500,500)
            bullet.hideturtle()
    player_bullets.clear()
    for zombie in enemy_zombies[:]:
        enemy_zombies.remove(zombie)
        zombie.goto(500,500)
        zombie.hideturtle()
    enemy_zombies.clear()

    Player.goto(0,0)
    Lives = 10
    Score = 0
    ScoreBoard.clear()
    ScoreBoard.write("Score: {}   High Score: {}    Lives: {}".format(Score, highScore, Lives), align="center", font=("Courier", 15, "normal"))
              
def on_screen(turtle, pos):

    x, y = turtle.pos()

    if x+pos > -300 and x+pos < 300 and y+pos < 300 and y+pos > -300:
        return True
    
    return False

running = True
def on_close():

    global running

    with open('ZombieLand game/highscore.csv', 'w') as f:
        f.write(str(highScore))

    running = False

window.listen()
window.onkeypress(go_left, "a")
window.onkeyrelease(stop_left, "a")
window.onkeypress(go_right, "d")
window.onkeyrelease(stop_right, "d")
window.onkeypress(go_forward, "w")
window.onkeyrelease(stop_forward, "w")
window.onkeypress(go_backward, "s")
window.onkeyrelease(stop_backward, "s")
window.onkeypress(shoot, "space")
window._root.protocol("WM_DELETE_WINDOW", on_close)

while running == True:

    window.update()

    move()

    for bullet in player_bullets[:]:
        x, y = bullet.pos()

        if on_screen(bullet, 5):
            bullet.forward(5)
        else:
            player_bullets.remove(bullet)
            bullet.hideturtle()

        for zombie in enemy_zombies[:]:
            if bullet.distance(zombie) < 10:
                player_bullets.remove(bullet)
                bullet.goto(500,500)
                bullet.hideturtle()

                enemy_zombies.remove(zombie)
                zombie.goto(500,500)
                zombie.hideturtle()

                Score+=1
                highScore = Score if Score > highScore else highScore
                ScoreBoard.clear()
                ScoreBoard.write("Score: {}   High Score: {}    Lives: {}".format(Score, highScore, Lives), align="center", font=("Courier", 15, "normal"))

                break

    x = random.randint(0,100)
    if x <= 3 and len(enemy_zombies) < 18:
        zombie = turtle.Turtle()
        zombie.shape("triangle")
        zombie.color("brown")
        zombie.shapesize(stretch_wid=1, stretch_len=1)
        zombie.penup()

        m = random.randint(-300,300)
        if x == 0:
            zombie.goto(-300, m)
        elif x == 1:
            zombie.goto(300, m)
        elif x == 2:
            zombie.goto(m, 300)
        elif x == 3:
            zombie.goto(m, -300)
        enemy_zombies.append(zombie)
 
    for zombie in enemy_zombies[:]:
        zombie.setheading(zombie.towards(Player))
        zombie.forward(1)

        if zombie.distance(Player) < 10:
            enemy_zombies.remove(zombie)
            zombie.goto(500,500)
            zombie.hideturtle()

            Lives-=1
            ScoreBoard.clear()
            ScoreBoard.write("Score: {}   High Score: {}    Lives: {}".format(Score, highScore, Lives), align="center", font=("Courier", 15, "normal"))

            if Lives <= 0:
                reset()
                continue
