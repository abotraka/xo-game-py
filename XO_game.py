import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("400x550")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.player_score = 0
        self.computer_score = 0
        self.starting_player = "You"

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Tic Tac Toe", font=('Helvetica', 18), bg="#f0f0f0").pack(pady=20)

        self.score_label = tk.Label(self, text=f"You: {self.player_score} - Computer: {self.computer_score}", font=('Helvetica', 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        frame = tk.Frame(self)
        frame.pack()

        for i in range(9):
            button = tk.Button(frame, text="", font=('Helvetica', 24), width=5, height=2, command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.reset_button = tk.Button(self, text="Reset Game", font=('Helvetica', 14), bg="#4caf50", fg="white", relief="flat", activebackground="#43a047", command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.reset_scores_button = tk.Button(self, text="Reset Scores", font=('Helvetica', 14), bg="#f44336", fg="white", relief="flat", activebackground="#e53935", command=self.reset_scores)
        self.reset_scores_button.pack(pady=10)

    def make_move(self, index):
        if self.board[index] == "" and self.current_player == "X":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.player_score += 1
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.update_scores()
                self.starting_player = "Computer"
                self.reset_game_board()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game_board()
            else:
                self.current_player = "O"
                self.computer_move()

    def computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ""]
        move = random.choice(available_moves)
        self.board[move] = self.current_player
        self.buttons[move].config(text=self.current_player)
        if self.check_winner():
            self.computer_score += 1
            messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            self.update_scores()
            self.starting_player = "You"
            self.reset_game_board()
        elif "" not in self.board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            self.reset_game_board()
        else:
            self.current_player = "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        if self.starting_player == "Computer":
            self.current_player = "O"
            self.computer_move()
        else:
            self.current_player = "X"

    def reset_game(self):
        self.reset_game_board()
        self.player_score = 0
        self.computer_score = 0
        self.update_scores()

    def reset_scores(self):
        self.player_score = 0
        self.computer_score = 0
        self.update_scores()

    def update_scores(self):
        self.score_label.config(text=f"You: {self.player_score} - Computer: {self.computer_score}")

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
