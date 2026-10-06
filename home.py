import tkinter as tk

# =======================================
# CREATE WINDOW
# =======================================

root = tk.Tk()
root.title("Ulha's Castle")
root.geometry("1000x700")

# Create Canvas
canvas = tk.Canvas(
    root,
    width=1000,
    height=700,
    bg="#4db3c7"
)

canvas.pack()


# =======================================
# SKY
# =======================================

canvas.create_rectangle(
    0, 0, 1000, 700,
    fill="#4db3c7",
    outline=""
)


# =======================================
# SUN
# =======================================

canvas.create_oval(
    780, 50, 880, 150,
    fill="#ffd93d",
    outline="#f5a623",
    width=3
)

# Sun rays
sun_rays = [
    (830, 35, 830, 10),
    (830, 165, 830, 190),
    (765, 100, 735, 100),
    (895, 100, 925, 100),
    (780, 50, 760, 30),
    (880, 50, 900, 30),
    (780, 150, 760, 170),
    (880, 150, 900, 170)
]

for x1, y1, x2, y2 in sun_rays:
    canvas.create_line(
        x1, y1, x2, y2,
        fill="#f5a623",
        width=4
    )


# =======================================
# CLOUDS
# =======================================

# Cloud 1
canvas.create_oval(
    50, 80, 180, 150,
    fill="#a9e7f2",
    outline="",
    tags="cloud1"
)

canvas.create_oval(
    120, 50, 250, 150,
    fill="#a9e7f2",
    outline="",
    tags="cloud1"
)

canvas.create_oval(
    200, 80, 300, 150,
    fill="#a9e7f2",
    outline="",
    tags="cloud1"
)


# Cloud 2
canvas.create_oval(
    400, 70, 520, 140,
    fill="#a9e7f2",
    outline="",
    tags="cloud2"
)

canvas.create_oval(
    470, 45, 600, 145,
    fill="#a9e7f2",
    outline="",
    tags="cloud2"
)

canvas.create_oval(
    560, 75, 680, 145,
    fill="#a9e7f2",
    outline="",
    tags="cloud2"
)


# =======================================
# BACKGROUND TREES
# =======================================

def tree(x, y):

    # Tree trunk
    canvas.create_rectangle(
        x - 10, y + 80,
        x + 10, y + 150,
        fill="#795548",
        outline="black"
    )

    # First layer
    canvas.create_polygon(
        x, y,
        x - 45, y + 100,
        x + 45, y + 100,
        fill="#4caf50",
        outline="#245c2a",
        width=2
    )

    # Second layer
    canvas.create_polygon(
        x, y + 35,
        x - 40, y + 120,
        x + 40, y + 120,
        fill="#3d963f",
        outline="#245c2a",
        width=2
    )


tree(70, 300)
tree(930, 300)


# =======================================
# GRASS / GROUND
# =======================================

canvas.create_rectangle(
    0, 450, 1000, 700,
    fill="#7ed957",
    outline=""
)


# =======================================
# MAIN DUPLEX HOUSE
# =======================================

canvas.create_rectangle(
    230, 250, 770, 500,
    fill="#dca866",
    outline="#333333",
    width=4
)


# =======================================
# LEFT WING
# =======================================

canvas.create_polygon(
    150, 300,
    280, 190,
    410, 300,
    fill="#b86643",
    outline="#333333",
    width=4
)

canvas.create_rectangle(
    190, 300, 370, 400,
    fill="#e4b56d",
    outline="#333333",
    width=3
)


# =======================================
# RIGHT WING
# =======================================

canvas.create_polygon(
    590, 300,
    720, 190,
    850, 300,
    fill="#b86643",
    outline="#333333",
    width=4
)

canvas.create_rectangle(
    630, 300, 810, 400,
    fill="#e4b56d",
    outline="#333333",
    width=3
)


# =======================================
# MAIN ROOF
# =======================================

canvas.create_polygon(
    210, 260,
    500, 80,
    790, 260,
    fill="#d8a65c",
    outline="#333333",
    width=5
)

# Dark roof border
canvas.create_line(
    210, 260,
    500, 80,
    790, 260,
    fill="#303b52",
    width=12
)


