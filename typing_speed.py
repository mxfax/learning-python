from tkinter import *
import time
import math
import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
file='exercisetext.txt' #SAMPLE with the text

start_time = None
finished = False


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Typing speed")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=500,height=500, bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=3)

#Label to display input
lbl = tk.Label(window, text="Type here")
lbl.grid(row=1, column=0)

#Text
text = Text(height=10, width=101)

#Adds some text to begin with.
with open(file, 'r') as f:
    content = f.read()

#List to compare characters with user input later
my_list = [chars for chars in content]

text.insert(INSERT, content)  
text.grid(row=0, column=3)

#block the user input
text.configure(state="disabled")

#Entries
entry = Entry(width=30)
entry.focus()
#Gets text in entry
entry.grid(row=1, column=3)
entry.config(width=100)

#Make window popup in front
def bring_to_front():
    window.focus_force()

checkbutton = Label(fg=GREEN, bg=YELLOW)
checkbutton.grid(column=3, row=2)

#listener and the timer
def on_key_press(event):
    global start_time, finished
    if finished:
        return
    if start_time is None and len(entry.get()) > 0:
        start_time = time.time()

    user_text = entry.get()
    current_index = len(user_text) - 1  #position of the last typed character

    if current_index >= 0:  #check if user typed something
        correct_char = content[current_index]
        typed_char = user_text[current_index]

        if typed_char == correct_char:
            checkbutton.config(text=f"✅ '{typed_char}' is correct", fg=GREEN)
        else:
            checkbutton.config(text=f"❌ Expected '{correct_char}' but got '{typed_char}'", fg=RED)
    else:
        checkbutton.config(text="Start typing...")

    if user_text == content:
        finished = True
        end_time = time.time()
        elapsed = end_time - start_time
        word_count = len(content.split())
        wps = word_count / elapsed
        checkbutton.config(text=f"✅ Completed! {wps:.2f} words/sec", fg=GREEN)

entry.bind("<KeyRelease>", on_key_press)


window.mainloop()
