# This is a Hangman project where the words will be derived from a website via Webscraping.
import requests
import bs4
import random
import sys


def webScraping():
    res = requests.get('https://www.ef-australia.com.au/english-resources/english-vocabulary/top-3000-words/')              # Requests the specific website to be used
    soup = bs4.BeautifulSoup(res.text, 'lxml')                                                                              # Converts source code into readable format
    soup.select("p")                                                                                                        # looks for p "class" in HTML format

    vocab = (soup.select("p")[11].text)                                                                                     # seperating the words I need from the other p class
    vocab2 = vocab.replace('\n\t', " ")                                                                                     # removes the \n\t html text
    answer = random.choice(vocab2.split())
    return answer

def playAgain():
    userinput = str(input("Do you want to play again? Y/N "))

    if userinput == "Y" or userinput == "y":
        game()
    elif userinput == "N" or userinput == "n":
        print("Thanks for Playing!")
        sys.exit()

    else:
        print("Wrong input selected, please try again")
        playAgain()


def game():
    answer = webScraping().upper()
    lives = 6
    answerlist = list(answer)
    emptylist = ["_"]*len(answerlist)
    print("Welcome to Hangman! Your job is to solve the following word by inputting letters. Once you're confident enough to solve it, you can try typing in the entire answer. Becareful though, you only have 6 lives.")

    for o in range(0,len(answerlist)):
        print("_", end= " ")

    while True:
        userinput = str(input("\nPick a letter or solve the word: \n")).upper()

        if userinput == answer:
            print(answer)
            print("Congratulations you've won!")
            playAgain()
            break

        elif userinput not in answerlist:
            lives = lives - 1
            if lives == 0:
                print("Game Over, you've hung the man\n")
                print("The correct answer was {}".format(answer))
                playAgain()
                break

            else:
                output2 = " ".join(emptylist)
                print(output2)
                print("That is the wrong guess! You now have {} lives".format(lives))

        elif userinput in emptylist:
            output2 = " ".join(emptylist)
            print(output2)
            print("You've already inputted that letter, try again")

        elif len(userinput) > 1:
            lives = lives - 1
            if lives == 0:
                print("Game Over, you've hung the man\n")
                print("The correct answer was {}".format(answer))
                playAgain()
                break

            else:
                output2 = " ".join(emptylist)
                print(output2)
                print("That is the wrong guess! You now have {} lives".format(lives))



        else:
            for i in range(0,len(answer)):
                if userinput == answerlist[i]:
                    emptylist[i] = userinput
            output = " ".join(emptylist)

            if "_" not in emptylist:
                print(output)
                print("Congratulations you've won!")
                playAgain()
                break
            else:
                print(output)

webScraping()
game()





