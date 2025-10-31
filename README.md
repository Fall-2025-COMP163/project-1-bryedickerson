[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21181542&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments


# Game Concept: What's your RPG world about?
The game idea I had in mind was pretty simple: I used the given classes (Warrior, Mage, Cleric, and Rogue) and stat models to do my calculations and format the game. Each character has differing base stats based on their class. For example, Warriors have higher strength than they do magic, and Mages have higher magic than they do strength. The output is the base stats of each character.

# Design Choices: Why did you choose your stat formulas?
I chose the stat formulas I did based on usual game logic regarding classes. In most RPGs (Role-playing Games), character classes have an effect on which of their stats will be high and which will be low. Warriors in RPG games may go by names like "warrior", "berserker", etc. These characters tend to have very high strength and health because warriors in real life are known for their immense strength and durability.

# Bonus Creative Features: Did you add anything unique?
I didn't have anything unique in mind for my project.

# AI Usage: What AI assistance did you use and where?
For the majority of the project, I used ChatGPT to explain concepts to me based off the coding suggestions it gave me. 
(EXAMPLE: Line 74 (if not isinstance function checks to see if the first argument, character, is a dictionary. Before I asked it to break it down for me, I believed that the isinstance function checked to see if the first argument was inside of the second argument, which I figured would be a list or dictionary.)

# How to Run: Clear instructions for testing your code
At the beginning of my code, it will ask for two inputs: Your character name, and your class choice. However, it checks if your input is available in the choices. For example, if you enter "Wizard" for your class, then it will ask again to enter a valid class. The only four I had in mind were the suggestions from the beginning (warrior, mage, cleric, and rogue). Once one of these classes are chosen, then the output will be the base-level stats of each class. 

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge
