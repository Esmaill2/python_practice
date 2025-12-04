import tkinter as tk
from tkinter import messagebox, filedialog
import CoinFlip

tale=0
head=0

def printing():
    return "hi"

def flip():
    CoinFlip.fliper()
    return CoinFlip.printer()

root = tk.Tk ()
root.title('CoinFliper')
root.geometry("800x500")

btn = tk.Button(root, text="Flip", command=lambda: messagebox.showinfo("result", flip()))
btn.pack()
root.bind('<Return>', lambda event: btn.invoke())

label = tk.Label(root, text="Hello", font=("Arial", 14))
label.pack()


root.mainloop()
