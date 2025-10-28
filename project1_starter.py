"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Bryant Dickerson
Date: 10/20/2025

AI Usage: AI helped with syntax fixes and function structure.
"""

# =============================
# Function 1 - Character Creator
# =============================
def create_character(name=None, character_class=None):
    """
    Creates a character dictionary with default stats based on the class.
    Loops until a valid class is entered.
    """

    # If no name or class passed (like from pytest), skip user input. Used AI here to identify
    if name is None:
        name = input("Enter your name: ") or ""

    # List of valid classes
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]

    # Ask for class until valid one is entered
    while character_class not in valid_classes:
        if character_class is None:
            character_class = input("Choose a class (Warrior, Mage, Rogue, Cleric): ")
        elif character_class not in valid_classes:
            print("Invalid class. Please choose Warrior, Mage, Rogue, or Cleric.")
            character_class = None  # reset so it loops again

    # Base stats depending on class
    if character_class == "Warrior":
        stats = {"strength": 80, "magic": 20, "health": 100}
    elif character_class == "Mage":
        stats = {"strength": 30, "magic": 90, "health": 60}
    elif character_class == "Rogue":
        stats = {"strength": 60, "magic": 40, "health": 80}
    else:  # Cleric
        stats = {"strength": 50, "magic": 70, "health": 70}

    # Build character dictionary (autograder expects these exact keys)
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": stats["strength"],
        "magic": stats["magic"],
        "health": stats["health"],
        "gold": 100
    }

    return character


# =============================
# Function 2 - Stat Calculations
# =============================
def calculate_stats(character_class, level):
    if character_class == "warrior":
        return 70 + (level * 10), 15 + (level * 3), 90 + (level * 8)
    elif character_class == "mage":
        return 30 + (level * 4), 90 + (level * 10), 60 + (level * 5)
    elif character_class == "rogue":
        return 55 + (level * 7), 45 + (level * 6), 70 + (level * 5)
    elif character_class == "cleric":
        return 50 + (level * 6), 75 + (level * 7), 80 + (level * 6)
    else:
        return 0, 0, 0


# =============================
# Function 3 - Character File Saving
# =============================
def save_character(character, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        return True
    except Exception:
        return False


# =============================
# Function 4 - Loading Character
# =============================
def load_character(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        character = {}
        for line in lines:
            key, value = line.strip().split(": ", 1)
            key = key.lower().replace("character ", "")
            if value.isdigit():
                value = int(value)
            character[key] = value
        return character
    except FileNotFoundError:
        return None
    except Exception:
        return None


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
