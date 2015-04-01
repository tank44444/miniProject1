import random

print("0 — rock") #34 12
print("1 — Spock") #04 23
print("2 — paper") #01 34
print("3 — lizard") #12 04
print("4 — scissors") #23 01
print("")

def number_to_choice_name(number):
     if number ==0:
         return "rock"
     elif number ==1:
         return "Spock"
     elif number ==2:
         return "paper"
     elif number ==3:
         return "lizard"
     elif number ==4:
         return "scissors"
     else:
         return "error"

def game(number1,number2):
    if number1 ==0:
        if number2 ==0:
            return "Player and computer tie!"
        elif number2 ==3 or 4:
            return "Player wins!"
        elif number2 ==1 or 2:
            return "Computer wins!"	 
 
    elif number1 ==1:
        if number2 ==1:
            return "Player and computer tie!"
        elif number2 ==0 or 4:
            return "Player wins!"
        elif number2 ==2 or 3:
            return "Computer wins!"

    elif number1 ==2:
        if number2 ==2:
            return "Player and computer tie!"
        elif number2 ==0 or 1:
            return "Player wins!"
        elif number2 ==3 or 4:
            return "Computer wins!"

    elif number1 ==3:
        if number2 ==3:
            return "Player and computer tie!"
        elif number2 ==1 or 2:
            return "Player wins!"
        elif number2 ==0 or 4:
            return "Computer wins!"

    elif number1 ==4:
        if number2 ==4:
            return "Player and computer tie!"
        elif number2 ==2 or 3:
            return "Player wins!"
        elif number2 ==0 or 1:
            return "Computer wins!"

 

while True:
     player = int(input("please choice: "))
     print("\nPlayer chooses ",number_to_choice_name(player))
     computer =random.randrange(0,4)
     print("Computer chooses ",number_to_choice_name(computer))
     print(game(player,computer),"\n")
     



