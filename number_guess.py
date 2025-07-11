import random

print("Lets play a guessing game...")
print('Think of a number between 1 and 10!')
user_number = int(input("Type a number: "))
computer_guess = random.randint(1, 10)


def main():
    if 1 <= user_number <= 10:
        print("Ok good...hmm...let me think...")
        print(f"Your number is {computer_guess}!")
        if computer_guess == user_number:
            print("I got it! Hahaha You Lose! XD")
        else:
            print("Oh no! I lost! I guess that means you win! :( whatever, man...")
           
    else:
        print("Try again, but be for real this time...rerun the program! >:(")

 
    
   
 
    

main()
