import random
computer_dice_roll= random.randint(1,6)
user_guess= int(input("Guess the number from 1 to 6 : "))
guess_correct= computer_dice_roll==user_guess
print(f"User guessed the number: {guess_correct}")
