# Digital Pet Simulator 🐶

A fun Python-based virtual pet simulator that demonstrates Object-Oriented Programming concepts.

## Documentation Files

- `SCREENSHOT 1.PNG`: Contains a visual demonstration of the pet simulator interface, showing the status display and available interactions
- Screen recording to be added: A video walkthrough of the application will be needed to demonstrate how to create a pet and use various features like feeding, playing, and training

## Features

- Create and name your own virtual pet
- Manage your pet's hunger, energy, and happiness levels
- Interact with your pet through various activities:
  - Feed your pet (🍖)
  - Let your pet sleep (⚡)
  - Play with your pet (😊)
  - Train your pet new tricks! 🎯
- Visual status display with emojis
- Trick learning system

## How to Use

1. Run the `pet.py` file
2. Create a new pet by instantiating the Pet class with a name
3. Interact with your pet using the available methods:
   - `eat()`
   - `sleep()`
   - `play()`
   - `get_status()`
   - `train(trick)`
   - `show_tricks()`

## Example

```python
pet = Pet("Buddy")
pet.get_status()  # Check initial status
pet.eat()         # Feed your pet
pet.train("sit")  # Teach a new trick
pet.show_tricks() # See what tricks your pet knows
```

