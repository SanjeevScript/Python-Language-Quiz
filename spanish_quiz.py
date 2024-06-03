# By Sanjeev q(≧▽≦q)

#Importing libs
import random
from colorama import Fore, Style, init

# Initialize colorama
init()

#All the words
words = [
    {"spanish": "casa", "english": "house"},
    {"spanish": "perro", "english": "dog"},
    {"spanish": "gato", "english": "cat"},
    {"spanish": "libro", "english": "book"},
    {"spanish": "escuela", "english": "school"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "amor", "english": "love"},
    {"spanish": "amigo", "english": "friend"},
    {"spanish": "día", "english": "day"},
    {"spanish": "noche", "english": "night"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "hombre", "english": "man"},
    {"spanish": "mujer", "english": "woman"},
    {"spanish": "niño", "english": "child"},
    {"spanish": "niña", "english": "girl"},
    {"spanish": "chico", "english": "boy"},
    {"spanish": "ciudad", "english": "city"},
    {"spanish": "país", "english": "country"},
    {"spanish": "mundo", "english": "world"},
    {"spanish": "agua", "english": "water"},
    {"spanish": "fuego", "english": "fire"},
    {"spanish": "tierra", "english": "earth"},
    {"spanish": "aire", "english": "air"},
    {"spanish": "cielo", "english": "sky"},
    {"spanish": "sol", "english": "sun"},
    {"spanish": "luna", "english": "moon"},
    {"spanish": "estrella", "english": "star"},
    {"spanish": "mar", "english": "sea"},
    {"spanish": "río", "english": "river"},
    {"spanish": "montaña", "english": "mountain"},
    {"spanish": "bosque", "english": "forest"},
    {"spanish": "árbol", "english": "tree"},
    {"spanish": "flor", "english": "flower"},
    {"spanish": "hierba", "english": "grass"},
    {"spanish": "fruta", "english": "fruit"},
    {"spanish": "verdura", "english": "vegetable"},
    {"spanish": "pan", "english": "bread"},
    {"spanish": "queso", "english": "cheese"},
    {"spanish": "vino", "english": "wine"},
    {"spanish": "cerveza", "english": "beer"},
    {"spanish": "café", "english": "coffee"},
    {"spanish": "té", "english": "tea"},
    {"spanish": "leche", "english": "milk"},
    {"spanish": "jugo", "english": "juice"},
    {"spanish": "ordenador", "english": "computer"},
    {"spanish": "teléfono", "english": "phone"},
    {"spanish": "televisión", "english": "television"},
    {"spanish": "radio", "english": "radio"},
    {"spanish": "música", "english": "music"},
    {"spanish": "película", "english": "movie"},
    {"spanish": "juego", "english": "game"},
    {"spanish": "deporte", "english": "sport"},
]

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
        print(f"{Fore.RED}{Style.BRIGHT}What is the English translation of '{word['spanish']}'?")
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
        print("You might want to brush up on your Spanish.")

    print(f"\n\u00A9 2024, Sanjeev Inc. q(≧▽≦q)")

def main():
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX + "Welcome to the Ultimate Spanish Quiz!")
    quiz_user(words)

if __name__ == "__main__":
    main()
