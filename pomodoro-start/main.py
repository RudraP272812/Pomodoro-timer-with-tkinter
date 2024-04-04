"""
# Author: Rudra Patel
# Date: 04/04/2024
#This Python project implements a timer based on the Pomodoro Technique,
# originally conceived by Francesco Cirillo in the late 1980s.

This technique uses a timer to break work down into focused intervals
(typically 25 minutes) separated by short breaks (typically 5 minutes).

This project will likely involve functionalities like:
  * Setting the work and break durations
  * Starting and resetting the timer
  * Keeping track of completed work sessions
  * Displaying the remaining time in the current interval
"""
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- Global variables ------------------------------- #
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
        Reset the timer to its initial state.

        This function resets the global `reps` variable to 0,
        cancels any existing timer using `after_cancel`, resets
        the label text to "Timer" with color set to GREEN, clears
        any checkmarks displayed, and resets the canvas timer text
        to "00:00".
    """
    global reps
    global timer
    window.after_cancel(timer)
    reps = 0
    label.config(text="Timer", fg=GREEN)
    checkMark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
        Start the timer based on the current rep count.

        This function increments the `reps` global variable by 1
        and determines whether to start a work session, short break,
        or long break based on the current rep count. It calls the
        `count_down` function with appropriate time duration and updates
        the label text accordingly.
    """
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
       Start the countdown timer.

       This function takes the count in seconds as input and converts
       it to minutes and seconds. It updates the canvas timer text with
       the current count, and if the count is greater than 0, schedules
       another call to `count_down` after 1 second. If the count reaches
       0, it calls `start_timer` to initiate the next timer session.
    """
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✓"
        checkMark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label()
label.config(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
Photo_image = PhotoImage(file="tomato.png")
canvas.create_image(101, 113, image=Photo_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

button = Button(text="Start", command=start_timer, highlightthickness=0)
button.grid(column=0, row=2)

button2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=2)

checkMark = Label(text="", fg=GREEN, bg=YELLOW)
checkMark.grid(column=1, row=3)

# to keep window on.
window.mainloop()
