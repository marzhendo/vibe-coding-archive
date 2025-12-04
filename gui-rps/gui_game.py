"""
Refactor the add() function to make it more efficient.
Add High Scores feature to the app.
Add unit tests for the calculator class. Use vitest as the test framework.
Add a reset button to the app.

"""
import tkinter as tk

import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f0f0")

        self.player_score = 0
        self.computer_score = 0
        self.ties_score = 0

        # Title
        self.title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Score Board
        self.score_label = tk.Label(root, text=f"Player: 0  |  Computer: 0  |  Ties: 0", font=("Helvetica", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        # Result Display
        self.result_label = tk.Label(root, text="Choose your move!", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
        self.result_label.pack(pady=20)

        # Buttons Frame
        self.buttons_frame = tk.Frame(root, bg="#f0f0f0")
        self.buttons_frame.pack(pady=20)

        # Buttons
        self.rock_btn = tk.Button(self.buttons_frame, text="Rock", width=10, command=lambda: self.play("rock"), bg="#ffcccc")
        self.rock_btn.pack(side=tk.LEFT, padx=10)

        self.paper_btn = tk.Button(self.buttons_frame, text="Paper", width=10, command=lambda: self.play("paper"), bg="#ccffcc")
        self.paper_btn.pack(side=tk.LEFT, padx=10)

        self.scissors_btn = tk.Button(self.buttons_frame, text="Scissors", width=10, command=lambda: self.play("scissors"), bg="#ccccff")
        self.scissors_btn.pack(side=tk.LEFT, padx=10)

        # Reset Button
        self.reset_btn = tk.Button(root, text="Reset", command=self.reset_game, bg="#ffeb3b")
        self.reset_btn.pack(pady=5)

        # Quit Button
        self.quit_btn = tk.Button(root, text="Quit", command=root.quit, bg="#ddd")
        self.quit_btn.pack(pady=20)

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties_score = 0
        self.score_label.config(text=f"Player: 0  |  Computer: 0  |  Ties: 0")
        self.result_label.config(text="Choose your move!", fg="#333")

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, player, computer):
        if player == computer:
            return 'tie'
        elif ((player == 'rock' and computer == 'scissors') or
              (player == 'paper' and computer == 'rock') or
              (player == 'scissors' and computer == 'paper')):
            return 'player'
        else:
            return 'computer'

    def play(self, player_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)

        result_text = f"You chose: {player_choice.title()}\nComputer chose: {computer_choice.title()}\n\n"

        if winner == 'player':
            self.player_score += 1
            result_text += "✅ You Win!"
            self.result_label.config(fg="green")
        elif winner == 'computer':
            self.computer_score += 1
            result_text += "❌ Computer Wins!"
            self.result_label.config(fg="red")
        else:
            self.ties_score += 1
            result_text += "⚖️ It's a Tie!"
            self.result_label.config(fg="blue")

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Player: {self.player_score}  |  Computer: {self.computer_score}  |  Ties: {self.ties_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
