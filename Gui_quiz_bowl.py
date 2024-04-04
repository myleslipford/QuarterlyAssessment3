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
