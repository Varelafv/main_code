import tkinter as tk

# Cr�er une fen�tre principale
root = tk.Tk()

# D�finir le titre de la fen�tre
root.title("Ma fen�tre avec deux boutons")

# D�finir la taille de la fen�tre
root.geometry("400x200")

# Fonction appel�e lorsque le premier bouton est cliqu�
def button1_click():
    print("Le premier bouton a �t� cliqu� !")

# Fonction appel�e lorsque le deuxi�me bouton est cliqu�
def button2_click():
    print("Le deuxi�me bouton a �t� cliqu� !")

# Cr�er deux boutons
button1 = tk.Button(root, text="Bouton 1", command=button1_click)
button2 = tk.Button(root, text="Bouton 2", command=button2_click)

# Afficher les boutons dans la fen�tre
button1.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.RIGHT, padx=10)

# Lancer la boucle d'�v�nements de la fen�tre
root.mainloop()
