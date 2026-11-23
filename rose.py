import turtle
import math
 
# Screen setup
screen = turtle.Screen()
screen.bgcolor("#1a0a1e")
screen.title("🌹 Gulabi Gulab - Rose Graphics")
screen.setup(700, 700)
 
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
 
def draw_petal(t, x, y, angle, size, color):
    """Ek pankh (petal) draw karta hai"""
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.end_fill()
 
def draw_rose(cx, cy):
    """Poora gulab draw karta hai"""
 
    # ---- Tana (Stem) ----
    t.penup()
    t.goto(cx, cy - 180)
    t.pendown()
    t.pensize(5)
    t.color("#2d6a2d")
    t.setheading(90)
    t.forward(180)
 
    # ---- Patte (Leaves) ----
    for side, angle in [(-1, 200), (1, -20)]:
        t.penup()
        t.goto(cx, cy - 100)
        t.pendown()
        t.color("#3a8a3a")
        t.begin_fill()
        t.setheading(90 + side * 50)
        t.circle(side * 35, 180)
        t.end_fill()
 
    # ---- Baahri Pankh - Outer Petals ----
    outer_colors = ["#cc1144", "#dd1155", "#ee2266", "#cc1144", "#dd1155", "#ee2266"]
    for i, col in enumerate(outer_colors):
        angle = i * 60
        rad = math.radians(angle)
        px = cx + 28 * math.cos(rad)
        py = cy + 28 * math.sin(rad) - 10
        draw_petal(t, px, py, angle - 90, 38, col)
 
    # ---- Bichli Pankh - Middle Petals ----
    mid_colors = ["#ee3377", "#ff4488", "#ee3377", "#ff4488", "#ee3377", "#ff4488"]
    for i, col in enumerate(mid_colors):
        angle = i * 60 + 30
        rad = math.radians(angle)
        px = cx + 16 * math.cos(rad)
        py = cy + 16 * math.sin(rad)
        draw_petal(t, px, py, angle - 90, 28, col)
 
    # ---- Andar Pankh - Inner Petals ----
    inner_colors = ["#ff66aa", "#ff77bb", "#ff66aa", "#ff77bb"]
    for i, col in enumerate(inner_colors):
        angle = i * 90 + 15
        rad = math.radians(angle)
        px = cx + 8 * math.cos(rad)
        py = cy + 8 * math.sin(rad) + 8
        draw_petal(t, px, py, angle - 90, 18, col)
 
    # ---- Beej (Center) ----
    t.penup()
    t.goto(cx, cy + 5)
    t.pendown()
    t.dot(18, "#ffcc00")
    t.penup()
    t.goto(cx, cy + 3)
    t.pendown()
    t.dot(10, "#ffaa00")
 
def draw_sparkles():
    """Chamakte sitare background mein"""
    import random
    random.seed(42)
    t.pensize(1)
    for _ in range(60):
        x = random.randint(-330, 330)
        y = random.randint(-330, 330)
        size = random.choice([2, 3, 4])
        alpha = random.choice(["#ffffff", "#ffddee", "#ffe0f0", "#ffccdd"])
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(size, alpha)
 
def draw_title():
    """Title likhta hai"""
    t.penup()
    t.goto(0, 250)
    t.pendown()
    t.color("#ff99cc")
    t.write("🌹  Gulab  🌹", align="center", font=("Georgia", 26, "bold italic"))
 
    t.penup()
    t.goto(0, -255)
    t.pendown()
    t.color("#ff77aa")
    t.write("Python Turtle Graphics", align="center", font=("Courier", 13, "normal"))
 
# ---- Main Program ----
draw_sparkles()
draw_title()
draw_rose(0, 30)
 
print("✅ Gulab tayar hai! Window band karne ke liye click karein.")
screen.exitonclick()
