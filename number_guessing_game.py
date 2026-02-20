import random
lowest_num = 1
highest_num = 100
guesses = 0
is_running = True
answer = random.randint(lowest_num, highest_num)

print("Number Guessing Game")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    guesses+=1
    if guess.isdigit():
        guess = int(guess)
        if guess<lowest_num or guess>highest_num:
            print(f"{guess} is out of range")
            print(f"Guess a number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print(f"{guess} is too low")
        elif guess>answer:
            print(f"{guess} is too high")
        else:
            print(f"{guess} is correct!!")
            print(f"That took {guesses} guesses")
            is_running = False

    else:
        print("Invalid Guess!!")
        print(f"Guess a number between {lowest_num} and {highest_num}")