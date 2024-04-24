# Task 1: Develop a list of questions and answers

questions = ["What is 15 - 6? ", "What is the capital of New Hampshire ", "How many stairs are in my house? ", "What is the Rock's last name? "]
answers = ["9", "Concord", "18", "Johnson"]

# Task 2: Quiz the user

user = []
for q in questions:
    user.append(input(q))
print(user)

count = 0 # keeps track of user's score
for i, a in enumerate(answers):
    if (a == user[i]):
        print("You got question " + str(i + 1) + " correct!")
        count += 1
    else:
        print("You got question " + str(i + 1) + " wrong.")

# Task 3: Score the quiz and give feedback

print("You got " + str(count) + " out of 4 questions correct.")