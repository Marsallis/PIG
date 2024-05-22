import tkinter as tk
from tkinter import messagebox
import random

class PigGame:
    def __init__(self, players):
        self.players = players
        self.max_score = 50
        self.player_scores = [0 for _ in range(players)]
        self.current_score = 0
        self.current_player = 0

    def roll(self):
        value = random.randint(1, 6)
        if value == 1:
            self.current_score = 0
            self.player_scores[self.current_player] = 0
            self.next_player()
            return value, True
        else:
            self.current_score += value
            return value, False

    def hold(self):
        self.player_scores[self.current_player] += self.current_score
        if self.player_scores[self.current_player] >= self.max_score:
            return True
        self.next_player()
        return False

    def next_player(self):
        self.current_score = 0
        self.current_player = (self.current_player + 1) % self.players

class PigGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pig Game")
        self.setup_game()

    def setup_game(self):
        self.players_label = tk.Label(self.root, text="Enter the number of players (2-4):")
        self.players_label.pack()

        self.players_entry = tk.Entry(self.root)
        self.players_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        players = self.players_entry.get()
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                self.game = PigGame(players)
                self.show_game_interface()
            else:
                messagebox.showerror("Error", "Player total must be between 2 - 4 players")
        else:
            messagebox.showerror("Error", "Invalid input, try again")

    def show_game_interface(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.score_label = tk.Label(self.root, text=f"Player {self.game.current_player + 1}'s turn")
        self.score_label.pack()

        self.roll_button = tk.Button(self.root, text="Roll", command=self.roll)
        self.roll_button.pack()

        self.hold_button = tk.Button(self.root, text="Hold", command=self.hold)
        self.hold_button.pack()

        self.dice_label = tk.Label(self.root, text="")
        self.dice_label.pack()

        self.current_score_label = tk.Label(self.root, text="Current score: 0")
        self.current_score_label.pack()

        self.total_score_label = tk.Label(self.root, text="Total scores: " + str(self.game.player_scores))
        self.total_score_label.pack()

    def roll(self):
        value, turn_over = self.game.roll()
        self.dice_label.config(text=f"Rolled: {value}")
        if turn_over:
            self.update_ui()
            messagebox.showinfo("Turn Over", "You rolled a 1! Turn over.")
        self.current_score_label.config(text=f"Current score: {self.game.current_score}")
        self.total_score_label.config(text="Total scores: " + str(self.game.player_scores))

    def hold(self):
        if self.game.hold():
            messagebox.showinfo("Game Over", f"Player {self.game.current_player + 1} wins!")
            self.root.quit()
        else:
            self.update_ui()

    def update_ui(self):
        self.score_label.config(text=f"Player {self.game.current_player + 1}'s turn")
        self.current_score_label.config(text="Current score: 0")
        self.total_score_label.config(text="Total scores: " + str(self.game.player_scores))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Pig Game")
    app = PigGameGUI(root)
    root.mainloop()
