import tkinter as tk
import random

def play(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    if choice == computer_choice:
        result = f"It's a Tie! Both chose {choice}."
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! {choice} beats {computer_choice}."
    else:
        result = f"You Lose! {computer_choice} beats {choice}."
    
    result_label.config(text=result)

screen = tk.Tk()
screen.title("Length Converter App")
screen.geometry("400x400")

for option in ["Rock", "Paper", "Scissors"]:
    tk.Button(screen, text=option, command=lambda choice=option: play(choice)).pack(pady=10)

result_label = tk.Label(screen, text="", font=("Arial", 14))
result_label.pack(pady=20)

screen.mainloop()