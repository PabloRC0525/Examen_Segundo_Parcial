import tkinter as tk
from tkinter import*
import random
from tkinter import messagebox
import string
class MATRICULA:
    def __init__(self,ACT,Nombre,AP,AM,NAC,Carr):
        self.Nombre = Nombre
        self.AP = AP
        self.AM = AM
        self.NAC = NAC
        self.Carr = Carr
        self.ACT = ACT
        
    def Matricula(self):
        if self.ACT.get() == "" or self.Nombre.get() == "" or self.AP.get() == "" or self.AM.get() == "" or self.Carr.get() == "":
            messagebox.showerror("Error","Uno o mas campos estan vacios")
        else:
            car = string.digits
            n = 0
            n2 = 1
            n3 = 2
            n4 = 3
            rdm = ''.join(random.choice(car) for i in range(3))
            AÑO = self.ACT.get()
            Nombre=self.Nombre.get().upper()
            AP=self.AP.get().upper()
            AM = self.AM.get().upper()
            Carr = self.Carr.get().upper()
            NAC = self.NAC.get()
            matricula = AÑO[n3] + AÑO[n4] + NAC[n3] + NAC[n4] + Nombre[n] + AP[n] + AM[n] + str(rdm) +Carr[n] + Carr[n2] + Carr[n3]
            messagebox.showinfo("Matricula","Su matricula es: " + matricula)


