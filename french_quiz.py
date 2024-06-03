#By Sanjeev q(≧▽≦q)

#Importing necessary libraries
import random
from colorama import Fore, Style, init


init()

#All the words
words = [
    {"french": "baguette", "english": "baguette"},
    {"french": "cycle", "english": "cycle"},
    {"french": "poutine", "english": "poutine"},
    {"french": "maison", "english": "house"},
    {"french": "voiture", "english": "car"},
    {"french": "chien", "english": "dog"},
    {"french": "chat", "english": "cat"},
    {"french": "livre", "english": "book"},
    {"french": "école", "english": "school"},
    {"french": "famille", "english": "family"},
    {"french": "amour", "english": "love"},
    {"french": "ami", "english": "friend"},
    {"french": "jour", "english": "day"},
    {"french": "nuit", "english": "night"},
    {"french": "temps", "english": "time"},
    {"french": "homme", "english": "man"},
    {"french": "femme", "english": "woman"},
    {"french": "enfant", "english": "child"},
    {"french": "fille", "english": "girl"},
    {"french": "garçon", "english": "boy"},
    {"french": "ville", "english": "city"},
    {"french": "pays", "english": "country"},
    {"french": "monde", "english": "world"},
    {"french": "eau", "english": "water"},
    {"french": "feu", "english": "fire"},
    {"french": "terre", "english": "earth"},
    {"french": "air", "english": "air"},
    {"french": "ciel", "english": "sky"},
    {"french": "soleil", "english": "sun"},
    {"french": "lune", "english": "moon"},
    {"french": "étoile", "english": "star"},
    {"french": "mer", "english": "sea"},
    {"french": "rivière", "english": "river"},
    {"french": "montagne", "english": "mountain"},
    {"french": "forêt", "english": "forest"},
    {"french": "arbre", "english": "tree"},
    {"french": "fleur", "english": "flower"},
    {"french": "herbe", "english": "grass"},
    {"french": "fruit", "english": "fruit"},
    {"french": "légume", "english": "vegetable"},
    {"french": "pain", "english": "bread"},
    {"french": "fromage", "english": "cheese"},
    {"french": "vin", "english": "wine"},
    {"french": "bière", "english": "beer"},
    {"french": "café", "english": "coffee"},
    {"french": "thé", "english": "tea"},
    {"french": "lait", "english": "milk"},
    {"french": "jus", "english": "juice"},
    {"french": "eau", "english": "water"},
    {"french": "ordinateur", "english": "computer"},
    {"french": "téléphone", "english": "phone"},
    {"french": "télévision", "english": "television"},
    {"french": "radio", "english": "radio"},
    {"french": "musique", "english": "music"},
    {"french": "film", "english": "movie"},
    {"french": "jeu", "english": "game"},
    {"french": "sport", "english": "sport"},
    {"french": "vélo", "english": "bicycle"},
    {"french": "moto", "english": "motorcycle"},
    {"french": "avion", "english": "plane"},
    {"french": "train", "english": "train"},
    {"french": "bus", "english": "bus"},
    {"french": "bateau", "english": "boat"},
    {"french": "route", "english": "road"},
    {"french": "rue", "english": "street"},
    {"french": "pont", "english": "bridge"},
    {"french": "place", "english": "square"},
    {"french": "parc", "english": "park"},
    {"french": "jardin", "english": "garden"},
    {"french": "chaise", "english": "chair"},
    {"french": "table", "english": "table"},
    {"french": "lit", "english": "bed"},
    {"french": "porte", "english": "door"},
    {"french": "fenêtre", "english": "window"},
    {"french": "toit", "english": "roof"},
    {"french": "mur", "english": "wall"},
    {"french": "plafond", "english": "ceiling"},
    {"french": "sol", "english": "floor"},
    {"french": "cuisine", "english": "kitchen"},
    {"french": "salon", "english": "living room"},
    {"french": "chambre", "english": "bedroom"},
    {"french": "salle de bain", "english": "bathroom"},
    {"french": "toilettes", "english": "toilet"},
    {"french": "garage", "english": "garage"},
    {"french": "jardin", "english": "garden"},
    {"french": "bureau", "english": "office"},
    {"french": "église", "english": "church"},
    {"french": "hôpital", "english": "hospital"},
    {"french": "école", "english": "school"},
    {"french": "magasin", "english": "store"},
    {"french": "supermarché", "english": "supermarket"},
    {"french": "marché", "english": "market"},
    {"french": "banque", "english": "bank"},
    {"french": "cinéma", "english": "cinema"},
    {"french": "musée", "english": "museum"}
]

#Calculates the score
def calculate_grade(score, attempted):
    if attempted == 0:
        return "N/A"  # Avoid division by zero
    percentage = (score / attempted) * 100
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 70:
        return "Good"
    elif percentage >= 50:
        return "Average"
    else:
        return "Needs Improvement"

#Shuffles words
def quiz_user(words):
    random.shuffle(words)
    score = 0
  
    attempted = 0  # Variable to track the number of questions attempted

    # Check if user wants to stop the quiz before starting
    user_input = input("Type 'stopkey' to quit or press Enter to start the quiz: ").strip().lower()
    if user_input == "stopkey":
        print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Quiz stopped by the user before it started.")
        return

    for word in words:
        print(f"{Fore.RED}{Style.BRIGHT}What is the English translation of '{word['french']}'?")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == "stopkey":
            print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Quiz stopped by the user.")
            break

        attempted += 1
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Correct!\n")
            score += 1
        else:
            print(f"{Style.BRIGHT}{Fore.RED}Wrong! The correct answer is '{word['english']}'.\n")

    grade = calculate_grade(score, attempted)
    print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Quiz complete! Your score: {score}/{attempted} attempted questions. Grade: {grade}")

    # Print personalized feedback message based on grade
    if grade == "Excellent":
        print("Great job! Excellent work!")
    elif grade == "Good":
        print("Well done!")
    elif grade == "Average":
        print("Not bad, keep it up!")
    elif grade == "Needs Improvement":
        print("You might want to brush up on your French.")

    print(f"\n\u00A9 2024, Sanjeev Inc. q(≧▽≦q)")

def main():
    print(Style.BRIGHT + Fore.CYAN + "Welcome to the Ultimate French Quiz!")
    quiz_user(words)

if __name__ == "__main__":
    main()

# © 2024 Sanjeev Inc. q(≧▽≦q)
