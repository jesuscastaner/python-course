# quiz game

questions = (
    "What color is the sky?",
    "How many legs does a cat have?",
    "Which animal says 'moo'?",
    "What is 2 + 2?",
    "What do bees make?"
)

options = (
    ("A. Green", "B. Blue", "C. Red", "D. Yellow"),
    ("A. 2", "B. 3", "C. 4", "D. 10"),
    ("A. Dog", "B. Cow", "C. Sheep", "D. Pig"),
    ("A. 3", "B. 4", "C. 5", "D. 6"),
    ("A. Honey", "B. Milk", "C. Water", "D. Coca Cola"),
)

answers = ("B", "C", "B", "B", "A")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1  #

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")
print("Correct answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print(f"You answered {score} question(s) correctly")

score = int(score / len(questions) * 100)
print(f"Score: {score}%")
