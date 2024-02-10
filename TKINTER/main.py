import tkinter as tk
from tkinter import ttk
import random
def choose_button(choice):
    computer = random.choice(["Rock", "Paper", "Scissors"])
    winner = find_winner(choice, computer)
    label2.config(text = f"{winner}")
    label3.config(text = f"Your choice: {choice}")
    label4.config(text = f"Computer's choice: {computer}")
def find_winner(user, computer):
    if (user == "Rock" and computer == "Paper") or (user == "Paper" and computer == "Scissors") or (user == "Scissors" and computer == "Rock"):
        return "Computer wins!"
    elif user == computer:
        return "It's a tie!"
    else:
        return "You win!"
root = tk.Tk()
root.title("RockPaperScissors")
root.geometry("500x500")
label1 = ttk.Label(root, text = "Welcome to Rock Paper Scissors!", font = ("Arial", 15))
label1.pack()
label2 = ttk.Label(root, text = "", font = ("Arial", 15))
label2.pack()
label3 = ttk.Label(root, text = "", font = ("Arial", 15))
label3.pack()
label4 = ttk.Label(root, text = "", font = ("Arial", 15))
label4.pack()
frame1 = ttk.Frame(root)
frame1.pack()
rock = ttk.Button(frame1, text = "Rock", command = lambda: choose_button("Rock"))
rock.grid(row = 0, column = 0)
paper = ttk.Button(frame1, text = "Paper", command = lambda: choose_button("Paper"))
paper.grid(row = 0, column = 1)
scissors = ttk.Button(frame1, text = "Scissors", command = lambda: choose_button("Scissors"))
scissors.grid(row = 0, column = 2)
root.mainloop()