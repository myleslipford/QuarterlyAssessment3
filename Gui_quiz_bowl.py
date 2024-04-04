from tkinter import *
from tkinter import ttk
import sqlite3

class QuizBowlGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Bowl Game")

        self.categories = ["      ", "Business Statistics", "Business Database mgmt Science", "General Biology II", "Mgmt organization Behavior", "Business Applications"]

        self.category_var = StringVar()
        self.category_var.set(self.categories[0])

        self.create_widgets()

    def create_widgets(self):
            Label(self.master, text="Select a Category:").grid(row=0, column=0, padx=10, pady=10)

            category_menu = OptionMenu(self.master, self.category_var, *self.categories)
            category_menu.grid(row=0, column=1, padx=10, pady=10)

            start_button = Button(self.master, text="Start Quiz Now", command=self.start_quiz)
            start_button.grid(row=1, columnspan=2, padx=10, pady=10)
            
    def start_quiz(self):
        category = self.category_var.get()
        self.master.destroy()
        QuizWindow(category)