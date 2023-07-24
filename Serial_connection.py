import tkinter as tk

# Créer une fenêtre principale
root = tk.Tk()

# Définir le titre de la fenêtre
root.title("Ma fenêtre avec deux boutons")

# Définir la taille de la fenêtre
root.geometry("400x200")

# Fonction appelée lorsque le premier bouton est cliqué
def button1_click():
    print("Le premier bouton a été cliqué !")

# Fonction appelée lorsque le deuxième bouton est cliqué
def button2_click():
    print("Le deuxième bouton a été cliqué !")

# Créer deux boutons
button1 = tk.Button(root, text="Bouton 1", command=button1_click)
button2 = tk.Button(root, text="Bouton 2", command=button2_click)

# Afficher les boutons dans la fenêtre
button1.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.RIGHT, padx=10)

# Lancer la boucle d'événements de la fenêtre
root.mainloop()
