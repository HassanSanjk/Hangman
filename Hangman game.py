#Hangman game

#Importing modules
import random

#Global variables
assist = False
words = {}

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

#Getting data from txt file
def get_data():
    try:
        file = open("words.txt", "r")
        for line in file:
            word,hint = line.strip().split(",",1)
            if word in words:
                print(f"Duplicate word: {word}")
            words[word] = hint
        file.close()
    except FileNotFoundError:
        print("Error: Data file not found.")
    except Exception as e:
        print(f"Error reading data file: {e}")

#Main function
def main():
    #Choosing a random word from dictionary
    word = random.choice(list(words.keys()))

    #Starting the game
    print("Welcome to Hangman!")
    print("****************************")
    top=middle=bottom=""
    wrong = 0
    solution= ["_"] * len(word)

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
            return

        #Checking if the user lost
        if wrong == 6:
            break
    print("\nyou lost!")
    print("the word was", word)
    return

#Asking user if they want to play again
def again():
    print("do you want to play again? (y/n)")
    if input().lower() == "y":
        main()
        again()

#Starting the program
if __name__ == "__main__":
    get_data()
    main()
    again()