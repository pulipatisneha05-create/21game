import random

def player_turn(current_number):
    while True:
        try:
            nums = input("Your turn! Enter 1 to 3 numbers separated by space: ").strip().split()
            nums = [int(num) for num in nums]

            # Validation
            if len(nums) < 1 or len(nums) > 3:
                print("❌ You must enter between 1 to 3 numbers.")
                continue

            expected = list(range(current_number + 1, current_number + len(nums) + 1))

            if nums != expected:
                print(f"❌ You must continue from {current_number}. Expected: {expected}")
                continue

            return nums[-1]

        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")


def computer_turn(current_number):
    print("Computer's turn:")

    count = random.randint(1, 3)

    numbers = [current_number + i for i in range(1, count + 1)]

    print(" ".join(map(str, numbers)))

    return numbers[-1]


def play_game():
    print("🎮 Welcome to the 21 Number Game!")
    print("👉 Rules: You and the computer will take turns saying 1 to 3 numbers in order.")
    print("🚫 The player forced to say '21' loses.\n")

    current_number = 0

    turn = random.choice(["player", "computer"])

    while current_number < 21:

        if turn == "player":

            current_number = player_turn(current_number)

            if current_number >= 21:
                print("💥 You said 21! You lose.")
                break

            turn = "computer"

        else:

            current_number = computer_turn(current_number)

            if current_number >= 21:
                print("🎉 Computer said 21! You win.")
                break

            turn = "player"


# Run the game
play_game()