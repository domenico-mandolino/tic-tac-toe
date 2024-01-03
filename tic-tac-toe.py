import tkinter as tk
from tkinter import messagebox
from ia import ia
from score_manager import ScoreManager

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [0] * 9

        self.score_manager = ScoreManager()
        self.score_manager.load_scores()

        self.buttons = [tk.Button(master, text="", font=("Helvetica", 24), width=5, height=2, command=lambda i=i: self.make_move(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

    def make_move(self, index):
        if self.board[index] == 0:
            self.board[index] = 1 if self.current_player == "X" else 2
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.score_manager.update_score(self.current_player)
                self.reset_game()
            elif 0 not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

                # Si le prochain joueur est l'IA, appeler la fonction pour son tour
                if self.current_player == "O":
                    self.ia_move()

    def ia_move(self):
        # Appeler la fonction de l'IA pour obtenir le meilleur mouvement
        move = ia(self.board, "O")
        if move is not False:
            self.make_move(move)

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != 0:
                return True
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != 0:
                return True
        if self.board[0] == self.board[4] == self.board[8] != 0:
            return True
        if self.board[2] == self.board[4] == self.board[6] != 0:
            return True
        return False


    def reset_game(self):
        for i in range(9):
            self.board[i] = 0
            self.buttons[i].config(text="")
        self.current_player = "X"

# Exemple d'utilisation
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
