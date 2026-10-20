# 🪄 Harry Potter Flappy Wings

Un jeu d'arcade inspiré de Flappy Bird, mettant en scène Harry Potter volant à travers Poudlard tout en évitant des sorcières ennemies.

![Langage](https://img.shields.io/badge/Python-3.13-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.5-green)

## 🎮 Description du Jeu

Le joueur contrôle Harry Potter. Le but est de voler le plus loin possible sans toucher les sorcières qui attaquent horizontalement.

- **Difficulté progressive** : plus votre score augmente, plus la vitesse des ennemis augmente.
- **Graphismes** : fond du château de Poudlard et personnages thématiques.
- **Score** : affiché en direct à l'écran, avec la vitesse actuelle.

## ⬇️ Télécharger (Windows)

Pas envie d'installer Python ? Téléchargez l'exécutable directement depuis la page
[Releases](https://github.com/EspritCode/Harry-Potter-Flappy-Wings/releases) :

1. Télécharger `main.exe` (build automatique via GitHub Actions).
2. Double-cliquer sur `main.exe` pour jouer.

## 🚀 Installation (depuis les sources)

Prérequis : [Python 3.10+](https://www.python.org/downloads/).

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/EspritCode/Harry-Potter-Flappy-Wings.git
   cd Harry-Potter-Flappy-Wings
   ```

2. **Créer un environnement virtuel et installer les dépendances :**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

3. **Lancer le jeu :**
   ```bash
   python main.py
   ```

## 🕹️ Commandes

- **Menu principal** : `ESPACE` pour commencer.
- **En jeu** : `ESPACE` pour faire monter Harry (le faire descendre avec la gravité).
- **Game Over** :
  - `R` pour recommencer la partie.
  - `Q` pour revenir au menu principal.

## 🏗️ Construire l'exécutable (PyInstaller)

```bash
pip install pyinstaller
pyinstaller --noconfirm main.spec
```

L'exécutable est généré dans `dist/main.exe`.

## 🖼️ Crédits

- Développé avec l'aide de **OptimusAI CLI**.
- Univers basé sur Harry Potter.
