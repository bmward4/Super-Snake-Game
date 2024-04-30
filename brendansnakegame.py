
import turtle
import time
import random
import pygame
from PIL import Image
from tkinter import Tk, Canvas, Button, PhotoImage

delay = 0.1

# Score
score = 0
high_score = 0

title_screen = Tk()
title_screen.title("Snake Game")

# Set up a canvas for the title screen
canvas = Canvas(title_screen, width=600, height=600, bg="lightgreen")
canvas.pack()

# Load a snake image for the title
snake_image = PhotoImage(file="/Users/brendanward/Desktop/snakeimages/snakeframe3.png")  

# Display the snake image on the title screen
canvas.create_image(300, 300, image=snake_image)

# Add a start button to transition to the game
start_button = Button(title_screen, text="Start Game", command=title_screen.destroy)
start_button.pack()


appleimg = "/Users/brendanward/Desktop/snakeimages/snakeapple.gif"

resizeapple = "/Users/brendanward/Desktop/snakeimages/snakeapple_resized.gif"

snakeheadup = "/Users/brendanward/Desktop/snakeimages/snakeheadresizedup.gif"
snakeheadleft = "/Users/brendanward/Desktop/snakeimages/snakeheadresizedleft.gif"
snakeheaddown = "/Users/brendanward/Desktop/snakeimages/snakeheadresizeddown.gif"
snakeheadright = "/Users/brendanward/Desktop/snakeimages/snakeheadresizedright.gif"

snakebody = "/Users/brendanward/Desktop/snakeimages/snakebodyresized.gif"

snakepower = "/Users/brendanward/Desktop/snakeimages/snakepowerresized.gif"
snakebodypower = "/Users/brendanward/Desktop/snakeimages/snakebodypowerresized.gif"

snakeobstacle = "/Users/brendanward/Desktop/snakeimages/snakeobstacle.gif"

flipper = "/Users/brendanward/Desktop/snakeimages/flipper.gif"
snakebodyflip = "/Users/brendanward/Desktop/snakeimages/flipbody.gif"

snakebomb = "/Users/brendanward/Desktop/snakeimages/snakebomb.gif"

backgroundone = "/Users/brendanward/Desktop/snakeimages/snakebackgrounddefault.gif"
backgroundtwo = "/Users/brendanward/Desktop/snakeimages/snakebackground2.gif"
backgroundthree = "/Users/brendanward/Desktop/snakeimages/snakebackground3.gif"
backgroundfour = "/Users/brendanward/Desktop/snakeimages/snakebackground4.gif"
backgroundfive = "/Users/brendanward/Desktop/snakeimages/snakebackground5.gif"

# Initialize pygame mixer
pygame.mixer.init()

eat_sound = pygame.mixer.Sound("/Users/brendanward/Desktop/snakeimages/munch-sound-effect.mp3")
power_up = pygame.mixer.Sound("/Users/brendanward/Desktop/snakeimages/powerupsound.mp3")
crash = pygame.mixer.Sound("/Users/brendanward/Desktop/snakeimages/crasheffect.mp3")
flippersound = pygame.mixer.Sound("/Users/brendanward/Desktop/snakeimages/flipper.mp3")
breakersound = pygame.mixer.Sound("/Users/brendanward/Downloads/Explosion+3.mp3")

# Load the music file
pygame.mixer.music.load("/Users/brendanward/Desktop/snakeimages/snakesong.mp3") 

# Play the music on a loop 
pygame.mixer.music.play(-1)


# Run the Tkinter event loop for the title screen
title_screen.mainloop()




# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("lightgreen")
#wn.bgpic(backgroundtwo)
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

wn.addshape(resizeapple)
wn.addshape(snakeheadup)
wn.addshape(snakeheadleft)
wn.addshape(snakeheadright)
wn.addshape(snakeheaddown)

wn.addshape(snakebody)

wn.addshape(snakepower)
wn.addshape(snakebodypower)

wn.addshape(snakeobstacle)

wn.addshape(flipper)
wn.addshape(snakebodyflip)

wn.addshape(snakebomb)

#Initialize segment and obstacle lists
segments = []
obstacles = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape(snakeheadup)
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape(resizeapple)
food.penup()
food.goto(0,100)

# Snake power
power = turtle.Turtle()
power.speed(0)
power.shape(snakepower)
power.penup()
power.goto(0,-100)

#Wall breaker
breaker = turtle.Turtle()
breaker.speed(0)
breaker.shape(snakebomb)
breaker.penup()
breaker.goto(0,200)

# Flipper
flip = turtle.Turtle()
flip.speed(0)
flip.shape(flipper)
flip.penup()
flip.goto(0,-200)

def movepeices(element):
    while True:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)

        # Check for collisions with other objects (food, obstacles, etc.)
        if not (
            any(seg.distance(x, y) < 20 for seg in segments) or
            head.distance(x,y) < 60 or
            food.distance(x, y) < 25 or
            power.distance(x, y) < 25 or
            flip.distance(x, y) < 25 or
            breaker.distance(x,y) < 25 or
            any(obs.distance(x, y) < 25 for obs in obstacles)
        ):
            break  # Break the loop if there are no collisions

    element.goto(x, y) 

def timer(element,function,milisec):
    element.goto(1000,1000)
    wn.ontimer(function, milisec)

def newfood():
    movepeices(food)

