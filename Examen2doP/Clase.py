import tkinter as tk
from tkinter import*
import random
from tkinter import messagebox
class MATRICULA:
    def __init__(self,Nombre,AP,AM,NAC,Carr):
        self.Nombre = Nombre
        self.AP = AP
        self.AM = AM
        self.NAC = NAC
        self.Carr = Carr
        
    def Matricula(self):
        if self.Nombre.get() == "" or self.Nombre.get() == "" or self.AP.get() == "" or self.AM.get() == "" or self.Carr.get() == "":
            messagebox.showerror("Error","Uno o mas campos estan vacios")
        else:
            n = 0
            n2 = 2
            AÑO = "2023"
            Nombre=self.Nombre.get().upper()
            AP=self.AP.get().upper()
            AM = self.AM.get().upper()
            Carr = self.Carr.get().upper()
            NAC = self.NAC.get()
            matricula = AÑO + Nombre + AP + AM + NAC + Carr
            messagebox.showinfo("Matricula","Su matricula es: " + matricula)


