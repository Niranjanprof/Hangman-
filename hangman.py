import random
import time

if __name__ == "__main__":
    print("Welcome to Hangman Game \n Guess the word \n ")
    print('___________________________________________')
    name = input("Enter the name: ")
    print(f"Hey {name}")
    print("What genre of word do you want? ")
    print("1.Fruit")
    print("2.Color")
    print("3.Vehicles")
    print("4.Groceries")
    print("5.Animals or Birds\n")
    time.sleep(1)
    words = []
    while True:
        try:
            i = int(input("Enter the number to choose the desired word: "))
        except:
            print("Wrong Input Choose the number")
            continue
        else:
            if not 0<i<6:
                print("Keep the range between 1 and 5")
                continue
        if i == 1:
            linestart = 'Fruit'
        if i == 2:
            linestart = 'Color'
        if i == 3:
            linestart = 'Vehicles'
        if i == 4:
            linestart = 'Groceries'
        if i == 5:
            linestart = 'AnimalsorBirds'
        file = open('hangmandata.txt')
        for line in file:
            if line.startswith(linestart):
                words = line.split()
        file.close()
        break
    word = words[random.randint(2, len(words) - 1)]
    print('\n\nHere is Your Word Find it through Guessing\n')
    time.sleep(1)
    print(f'Clue: its a {linestart}\n')
    time.sleep(1)
    print(f'Clue: its a {len(word)} letter word\n')
    time.sleep(1)
    guess = ['_'] * len(word)
    guess_list = [x for x in word]
    for i in guess:
        print(i, end=' ')
    print()
    print(f'\nOne character at a time\n\n {len(word) + 2} chances\n')
    time.sleep(1)
    print('StartGuessing\n')
    time.sleep(1)
    chance = len(word) + 2
    while chance > 0:
        try:
            char_try = input("Enter a Character: ").lower()
        except:
            print("One Character is the accepted input")
            chance -= 1
            print(f'{chance} Chances left')
            continue
        if char_try.isalpha() and len(char_try) == 1:
            if char_try in guess_list:
                pos = 0
                while True:
                    try:
                        pos = guess_list.index(char_try, pos)
                        guess_list[pos] = chance
                        guess[pos] = char_try
                        for i in guess:
                            print(i, end=' ')
                        print('\n')
                    except:
                        break
                chance -= 1
                print(f'{chance} Chances left\n')
                if '_' not in guess:
                    print('You win')
                    break
                char_try = ''
                continue
            else:
                print("Wrong Guess\n")
                chance -= 1
                print(f'{chance} Chances left')
                continue
        if not (char_try.isalpha() and len(char_try) < 1):
            print("Invalid Input \nTry : One Character is the accepted input\n")
            chance -= 1
            print(f'{chance} Chances left')
            continue

    if '_' in guess:
        print('You lose')
        print("Time up\n")
        print(word + ' is the word')
        print("Come Back Again\n")
