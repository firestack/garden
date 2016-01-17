
from Tkinter import *

MAX_ROWS = 36
FONT_SIZE = 10 # (pixels)

root = Tk()
root.title("Named colour chart")
row = 0
col = 0
for color in COLORS:
  e = Label(root, text=color, background=color, 
        font=(None, -FONT_SIZE))
  e.grid(row=row, column=col, sticky=E+W)
  row += 1
  if (row > MAX_ROWS):
    row = 0
    col += 1

root.mainloop()