# =======================================
# SECOND FLOOR FRONT
# =======================================

canvas.create_polygon(
    365, 255,
    500, 160,
    635, 255,
    fill="#f1d07d",
    outline="#333333",
    width=3
)
# =======================================
# SECOND FLOOR WINDOW
# =======================================

canvas.create_arc(
    455, 190, 545, 275,
    start=0,
    extent=180,
    fill="#8fd3e8",
    outline="#333333",
    width=3
)

canvas.create_rectangle(
    455, 232, 545, 275,
    fill="#8fd3e8",
    outline="#333333",
    width=3
)

canvas.create_line(
    500, 190,
    500, 275,
    width=2
)

canvas.create_line(
    455, 250,
    545, 250,
    width=2
)


# =======================================
# LEFT WINDOW
# =======================================

canvas.create_rectangle(
    250, 315, 350, 385,
    fill="#8fd3e8",
    outline="#333333",
    width=3
)

canvas.create_line(
    300, 315,
    300, 385,
    width=2
)

canvas.create_line(
    250, 350,
    350, 350,
    width=2
)


# =======================================
# RIGHT WINDOW
# =======================================

canvas.create_rectangle(
    650, 315, 750, 385,
    fill="#8fd3e8",
    outline="#333333",
    width=3
)

canvas.create_line(
    700, 315,
    700, 385,
    width=2
)

canvas.create_line(
    650, 350,
    750, 350,
    width=2
)


# =======================================
# LOWER LEFT WINDOW
# =======================================

canvas.create_rectangle(
    270, 410, 350, 475,
    fill="#8fd3e8",
    outline="#333333",
    width=3
)

canvas.create_line(
    310, 410,
    310, 475,
    width=2
)

canvas.create_line(
    270, 442,
    350, 442,
    width=2
)


# =======================================
# LOWER RIGHT WINDOW
# =======================================

canvas.create_rectangle(
    650, 410, 730, 475,
    fill="#8fd3e8",
    outline="#333333",
    width=3
)

canvas.create_line(
    690, 410,
    690, 475,
    width=2
)

canvas.create_line(
    650, 442,
    730, 442,
    width=2
)


# =======================================
# MAIN ENTRANCE
# =======================================

canvas.create_rectangle(
    445, 350, 555, 500,
    fill="#ead9b0",
    outline="#333333",
    width=4
)

# Door
canvas.create_rectangle(
    465, 365, 535, 500,
    fill="#a85d3b",
    outline="#333333",
    width=3
)

# Door center
canvas.create_line(
    500, 365,
    500, 500,
    fill="#713b29",
    width=2
)

# Door handles
canvas.create_oval(
    485, 430, 493, 438,
    fill="black"
)

canvas.create_oval(
    507, 430, 515, 438,
    fill="black"
)


# =======================================
# BALCONY
# =======================================

canvas.create_rectangle(
    420, 325, 580, 345,
    fill="#777777",
    outline="#333333",
    width=3
)

# Curved balcony railing
canvas.create_arc(
    420, 280, 580, 350,
    start=0,
    extent=180,
    outline="black",
    width=4
)

# Balcony bars
for x in range(425, 581, 15):

    canvas.create_line(
        x, 315,
        x, 340,
        fill="black",
        width=2
    )


# =======================================
# COLUMNS
# =======================================

canvas.create_rectangle(
    400, 270, 425, 450,
    fill="#eeeeee",
    outline="#555555",
    width=2
)

canvas.create_rectangle(
    575, 270, 600, 450,
    fill="#eeeeee",
    outline="#555555",
    width=2
)


# =======================================
# STEPS
# =======================================

for i in range(7):

    y = 500 + i * 18

    canvas.create_rectangle(
        430 - i * 12,
        y,
        570 + i * 12,
        y + 18,
        fill="#dddddd",
        outline="#777777"
    )


# =======================================
# POND
# =======================================

canvas.create_oval(
    250, 570, 750, 680,
    fill="#6bb7df",
    outline="#555555",
    width=5
)

