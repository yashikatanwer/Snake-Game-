import turtle
import time
import random

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("pink")
win.setup(width=600, height=600)
win.tracer(0)  # Turns off auto screen updates

# Snake Head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()  
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
food.goto(0, 100)

# Snake Body Segments
segments = []

# Score
score = 0

# Display Score
score_display = turtle.Turtle()
score_display.speed(0) 
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "underline"))

# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down": 
        head.direction = "up" 

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard bindings
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")

# Main game loop
while True:
    win.update()

    # Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: 
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)  
        segments.clear()

        score = 0
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "underline"))

    # Check for collision with food
    if head.distance(food) < 20: 
        # Move food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segment to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("sky blue")
        new_segment.penup()
        segments.append(new_segment)

        # Increase score
        score += 10
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "underline"))

    # Move the end segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with self
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "underline"))

    time.sleep(0.1)
