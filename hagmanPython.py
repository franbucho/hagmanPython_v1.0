import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego del Ahorcado")
        self.word_to_guess = ""
        self.guessed_letters = []
        self.attempts_left = 6

        # Palabras para adivinar
        self.words = ["python", "javascript", "java", "ruby", "html", "css", "php", "swift", "kotlin", "csharp"]

        # Elementos de la interfaz
        self.word_display_label = tk.Label(master, text="", font=("Helvetica", 24))
        self.word_display_label.pack(pady=20)

        self.guess_entry = tk.Entry(master, font=("Helvetica", 16))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Adivinar", command=self.make_guess, font=("Helvetica", 16))
        self.guess_button.pack(pady=10)

        self.hint_button = tk.Button(master, text="Pista", command=self.show_hint, font=("Helvetica", 16))
        self.hint_button.pack(pady=10)

        self.restart_button = tk.Button(master, text="Reiniciar Juego", command=self.restart_game, font=("Helvetica", 16))
        self.restart_button.pack(pady=10)

        # Dibujar ahorcado
        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()
        self.draw_hangman()

        # Iniciar juego
        self.restart_game()

    def choose_word(self):
        return random.choice(self.words)

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def draw_hangman(self):
        self.canvas.create_line(20, 180, 180, 180, width=2)  # Base horizontal
        self.canvas.create_line(50, 180, 50, 20, width=2)    # Poste vertical
        self.canvas.create_line(50, 20, 125, 20, width=2)     # Línea superior
        self.canvas.create_line(125, 20, 125, 50, width=2)    # Soga
        self.canvas.create_oval(120, 50, 130, 60)            # Cabeza
        self.canvas.create_line(125, 60, 125, 120)           # Cuerpo
        self.canvas.create_line(125, 80, 110, 70)            # Brazo izquierdo
        self.canvas.create_line(125, 80, 140, 70)            # Brazo derecho
        self.canvas.create_line(125, 120, 110, 140)          # Pierna izquierda
        self.canvas.create_line(125, 120, 140, 140)          # Pierna derecha

        for part in range(1, 11):
            self.canvas.itemconfig(part, state="hidden")

    def update_hangman(self):
        self.canvas.itemconfig(11 - self.attempts_left, state="normal")

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if guess in self.guessed_letters:
            messagebox.showinfo("Advertencia", "Ya has adivinado esa letra. Intenta con otra.")
        else:
            self.guessed_letters.append(guess)

            if guess not in self.word_to_guess:
                self.attempts_left -= 1
                self.update_hangman()
                messagebox.showinfo("Incorrecto", f"Incorrecto. Te quedan {self.attempts_left} intentos.")

            word_display = self.display_word()
            self.word_display_label.config(text=word_display)

            if "_" not in word_display:
                messagebox.showinfo("¡Felicidades!", "¡Has adivinado la palabra!")

            if self.attempts_left == 0:
                messagebox.showinfo("Fin del Juego", f"¡Lo siento! La palabra era: {self.word_to_guess}")

    def show_hint(self):
        hint = random.choice(self.word_to_guess)
        messagebox.showinfo("Pista", f"Una letra de la palabra es: {hint.upper()}")

    def restart_game(self):
        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.attempts_left = 6

        self.word_display_label.config(text=self.display_word())
        self.guess_entry.delete(0, tk.END)

        for part in range(1, 11):
            self.canvas.itemconfig(part, state="hidden")

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    game.run()
