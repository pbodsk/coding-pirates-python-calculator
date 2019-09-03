from tkinter import *
from tkinter.ttk import Style
import tkinter as tk


class Example(Frame):
    def __init__(self, master):
        super().__init__()
        self.init_ui(master)

    def init_ui(self, master):
        self.style = Style()
        self.style.theme_use("default")
        self.master.title("Calculator")


        self.label = Label(master, text="Enter two numbers")
        self.label.pack()

        self.entry1 = Entry()
        self.entry1.pack()

        self.entry2 = Entry()
        self.entry2.pack()

        self.val = IntVar()
        self.resultLabel = Label(master, textvariable=self.val)
        self.resultLabel.pack()

        buttonFrame = Frame()

        add_button = Button(buttonFrame, text="+", command=self.add)
        add_button.grid(row=0, column=0)

        minus_button = Button(buttonFrame, text="-", command=self.subtract)
        minus_button.grid(row=0, column=1)

        multiply_button = Button(buttonFrame, text="*", command=self.multiply)
        multiply_button.grid(row=0, column=2)

        divide_button = Button(buttonFrame, text="/", command=self.divide)
        divide_button.grid(row=0, column=3)

        clear_button = Button(buttonFrame, text="c", command=self.clear)
        clear_button.grid(row=0, column=4)

        buttonFrame.pack()

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.pack()

    def add(self):
        val1 = int(self.entry1.get())
        val2 = int(self.entry2.get())
        self.val.set(val1 + val2)

    def subtract(self):
        val1 = int(self.entry1.get())
        val2 = int(self.entry2.get())
        self.val.set(val1 - val2)

    def multiply(self):
        val1 = int(self.entry1.get())
        val2 = int(self.entry2.get())
        self.val.set(val1 * val2)

    def divide(self):
        val1 = int(self.entry1.get())
        val2 = int(self.entry2.get())
        self.val.set(val1 / val2)

    def clear(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.val.set(0)
        self.entry1.focus()

def main():
    root = Tk()
    root.geometry("450x250+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()