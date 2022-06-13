from tkinter import *
import time
from threading import *

startTime = 0
endTime = 0

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50,pady=50)
# canvas = Canvas(width = 400, height = 200)
# canvas.pack()
# quote_text = canvas.create_text(100, 50, text="This is a sample text for typing. Use this text as reference for typing",  font=("Arial", 10, "bold"),width = 200)
typing_text = Label(window,text = "my much person few head states omes low after any told fly she notice great pager an six done direct",font = ("Arial",10,"bold"),wraplength=500)
typing_text.pack()
# typing_text.
written_text = StringVar()
text = Text(window,wrap = WORD,height = 5)
text.insert(INSERT,"")
text.pack()


# sec = StringVar()
# sec.set('60')
# countdown_label = Label(window, textvariable = sec, width = 2, font = ("Arial", 10))
# countdown_label.pack()
def record_Start(event):
    # print(event)
    # seconds = 60
    # print(seconds)
    # while seconds>-1:
    #     time.sleep(1)
    #     sec.set(seconds)
    #     seconds-=1
    #     window.update()
    global startTime
    startTime = time.time_ns()
    print(startTime)

def record_End():
    global endTime
    endTime = time.time_ns()
    diff = endTime - startTime
    time_in_s = diff/1000000000
    time_in_min = time_in_s/60
    print(f"In min: {time_in_min}")
    typed_text = str(text.get("1.0",END))
    num_words = typed_text.split(" ")
    diff = []
    typed = typing_text.cget("text").split(" ")
    if len(num_words)==len(typed):
        for i in range(0,len(num_words)):
            if num_words[i]!=typed[i]:
                diff.append(typed[i])
        typing_speed = len(num_words) / time_in_min
        print(typing_speed)
        popup = Toplevel(window)
        popup.geometry("750x250")
        popup.title("Result")
        if len(diff) == 0:
            message = Label(popup, text=f"Your typing speed is {int(typing_speed)} WPM.")
            message.pack()
        else:
            message = Label(popup,text=f"You typed the following words incorrectly: {diff}. Your typing speed is: {int(typing_speed)} WPM.")
            message.pack()
    else:
        popup = Toplevel(window)
        popup.geometry("650x150")
        popup.title("Result")
        message = Label(popup, text = "You didn't type the full text. Please attempt the full text before assessing your typing speed.")
        message.pack()
    text.delete("1.0",END)


button = Button(window, text = "Submit", command = record_End)
button.pack()
text.bind("<FocusIn>",record_Start)
window.mainloop()

