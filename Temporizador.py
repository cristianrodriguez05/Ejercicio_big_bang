import tkinter as tk
import time
from playsound import playsound
from threading import Thread

def cronometro():

    def CasiFinRonda():
        playsound("Ultimos segundos.mp3")

    def FinRonda():
        playsound("Fin de ronda.mp3")

    def iniciar():
        global repeticion, tiempo, descanso, t, i
        tiempo = int(e1.get()) 
        repeticion = int(e2.get()) 
        descanso = int(e3.get()) 
        t = tiempo
        i = 1
        tiempoRutina()

    def tiempoRutina():
        global t, tiempo, repeticion, i

        for w in pantallaReloj.winfo_children():
            w.grid_remove()

        tk.Label(pantallaReloj, text="RONDA "+str(i), bg="#000000", fg="OliveDrab3", font=("", 30)).grid(row=0, column=0)
        tk.Label(pantallaReloj, text=time.strftime("%H:%M:%S", time.gmtime(t)), bg="#000000", fg="OliveDrab3", font=("", 40)).grid(row=1, column=0)

        if t==0:
            i=i+1

        if(t>0):
            t -= 1
            ventanaCronometro.after(1000, tiempoRutina)
        else:
            repeticion -= 1
            t = descanso
            if(repeticion > 0):
                ventanaCronometro.after(1000, tiempoDescanso)

        CasiFinR = Thread(target=CasiFinRonda)
        FinR = Thread(target=FinRonda)

        if(t>0 and t<5):
            CasiFinR.start()
        
        if(t == 0):
            FinR.start()

    def tiempoDescanso():
        global t, tiempo

        for w in pantallaReloj.winfo_children():
            w.grid_remove()

        tk.Label(pantallaReloj, text="DESCANSO", bg="#000000", fg="OliveDrab3", font=("", 30)).grid(row=0, column=0)
        tk.Label(pantallaReloj, text=time.strftime("%H:%M:%S", time.gmtime(t)), bg="#000000", fg="OliveDrab3", font=("", 40)).grid(row=1, column=0)
        
        if(t>0):
            t -= 1
            ventanaCronometro.after(1000, tiempoDescanso)
        else:
            t = tiempo
            ventanaCronometro.after(1000, tiempoRutina)
        
        CasiFinR = Thread(target=CasiFinRonda)
        FinR = Thread(target=FinRonda)

        if(t>0 and t<5):
            CasiFinR.start()
            
        if(t == 0):
            FinR.start()

    ventanaCronometro = tk.Toplevel(marco)
    ventanaCronometro.geometry("410x360")
    ventanaCronometro.configure(background="#000000")

    fondo = tk.Frame(ventanaCronometro)
    fondo.config(bg="#000000")
    fondo.pack(fill="both", expand="true", padx=20, pady=30)

    tk.Label(fondo, text="       Temporizador EMOM       ", bg="OliveDrab3",font=(None, 20)).grid(row=0, column=0)

    pantallaReloj = tk.Frame(fondo, bg="#000000")
    pantallaReloj.grid(row=1, column=0, ipady=10)

    iniciar()

    ventanaCronometro.mainloop()

marco=tk.Tk()
marco.title("Temporizador EMOM")
marco.geometry("410x360")
marco.configure(background="#000000")

Encabezado1 = tk.Label(marco, text="         Temporizador EMOM          ", bg="OliveDrab3",font=(None, 20)).grid(row=0,column=0,columnspan=2)

Bar1 = tk.Label(marco, text="___________________________________________________", bg="#000000", fg="#000000",).grid(row=25,column=0,columnspan=2)

Barra2 = tk.Label(marco, text="___________________________________________________", bg="#000000", fg="OliveDrab3").grid(row=8,column=0,columnspan=2)

Titulo2 = tk.Label(marco, text="    CADA    ", bg="#000000", fg="OliveDrab3").grid(row=9,column=0,columnspan=2)

e1 = tk.Entry(marco, bg="#000000", fg="OliveDrab3")
e1.grid(row=12,column=0,columnspan=2)

Texto2 = tk.Label(marco, text="Segundos", bg="#000000", fg="OliveDrab3").grid(row=13,column=0,columnspan=2)
Barra3 = tk.Label(marco, text="___________________________________________________", bg="#000000", fg="OliveDrab3").grid(row=14,column=0,columnspan=2)
Titulo3 = tk.Label(marco, text="    REPETICIONES   ", bg="#000000", fg="OliveDrab3").grid(row=15,column=0,columnspan=2)
e2 = tk.Entry(marco, bg="#000000", fg="OliveDrab3")
e2.grid(row=16,column=0,columnspan=2)

Barra4 = tk.Label(marco, text="___________________________________________________", bg="#000000", fg="OliveDrab3").grid(row=17,column=0,columnspan=2)
Titulo4 = tk.Label(marco, text="    DESCANSO    ", bg="#000000", fg="OliveDrab3").grid(row=18,column=0,columnspan=2)
e3 = tk.Entry(marco, bg="#000000", fg="OliveDrab3")
e3.grid(row=19,column=0,columnspan=2)

Texto3 = tk.Label(marco, text="Segundos", bg="#000000", fg="OliveDrab3").grid(row=20,column=0,columnspan=2)
Barra5 = tk.Label(marco, text="___________________________________________________",bg="#000000", fg="OliveDrab3").grid(row=23,column=0,columnspan=2)

Bar2 = tk.Label(marco, text="___________________________________________________", bg="#000000", fg="#000000",).grid(row=25,column=0,columnspan=2)

btnEmpezar = tk.Button(marco,text='Empezar',command=cronometro, borderwidth=7,bg="OliveDrab3",width=50, anchor="n")
btnEmpezar.grid(row=26,column=0,columnspan=2)

marco.mainloop()
