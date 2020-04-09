import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

count_val = 45
label1 = tk.Label(root, text='Hello World test ab ' + str(count_val))
canvas1.create_window(150, 150, window=label1)

count_val = count_val + 3
root.mainloop()
