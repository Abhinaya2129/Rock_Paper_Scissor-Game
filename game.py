import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Rock-Paper-Scissors Game")

    
        self.user_score = 0
        self.computer_score = 0

        
        self.instructions = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.instructions.pack(pady=10)

        
        self.rock_button = tk.Button(window, text="Rock", width=20, command=lambda: self.play("Rock"))
        self.rock_button.pack(pady=5)
        self.paper_button = tk.Button(window, text="Paper", width=20, command=lambda: self.play("Paper"))
        self.paper_button.pack(pady=5)
        self.scissors_button = tk.Button(window, text="Scissors", width=20, command=lambda: self.play("Scissors"))
        self.scissors_button.pack(pady=5)

        
        self.result_label = tk.Label(window, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        
        self.score_label = tk.Label(window, text="Scores - You: 0, Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.update_scores(result)
        self.show_result(user_choice, computer_choice, result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "User"
        else:
            return "Computer"

    def update_scores(self, result):
        if result == "User":
            self.user_score += 1
        elif result == "Computer":
            self.computer_score += 1
        self.score_label.config(text=f"Scores - You: {self.user_score}, Computer: {self.computer_score}")
    def reset(self,user_score,computer_score):
        self.user_score = 0
        self.computer_score = 0

    def show_result(self, user_choice, computer_choice, result):
        if result == "Tie":
            result_text = "It's a tie!"
        elif result == "User":
            result_text = "You win!"
        else:
            result_text = " You Lose. "

        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result_text}")
        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            window.reset(0,0)
        else:
            window.quit()
        
if __name__ == "__main__":
    window = tk.Tk()
    game = RockPaperScissorsGame(window)
    window.mainloop()
