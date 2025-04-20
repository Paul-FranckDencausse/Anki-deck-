# vocab_anki.py

with open("vocab.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()

cartes = []

for ligne in lignes:
    if ":" in ligne:
        francais, portugais = ligne.split(":", 1)
        question = francais.strip()
        reponse = portugais.strip()
        cartes.append(f"{question},{reponse}")

# Sauvegarde au format CSV compatible Anki
with open("fr_pt_deck.csv", "w", encoding="utf-8") as f:
    f.write("\n".join(cartes))

print("Deck FR-PT généré avec succès !")
