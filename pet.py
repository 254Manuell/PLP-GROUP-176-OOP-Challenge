class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at middle value
        self.energy = 10  # Starting with full energy
        self.happiness = 5  # Starting at middle value
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness but not above 10
        print(f"{self.name} ate some food! Yummy!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy but not above 10
        print(f"{self.name} had a nice nap!")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play!")
            return
        
        self.energy = max(0, self.energy - 2)  # Decrease energy but not below 0
        self.happiness = min(10, self.happiness + 2)  # Increase happiness but not above 10
        self.hunger = min(10, self.hunger + 1)  # Increase hunger but not above 10
        print(f"{self.name} had fun playing!")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'🍖' * self.hunger}{'⭕' * (10-self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'⚡' * self.energy}{'⭕' * (10-self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'😊' * self.happiness}{'⭕' * (10-self.happiness)} ({self.happiness}/10)")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 1)  # Training makes them a bit tired
            self.happiness = min(10, self.happiness + 1)  # Learning is fun!
            print(f"{self.name} learned how to {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}!")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet!")
        else:
            print(f"\n{self.name}'s Tricks:")
            for trick in self.tricks:
                print(f"- {trick}")

# Example usage
if __name__ == "__main__":
    # Create a new pet
    pet = Pet("Buddy")
    
    # Test all the features
    pet.get_status()
    pet.eat()
    pet.play()
    pet.train("sit")
    pet.train("roll over")
    pet.show_tricks()
    pet.sleep()
    pet.get_status()
