from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = Tk()
root.title("Calculator")

screen = StringVar()
entry = Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=X, ipadx=8, padx=10, pady=10, ipady=8)

button_frame = Frame(root)
button_frame.pack()

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

i = 0
buttons = []
for btn_text in button_texts:
    button = Button(button_frame, text=btn_text, font="lucida 15", relief=RAISED, width=2)
    button.grid(row=i // 4, column=i % 4)
    button.bind("<Button-1>", click)
    buttons.append(button)
    i += 1

root.mainloop()
