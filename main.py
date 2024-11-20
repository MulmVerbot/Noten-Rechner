import tkinter as tk
import time
from tkinter import messagebox
import os
import sys
#            _ .-') _             .-') _                   
#           ( (  OO) )           ( OO ) )                  
#           \     .'_  .---.,--./ ,--,'   ,--.   .-----.  
#           ,`'--..._)/_   ||   \ |  |\  /  .'  / ,-.   \ 
#           |  |  \  ' |   ||    \|  | ).  / -. '-'  |  | 
#           |  |   ' | |   ||  .     |/ | .-.  '   .'  /  
#           |  |   / : |   ||  |\    |  ' \  |  |.'  /__  
#           |  '--'  / |   ||  | \   |  \  `'  /|       | 
#           `-------'  `---'`--'  `--'   `----' `-------'  <-2024->

class NoTi():
    def __init__(self, master):
        self.master = master
        self.Windows = None
        self.Programm_Name = "Noti"
        self.Benutzerordner = os.path.expanduser('~')
        self.Pfad_DB_ordner = os.path.join(self.Benutzerordner, "Hefte")
        self.Pfad_DB = os.path.join(self.Pfad_DB_ordner, "Eintrag.txt")
       
        if not os.path.exists(self.Pfad_DB_ordner):
            self.erster_start = True
        elif os.path.exists(self.Pfad_DB_ordner):
            self.erster_start = False
        else:
            self.erster_start = True

        self.init_start()

    def init_start(self):
        print("init_start")
        self.GUI_init()
        self.OS_check()

        if self.erster_start == True:
            print("bereite ein paar Sachen zum ersten Start vor...")
            try:
                os.mkdir(self.Pfad_DB)
            except PermissionError:
                messagebox.showerror(title=self.Programm_Name, message=f"Fehler beim schreiben im Benutzerordner, stellen Sie sicher dass Zugriff darauf besteht.")
            except Exception as e1:
                print(f"Fehler beim erstellen der Programmordner: {e1}")
        


    def GUI_init(self):
        print("GUI_init(def)")
        self.Info_l = tk.Label(root, text="Heft laden drücken")
        self.Info_l.pack()
        self.Heft_öffnen_knopp = tk.Button(root, text="Heft laden", command=self.Heft_laden_c)
        self.Heft_öffnen_knopp.pack()

    def GUI_schreibfeld_laden(self):
        self.schreibfeld = tk.Text(root, width=200, height=200)
        try:
            self.Heft_öffnen_knopp.pack_forget()
            self.Info_l.pack_forget()
        except:
            pass
        self.schreibfeld.pack()

    def OS_check(self):
        if sys.platform == "darwin":
            self.Windows = False
            print("[-Plattform-] Darwin")
        else:
            self.Windows = True
            print("[-Plattform-] Windows")

    def Heft_laden_c(self):
        print("Heft_laden_c(def)")
        self.GUI_schreibfeld_laden()
        try:
            with open(self.Pfad_DB, "r") as DB_gel:
                geladenes_Heft = DB_gel.read()
                if DB_gel.read() == "" or None:
                    geladenes_Heft = "Leer"
            self.schreibfeld.insert("0.0", geladenes_Heft)
        except Exception as e:
            print(f"[-ERR-] Die Liste konnte nicht geladen werden. Fehlermeldung: {e}")
            geladenes_Heft = "Leer"

if __name__ == "__main__":
    root = tk.Tk()
    width = 800
    height = 520
    def mittig_fenster(root, width, height):
        fenster_breite = root.winfo_screenwidth()
        fenster_höhe = root.winfo_screenheight()
        x = (fenster_breite - width) // 2
        y = (fenster_höhe - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
    mittig_fenster(root, width, height)
    NoTi = NoTi(root)
    root.mainloop()