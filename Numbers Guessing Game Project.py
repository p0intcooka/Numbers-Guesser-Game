# Import module for random number generation
import random

# Game configuration
MAX_ATTEMPTS = 5  # Attempts per level
current_level = 1  # Start at level 1
total_points = 0  # Accumulated score

print("=== Multi-Level Number Guesser ===")

# Main game loop
while True:
    # Level setup: range increases by 10 each level
    range_end = 10 * current_level
    secret = random.randint(1, range_end)
    attempts_left = MAX_ATTEMPTS
    hint_given = False  # Track hint status

    print(f"\n★ Level {current_level} (1-{range_end}) ★")
    print(f"Attempts remaining: {attempts_left}")

    # Guessing loop for current level
    while attempts_left > 0:
        try:
            guess = int(input("Your guess: "))
            
            # Validate input range
            if guess < 1 or guess > range_end:
                print(f"Enter a number between 1-{range_end}!")
                continue  # Skip rest of loop
            
            # Check guess against secret number
            if guess == secret:
                # Calculate points: (remaining attempts) × level × 10
                points = attempts_left * current_level * 10
                total_points += points
                print(f"Correct! +{points} points")
                break  # Exit guessing loop
            else:
                attempts_left -= 1
                print("Higher!" if guess < secret else "Lower!")
                
                # Provide hint after 2 wrong guesses
                if (MAX_ATTEMPTS - attempts_left) >= 2 and not hint_given:
                    parity = "even" if secret % 2 == 0 else "odd"
                    print(f"Hint: The number is {parity}!")
                    hint_given = True  # Prevent repeat hints
                
                # Show remaining attempts if not zero
                if attempts_left > 0:
                    print(f"Attempts left: {attempts_left}")
                    
        except ValueError:  # Handle non-integer inputs
            print("Invalid input! Enter a whole number.")

    # End game if no attempts remain
    if attempts_left == 0:
        print(f"\nGame Over! The number was {secret}")
        break  # Exit main loop

    # Ask user to continue to next level
    continue_game = input("\nContinue to next level? (y/n): ").lower()
    if continue_game == 'y':
        current_level += 1  # Increase difficulty
    else:
        print(f"\nTotal points: {total_points}")
        break  # Exit main loop