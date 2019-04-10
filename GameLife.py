from tkinter import *

SIZE = 20

class But:
    def __init__(self):
        self.button = Button(root)
        self.button.bind("<Button-1>", self.pressed)
        #self.button.pack()
        self.button["width"] = 1
        self.button["height"] = 1

        self.button["bg"] = "red"
        self.alive = 0
    def pressed(self, event):
        self.alive = (self.alive  + 1) % 2
        if self.alive == 1:
            self.button["bg"] = "blue"
        else:
            self.button["bg"] = "red"

def rpressed(event):
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
            if koords[i][j].alive == 1 and (s < 2 or s > 3):
                buffer.append([i,j])
            if koords[i][j].alive == 0 and s == 3:
                buffer.append([i,j])
    for i in buffer:
        koords[i[0]][i[1]].pressed("<Button-1>")


root = Tk()
root.title("Game Life")
root.bind("<Button-3>", rpressed)
koords = [[But() for i in range(SIZE)] for j in range(SIZE)]
for i in range(SIZE):
    for j in range(SIZE):
        koords[i][j].button.grid(row = i, column = j)

root.mainloop()