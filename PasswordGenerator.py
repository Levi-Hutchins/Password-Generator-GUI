import tkinter as tk
from tkinter import ttk
import string
import random

def PasswordGenerator():

    everything = list(string.ascii_lowercase+string.ascii_uppercase+string.digits+"!@#$%^&()")
    random.shuffle(everything)
    password = []
    for i in range(14):
        password.append(random.choice(everything))
    random.shuffle(password)
    generatedPassword = "".join(password)

    return generatedPassword

def passwordsWindow():
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Passwords ")
    ttk.Label(tab1)
    tabControl.pack(expand=1, fill="both")

    displayPassword = ""

    for j in range(5):
        displayPassword += PasswordGenerator() +"\n\n"

    ttk.Label(tab1,text=displayPassword).grid(column = 0,
                               row = 0,
                               padx = 30,
                               pady = 30)
    storePassword(displayPassword)

def storePassword(generatedPasswords):

    try:
        with open("NotPasswords.txt","w") as passwordFile:
            passwordFile.write("Please keep the following passwords safe\n")
            passwordFile.write(generatedPasswords)
    except FileNotFoundError:
        print(passwordFile," Does not exist!")

def main():
    global win
    global tabControl

    win = tk.Tk()
    win.geometry("501x250")
    win.title("Password Generator")

    tabControl = ttk.Notebook(win)

    aboutTab = ttk.Frame(tabControl)
    aboutInfo = "This is a random password generator designed and developed by\nLevi Hutchins. " \
                "On the Generator tab there is a button that once\nclicked will create a new tab " \
                "called Passwords which display 5 strong\npasswords. It will then save those passwords to" \
                "a document in the \nsame repository as the program."
    tabControl.add(aboutTab,text="About")
    ttk.Label(aboutTab,text=aboutInfo).grid(column = 0,
                               row = 0,
                               padx = 30,
                               pady = 30)
    tabControl.pack(expand=1,fill="both")

    generatorTab = ttk.Frame(tabControl)
    tabControl.add(tab1,text="Generator")
    ttk.Label(generatorTab)
    tabControl.pack(expand=1,fill="both")

    genButton = tk.Button(generatorTab,text="Generate Passwords",command=lambda:passwordsWindow())
    genButton.pack()

    win.mainloop()


main()
