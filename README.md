# Digital Pet Simulator 🐶

A fun Python-based virtual pet simulator that demonstrates Object-Oriented Programming concepts.

## Application Preview

### Screenshot
![Pet Simulator Interface](Screen%20Captures/SCREENSHOT%201.PNG)

### Video Demonstration
<video width="100%" controls>
  <source src="Screen%20Captures/main.py%20-%20OOP%20CHALLENGE%20GROUP%20176%20-%20Visual%20Studio%20Code%202025-04-22%2022-28-17.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

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
