from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "\u2713"
reps = 0
count = 0
countdown_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    global count
    count = 0
    window.after_cancel(countdown_timer)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text,text = "00:00")
    checkbutton.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Break", fg=RED)
        add_check()
        bring_to_front()
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Break", fg=PINK)
        add_check()
        bring_to_front()
        
    else:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec:02d}")
    if count > 0:
        global countdown_timer
        countdown_timer = window.after(1000, countdown, count -1)
    else:
        start_timer()
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
tomato = PhotoImage(file = "100DaysCoding/Day 28 Pomodoro/tomato.png")
window.config(padx=100, pady=50, bg=YELLOW)

#put a tomato picture to the screen
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112,image = tomato)
timer_text = canvas.create_text(100,140, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(row=1, column=3)

#add a checkmark for every working phase
def add_check():
    global count
    count += 1 
    new_checkmark = CHECKMARK * count
    checkbutton.config(text=new_checkmark)

#Make window popup in front
def bring_to_front():
    window.focus_force()


#Labels
timer = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=3)
timer.config(padx=10,pady=10)

checkbutton = Label(fg=GREEN, bg=YELLOW)
checkbutton.grid(column=3, row=3)


#Buttons Start and Reset
button = Button(text="Start", command=start_timer, bg=YELLOW, bd=0, highlightthickness=0)
button.grid(column=2, row=2)
button.config(pady=2, padx=2)

button2 = Button(text="Reset", command=reset_timer, bg=YELLOW,bd=0, highlightthickness=0)
button2.grid(column=5, row=2)
button2.config(pady=2, padx=2)




window.mainloop()
