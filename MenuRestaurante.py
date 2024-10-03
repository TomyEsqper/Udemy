from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox
operador = ''
precios_comida = [5000, 6000, 5500, 3400, 6100, 3200, 6400, 9200]
precios_bebida = [6000, 4000, 2000, 1000, 1000, 4000, 5300, 2000]
precios_postre = [5000, 5500, 4600, 7000, 9000, 1000, 4300, 3200]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END) 
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,  END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,  END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0,  END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

def TOTAL():
    sub_total_Comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_Comida = sub_total_Comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

     
    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[p])
        p += 1

    sub_total = sub_total_Comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.12
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_Comida, 0)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 0)}')
    var_costo_postre.set(f'$ {round(sub_total_postre, 0)}')
    var_subtotal.set(f'$ {round(sub_total, 0)}')
    var_impuesto.set(f'$ {round(impuestos, 0)}')
    var_total.set(f'$ {round(total, 0)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N° - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 60 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 72 + '\n')
    
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1  
    
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1  

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postre[x]}\n')
        x += 1  

    texto_recibo.insert(END, f'-' * 72 + '\n')
    texto_recibo.insert(END, f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de las bebidas: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 72 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("información", "Su recibo ha sido guardado")

def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set(0)
    for texto in texto_bebida:
        texto.set(0)
    for texto in texto_postre:
        texto.set(0)

    for cuadros in cuadros_comida:
        cuadros.config(state = DISABLED)
    for cuadros in cuadros_bebida:
        cuadros.config(state = DISABLED)
    for cuadros in cuadros_postre:
        cuadros.config(state = DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')
#iniciar tkinterbebidaacion = Tk()
aplicacion = Tk()
#Tamaño ventana

aplicacion.geometry('1080x720+0+0')

#Evitar maximixar
aplicacion.resizable(0,0)

#Editar titulo ventana
aplicacion.title("Gestor restaurante")

#color fondo ventana
aplicacion.config(bg= "green")

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistemas de facturacion', fg='azure4', font = ('Dosis', 45), bg = 'burlywood', width = 29)
etiqueta_titulo.grid (row=0, column=0 )  

#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT, bg='Azure4')
panel_izquierdo.pack(side=LEFT)

#panel costos   
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd= 1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()
  
#panel recibo
panel_recibo = Frame(panel_derecha, bd= 1, relief=FLAT, bg='burlywood')
panel_recibo.pack()
 
#panel botones
panel_botones = Frame(panel_derecha, bd= 1, relief=FLAT, bg='burlywood')
panel_botones.pack()

#Lista productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'browneis', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

#Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []

contador = 0
for comida in  lista_comidas:
    #Crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()

    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_comida[contador], 
                         command=revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky=W)

    #crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6, 
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column = 1)
    contador += 1

#Generar items comida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

contador = 0
for bebida in lista_bebidas:
    #Crear checkbutton

    variables_bebida.append('')
    variables_bebida[contador] = IntVar()

    bebida = Checkbutton(panel_bebidas, 
                         text=bebida.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0, 
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador, 
                column=0, 
                sticky=W)
    
    #crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6, 
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column = 1)
    
    contador += 1

#Generar items comida
variables_postre = []
cuadros_postre = []
texto_postre = []

contador = 0
for postre in lista_postres:

    #Crear checkbutton

    variables_postre.append('')
    variables_postre[contador] = IntVar()

    postre = Checkbutton(panel_postres, 
                         text=postre.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador, 
                column=0,
                sticky=W)
    
    #crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, 
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6, 
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column = 1)
    contador += 1

#Varaibles
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#Etiquetas costos y campos de entrada

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo  comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0,
                           column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable = var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=40)


etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,
                           column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable = var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=40)


etiqueta_costo_postre = Label(panel_costos,
                              text='Costo postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2,
                           column=0)
texto_costo_postre = Entry(panel_costos,
                           font=('Dosis',12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=40)


etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0,
                           column=2)
texto_subtotal = Entry(panel_costos,
                           font=('Dosis',12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=40)


etiqueta_impuesto = Label(panel_costos,
                              text='Impuesto',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1,
                           column=2)
texto_impuesto = Entry(panel_costos,    
                           font=('Dosis',12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=40)


etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos,    
                           font=('Dosis',12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=40)


#Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados =[ ]
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 12, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    
    boton.grid(row=0, column=columnas)
    columnas += 1      

botones_creados[0].config(command=TOTAL)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)
#area de recibo

texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=40,
                    height=10)
texto_recibo.grid(row=0, column=0)

#calculadora
visor_calculadora =Entry(panel_calculadora,
                         font=('Dosis', 12, 'bold'),
                         width=40,
                         bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+',
                       '4', '5', '6', '-',
                       '1', '2', '3', 'x',
                       'R', 'B', '0', '/']
botones_guardados = []
fila = 1
columnas = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                    text=boton.title(),
                    font=('Dosis', 15, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=7)
    boton.grid(row=fila,
               column=columnas)
    
    botones_guardados.append(boton)
    
    if columnas == 3:
        fila += 1
    
    columnas += 1
    
    if columnas == 4:
        columnas = 0

botones_guardados[0].config(command= lambda : click_boton('7'))
botones_guardados[1].config(command= lambda : click_boton('8'))
botones_guardados[2].config(command= lambda : click_boton('9'))
botones_guardados[3].config(command= lambda : click_boton('+'))
botones_guardados[4].config(command= lambda : click_boton('4'))
botones_guardados[5].config(command= lambda : click_boton('5')) 
botones_guardados[6].config(command= lambda : click_boton('6'))
botones_guardados[7].config(command= lambda : click_boton('-'))
botones_guardados[8].config(command= lambda : click_boton('1'))
botones_guardados[9].config(command= lambda : click_boton('2'))
botones_guardados[10].config(command= lambda : click_boton('3'))
botones_guardados[11].config(command= lambda : click_boton('*'))
botones_guardados[12].config(command= obtener_resultado)
botones_guardados[13].config(command= borrar)
botones_guardados[14].config(command= lambda : click_boton('0'))
botones_guardados[15].config(command= lambda : click_boton('/'))


# Evitar que la pantalla se cierre
aplicacion.mainloop()
