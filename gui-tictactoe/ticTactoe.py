"""
Create a GUI Tic Tac Toe game using tkinter with a 3x3 grid of buttons
where two players take turns clicking to place X and O marks.
Display whose turn it is at the top, and automatically detect when
a player wins (three in a row horizontally, vertically, or diagonally)
or when the game ends in a draw.
Show a message announcing the winner or draw, include a "New Game" button
to reset the board, and keep track of the score for both Player X and Player O
across multiple rounds.
"""
import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.score_x = 0
        self.score_o = 0

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="Tic Tac Toe", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)


        # Score Board
        self.score_label = tk.Label(self.root, text=f"Player X: {self.score_x}  |  Player O: {self.score_o}", font=("Helvetica", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text=f"Player {self.current_player}'s Turn", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
        self.result_label.pack(pady=5)

        # Game Board
        self.board_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.board_frame.pack(pady=20)

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.board_frame, text="", width=10, height=3, font=("Helvetica", 16),
                               bg="#ffffff", fg="#333", command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        # New Game Button
        self.new_game_btn = tk.Button(self.root, text="New Game", command=self.new_game, bg="#ffeb3b")
        self.new_game_btn.pack(pady=5)

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner() and self.current_player == "X":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                self.show_winner()
            elif "" not in self.board:
                self.show_draw()
            else:
                self.switch_player()
                self.root.after(500, self.computer_move)

    def computer_move(self):
        if not self.check_winner() and "" in self.board:
            available_moves = [i for i, x in enumerate(self.board) if x == ""]
            if available_moves:
                move = random.choice(available_moves)
                self.board[move] = "O"
                self.buttons[move].config(text="O")

                if self.check_winner():
                    self.show_winner()
                elif "" not in self.board:
                    self.show_draw()
                else:
                    self.switch_player()

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != "":
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True

        return False

    def show_winner(self):
        winner = "X" if self.current_player == "O" else "O" # This logic was slightly flawed in original because switch_player wasn't called yet? 
        # Actually, if check_winner is true, current_player is the one who just moved.
        # Wait, in on_button_click:
        # 1. set board[index] = current_player (e.g., X)
        # 2. check_winner() -> True
        # 3. show_winner()
        # So current_player is the winner.
        
        winner = self.current_player
        if winner == "X":
            msg = "Player Win!"
        else:
            msg = "Computer Win!"
            
        self.result_label.config(text=msg, fg="green")
        self.update_score(winner)

    def show_draw(self):
        self.result_label.config(text="It's a Draw!", fg="blue")

    def update_score(self, winner):
        if winner == "X":
            self.score_x += 1
        else:
            self.score_o += 1
        self.score_label.config(text=f"Player X: {self.score_x}  |  Player O: {self.score_o}")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.result_label.config(text=f"Player {self.current_player}'s Turn", fg="#333")

    def new_game(self):
        self.board = ["" for _ in range(9)]
        for button in self.buttons:
            button.config(text="")
        self.result_label.config(text="")
        self.current_player = "X"
        self.result_label.config(text=f"Player {self.current_player}'s Turn", fg="#333")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
