import json
import random

# 📥 Wczytaj karty z pliku JSON
with open("tarot.json", "r") as file:
    tarot_cards = json.load(file)

# 🔮 1. Szukanie karty po nazwie
def search_card(name):
    for card in tarot_cards:
        if card["name"].lower() == name.lower():
            print(f"\n🔮 {card['name']}")
            print("✨ Keywords:", ", ".join(card["keywords"]))
            print("📜 Meaning:", card["short_description"])
            return
    print("❌ Nie znaleziono takiej karty. Sprawdź pisownię.")

# ☀️ 2. Karta dnia – losowa
def daily_card():
    card = random.choice(tarot_cards)
    print(f"\n☀️ Karta dnia: {card['name']}")
    print("✨ Keywords:", ", ".join(card["keywords"]))
    print("📜 Meaning:", card["short_description"])

# 🔮 3. Rozkład 3 kart – słowa klucze
def three_card_spread():
    cards = random.sample(tarot_cards, 3)
    print("\n🔮 Twój rozkład trzech kart:")
    for i, card in enumerate(cards, start=1):
        print(f"  {i}. {card['name']} – Keywords: {', '.join(card['keywords'])}")

# 📍 Menu konsolowe
def main():
    while True:
        print("\n=== Tarot Chatbot ===")
        print("1. Zapytaj o kartę")
        print("2. Wylosuj kartę dnia")
        print("3. Zadaj pytanie (3 karty)")
        print("4. Zakończ")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Podaj nazwę karty (np. The Fool): ")
            search_card(name)
        elif choice == "2":
            daily_card()
        elif choice == "3":
            three_card_spread()
        elif choice == "4":
            print("🔚 Do zobaczenia!")
            break
        else:
            print("❌ Niepoprawna opcja.")

if __name__ == "__main__":
    main()