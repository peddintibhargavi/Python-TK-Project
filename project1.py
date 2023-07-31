import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Graphic Model with Tkinter")

# Create a canvas widget
canvas_width = 400
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Function to draw a rectangle on the canvas
def draw_rectangle():
    x1, y1 = 50, 50
    x2, y2 = 150, 100
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

# Function to draw an oval on the canvas
def draw_oval():
    x1, y1 = 200, 50
    x2, y2 = 300, 100
    canvas.create_oval(x1, y1, x2, y2, fill="red")

# Function to draw a line on the canvas
def draw_line():
    x1, y1 = 50, 200
    x2, y2 = 350, 250
    canvas.create_line(x1, y1, x2, y2, fill="green", width=3)

# Button to draw a rectangle
rectangle_btn = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
rectangle_btn.pack()

# Button to draw an oval
oval_btn = tk.Button(root, text="Draw Oval", command=draw_oval)
oval_btn.pack()

# Button to draw a line
line_btn = tk.Button(root, text="Draw Line", command=draw_line)
line_btn.pack()

# Start the main event loop
root.mainloop()
