import random
import string
def main():
    passGen = True
    while passGen == True: #until the user indicates they no longer want new passwords, prompt and generate passwords
        passGenCont = True
        userIn = int(input("Indicate, on a scale of 1 to 3, how strong you wish your password to be:"))
        acptNum = [1, 2, 3] #verify that user input is 1, 2, 3
        x = acptNum.count(userIn)
        if x == 1:
            password = randPassGen(strg = userIn)
            print("Your new password is: ",password)
            while passGenCont == True: #asks user if they want to continue; repeats until they enter a valid input
                cont = input("Do you wish to have another password generates (Enter 1 for yes and 0 for no):")
                acptNum = ['0', '1'] #verify that user input is 0 or 1
                x = acptNum.count(cont)
                if x == 1:
                    if cont == 1:
                        pass
                    elif cont == 0:
                        passGen = False
                        print("Thank you for using our password generator. Have a nice day!")
                    passGenCont = False
                else:
                    print("That is not an acceptable input. Try again.")
        else:
            print("That is not an acceptable input. Try again.")
def randPassGen(strg): #function which generates varying passwords depending on desired password strength
    if strg == 1: #weak password randomly chosen from a list of words and returned
        wordList = ["password", "birthday", "cats", "dogs", "cake", "1234"]
        randNum = random.randint(0,5)
        password = wordList[randNum]
        return password
    elif strg == 2: #medium password generated from a random combination of letters (upper and lowercase), numbers, and symbols 8-characters long
        password = ""
        leng = range(8)
        for x in leng:
            randNum = random.randint(0,3)
            if randNum == 0: #adds random lowercase letter to password
                a = str(random.choice(string.ascii_lowercase))
                password = password + a
            elif randNum == 1: #adds random uppercase letter to password
                a = str(random.choice(string.ascii_uppercase))
                password = password + a
            elif randNum == 2: #adds random number to password 
                a = str(random.choice(string.digits))
                password = password + a
            elif randNum == 3: #adds random symbol to password
                a = str(random.choice(string.punctuation))
                password = password + a
        return password
    elif strg == 3: #strong password generated from a random combination of letters (upper and lowercase), numbers, and symbols 16-characters long
        password = ""
        leng = range(16)
        for x in leng:
            randNum = random.randint(0,3)
            if randNum == 0: #adds random lowercase letter to password
                a = str(random.choice(string.ascii_lowercase))
                password = password + a
            elif randNum == 1: #adds random uppercase letter to password
                a = str(random.choice(string.ascii_uppercase))
                password = password + a
            elif randNum == 2: #adds random number to password 
                a = str(random.choice(string.digits))
                password = password + a
            elif randNum == 3: #adds random symbol to password
                a = str(random.choice(string.punctuation))
                password = password + a
        return password
main()
   
