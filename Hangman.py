#Hangman game

#Importing modules
import random
from fileUtils import file_utils
import time

#Global variables
assist = False
words = {}
leaderboard = {}
WORDS_FILE = "Words.txt"
LEADERBOARDS_FILE = "Leaderboards.txt"

#Asking user if they want a hint
def show_hint():
    global assist
    if not assist:
        print("----------------------------")
        print("do you want a hint? (y/n)")
        print("----------------------------")
        if input().lower() == "y":
            assist = True

#Showing hint
def tip(assist,word):
    if assist:
        print("Hint:", words[word])

def show_leaderboard():
    print("Leaderboard:")
    print("Name\tScore")
    for name, score in leaderboard.items():
        print(f"{name}\t{score}")

#Main function
def main():

    #Choosing a random word from dictionary
    word = random.choice(list(words.keys()))

    #Starting the game
    print("Welcome to Hangman!")
    print("****************************")
    name = input("What's your name? ")
    top=middle=bottom=""
    wrong = 0
    solution= ["_"] * len(word)
    start_time = time.time()
    global assist

    #Main loop
    while True:
        #Asking user for a letter
        letter= input("\nguess a letter: ").lower()
        print("\n****************************")

        #Checking if the input is valid
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input!!")
            continue

        #Checking if the letter is in the word
        if letter in word:
            for j in range (len(word)):
                if word[j] == letter:
                    solution[j]= letter
        
        #If the letter is not in the word
        else:
            print("wrong guess!")
            wrong += 1

            #Drawing the hangman
            match(wrong):
                case 1:
                    top = " O"
                case 2:
                    middle = " |"
                case 3:
                    middle = "/|"
                case 4:
                    middle = "/|\\"
                case 5:
                    bottom = "/"
                case 6:
                    bottom = "/ \\"

            show_hint()

        #Printing the left guesses and the hangman
        print("you have", 6-wrong, "guesses left")
        tip(assist,word)
        print(top)
        print(middle)
        print(bottom)
        
        #Printing the solution that user got
        for j in solution:
            print(j, end=" ")

        #Checking if the user won
        if "_" not in solution:
            print("\nThe word is in fact", word,"!!")
            print("you won!")
            print("****************************")
            time_taken = time.time() - start_time
            score = int(max(1,(6-wrong)*(10000 / (time_taken + 1))))
            if assist:
                score //= 2
            print("*******************************")
            print("Summary:")
            print("You got ",wrong," wrong guesses")
            print(f"your time is {time_taken:.2f} seconds")
            print("your score is", score)
            print("*******************************")
            file_utils.update_leaderboard(leaderboard,name,score,LEADERBOARDS_FILE)
            assist = False
            return

        #Checking if the user lost
        if wrong == 6:
            break
    print("\nyou lost!")
    print("the word was", word)
    assist = False
    return

#Asking user if they want to play again
def again():
    print("do you want to play again? (y/n)")
    if input().lower() == "y":
        main()
        again()

#Starting the program
if __name__ == "__main__":
    words = file_utils.read_words(WORDS_FILE)
    leaderboard = file_utils.read_leaderboard(LEADERBOARDS_FILE)
    if not words:
        print("Words file are empty")
        exit()
    play = input("do you want to play hangman? (y/n)").lower()
    if play != "y":
        print("--------------------------------------------------------------")
        lead = input("Do you want to see the leaderboard? (y/n) ").lower()
        print("--------------------------------------------------------------")
        if lead == "y":
            show_leaderboard()
        else:
            print("have a nice day!")
            exit()
    else:
        main()
        again()