"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
import random 
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    """
    Returns a random choice for the computer in a game of rock, paper, scissors.

    The function selects one of the three options: 'rock', 'paper', or 'scissors'
    using the random module.

    Returns:
        str: A string representing the computer's choice ('rock', 'paper', or 'scissors').
    """
    return random.choice(['rock', 'paper', 'scissors']) 

def determine_winner(player, computer):
    """
    Determines the winner of a rock-paper-scissors game.

    Parameters:
        player (str): The choice of the player, must be one of 'rock', 'paper', or 'scissors'.
        computer (str): The choice of the computer, must be one of 'rock', 'paper', or 'scissors'.

    Returns:
        str: 'tie' if both choices are the same, 'player' if the player wins, 
             or 'computer' if the computer wins.
    """
    if player == computer:
        return 'tie'
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')
    ):
        return 'player' 
    else:
        return 'computer'
    
def load_high_score():
    try:
        with open('high_scores.txt', 'r') as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(score):
    current_high = load_high_score()
    if score > current_high:
        with open('high_scores.txt', 'w') as f:
            f.write(str(score))

def main(): 
    """
    Main function to run a Rock, Paper, Scissors game between a player and the computer.
    The function implements a game loop that:
    - Prompts the player to enter their choice (rock, paper, scissors) or quit
    - Accepts shorthand inputs (r, p, s) and maps them to full choice names
    - Validates player input and handles invalid entries
    - Generates a random computer choice
    - Determines the winner of each round
    - Tracks and displays the running score for both player and computer
    - Continues until the player enters 'quit'
    The game maintains a score counter that persists across multiple rounds
    and displays the updated score after each round is played.
    """
    player_score = 0 
    computer_score = 0 
    tie_score = 0
    print(f"Current high score: {load_high_score()}")
    while True:
        player_input = input("Enter rock (r), paper (p), scissors (s) or quit to exit: ").lower()
        
        # Map shortcuts to full names
        choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        player_choice = choice_map.get(player_input, player_input)
        if player_choice == 'quit':
            save_high_score(player_score)
            print(f"Final score: {player_score}. High score saved if updated.")
            print("Thanks for playing!")
            break 
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue 
        computer_choice = get_computer_choice() 
        print(f"Computer chose: {computer_choice}") 
        winner = determine_winner(player_choice, computer_choice) 
        if winner == 'player':
            player_score += 1 
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1 
            print("Computer wins this round!")
        else:
            tie_score += 1
            print("It's a tie!")
        print(f"Scoreboard - You: {player_score}, Computer: {computer_score}, Ties: {tie_score}\n") 

def gui_app():
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    
    # Global scores
    player_score = 0
    computer_score = 0
    tie_score = 0
    
    def view_high_scores():
        high = load_high_score()
        messagebox.showinfo("High Scores", f"Your high score: {high}")
    
    def on_quit():
        save_high_score(player_score)
        root.quit()
        
    def reset_game():
        nonlocal player_score, computer_score, tie_score
        save_high_score(player_score)  # Update high score if current player score is higher
        player_score = 0
        computer_score = 0
        tie_score = 0
        score_label.config(text=f"Scoreboard - You: {player_score}, Computer: {computer_score}, Ties: {tie_score}")
        result_label.config(text="")
        computer_choice_label.config(text="")
    
    # Labels
    score_label = tk.Label(root, text=f"Scoreboard - You: {player_score}, Computer: {computer_score}, Ties: {tie_score}")
    score_label.pack(pady=10)
    
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)
    
    computer_choice_label = tk.Label(root, text="")
    computer_choice_label.pack(pady=10)
    
    def play_round(player_choice):
        nonlocal player_score, computer_score, tie_score
        computer_choice = get_computer_choice()
        computer_choice_label.config(text=f"Computer chose: {computer_choice}")
        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            player_score += 1
            result_label.config(text="You win this round!")
        elif winner == 'computer':
            computer_score += 1
            result_label.config(text="Computer wins this round!")
        else:
            tie_score += 1
            result_label.config(text="It's a tie!")
        score_label.config(text=f"Scoreboard - You: {player_score}, Computer: {computer_score}, Ties: {tie_score}")
    
    # Buttons
    rock_button = tk.Button(root, text="Rock", command=lambda: play_round('rock'))
    rock_button.pack(side=tk.LEFT, padx=10)
    
    paper_button = tk.Button(root, text="Paper", command=lambda: play_round('paper'))
    paper_button.pack(side=tk.LEFT, padx=10)
    
    scissors_button = tk.Button(root, text="Scissors", command=lambda: play_round('scissors'))
    scissors_button.pack(side=tk.LEFT, padx=10)
    
    quit_button = tk.Button(root, text="Quit", command=on_quit)
    quit_button.pack(pady=10)
    
    reset_button = tk.Button(root, text="Reset Game", command=reset_game)
    reset_button.pack(pady=10)
    
    high_score_button = tk.Button(root, text="View High Scores", command=view_high_scores)
    high_score_button.pack(pady=10)
    
    root.mainloop()

def add(a, b):
    return a + b

# Uncomment the line below to run the GUI instead of the console game
gui_app()

if __name__ == "__main__":
    main()  # Runs the Rock Paper Scissors game by default
