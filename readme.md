LexiAcces — Assistant de Traduction & Synthèse Vocale

**LexiAcces** est une application desktop intuitive développée en Python permettant de traduire du texte du français vers l'anglais et d'écouter la prononciation grâce à un moteur de synthèse vocale (TTS) avec accent anglophone naturel.

---

## 🚀 Fonctionnalités Clés

* **Traduction instantanée :** Intégration de l'API `MyMemory` pour une traduction rapide et fiable du français vers l'anglais.
* **Synthèse vocale intelligente (Text-to-Speech) :** Utilisation du moteur `pyttsx3` configuré pour sélectionner automatiquement une voix anglaise native sur le système (ex. *Microsoft Zira* / *Microsoft David*) afin d'éviter les biais d'accent.
* **Interface Graphique Ergonomique (GUI) :** Conçue avec `Tkinter`, offrant une séparation nette entre l'espace de saisie, la zone de résultat et les contrôles d'action.
* **Gestion des erreurs & Robustesse :** Validation des saisies utilisateur et contrôle des flux vocaux pour éviter les blocages système sous Windows.

---

## 🛠️ Stack Technique

| Composant | Technologie / Bibliothèque |
| :--- | :--- |
| **Langage** | Python 3.14 |
| **Interface Graphique** | Tkinter |
| **Moteur de Traduction** | `deep-translator` (MyMemory API) |
| **Synthèse Vocale** | `pyttsx3` |
| **Environnement** | VS Code (Windows) |

---

## 📂 Structure du Projet

```text
LexiAcces/
├── main.py          # Script principal (GUI, logique de traduction & TTS)
├── .gitignore       # Fichiers et dossiers ignorés par Git
└── README.md        # Documentation du projet