canvas.create_oval(
    280, 590, 720, 660,
    fill="#4d9dcc",
    outline="#333333",
    width=3
)

# Water line
canvas.create_arc(
    330, 610, 650, 650,
    start=0,
    extent=180,
    outline="#9edcf5",
    width=2
)


# =======================================
# CAT HOUSE
# =======================================
# Cat house body
canvas.create_rectangle(
    720, 450, 880, 560,
    fill="#d99452",
    outline="#333333",
    width=4
)

# Cat house roof
canvas.create_polygon(
    700, 450,
    800, 370,
    900, 450,
    fill="#9c4f3d",
    outline="#333333",
    width=4
)

# Cat house entrance
canvas.create_oval(
    755, 475, 845, 560,
    fill="#30251f",
    outline="#222222",
    width=3
)

# Cat house label
canvas.create_text(
    800, 580,
    text="CAT HOUSE",
    font=("Arial", 14, "bold"),
    fill="#57301f"
)


# =======================================
# CAT
# =======================================

# Cat body
canvas.create_oval(
    780, 510, 825, 540,
    fill="#f2a65a",
    outline="#4d3425",
    width=2,
    tags="cat"
)

# Cat head
canvas.create_oval(
    815, 495, 850, 530,
    fill="#f2a65a",
    outline="#4d3425",
    width=2,
    tags="cat"
)

# Left ear
canvas.create_polygon(
    818, 502,
    820, 487,
    832, 500,
    fill="#dac2aa",
    outline="#4d3425",
    tags="cat"
)

# Right ear
canvas.create_polygon(
    835, 500,
    845, 487,
    849, 505,
    fill="#f2a65a",
    outline="#4d3425",
    tags="cat"
)

# Left eye
canvas.create_oval(
    825, 507, 830, 512,
    fill="black",
    tags="cat"
)

# Right eye
canvas.create_oval(
    838, 507, 843, 512,
    fill="black",
    tags="cat"
)

# Nose
canvas.create_polygon(
    832, 515,
    837, 515,
    834, 519,
    fill="pink",
    tags="cat"
)

# Tail
canvas.create_arc(
    770, 495, 810, 535,
    start=80,
    extent=220,
    style="arc",
    outline="#0f0801",
    width=6,
    tags="cat"
)

# Legs
canvas.create_line(
    790, 532,
    790, 545,
    fill="#f2a65a",
    width=5,
    tags="cat"
)

canvas.create_line(
    810, 532,
    810, 545,
    fill="#f2a65a",
    width=5,
    tags="cat"
)


# =======================================
# TITLE
# =======================================

canvas.create_text(
    500, 25,
    text="Ulha's Castle",
    font=("Arial", 24, "bold"),
    fill="white"
)


# =======================================
# CLOUD ANIMATION
# =======================================

def move_clouds():

    # Move first cloud
    canvas.move(
        "cloud1",
        2,
        0
    )

    # Move second cloud
    canvas.move(
        "cloud2",
        1,
        0
    )

    # Check cloud 1 position
    position1 = canvas.bbox("cloud1")

    if position1[0] > 1000:

        canvas.move(
            "cloud1",
            -1100,
            0
        )

    # Check cloud 2 position
    position2 = canvas.bbox("cloud2")

    if position2[0] > 1000:

        canvas.move(
            "cloud2",
            -1100,
            0
        )

    # Repeat animation
    root.after(
        50,
        move_clouds
    )


# =======================================
# CAT ANIMATION
# =======================================

cat_x = 0
cat_direction = 1


def move_cat():

    global cat_x
    global cat_direction

    # Move the cat
    canvas.move(
        "cat",
        cat_direction * 2,
        0
    )

    cat_x = cat_x + cat_direction * 2

    # When cat reaches the left side
    if cat_x <= -150:

        cat_direction = 1

    # When cat reaches the right side
    if cat_x >= 120:

        cat_direction = -1

    # Repeat cat animation
    root.after(
        80,
        move_cat
    )


# =======================================
# START ANIMATIONS
# =======================================

move_clouds()
move_cat()


# =======================================
# RUN PROGRAM
# =======================================

root.mainloop()