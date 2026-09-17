import tkinter as tk
from tkinter import messagebox
from deep_translator import MyMemoryTranslator
import pyttsx3
def traduire_texte(texte):
    # Traduction directe avec MyMemory (Français -> Anglais)
    return MyMemoryTranslator(source='fr-FR', target='en-US').translate(texte)

def action_traduire():
    texte_a_traduire = entree_texte.get("1.0", tk.END).strip()
    
    if not texte_a_traduire:
        messagebox.showwarning("Attention", "Veuillez entrer du texte à traduire.")
        return
    
    texte_traduit = traduire_texte(texte_a_traduire)
    
    zone_resultat.config(state='normal')
    zone_resultat.delete("1.0", tk.END)
    zone_resultat.insert(tk.END, texte_traduit)
    zone_resultat.config(state='disabled')

def action_ecouter():
    texte_traduit = zone_resultat.get("1.0", tk.END).strip()
    
    if not texte_traduit:
        messagebox.showwarning("Attention", "Il n'y a aucun texte traduit à lire.")
        return
    
    
    moteur_vocal = pyttsx3.init()
    
    
    voix_disponibles = moteur_vocal.getProperty('voices')
    for voix in voix_disponibles:
        nom_voix = voix.name.lower()
        id_voix = voix.id.lower()
        if "english" in nom_voix or "en_" in id_voix or "zira" in nom_voix or "david" in nom_voix:
            moteur_vocal.setProperty('voice', voix.id)
            break
            
    
    moteur_vocal.say(texte_traduit)
    moteur_vocal.runAndWait()
    moteur_vocal.stop()
fenetre = tk.Tk()
fenetre.title("LexiAcces — Traducteur Simple")
fenetre.geometry("520x550")
fenetre.config(bg="#f0f2f5")
titre = tk.Label(
    fenetre, 
    text="LexiAcces", 
    font=("Arial", 20, "bold"), 
    bg="#f0f2f5", 
    fg="#1a73e8"
)
titre.pack(pady=10)
label_entree = tk.Label(
    fenetre, 
    text="Texte en français :", 
    font=("Arial", 11, "bold"), 
    bg="#f0f2f5"
)
label_entree.pack(anchor="w", padx=25)
entree_texte = tk.Text(fenetre, height=4, width=55, font=("Arial", 10))
entree_texte.pack(padx=25, pady=5)
bouton_traduire = tk.Button(
    fenetre, 
    text="Traduire ➔", 
    font=("Arial", 11, "bold"), 
    bg="#1a73e8", 
    fg="white", 
    padx=15, 
    pady=5, 
    command=action_traduire
)
bouton_traduire.pack(pady=10)
label_sortie = tk.Label(
    fenetre, 
    text="Traduction (Anglais) :", 
    font=("Arial", 11, "bold"), 
    bg="#f0f2f5"
)
label_sortie.pack(anchor="w", padx=25)
zone_resultat = tk.Text(fenetre, height=4, width=55, font=("Arial", 10), state='disabled')
zone_resultat.pack(padx=25, pady=5)
bouton_ecouter = tk.Button(
    fenetre, 
    text="Écouter la traduction 🔊", 
    font=("Arial", 11, "bold"), 
    bg="#34a853", 
    fg="white", 
    padx=15, 
    pady=5, 
    command=action_ecouter
)
bouton_ecouter.pack(pady=15)
fenetre.mainloop()