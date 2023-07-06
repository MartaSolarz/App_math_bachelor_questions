import tkinter as tk

from manager import Manager

class Guis():
    
    def __init__(self, app, data) -> None:
        self.app = app
        self.questions = data

    def AM_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Analiza matematyczna")

        title = tk.Label(new_window, text="Analiza matematyczna", fg='green')
        title.pack()

        questions = self.questions.choose_category("AM")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()

    def GAL_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Geometria z algebrą liniową")

        title = tk.Label(new_window, text="Geometria z algebrą liniową", fg='red')
        title.pack()

        questions = self.questions.choose_category("GAL")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()


    def WDM_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Wstęp do matematyki")

        title = tk.Label(new_window, text="Wstęp do matematyki", fg='blue')
        title.pack()

        questions = self.questions.choose_category("WDM")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()


    def WDI_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Wstęp do informatyki")

        title = tk.Label(new_window, text="Wstęp do informatyki", fg='purple')
        title.pack()
        
        questions = self.questions.choose_category("WDI")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()

    def RRZ_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Równania różniczkowe zwyczajne")

        title = tk.Label(new_window, text="Równania różniczkowe zwyczajne", fg='green')
        title.pack()

        questions = self.questions.choose_category("RRZ")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()    

    def RP_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Rachunek prawdopodobieństwa")

        title = tk.Label(new_window, text="Rachunek prawdopodobieństwa", fg='green')
        title.pack()

        questions = self.questions.choose_category("RP")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()

    def TOPO_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Topologia")

        title = tk.Label(new_window, text="Topologia", fg='green')
        title.pack()

        questions = self.questions.choose_category("TOPO")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()

    def ALG_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Algebra")

        title = tk.Label(new_window, text="Algebra", fg='green')
        title.pack()

        questions = self.questions.choose_category("ALG")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()

    def MO_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Matematyka obliczeniowa")

        title = tk.Label(new_window, text="Matematyka obliczeniowa", fg='green')
        title.pack()

        questions = self.questions.choose_category("MO")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()

    def SAD_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Statystyczna analiza danych")

        title = tk.Label(new_window, text="Statystyczna analiza danych", fg='green')
        title.pack()

        questions = self.questions.choose_category("SAD")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()

    def FUN_gui(self):
        new_window = tk.Toplevel(self.app)
        new_window.title("Funkcje analityczne")

        title = tk.Label(new_window, text="Funkcje analityczne", fg='green')
        title.pack()

        questions = self.questions.choose_category("FUN")
        manager = Manager(new_window, questions)

        exit_button = tk.Button(new_window, text='Wyjście', width=25, command=new_window.destroy)    
        exit_button.pack()

        display_all_questions = tk.Button(new_window, text='Pokaż wszystkie pytania', width=25, command=manager.display_all_questions)
        display_all_questions.pack()

        start_learn = tk.Button(new_window, text="Zacznij naukę", width=25, command=manager.start_order_learn)
        start_learn.pack()