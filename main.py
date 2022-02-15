from tkinter import *

window = Tk()
window.title("Paint")
window.geometry("400x400")
color = "black"


def paint(event):
    global color
    x1, y1 = (event.x - 3), (event.y - 3)
    x2, y2 = (event.x + 3), (event.y + 3)
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def redcolor():
    global color
    color = "red"


def blackcolor():
    global color
    color = "black"


def yellowcolor():
    global color
    color = "yellow"


def bluecolor():
    global color
    color = "blue"


redbutton = Button(window, text="Red", command=redcolor, borderwidth=2, relief="groove")
redbutton.place(width=50, height=25, x=2, y=375)

blackbutton = Button(window, text="Black", command=blackcolor, borderwidth=2, relief="groove")
blackbutton.place(width=50, height=25, x=52, y=375)

yellowbutton = Button(window, text="Yellow", command=yellowcolor, borderwidth=2, relief="groove")
yellowbutton.place(width=50, height=25, x=102, y=375)

bluebutton = Button(window, text="Blue", command=bluecolor, borderwidth=2, relief="groove")
bluebutton.place(width=50, height=25, x=152, y=375)

wn = Canvas(window, width=400, height=365, bg="white")
wn.config(borderwidth=2, relief="groove")
wn.bind("<B1-Motion>", paint)
wn.pack()

mainloop()
