# Deck Anki - Vocabulaire Français-Portugais (Européen)

Ce projet permet de générer rapidement un deck Anki avec des cartes de vocabulaire franco-portugais (européen). Le script prend un fichier texte contenant des paires de mots en français et portugais et les transforme en un fichier CSV compatible avec Anki.

## Prérequis

  - Python 3.x
  - Anki (pour importer le fichier CSV)

## Installation

1. **Clonez ou téléchargez ce repository** :
   ```bash
   git clone https://github.com/ton-repository/vocab-fr-pt-anki.git
   cd vocab-fr-pt-anki
2. **Créez votre fichier vocab.txt avec des paires de mots en français et portugais.**
3. **Exécutez le script Python pour générer le fichier CSV compatible Anki** :
   python vocab_anki.py
## Importation dans Anki
  - Ouvrez Anki.

  - Cliquez sur "Importer".

  - Sélectionnez le fichier fr_pt_deck.csv généré.

  - Configurez les paramètres d'importation :

  - Séparez les champs par virgule.

  - Sélectionnez Recto/Verso pour correspondre à vos cartes.

   - Cliquez sur Importer.

## Personnalisation
Vous pouvez personnaliser le script pour inclure plus de mots ou inverser la langue (portugais → français) en modifiant simplement la partie du code qui sépare les colonnes question et réponse.

Si vous avez une liste plus longue, assurez-vous qu'elle respecte le format mot_francais : mot_portugais dans chaque ligne du fichier vocab.txt.
