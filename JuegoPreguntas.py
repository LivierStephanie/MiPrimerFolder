def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Entaer (A, B, C): ")
        guess = guess.upper()

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#----------------------------
def check_answer(answer , guess):
    if answer == guess:
        print("CORRECT!!!")
        return 1
    else:
        print("WRON!!!")
        return 0
    
#---------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------------")
    print("RESULTS")
    print("---------------------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end ="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end ="")
    print()

    score = (correct_guesses/len(questions))*100
    print("Total de puntos:  " + str(score)+"%")

#---------------------------
def play_again():
    response = input ("Do you want to play again??     (Yes/no):   ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#------------------------

questions = {
    "¿Cuales no es un color primario?" : "A",
    "¿Cuantos huesos tiene el cuerpo humano? " : "B",
    "¿Cual es el oceano mas grande del mundo? " : "C"
}

options = [["Morado", "Azul", "Amarillo"],
           ["180", "206", "450"],
           ["Golfo de Mexico", "Atlantico", "Pacifico"]]


new_game()

while play_again():
    new_game()

print("Byeeeeee")
