import tkinter as tk

labeltext = "I should go home"
buttontext = "It is morning"

def changelabel():
    global labeltext
    if labeltext == "I should go home":
        labeltext = "I should go outside"
        top_label.config(text=labeltext)
    else:
        labeltext = "I should go home"
        top_label.config(text=labeltext)
    changebutton()
def changebutton():
    global buttontext
    if buttontext == "It is morning":
        buttontext = "It is getting dark"
        bottom_button.config(text=buttontext)
    else:
        buttontext = "It is morning"
        bottom_button.config(text=buttontext)
    inputted_data = user_entry.get()
    print(inputted_data)

main_window = tk.Tk()
main_window.title("GUI No.2")
main_window.geometry('200x250')

top_label = tk.Label(main_window, text=labeltext)
top_label.pack(side="top")

bottom_button = tk.Button(main_window, text=buttontext, command=changelabel)
bottom_button.pack(side="bottom")

user_entry = tk.Entry(main_window)
user_entry.pack()

main_window.mainloop()