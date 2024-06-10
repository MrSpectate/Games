import random

def play_game():
    # number to guess 1 to 100
    number_to_guess = random.randint(1, 100)

    # attempts
    attempts = 0

    # loop
    while True:
        # guess a number
        guess = input("Guess the number (between 1 and 100): ")

        # check if the input is a valid integer
        if not guess.isdigit():
            print("Enter a valid number")
            continue
        
        guess = int(guess)
        attempts += 1

        if guess > number_to_guess:
            print("It's too high")
        elif guess < number_to_guess:
            print("It's too low")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
