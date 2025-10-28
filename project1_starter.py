"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Bryant Dickerson
Date: 10/20/2025

AI Usage: AI helped with syntax fixes and function structure.
"""
# AI Usage: Used AI to identify errors and help me fix variable mistakes
# Input section
name = input("Enter your name: ")
character_class = input("What class will you choose? (Warrior/Mage/Rogue/Cleric)?: ")

# Global base variables
strength = 0   # scale 0–1000
level = 1      # scale 1–100
magic = 0      # scale 0–100
health = 0     # scale 0–100
gold = 100     # scale 100–999,999,999,999


# =============================
# Function 1 - Character Creator
# =============================

def create_character(name, character_class):
    # stat constants
    level = 1
    gold = 100
    # Added the if statement is below since test cases weren't passing 
    if name is None:
        name = input("Enter your name: ")
    # stats assigned based on character class
    if character_class == "Warrior":
        strength = 70
        magic = 15
        health = 90
    elif character_class == "Mage":
        strength = 30
        magic = 90
        health = 60
    elif character_class == "Rogue":
        strength = 55
        magic = 45
        health = 70
    elif character_class == "Cleric":
        strength = 50
        magic = 75
        health = 80
    else:
        return "Character selection unavailable, choose another."

    # return dictionary
    return {
        "Name": name,
        "Class": character_class,
        "Level": level,
        "Strength": strength,
        "Magic": magic,
        "Health": health,
        "Gold": gold
    }


# =============================
# Function 2 - Stat Calculations
# =============================
def calculate_stats(character_class, level):
    # formulas depend on class and level
    if character_class == "Warrior":
        strength = 70 + (level * 10)
        magic = 15 + (level * 3)
        health = 90 + (level * 8)

    elif character_class == "Mage":
        strength = 30 + (level * 4)
        magic = 90 + (level * 10)
        health = 60 + (level * 5)

    elif character_class == "Rogue":
        strength = 55 + (level * 7)
        magic = 45 + (level * 6)
        health = 70 + (level * 5)

    elif character_class == "Cleric":
        strength = 50 + (level * 6)
        magic = 75 + (level * 7)
        health = 80 + (level * 6)

    else:
        return (0, 0, 0)  # invalid class
    return strength, magic, health


# =============================
# Function 3 - Character File Saving
# =============================
def save_character(character, filename):
    with open(filename, "w") as file:
        file.write(f"Name: {character['Name']}\n")
        file.write(f"Class: {character['Class']}\n")
        file.write(f"Level: {character['Level']}\n")
        file.write(f"Strength: {character['Strength']}\n")
        file.write(f"Magic: {character['Magic']}\n")
        file.write(f"Health: {character['Health']}\n")
        file.write(f"Gold: {character['Gold']}\n")
    return True

# =============================
# Function 4 - Loading Character
# =============================
def load_character(filename):
    lines = open(filename, "r").readlines()
    character = {}
    for line in lines:
        key, value = line.strip().split(": ")
        if value.isdigit():
            character[key] = int(value)
        else:
            character[key] = value
    return character

# =============================
# Function 5 - Printing Statements
# =============================
def display_character(character):
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['Name']}")
    print(f"Class: {character['Class']}")
    print(f"Level: {character['Level']}")
    print(f"Strength: {character['Strength']}")
    print(f"Magic: {character['Magic']}")
    print(f"Health: {character['Health']}")
    print(f"Gold: {character['Gold']}")
    print("=======================")


# =============================
# Function 6 - Level-Up Functions
# =============================
def level_up(character):
    character["Level"] += 1
    s, m, h = calculate_stats(character["Class"], character["Level"])
    character["Strength"] = s
    character["Magic"] = m
    character["Health"] = h
    print(f"\n{character['Name']} leveled up to Level {character['Level']}!")


# =============================
# Testing Space
# =============================
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    # create character
    char1 = create_character(name, character_class)

    # if valid, display and test functions
    if isinstance(char1, dict):
        display_character(char1)
        level_up(char1)
        display_character(char1)
        save_character(char1, "my_character.txt")
        loaded = load_character("my_character.txt")
        print("\nLoaded character from file:")
        display_character(loaded)
    else:
        print(char1)