def newpower():
    movepeices(power)

def newflip():
    movepeices(flip)

def newbreak():
    movepeices(breaker)


rng = random.randint(5, 10)

#Obstacles
def place_obstacles(num_obstacles): 
    for _ in range(num_obstacles):
        obs = turtle.Turtle()
        obs.speed(0)
        obs.shape(snakeobstacle)  
        obs.penup()
        obstacles.append(obs) # Append the obstacle stamp to the list
        movepeices(obs)
def clear_obstacles():
    for obs in obstacles:
        obs.clear()  # Clear the turtle's drawing
        obs.hideturtle()  # Hide the turtle
    obstacles.clear()

place_obstacles(rng)
 
#Segments
def newsegement(bodystyle):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(bodystyle)
        new_segment.penup()
        segments.append(new_segment)


flipped_controls = False
flipped_controls_duration = 50

def toggle_flipped_controls():
    global flipped_controls
    flipped_controls = not flipped_controls

def reset_controls():
    global flipped_controls
    flipped_controls = False

def go_up():
    if not flipped_controls:
        if head.direction != "down":
            head.direction = "up"
    else:
        if head.direction != "up":
            head.direction = "down"

def go_down():
    if not flipped_controls:
        if head.direction != "up":
            head.direction = "down"
    else:
        if head.direction != "down":
            head.direction = "up"

def go_left():
    if not flipped_controls:
        if head.direction != "right":
            head.direction = "left"
    else:
        if head.direction != "left":
            head.direction = "right"

def go_right():
    if not flipped_controls:
        if head.direction != "left":
            head.direction = "right"
    else:
        if head.direction != "right":
            head.direction = "left"

def move():
    if head.direction == "up":
        head.shape(snakeheadup)

        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        head.shape(snakeheaddown)
   

        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        head.shape(snakeheadleft)
        
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        head.shape(snakeheadright)
        
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")





# Main game loop
while True:
    wn.update()
    rng = random.randint(5, 10)

    if score < 300:
        wn.bgpic(backgroundone)
    
    if score >= 300:
        wn.bgpic(backgroundthree)

    if score >= 600:
        wn.bgpic(backgroundfive)




    # Check for a collision with the food
    if head.distance(food) < 20:
        eat_sound.play()
        newfood()

        newsegement(snakebody)
        delay += 0.002
        if flipped_controls == True:
            score += 15
        else:
            score += 10

    #check for collision with power food
    if head.distance(power) < 20:
        power_up.play()
        newsegement(snakebodypower)
        timer(power, newpower,3500)
        # Shorten the delay
        delay -= 0.005
        # Increase the score
        if flipped_controls == True:
            score += 30
        else:
            score += 20

        if score > high_score:
            high_score = score
        
    #check for collision with flipper
    if head.distance(flip) < 20:
        flippersound.play()
        score += 50 
        newsegement(snakebodyflip)
        toggle_flipped_controls()
        timer(flip, newflip,10000)
        
        
    #Check for collision with breaker
    if head.distance(breaker) < 20:
        breakersound.play()
        timer(breaker,newbreak,random.randint(7000,15000))
        score -= 10
        clear_obstacles()
        place_obstacles(rng)



    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()    


    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        pygame.mixer.music.pause()
        
        crash.play()
        time.sleep(3)
        pygame.mixer.music.unpause()
        time.sleep(1)
        head.goto(0,0)
    
        clear_obstacles()
        place_obstacles(rng)

        head.direction = "stop"
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        # Clear the segments list
        segments.clear()

        reset_controls()
        # Reset the score
        score = 0
        power.goto(0,-100)
        food.goto(0,100)
        flipped_controls_duration = 50
        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 



    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            
            pygame.mixer.music.pause()
      
            crash.play()
            time.sleep(3)
            pygame.mixer.music.unpause()
            
            time.sleep(1)
            head.goto(0,0)
            head.shape(snakeheadup)
            head.direction = "stop"
            pygame.mixer.music.stop
            
            clear_obstacles()
            place_obstacles(rng)

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
            reset_controls()
            power.goto(0,-100)
            food.goto(0,100)
            flipped_controls_duration = 50
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for obs in obstacles:  
        if obs.distance(head) < 15:
            pygame.mixer.music.pause()
            crash.play()
            time.sleep(3)
            pygame.mixer.music.unpause()
            time.sleep(1)
            # Clear obstacles when the player hits an obstacle
            clear_obstacles()
            place_obstacles(rng)
            head.goto(0, 0)
            head.shape(snakeheadup)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            # Clear the segments list
            segments.clear()
            # Reset the score
            reset_controls()
            score = 0
            power.goto(0, -100)
            food.goto(0, 100)
            flipped_controls_duration = 50
            # Reset the delay
            delay = 0.1
            pen.clear()


        if flipped_controls:
            flipped_controls_duration -= delay
            if flipped_controls_duration <= 0:
                reset_controls()
                flippersound.play()
                flipped_controls_duration = 50  # Reset the timer
                
            pen.clear()
            pen.pencolor("red")
            pen.write("Controls Flipped! Time remaining: {}".format(round(flipped_controls_duration*delay,2)), align="center", font=("Courier", 24, "bold"))

        else:
            # Display the regular score when controls are not flipped
            pen.clear()
            pen.pencolor("white")
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            


    
    time.sleep(delay)


wn.mainloop()