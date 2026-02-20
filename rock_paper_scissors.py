import random

OPTIONS = ("rock", "paper", "scissors")

def print_instructions():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' at any time to exit.\n")

def get_player_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice == "quit":
            return None
        if choice in OPTIONS:
            return choice
        print("Invalid input. Please try again.")

def get_computer_choice():
    return random.choice(OPTIONS)

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif player == "rock" and computer == "scissors":
        return "win"
    elif player == "paper" and computer == "rock":
        return "win"
    elif player == "scissors" and computer == "paper":
        return "win"
    else:
        return "lose"

def play_game():
    print_instructions()
    wins, losses, ties = 0, 0, 0

    while True:
        player = get_player_choice()
        if player is None:
            break
        computer = get_computer_choice()
        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        result = decide_winner(player, computer)
        if result == "tie":
            print("It's a tie!\n")
            ties += 1
        elif result == "win":
            print(f"You win! {player.capitalize()} beats {computer}.\n")
            wins += 1
        else:
            print(f"You lose! {computer.capitalize()} beats {player}.\n")
            losses += 1

        print(f"Score: Wins: {wins}, Losses: {losses}, Ties: {ties}\n")

    print("Thanks for playing!")
    print(f"Final Score: Wins: {wins}, Losses: {losses}, Ties: {ties}")

if __name__ == "__main__":
    play_game()