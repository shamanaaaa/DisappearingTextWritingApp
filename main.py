import tkinter as tk
import time

game_on = True
countdown = 5
global count_worlds_outer

app = tk.Tk()
app.title("Text disappearing app")
greeting = tk.Label(text="Start writing to start the countdown to text disappear", height=5, font=("Arial", 20))

text_box = tk.Text()


def retrieve_input():
    text_input = (text_box.get("1.0", 'end-1c'))
    text_split = text_input.split(sep=" ")
    return len(text_split)


def stop():
    global game_on
    game_on = False


exit_button = tk.Button(text="Exit!", width=15, height=2, bg="black", fg="white", command=stop)

while game_on:
    count_worlds_outer = 0
    countdown = 5
    text_box.delete('1.0', 'end-1c')

    while countdown > 0:
        count_worlds_inner = retrieve_input()
        if count_worlds_inner > count_worlds_outer:
            count_worlds_outer = count_worlds_inner
            countdown = 5
        if countdown > 3:
            text_box.config(fg="green")
        elif countdown > 2:
            text_box.config(fg="orange")
        elif countdown > 1:
            text_box.config(fg="red")
        time.sleep(0.01)
        countdown -= 0.01
        greeting.pack()
        text_box.pack()
        exit_button.pack()
        app.update()

