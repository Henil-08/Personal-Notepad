from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)


def openFile():
    global file
    textArea.delete(1.0, END)
    file = askopenfilename(defaultextension=".txt", filetypes=(("All Files", "*.*"), ("Text Documents", "*.txt")))

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close


def saveFile():
    global file 

    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=(("All Files", "*.*"), ("Text Documents", "*.txt")))

        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close
            root.title(os.path.basename(file) + " - Notepad")
    
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close

def saveexitFile():
    global file 

    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=(("All Files", "*.*"), ("Text Documents", "*.txt")))

        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close
            root.title(os.path.basename(file) + " - Notepad")
            root.destroy()
    
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close
        root.destroy()


def exitFile():
    root.destroy()


def cut():
    textArea.event_generate(("<<Cut>>"))


def copy():
    textArea.event_generate(("<<Copy>>"))


def paste():
    textArea.event_generate(("<<Paste>>"))


def about():
    showinfo(title="Notepad", message="Created By Henil Gajjar")


if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("700x500")
    
    # Adding the Text Box
    textArea = Text(root, font="lucida 13")
    file = None
    textArea.pack(expand=True, fill=BOTH)

    # Adding Menus and SubMenus
    mainMenu = Menu(root)
    fileMenu = Menu(mainMenu, tearoff=0)

    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Save and Exit", command=saveexitFile)
    fileMenu.add_command(label="Exit", command=exitFile)
    mainMenu.add_cascade(label="File", menu=fileMenu)

    editMenu = Menu(mainMenu, tearoff=0)
    editMenu.add_command(label="Cut                       Ctrl + X", command=cut)
    editMenu.add_command(label="Copy                    Ctrl + C", command=copy)
    editMenu.add_command(label="Paste                    Ctrl + V", command=paste)
    mainMenu.add_cascade(label="Edit", menu=editMenu)

    helpMenu = Menu(mainMenu, tearoff=0)
    helpMenu.add_command(label="About", command=about)
    mainMenu.add_cascade(label="Help", menu=helpMenu)   

    # Adding the Scroll bar
    scrollBar = Scrollbar(textArea)
    scrollBar.pack(side=RIGHT, fill=Y)

    root.config(menu=mainMenu)
    scrollBar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)
    root.mainloop()

