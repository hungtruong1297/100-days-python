from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 1
check_marks = ''
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    window.after_cancel(timer)
    
    check_mark_text.config(text='')
    timer_text.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(clock_text, text="00:00")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global check_marks

    WORK_SEC = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_text.config(text="WORK", fg=GREEN)
        count_down(WORK_SEC)
        print(f'reps:{reps}')
        print(f'period: WORK')

    if reps == 2 or reps == 4 or reps == 6:
        timer_text.config(text="BREAK", fg=PINK)
        count_down(SHORT_BREAK_SEC)
        print(f'reps:{reps}')
        print(f'period: SHORT_BREAK')

    if reps == 8:
        timer_text.config(text="BREAK", fg=RED)
        count_down(LONG_BREAK_SEC)
        print(f'reps:{reps}')
        print(f'period: LONG_BREAK')
        
    if reps == 9:
        timer_text.config(text="DONE", fg=RED)
        print(f'Stop timer')
        # TODO: implement stop timer

    ## add check marks
    if reps % 2 == 0 and reps != 8:
        check_marks = check_marks + "✔"
        check_mark_text.config(text=check_marks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    global timer
    
    minute = floor(count / 60)
    second = count % 60

    if second < 10:
        second = f'0{second}'

    count_in_text = f'{minute}:{second}'
    canvas.itemconfig(clock_text, text=count_in_text)
    if count == 0:
        reps = reps + 1
        start_timer()
    if count>0:
        timer = window.after(1, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_text = Label(text="Timer", bg=YELLOW, fg=GREEN ,font=(FONT_NAME, 45))
timer_text.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/hung.truongngoc/Documents/self-projects/100-days-python/pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)

clock_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_text = Label(text=check_marks, fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark_text.grid(row=3, column=1)










window.mainloop()