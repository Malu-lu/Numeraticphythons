import random

menu = ["Welcome to The Number Guessing Game", "Guess digits in between 1-10", "When you guess incorrectly type in a new digit" ]

print(menu[0])
print(menu[1])



def guess_number():
  while True:
      # Generate a random number between 1 and 10
      number = random.randint(1, 10)
  
      # Get the user's guess
      guess = int(input("Guess a number between 1 and 10: "))
  
      # Check if the guess is correct
      if guess == number:
          print("You guessed correctly!")
      else:
          # If the guess is incorrect, give the user feedback
          if guess < number:
              print("Your guess is too low.")
          else:
              print("Your guess is too high.")
  
      # Ask the user if they want to play again
      play_again = input("Do you want to play again? (y/n): ")
  
      if play_again != "y":
          break

guess_number()
print("Thank you for playing!")   






