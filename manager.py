import tkinter as tk
from tkinter import messagebox
import random as rnd

class Manager:
    def __init__(self, app, questions):
        self.app = app
        self.questions = questions
        self.remaining_questions = questions
        self.current_question = None
        self.checkbox = None
        self.window = None

    def display_all_questions(self):
        
        new_window = tk.Toplevel(self.app)
        new_window.attributes('-fullscreen', True)
        new_window.title("Wszystkie pytania")
    
        scrollbar = tk.Scrollbar(new_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
        listbox = tk.Listbox(new_window, yscrollcommand=scrollbar.set)
        listbox.pack(fill=tk.BOTH, expand=True)
    
        for i, question in enumerate(self.questions):
            listbox.insert(tk.END, f"{i+1}. {question}")
    
        scrollbar.config(command=listbox.yview)
    
        close_button = tk.Button(new_window, text='Zamknij', width=25, command=new_window.destroy)
        close_button.pack()        

    def start_order_learn(self):
        if not self.remaining_questions:
            messagebox.showinfo("Informacja", "Brak pytań.")
            return

        new_window = tk.Toplevel(self.app)
        new_window.title("Tryb nauki w kolejności chronologicznej zagadnień")
        new_window.attributes('-fullscreen', True)

        width = self.app.winfo_screenwidth()
        window_width = int(width * 0.8)

        self.question_label = tk.Label(new_window, wraplength=window_width)
        self.question_label.pack()

        self.show_next_question()

        next_button = tk.Button(new_window, text="Następne pytanie", width=25, command=self.show_next_question)
        next_button.pack()

        close_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)
        close_button.pack()

        def on_closing():
            if messagebox.askokcancel("Potwierdzenie", "Czy na pewno chcesz zamknąć okno?"):
                self.app.focus_set()
                new_window.destroy()

        new_window.protocol("WM_DELETE_WINDOW", on_closing)

    def show_next_question(self):
        if self.remaining_questions:
            self.current_question = rnd.choice(self.remaining_questions)
            self.question_label.configure(text=self.current_question)


