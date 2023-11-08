from tkinter import *
import tkinter
from datetime import datetime



#cores
cor1 = '#3d3d3d' #preta
cor2 = '#fafcff' #branca
cor3 = '#21c25c' #verde
cor4 = '#eb463b' #vermelha
cor5 = '#dedcdc' #cinza
cor6 = '#3080f0' #azul

fundo = cor1
cor = cor2

window=Tk()
window.title('')
window.geometry('440x180')
window.resizable(width=False, height=False)
window.configure(bg=cor1)

def relogio():
    tempo = datetime.now()

    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%a')
    dia = tempo.day
    mes = tempo.strftime('%B')
    ano = tempo.strftime('%Y')

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + ' ' + str(dia) + 
              '/' + str(mes) + '/' + str(ano)) 

l1 = Label(window, text='10:50:22', font=('Arial 80'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
 
l2 = Label(window, text='', font=('Arial 20'), bg=fundo, fg=cor)
l2.grid(row=3, column=0, sticky=NW, padx=5)


relogio()
window.mainloop()


