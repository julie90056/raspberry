import tkinter as tk

root = tk.Tk()

tk.Scale(root, from_=0, to=42).pack()
tk.Scale(root, from_=0, to=200, orient="horizontal").pack()

root.mainloop()