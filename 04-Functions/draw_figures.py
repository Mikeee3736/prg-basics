import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Draw square
figures.pen.penup()
figures.pen.goto(100, -250)
figures.pen.pendown()
figures.draw_square(50)

# Draw triangle
figures.pen.penup()
figures.pen.goto(-100, -100)
figures.pen.pendown()
figures.draw_triangle(100)

# Draw rectangle
figures.pen.penup()
figures.pen.goto(0, 200)
figures.pen.pendown()
figures.draw_rectangle(30, 60)

# Hide turtle and finish
figures.pen.hideturtle()
window.mainloop()
