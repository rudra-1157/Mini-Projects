questions = (
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Who painted the Mona Lisa?",
    "What is the chemical symbol for gold?",
    "In which year did World War II end?",
)

options = (
    ("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
    ("A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"),
    ("A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Michelangelo"),
    ("A. Go", "B. Gd", "C. Au", "D. Ag"),
    ("A. 1940", "B. 1939", "C. 1950", "D. 1945"),
)

answers = ("A", "B", "A", "C", "D")
points = [1, 2, 3, 4, 5]
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += points[question_num]   # ✅ add points to score
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("----------------------")
print("-------Result-------")

print("Answers: ", " ".join(answers))
print("Guesses: ", " ".join(guesses))

print(f"Your score is: {score} out of {sum(points)}")
print("----------------------")
