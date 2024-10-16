import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(True, True)  # Allow window resizing

        self.current_player = "X"
        self.moves_count = 0
        self.x_score = 0  # Player X's score
        self.o_score = 0  # Player O's score
        self.buttons = {}

        # Create score labels
        self.score_frame = tk.Frame(self.root)
        self.score_frame.grid(row=0, column=0, columnspan=3, pady=10)

        self.x_score_label = tk.Label(self.score_frame, text=f"Player X: {self.x_score}", font=("Arial", 14))
        self.x_score_label.grid(row=0, column=0, padx=20)

        self.o_score_label = tk.Label(self.score_frame, text=f"Player O: {self.o_score}", font=("Arial", 14))
        self.o_score_label.grid(row=0, column=1, padx=20)

        self.create_buttons()

    # Function to check for a win or draw using the most recent move
    def check_winner(self, row, col):
        # Check row
        if all(self.buttons[(row, c)]["text"] == self.current_player for c in range(3)):
            return True
        # Check column
        if all(self.buttons[(r, col)]["text"] == self.current_player for r in range(3)):
            return True
        # Check main diagonal
        if row == col and all(self.buttons[(i, i)]["text"] == self.current_player for i in range(3)):
            return True
        # Check anti-diagonal
        if row + col == 2 and all(self.buttons[(i, 2-i)]["text"] == self.current_player for i in range(3)):
            return True
        # Check for draw
        if self.moves_count == 9:
            return "Draw"
        return None

    # Handle button clicks
    def on_click(self, row, col):
        if self.buttons[(row, col)]["text"] == "":
            self.buttons[(row, col)]["text"] = self.current_player
            self.moves_count += 1
            result = self.check_winner(row, col)

            if result:
                if result == "Draw":
                    messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                else:
                    messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                    self.update_score()  # Update score when there is a winner
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    # Update the score based on the current player
    def update_score(self):
        if self.current_player == "X":
            self.x_score += 1
            self.x_score_label.config(text=f"Player X: {self.x_score}")
        else:
            self.o_score += 1
            self.o_score_label.config(text=f"Player O: {self.o_score}")

    # Reset the game state
    def reset_game(self):
        self.current_player = "X"
        self.moves_count = 0
        for button in self.buttons.values():
            button["text"] = ""

    # Create and arrange buttons in a grid
    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[(row, col)] = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                                                     command=lambda r=row, c=col: self.on_click(r, c))
                self.buttons[(row, col)].grid(row=row+1, column=col, sticky="nsew")  # Adjusted grid row

        # Configure row and column expansion
        for i in range(3):
            self.root.grid_rowconfigure(i+1, weight=1)  # Adjusted to account for score display
            self.root.grid_columnconfigure(i, weight=1)


# Initialize the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
