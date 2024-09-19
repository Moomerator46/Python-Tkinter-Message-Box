import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys

def show_popup():
  messagebox.showinfo("title here", "message here") # adds an info message box
  messagebox.showwarning("title here", "message here") # adds a warning message box
  messagebox.showerror("title here", "message here") # adds an error message box
  question = messagebox.askquestion("title here", "message here") # asks a yes/no question
  if question == 'yes':
    # if the question answer is yes
    print("clicked yes")
  else:
    # if the question answer was no
    print("clicked no")

def close():
  sys.exit()

window = tk.Tk()
window.title("title of the window here")

txt = ttk.Label(window, text="text of label here")
txt.pack(pady=65)
btn = ttk.Button(master=window, text="Show Pop-Up", command=show_popup)
btn.pack()
ext_btn = ttk.Button(master=window, text="Close", command=close)
ext_btn.pack()

window.mainloop()
