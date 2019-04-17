from tkinter import Tk
from tkinter import Button


SIZE = 20
run = 0

color_live = 'blue'
color_die = "red"
count_cells_around_for_live = 3


def change_run():
    global run
    run = (run + 1) % 2


class But:
    def __init__(self):
        self.button = Button(root)
        self.button.bind("<Button-1>", self.pressed)
        self.button["width"] = 1
        self.button["height"] = 1
        self.button["bg"] = color_die
        self.alive = 0

    def pressed(self, event):
        self.alive = (self.alive  + 1) % 2
        if self.alive == 1:
            self.button["bg"] = color_live
        else:
            self.button["bg"] = color_die


def rpressed(move):
    buffer = []
    for i in range(1, SIZE - 1):
        for j in range(1, SIZE - 1):
            s = 0
            if koords[i - 1][j].alive == 1:
                s += 1
            if koords[i - 1][j + 1].alive == 1:
                s += 1
            if koords[i][j + 1].alive == 1:
                s += 1
            if koords[i + 1][j + 1].alive == 1:
                s += 1
            if koords[i + 1][j].alive == 1:
                s += 1
            if koords[i + 1][j - 1].alive == 1:
                s += 1
            if koords[i][j - 1].alive == 1:
                s += 1
            if koords[i - 1][j - 1].alive == 1:
                s += 1
            if koords[i][j].alive == 1 and (s < count_cells_around_for_live  - 1 or s > count_cells_around_for_live):
                buffer.append([i, j])
            if koords[i][j].alive == 0 and s == count_cells_around_for_live:
                buffer.append([i, j])
    for i in buffer:
        koords[i[0]][i[1]].pressed("<Button-1>")


root = Tk()
root.title("Game Life")
root.bind("<Button-3>", rpressed)
koords = [[But() for i in range(SIZE)] for j in range(SIZE)]
for i in range(SIZE):
    for j in range(SIZE):
        koords[i][j].button.grid(row=i, column=j)
btn = Button(command=change_run, bg="green")
btn["width"] = 1
btn.grid(row=0, column=0)

while True:
    if run:
        rpressed(1)
    root.update()
