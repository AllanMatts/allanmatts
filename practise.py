print('\n\t\tQUIZ GAME\n')
questions = [
    "What is the largest ocean on Earth?",
    "What is the tallest mountain in the world?",
    "What is the fastest animal on land?",
    "What is the hottest planet in our solar system?",
    "Which programming language did you use to write this ?\n"
]

answers = [
    "The Pacific Ocean",
    "Mount Everest",
    "The cheetah",
    "Venus",
    "Python"
]

# Loop through questions and display them with formatted strings
for i, question in enumerate(questions):
    print(f"\nQuestion {i + 1}: {question}")
    print(f"\tYour answer: {input()}")

    # Check if answer is correct
    if input().lower() == answers[i].lower():
        print(f"\tCorrect! ")
    else:
        print(f"\tOops, the answer is actually {answers[i]}. ")

print("\nThank you for playing this Quiz!\n")