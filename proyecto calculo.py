import sys
PYTHON_VERSION = sys.version_info.major

from punto import *
from math import pi

class Figura:

    def __init__(self, p1, p2):
        self.origen = p1
        self.destino = p2
        self.area = 0
        self.perimetro = 0

class Cuadrado(Figura):  

    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.destino)
        self.area = lado * lado

    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(self.destino)
        self.perimetro = lado + lado + lado + lado
        

class Circulo(Figura):  

    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.destino)
        self.area = pi * (radio ** 2)

    def calcular_perimetro(self):
        radio = self.origen.calcular_distancia(self.destino)
        self.perimetro = 2* pi * (radio )


class Rectangulo(Figura):  

    def calcular_area(self):
        temp = Punto(self.origen.x,self.destino.y)
        base = temp.calcular_distancia(self.destino)
        altura = temp.calcular_distancia(self.origen)
        self.area = altura * base

    def calcular_perimetro(self):
        temp = Punto(self.origen.x,self.destino.y)
        base = temp.calcular_distancia(self.destino)
        altura = temp.calcular_distancia(self.origen)
        self.perimetro = (altura + base) * 2

class Triangulo(Figura):  

    def calcular_area(self):
        temp = Punto(self.origen.x,self.destino.y)
        base = temp.calcular_distancia(self.destino)
        altura = temp.calcular_distancia(self.origen)
        self.area = (altura * base)/2

    def calcular_perimetro(self):
        temp = Punto(self.origen.x,self.destino.y)
        base = temp.calcular_distancia(self.destino)
        altura = temp.calcular_distancia(self.origen)
        hipotenusa = self.origen.calcular_distancia(self.destino)
        self.perimetro = base + altura + hipotenusa



if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")



