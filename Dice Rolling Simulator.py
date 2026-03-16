import random

dice_faces = {
    1: "-----------\n|         |\n|    O    |\n|         |\n-----------",
    2: "-----------\n|  O      |\n|         |\n|      O  |\n-----------",
    3: "-----------\n|  O      |\n|    O    |\n|      O  |\n-----------",
    4: "-----------\n|  O   O  |\n|         |\n|  O   O  |\n-----------",
    5: "-----------\n|  O   O  |\n|    O    |\n|  O   O  |\n-----------",
    6: "-----------\n|  O   O  |\n|  O   O  |\n|  O   O  |\n-----------"
}

while True:
    total_number = 0
    try:
        number = int(input("\nHow many dice do you want to roll: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    for i in range(0, number):
        random_number = random.randint(1, 6)
        total_number += random_number
        
        print(f"\nRoll {i+1}:")
        print(dice_faces[random_number])  
        print(f"Value: {random_number}")

    print("\n" + "="*20)
    print("Total Sum: ", total_number)
    print("="*20)

    choice = input("\nDo you want to play again? (y/n): ")
    if choice.lower() == 'n':
        print("Thanks for playing")
        break