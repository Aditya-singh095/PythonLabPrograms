import turtle


# -------------------------
# Koch Snowflake
# -------------------------

def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    length /= 3

    koch(t, length, depth - 1)
    t.left(60)
    koch(t, length, depth - 1)
    t.right(120)
    koch(t, length, depth - 1)
    t.left(60)
    koch(t, length, depth - 1)


def draw_snowflake(t, length, depth):
    for _ in range(3):
        koch(t, length, depth)
        t.right(120)


# -------------------------
# Spiral
# -------------------------

def draw_spiral(t, length, angle, steps):
    for i in range(steps):
        t.forward(length)
        t.right(angle)
        length += 2


# -------------------------
# Main Program
# -------------------------

def main():
    print("===== Turtle Pattern Generator =====")
    print("1. Koch Snowflake")
    print("2. Spiral")

    choice = input("Choose a pattern: ")

    width = int(input("Screen width: "))
    height = int(input("Screen height: "))

    bg_color = input("Background color: ")
    pen_color = input("Pen color: ")
    pen_size = int(input("Pen size: "))

    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor(bg_color)
    screen.title("Turtle Pattern Generator")

    t = turtle.Turtle()
    t.color(pen_color)
    t.pensize(pen_size)
    t.speed(0)

    if choice == "1":
        length = int(input("Snowflake side length: "))
        depth = int(input("Recursion depth (0-5): "))

        t.penup()
        t.goto(-length / 2, length / 3)
        t.pendown()

        draw_snowflake(t, length, depth)

    elif choice == "2":
        length = int(input("Starting length: "))
        angle = float(input("Turning angle: "))
        steps = int(input("Number of steps: "))

        draw_spiral(t, length, angle, steps)

    else:
        print("Invalid choice.")

    turtle.done()


if __name__ == "__main__":
    main()
