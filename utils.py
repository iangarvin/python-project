#-------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("#-------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


#-------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0


#-------------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------------")
    print("RESULTS")
    print("-------------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")

    score = int((correct_guesses/len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


#-------------------------------
def play_again():
    response = input("Do you want to play again: (yes or No)")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

#-------------------------------


questions = {"Who created python?": "A",
             "What year was python created?": "B",
             "Python is attributed to which comedy group": "C",
             "Is the earth round?": "A"
             }

options = [["A. Guido van Rossium", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerberg"],
           ["A.1989", "B. 1991", "C. 2000", "D. 2116 "],
           ["A. Lonely island", "B. Smoch", "C. Monty python", "D. SNL"],
           ["A. True", "B. False", "B. None of above", "D. puzzled"]
           ]

new_game()

while play_again():
    new_game()

print("Byee")
