import Tkinter as tk
from Tkinter import *
import Tkinter 

class Temporizador:



   
   #def calcular():

   def cronometro(self, marco):
      ventanaCronometro=Toplevel(marco)
      ventanaCronometro.geometry("480x400")
      ventanaCronometro.configure(background="#000000")

      Encabezado_1 = tk.Label(ventanaCronometro, text="         Temporizador EMOM          ", bg="OliveDrab3",font=(None, 20)).grid(row=0,column=0,columnspan=3)

      Barra_1 = tk.Label(ventanaCronometro, text="___________________________________________________", bg="black",fg="black").grid(row=1,column=0,columnspan=3)
      Titulo_1 = tk.Label(ventanaCronometro, text="    EJERCICIO   ", bg="DarkOliveGreen1").grid(row=2,column=0,columnspan=3)
      ejercicio = tk.StringVar()
      Etiqueta1 =tk.Label(ventanaCronometro, textvariable = ejercicio, bg="grey").grid(row=3, column=0,columnspan=3)
      
      Barra_2 = tk.Label(ventanaCronometro, text="___________________________________________________", bg="black",fg="black").grid(row=4,column=0,columnspan=3)
      rondaActual= tk.StringVar()
      rondaFinal= tk.StringVar()
      Titulo_2 = tk.Label(ventanaCronometro, text="    RONDA    ", bg="DarkOliveGreen1").grid(row=5,column=0,columnspan=3)
      Etiqueta2=tk.Label(ventanaCronometro, textvariable = rondaActual, bg="grey").grid(row=6, column=0,columnspan=3)
      Titulo_3 = tk.Label(ventanaCronometro, text="    DE    ", bg="DarkOliveGreen1").grid(row=7,column=0,columnspan=3)
      Etiqueta3=tk.Label(ventanaCronometro, textvariable = rondaFinal, bg="grey").grid(row=8, column=0,columnspan=3)
      
      Barra_3 = tk.Label(ventanaCronometro, text="___________________________________________________", bg="black",fg="black").grid(row=9,column=0,columnspan=3)
      time= tk.Label(ventanaCronometro,bg="grey" ,fg='red', width=20, font=("","18")).grid(row=10,column=0,columnspan=3)
      
      Barra_4 = tk.Label(ventanaCronometro, text="___________________________________________________", bg="black",fg="black").grid(row=11,column=0,columnspan=3)
      anuncio = tk.StringVar()
      Etiqueta4 =tk.Label(ventanaCronometro, textvariable = anuncio, bg="grey").grid(row=12, column=0,columnspan=3)

      Barra_5 = tk.Label(ventanaCronometro, text="___________________________________________________", bg="black",fg="black").grid(row=13,column=0,columnspan=3)
      btnPausar = Button(ventanaCronometro,text='Pausar', borderwidth=7,bg="OliveDrab3",width=20, anchor="n").grid(row=14,column=0)
      btnContinuar = Button(ventanaCronometro,text='Continuar', borderwidth=7,bg="OliveDrab3",width=20, anchor="n").grid(row=14,column=1)
      btnReiniciar = Button(ventanaCronometro,text='Reiniciar', borderwidth=7,bg="OliveDrab3",width=20, anchor="n").grid(row=14,column=2)
      
   def iniciar(self):

      marco=tk.Tk()
      marco.title("Temporizador EMOM")
      marco.geometry("410x500")
      marco.configure(background="#000000")

      Encabezado1 = tk.Label(marco, text="         Temporizador EMOM          ", bg="OliveDrab3",font=(None, 20)).grid(row=0,column=0,columnspan=2)
      Bar1 = tk.Label(marco, text="___________________________________________________", bg="black",fg="black").grid(row=1,column=0,columnspan=2)
 

      Titulo1 = tk.Label(marco, text="    RUTINA   ", bg="DarkOliveGreen1").grid(row=5,column=0,columnspan=2)
      e1 = Entry(marco)
      e1.pack()
      e1.grid(row=7,column=0,columnspan=2,padx=10,ipadx=100)
      Barra2 = tk.Label(marco, text="___________________________________________________", bg="black",fg="grey").grid(row=8,column=0,columnspan=2)
      
      Titulo2 = tk.Label(marco, text="    CADA    ", bg="DarkOliveGreen1").grid(row=9,column=0,columnspan=2)
      e2 = Entry(marco)
      e2.pack()
      e2.grid(row=10,column=0,columnspan=2)
      Texto1 = tk.Label(marco, text="Minutos", bg="grey").grid(row=11,column=0,columnspan=2)
      e3 = Entry(marco)
      e3.pack()
      e3.grid(row=12,column=0,columnspan=2)
      Texto2 = tk.Label(marco, text="Segundos", bg="grey").grid(row=13,column=0,columnspan=2)
      Barra3 = tk.Label(marco, text="___________________________________________________", bg="black",fg="grey").grid(row=14,column=0,columnspan=2)

      Titulo3 = tk.Label(marco, text="    REPETICIONES   ", bg="DarkOliveGreen1").grid(row=15,column=0,columnspan=2)
      e4 = Entry(marco)
      e4.pack()
      e4.grid(row=16,column=0,columnspan=2)
      Barra4 = tk.Label(marco, text="___________________________________________________", bg="black",fg="grey").grid(row=17,column=0,columnspan=2)

      Titulo4 = tk.Label(marco, text="    DESCANSO    ", bg="DarkOliveGreen1").grid(row=18,column=0,columnspan=2)
      e5 = Entry(marco)
      e5.pack()
      e5.grid(row=19,column=0,columnspan=2)
      Texto3 = tk.Label(marco, text="Minutos", bg="grey").grid(row=20,column=0,columnspan=2)
      e6 = Entry(marco)
      e6.pack()
      e6.grid(row=21,column=0,columnspan=2)
      Texto4 = tk.Label(marco, text="Segundos", bg="grey").grid(row=22,column=0,columnspan=2)
      Barra5 = tk.Label(marco, text="___________________________________________________", bg="black",fg="grey").grid(row=23,column=0,columnspan=2)
      
      Bar2 = tk.Label(marco, text="___________________________________________________", bg="black",fg="black").grid(row=25,column=0,columnspan=2)
      btnEmpezar = Button(marco,text='Empezar',command=lambda: temporizador.cronometro(marco), borderwidth=7,bg="OliveDrab3",width=50, anchor="n")
      btnEmpezar.grid(row=26,column=0,columnspan=2)
    
      
      marco.mainloop()


temporizador = Temporizador()
temporizador.iniciar()
