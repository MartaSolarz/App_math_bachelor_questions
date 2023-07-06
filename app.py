import tkinter as tk
from tkinter import messagebox

from guis import Guis

class App:
    def __init__(self, questions) -> None:
        self.app = tk.Tk()
        self.messagebox = messagebox
        self.guis = Guis(self.app, questions)
    
        self.create_app()

    def create_app(self):
        self.app.title('Egzamin licencjacki matematyka')

        frame = tk.Frame(self.app)
        frame.pack()

        choose_label = tk.Label(frame, text='Wybierz przedmiot')
        choose_label.pack()     

        button_frame = tk.Frame(frame)
        button_frame.pack()

        am = tk.Button(button_frame, text='AM', fg='green', command=self.guis.AM_gui)
        am.pack(side=tk.LEFT)

        gal = tk.Button(button_frame, text='GAL', fg='red', command=self.guis.GAL_gui)
        gal.pack(side=tk.LEFT)

        wdm = tk.Button(button_frame, text='WDM', fg='blue', command=self.guis.WDM_gui)
        wdm.pack(side=tk.LEFT)

        wdi = tk.Button(button_frame, text='WDI', fg='purple', command=self.guis.WDI_gui)
        wdi.pack(side=tk.LEFT)

        rp = tk.Button(button_frame, text='RP', fg='green', command=self.guis.RP_gui)
        rp.pack(side=tk.LEFT)

        rrz = tk.Button(button_frame, text='RRZ', fg='red', command=self.guis.RRZ_gui)
        rrz.pack(side=tk.LEFT)

        topo = tk.Button(button_frame, text='TOPO', fg='blue', command=self.guis.TOPO_gui)
        topo.pack(side=tk.LEFT)

        alg = tk.Button(button_frame, text='ALG', fg='purple', command=self.guis.ALG_gui)
        alg.pack(side=tk.LEFT)

        mo = tk.Button(button_frame, text='MO', fg='green', command=self.guis.MO_gui)
        mo.pack(side=tk.LEFT)

        sad = tk.Button(button_frame, text='SAD', fg='red', command=self.guis.SAD_gui)
        sad.pack(side=tk.LEFT)

        fun = tk.Button(button_frame, text='FUN', fg='blue', command=self.guis.FUN_gui)
        fun.pack(side=tk.LEFT)

        exit_button = tk.Button(self.app, text='Wyjście', width=25, command=self.app.destroy)
        exit_button.pack()

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.app.mainloop()


    def on_closing(self):
        if self.messagebox.askokcancel("Potwierdzenie", "Czy na pewno chcesz zamknąć okno?"):
            self.app.focus_set()
            self.app.destroy()
