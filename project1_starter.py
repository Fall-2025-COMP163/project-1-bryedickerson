"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Bryant Dickerson
Date: 10/20/2025

AI Usage: AI helped with syntax fixes and function structure.
"""

# =============================
# Function 1 - Character Creator
# =============================
def create_character(name, character_class):
    """
    Creates a character dictionary with default stats based on the class.
    Loops until a valid class is entered.
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    while character_class not in valid_classes:
        print("Invalid class. Please choose Warrior, Mage, Rogue, or Cleric.")
        character_class = input("Choose a class: ")
# AI USAGE - Used ChatGPT to create a while loop to keep receiving input until the code accepted it.
    # Build character dictionary (autograder expects these exact keys)
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength":strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }

    return character


# =============================
# Function 2 - Stat Calculations
# =============================
def calculate_stats(character_class, level):
    character_class = character_class.lower() # AI suggested for me to use .lower(), I don't believe it worked out.
    strength = 5
    magic = 15
    health = 80

    if character_class == "warrior":
        strength += 85
        magic += 5
        health += 15
    elif character_class == "mage":
        strength += 30
        magic += 70
        health += 0
    elif character_class == "rogue":
        strength += 55
        magic += 25
        health -= 10
    elif character_class == "cleric":
        strength += 45
        magic += 35
        health += 10
    else:
        print('invalid')
        return calculate_stats('Warrior', level)
    return strength, magic, health


# =============================
# Function 3 - Character File Saving
# =============================
def save_character(character, filename):
    import os
    if not isinstance(character, dict) or not filename:
        return False
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False

    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True


# =============================
# Function 4 - Loading Character
# =============================
import os

def load_character(filename):
    # Check if file exists first
    if not os.path.exists(filename):
        return None

    # Open and read lines safely
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        # Skip empty or malformed lines
        if ": " not in line:
            continue
        key, value = line.strip().split(": ", 1)
        key = key.lower().replace("character ", "")
        # Convert numeric values
        if value.isdigit():
            value = int(value)
        character[key] = value

    # If the file was empty, return None
    if len(character) == 0:
        return None

    return character

# =============================
# Function 5 - Display Character
# =============================
def display_character(character):
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character.get('name', '')}")
    print(f"Class: {character.get('class', '')}")
    print(f"Level: {character.get('level', 0)}")
    print(f"Strength: {character.get('strength', 0)}")
    print(f"Magic: {character.get('magic', 0)}")
    print(f"Health: {character.get('health', 0)}")
    print(f"Gold: {character.get('gold', 0)}")
    print("=======================")


# =============================
# Function 6 - Level-Up Function
# =============================
def level_up(character):
    character["level"] += 1
    s, m, h = calculate_stats(character["class"], character["level"])
    character["strength"] = s
    character["magic"] = m
    character["health"] = h
    print(f"\n{character['name']} leveled up to Level {character['level']}!")


# =============================
# Testing Space
# =============================
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    n = input("Enter your name: ")
    c = input("What class will you choose? (Warrior/Mage/Rogue/Cleric): ")

    char = create_character(n, c)
    if char is not None:
        display_character(char)
        level_up(char)
        display_character(char)
        save_character(char, "my_character.txt")
        loaded = load_character("my_character.txt")
        print("\nLoaded character from file:")
        display_character(loaded)
    else:
        print("Invalid class. Please choose Warrior, Mage, Rogue, or Cleric.")
