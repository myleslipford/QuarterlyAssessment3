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


class QuizWindow:
    def __init__(self, category):
        self.category = category

        self.questions = self.load_questions_from_db()
        self.total_questions = len(self.questions)
        self.correct_answers = 0

        self.root = Tk()
        self.root.title("Quiz Window")

        self.current_question_index = 0

        self.selected_option = StringVar()

        self.create_widgets()
        self.display_question()  # Call display_question after creating all widgets

    def create_widgets(self):
        self.question_label = Label(self.root, text="")
        self.question_label.pack(padx=10, pady=10)

        self.options = []
        for i in range(4):
            option = StringVar()
            self.options.append(option)
            ttk.Radiobutton(self.root, textvariable=option, variable=self.selected_option, value=str(i)).pack(anchor="w", padx=10)

        self.feedback_label = Label(self.root, text="")
        self.feedback_label.pack(pady=5)

        self.submit_button = Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.next_button = Button(self.root, text="Next Question", command=self.display_next_question)
        self.next_button.pack(pady=5)
        self.next_button.pack_forget()  # Hide initially

        self.score_label = Label(self.root, text="")
        self.score_label.pack(pady=5)


    def load_questions_from_db(self):
        conn = sqlite3.connect("QuestionsDatabase.db")
        c = conn.cursor()
        c.execute(f"SELECT question, option1, option2, option3, option4, answer FROM {self.category.replace(' ', '_')}")
        questions = c.fetchall()
        conn.close()
        return questions
    

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question, *options, correct_answer = self.questions[self.current_question_index]
            self.question_label.config(text=question)
            self.selected_option.set("")  # Clear selection
            for i in range(4):
                self.options[i].set(options[i])
        else:
            self.show_score()

    def check_answer(self):
        selected_option = self.selected_option.get()

        if selected_option == "":
            self.feedback_label.config(text="Please select an option.", fg="red")
            return

        selected_option = int(selected_option)
        correct_answer = self.questions[self.current_question_index][-1]
        correct_answer_words = correct_answer.split()  # Split correct answer into words

        selected_option_text = self.options[selected_option].get()
        selected_option_words = selected_option_text.split()  # Split selected option into words

        if all(word in selected_option_words for word in correct_answer_words):
            self.feedback_label.config(text="Correct!", fg="green")
            self.correct_answers += 1
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer is: {correct_answer}", fg="red")

        self.submit_button.pack_forget()  # Hide submit button
        self.next_button.pack()  # Show next button

    def display_next_question(self):
        self.current_question_index += 1
        self.feedback_label.config(text="")
        self.submit_button.pack()  # Show submit button
        self.next_button.pack_forget()  # Hide next button
        self.display_question()

    def show_score(self):
        score_text = f"You have completed the quiz!\nYour score: {self.correct_answers}/{self.total_questions}"
        self.score_label.config(text=score_text)

        back_to_menu_button = Button(self.root, text="Back to Menu", command=self.back_to_menu)
        back_to_menu_button.pack(pady=10)
        
    def back_to_menu(self):
        self.root.destroy()
        root = Tk()
        app = QuizBowlGame(root)
        root.mainloop()

def main():
    root = Tk()
    app = QuizBowlGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()