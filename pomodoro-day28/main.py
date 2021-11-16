from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1.5
reps = 1
tick_text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    time_min = 0
    if reps % 2 == 1:
        time_min = work_time
        head_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        time_min = long_break_time
        head_label.config(text="Long Break", fg=RED)
    else:
        time_min = short_break_time
        head_label.config(text="Short Break", fg=PINK)
    count_down(time_min)
    reps += 1


def reset_timer():
    global timer
    global tick_text
    global reps
    window.after_cancel(timer)
    head_label.config(text = "Timer")
    tick_text = ""
    reps = 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    # print(count)
    global tick_text
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    if count == 0:
        if reps % 2 == 0 and reps < 8:
            tick_text += "✓"
            tick_label.config(text=tick_text)

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

head_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
head_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# count_down(5)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

tick_label = Label(text="")
tick_label.grid(row=3, column=1)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command = reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
