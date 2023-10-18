import tkinter as tk
from manager import Manager

class Guis:

    def __init__(self, app, data) -> None:
        self.app = app
        self.questions = data
        self.colors = {
            "AM": 'red',
            "GAL": 'red',
            "WDM": 'red',
            "WDI": 'red',
            "RRZ": 'green',
            "RP": 'green',
            "TOPO": 'green',
            "ALG": 'green',
            "MO": 'green',
            "SAD": 'blue',
            "FUN": 'blue'
        }

    def createWindow(self, category, title_text):
        new_window = tk.Toplevel(self.app)
        new_window.title(title_text)

        title = tk.Label(new_window, text=title_text, fg=self.colors[category])
        title.pack()

        questions = self.questions.choose_category(category)
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()

    def AM_gui(self):
        self.createWindow("AM", "Analiza matematyczna")

    def GAL_gui(self):
        self.createWindow("GAL", "Geometria z algebrą liniową")

    def WDM_gui(self):
        self.createWindow("WDM", "Wstęp do matematyki")

    def WDI_gui(self):
        self.createWindow("WDI", "Wstęp do informatyki")

    def RRZ_gui(self):
        self.createWindow("RRZ", "Równania różniczkowe zwyczajne")

    def RP_gui(self):
        self.createWindow("RP", "Rachunek prawdopodobieństwa")

    def TOPO_gui(self):
        self.createWindow("TOPO", "Topologia")

    def ALG_gui(self):
        self.createWindow("ALG", "Algebra")

    def MO_gui(self):
        self.createWindow("MO", "Matematyka obliczeniowa")

    def SAD_gui(self):
        self.createWindow("SAD", "Statystyczna analiza danych")

    def FUN_gui(self):
        self.createWindow("FUN", "Funkcje analityczne")
