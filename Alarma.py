from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import pygame, sys
from pygame.locals import *
from pygame import mixer
from PIL import ImageTk,Image
root = Tk()
pygame.init()

hr=StringVar()
min=StringVar()
ventana = Frame(root, bg="#CCFFCC")
ventana.pack(fill='both', expand=1)
root.geometry("250x400")
mixer.init()

titulo = Label(ventana, text="ALARMA", font=("Bernard MT",15, "bold"), bg="#CCFFCC")
titulo.place(relx=0.35,rely=0.05)

etiquetahora = Label(ventana, text="Hora", font=("Bernard MT",10), bg="#CCFFCC")
etiquetahora.place(relx=0.15, rely=0.15)
entradahora = Entry(ventana, textvariable=hr).place(relx=0.35, rely=0.15)

etiquetaminutos = Label(ventana, text="Minutos", font=("Bernard MT",10),bg="#CCFFCC")
etiquetaminutos.place(relx=0.15, rely=0.21)
entradaminutos = Entry(ventana, textvariable=min).place(relx=0.35, rely=0.21)

botonAlarma = Button(ventana, text="Establecer alarma", font=("Bernard MT",10)).place(relx=0.30, rely=0.28)

def detener():
     pygame.mixer.music.stop()
     ventana.config(bg="#CCFFCC")
     etiquetahora.config(bg="#CCFFCC")
     etiquetaminutos.config(bg="#CCFFCC")
     titulo.config(bg="#CCFFCC")
     miEtiqueta.config(bg="#CCFFCC")

botonStop = Button(ventana, text="Detener alarma", font=("Bernard MT",10), command=detener).place(relx=0.33, rely=0.51)

def clock():
    horas = time.strftime("%H")
    minutos = time.strftime("%M")
    segundos = time.strftime("%S")

    horaLocal = horas + ":" + minutos + ":" + segundos
    miEtiqueta.config(text=horaLocal)
    miEtiqueta.after(1000, clock)

    alarmaHora = hr.get()
    alarmaMinutos = min.get()

    if horas == alarmaHora and minutos == alarmaMinutos and segundos == "00":
        mixer.music.load("Time.mp3")
        mixer.music.play()
        ventana.config(bg="#FF6666")
        etiquetahora.config(bg="#FF6666")
        etiquetaminutos.config(bg="#FF6666")
        titulo.config(bg="#FF6666")
        miEtiqueta.config(bg="#FF6666")

miEtiqueta = Label(root, text="", font=("Javanese text", 20, "bold"),bg="#CCFFCC")
miEtiqueta.place(relx=0.30, rely=0.35)

img = Image.open("Alarmaa.PNG")
imagen = img.resize((100,100))
imagenP = ImageTk.PhotoImage(imagen)
Ponerimagen = Label(ventana, image=imagenP).place(relx=0.32,rely=0.60)

clock()
root.mainloop()