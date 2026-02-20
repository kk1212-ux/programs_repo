######################### Quiz Program ##########################

questions = ("1. What does CPU stand for?",
             "2. Which of the following is an input device?",
             "3. What is the brain of the computer?",
             "4. Which one of these is a storage device?",
             "5. What does RAM stand for?")

options = (("A. Central Processing Unit", "B. Computer Primary Unit", "C. Central Power Unit", "D. Control Program Unit"),
           ("A. Printer", "B. Monitor", "C. Keyboard", "D. Speaker"),
           ("A. Hard Drive", "B. CPU", "C. RAM", "D. Keyboard"),
           ("A. Mouse", "B. Scanner", "C. Hard Disk", "D. Microphone"),
           ("A. Readily Accessible Memory", "B. Random Access Memory", "C. Rapid Action Module", "D. Read Access Machine"))

answers = ("A", "C", "B", "C", "B")
guesses = []
score = 0
question_no = 0

for question in questions:
    print("------------------------------------------------")
    print(question)
    for option in options[question_no]:
        print(option)
    guess = input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_no]:
        print("CORRECT!!")
        score += 1
    else:
        print("INCORRECT!!")
        print(f"Correct Option is {answers[question_no]}")
    question_no += 1

print("------------------------------------------------")
print("                    RESULTS                     ")
print("------------------------------------------------")
print("Answers: ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()
print("Guesses: ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()
final_score = int((score/len(questions))*100)
print(f"Your score is: {final_score}%")