from pet import Pet

def display_menu():
    print("\n=== Digital Pet Menu ===")
    print("1. Feed pet")
    print("2. Play with pet")
    print("3. Let pet sleep")
    print("4. Check pet status")
    print("5. Teach new trick")
    print("6. Show tricks")
    print("7. Exit")
    return input("Choose an option (1-7): ")

def main():
    print("Welcome to Digital Pet Simulator! 🐶")
    name = input("What would you like to name your pet? ")
    pet = Pet(name)
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.get_status()
        elif choice == "5":
            trick = input("What trick would you like to teach? ")
            pet.train(trick)
        elif choice == "6":
            pet.show_tricks()
        elif choice == "7":
            print(f"Goodbye! Take care of {pet.name}! 👋")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
