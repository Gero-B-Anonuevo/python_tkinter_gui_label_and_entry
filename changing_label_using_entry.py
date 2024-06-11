import tkinter as tk

labeltext = "What do you want to say?"
buttontext = "Enter"

def changelabel():
    global labeltext
    if labeltext == "What do you want to say?":
        if user_entry.get() == "":
            labeltext = "What do you want to say?"
        else:
            labeltext = user_entry.get()
            top_label.config(text=labeltext)
        changebutton()
    else:
        labeltext = "What do you want to say?"
        top_label.config(text=labeltext)
        user_entry.delete(0, 'end')
        bottom_button.config(text="Enter")
def changebutton():
    global buttontext
    if labeltext == "What do you want to say?":
        buttontext = "Enter"
        bottom_button.config(text=buttontext)
    else:
        buttontext = "Clear"
        bottom_button.config(text=buttontext)
    change_color()
def change_color():
    if user_entry.get() == "":
        bottom_button.config(bg="red")
    else:
        bottom_button.config(bg="white")

main_window = tk.Tk()
main_window.title("GUI No.2")
main_window.geometry('200x250')

top_label = tk.Label(main_window, text=labeltext)
top_label.pack(side="top")

bottom_button = tk.Button(main_window, text=buttontext, command=changelabel)
bottom_button.pack(side="bottom")
bottom_button.config(bg="white")

user_entry = tk.Entry(main_window)
user_entry.pack()

main_window.mainloop()