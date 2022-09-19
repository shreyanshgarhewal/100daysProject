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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
minutes = 00
seconds = 12
time_0 = f"{minutes}" + ":" + f"{seconds}"


def reset_timer():
    global timer, m, s
    m = minutes
    s = seconds

    if m >= 10:
        if s < 10:
            timer = f"{m}" + ":" + f"0{s}"
        else:
            timer = f"{m}" + ":" + f"{s}"
    else:
        if s < 10:
            timer = f"0{m}" + ":" + f"0{s}"

        else:
            timer = f"0{m}" + ":" + f"{s}"
    canvas.itemconfig(timer_text, text=timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
m = minutes
s = seconds

timer = f"{m}" + ":" + f"{s}"


def count_down():
    global timer, m, s
    if m >= 0 & s >= 0:

        if m >= 10:
            if s < 10:
                timer = f"{m}" + ":" + f"0{s}"
            else:
                timer = f"{m}" + ":" + f"{s}"
        else:
            if s < 10:
                timer = f"0{m}" + ":" + f"0{s}"

            else:
                timer = f"0{m}" + ":" + f"{s}"

        if s == 0:
            m -= 1
            s = 59

        s = s - 1

        canvas.itemconfig(timer_text, text=timer)
        window.after(1000, count_down)
        print(timer)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label()
title_label.config(text="-Timer-", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
title_label.grid(row=0, column=1)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_img)
timer_text = canvas.create_text(105, 140, text="00:00", fill="white", font=("Arial", 40, "bold"))
canvas.grid(row=1, column=1)


start_button = Button()
start_button["text"] = "start"
start_button.config(command=count_down)
start_button.grid(row=2, column=0)

check_label = Label()
check_label.config(text="✔", bg=YELLOW, fg=GREEN, font=("Arial", 20, "bold"))
check_label.grid(row=3, column=1)

reset_button = Button()
reset_button["text"] = "reset"
reset_button.config(command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