class UI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('250x150')

        self.label1 = tk.Label(self.root, text='X1')
        self.label1.grid(row=2, column=0)
        self.inf_x1 = tk.StringVar(self.root)
        self.entry1 = tk.Entry(self.root, textvariable=self.inf_x1)
        self.entry1.grid(row=2, column=1)
        self.label2 = tk.Label(self.root, text='Y1')
        self.label2.grid(row=3, column=0)
        self.inf_y1 = tk.StringVar(self.root)
        self.entry2 = tk.Entry(self.root, textvariable=self.inf_y1)
        self.entry2.grid(row=3, column=1)

        self.label1 = tk.Label(self.root, text='X2')
        self.label1.grid(row=4, column=0)
        self.inf_x2 = tk.StringVar(self.root)
        self.entry1 = tk.Entry(self.root, textvariable=self.inf_x2)
        self.entry1.grid(row=4, column=1)
        self.label2 = tk.Label(self.root, text='Y2')
        self.label2.grid(row=5, column=0)
        self.inf_y2 = tk.StringVar(self.root)
        self.entry2 = tk.Entry(self.root, textvariable=self.inf_y2)
        self.entry2.grid(row=5, column=1)

        self.btn_cuadrado = tk.Button(self.root, text="Cuadrado", command=self.win2)
        self.btn_cuadrado.grid(row=0,column=0)
        self.btn_circulo = tk.Button(self.root, text="Circulo", command=self.win3)
        self.btn_circulo.grid(row=0,column=1)
        self.btn_rectangulo = tk.Button(self.root, text="Rectangulo", command=self.win4)
        self.btn_rectangulo.grid(row=1,column=0)
        self.btn_triangulo = tk.Button(self.root, text="Triangulo", command=self.win5)
        self.btn_triangulo.grid(row=1,column=1)
        self.root.mainloop()

    def win2(self):
        print self.inf_y2.get()
        p1 = Punto(int(self.inf_x1.get()),int(self.inf_y1.get()))
        p2 = Punto(int(self.inf_x2.get()),int(self.inf_y2.get()))
        figura = Cuadrado(p1, p2)
        figura.calcular_area()
        figura.calcular_perimetro()
        tl = tk.Toplevel(self.root, bg="Orange")
        tl.title("Circulo")
        tl.geometry('200x200')
        tl.focus_set()
        tl.grab_set()
        tl.transient(master=self.root)

        inf_p = tk.StringVar(tl)
        entry1 = tk.Entry(tl, textvariable=inf_p)
        entry1.grid(row=0, column=1)
        
        label1 = tk.Label(tl, text='Perimetro', bg="red")
        label1.grid(row=0, column=0)

        inf_a = tk.StringVar(tl)
        entry1 = tk.Entry(tl, textvariable=inf_a)
        entry1.grid(row=1, column=1)
        
        label1 = tk.Label(tl, text='Area', bg="red")
        label1.grid(row=1, column=0)

        inf_a.set(figura.area)
        inf_p.set(figura.perimetro)
        
    def win3(self):
        print self.inf_y2.get()
        p1 = Punto(int(self.inf_x1.get()),int(self.inf_y1.get()))
        p2 = Punto(int(self.inf_x2.get()),int(self.inf_y2.get()))
        figura = Circulo(p1, p2)
        figura.calcular_area()
        figura.calcular_perimetro()
        tl = tk.Toplevel(self.root, bg="Orange")
        tl.title("Cuadrado")
        tl.geometry('200x200')
        tl.focus_set()
        tl.grab_set()
        tl.transient(master=self.root)

        inf_p = tk.StringVar(tl)
        entry1 = tk.Entry(tl, textvariable=inf_p)
        entry1.grid(row=0, column=1)
        
        label1 = tk.Label(tl, text='Perimetro', bg="red")
        label1.grid(row=0, column=0)

        inf_a = tk.StringVar(tl)
        entry1 = tk.Entry(tl, textvariable=inf_a)
        entry1.grid(row=1, column=1)
        
        label1 = tk.Label(tl, text='Area', bg="red")
        label1.grid(row=1, column=0)

        inf_a.set(figura.area)
        inf_p.set(figura.perimetro)

    def win4(self):
        print self.inf_y2.get()
        p1 = Punto(int(self.inf_x1.get()),int(self.inf_y1.get()))
        p2 = Punto(int(self.inf_x2.get()),int(self.inf_y2.get()))
        figura = Rectangulo(p1, p2)
        figura.calcular_area()
        figura.calcular_perimetro()
        tl = tk.Toplevel(self.root, bg="Orange")
        tl.title("Rectangulo")
        tl.geometry('200x200')
        tl.focus_set()
        tl.grab_set()
        tl.transient(master=self.root)

        inf_p = tk.StringVar(tl)
        entry1 = tk.Entry(tl, textvariable=inf_p)
        entry1.grid(row=0, column=1)
        
        label1 = tk.Label(tl, text='Perimetro', bg="red")
        label1.grid(row=0, column=0)

        inf_a = tk.StringVar(tl)
        entry1 = tk.Entry(tl, textvariable=inf_a)
        entry1.grid(row=1, column=1)
        
        label1 = tk.Label(tl, text='Area', bg="red")
        label1.grid(row=1, column=0)

        inf_a.set(figura.area)
        inf_p.set(figura.perimetro)

    def win5(self):
        print self.inf_y2.get()
        p1 = Punto(int(self.inf_x1.get()),int(self.inf_y1.get()))
        p2 = Punto(int(self.inf_x2.get()),int(self.inf_y2.get()))
        figura = Triangulo(p1, p2)
        figura.calcular_area()
        figura.calcular_perimetro()
        tl = tk.Toplevel(self.root, bg="Orange")
        tl.title("Triangulo")
        tl.geometry('200x200')
        tl.focus_set()
        tl.grab_set()
        tl.transient(master=self.root)

        inf_p = tk.StringVar(tl)
        entry1 = tk.Entry(tl, textvariable=inf_p)
        entry1.grid(row=0, column=1)
        
        label1 = tk.Label(tl, text='Perimetro', bg="red")
        label1.grid(row=0, column=0)

        inf_a = tk.StringVar(tl)
        entry1 = tk.Entry(tl, textvariable=inf_a)
        entry1.grid(row=1, column=1)
        
        label1 = tk.Label(tl, text='Area', bg="red")
        label1.grid(row=1, column=0)

        inf_a.set(figura.area)
        inf_p.set(figura.perimetro)
ui = UI()
