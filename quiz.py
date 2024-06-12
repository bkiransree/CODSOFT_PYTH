import tkinter as tk
from tkinter import messagebox
import random

class QuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
                "answer": "B"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "B"
            },
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "options": ["A. Ernest Hemingway", "B. Harper Lee", "C. J.K. Rowling", "D. George Orwell"],
                "answer": "B"
            }
        ]
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), width=30, command=lambda idx=i: self.select_option(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
            self.current_question_index += 1
        else:
            self.show_result()

    def select_option(self, option_idx):
        selected_option = self.questions[self.current_question_index - 1]["options"][option_idx]
        correct_option = self.questions[self.current_question_index - 1]["answer"]
        if selected_option.startswith(correct_option):
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Your answer is incorrect!\nThe correct answer is: {correct_option}")
        self.next_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour final score is: {self.score}")

def main():
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
