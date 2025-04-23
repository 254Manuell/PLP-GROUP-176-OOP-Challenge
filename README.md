# Digital Pet Simulator 🐶

A fun Python-based virtual pet simulator that demonstrates Object-Oriented Programming concepts.

## Application Preview

### Screenshot
![image alt](https://github.com/254Manuell/PLP-GROUP-176-OOP-Challenge/blob/ece3a83b15005e1cd9c56948595c898337fcba03/SCREENSHOT%201.PNG) 

### Video Demonstration
(https://drive.google.com/file/d/14Zkvl9paw6GpEM4Tv2xzsTTWOzJEzcAY/view?usp=drive_link) 

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
