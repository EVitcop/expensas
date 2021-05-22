# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:50:35 2019
Crea un movimiento de expensas 
@author: eduardo.vitcop
"""
from datetime import datetime
from tkinter  import *
from tkinter  import messagebox as Messagebox
import sys
from base_de_datos import conectar_BD
from configuracion_expensas import ConfiguracionExpensas
from movimiento import Movimiento
from validaciones_fecha import fecha_valida
from validaciones_fecha import mes_valido


"""
def fecha_valida(nuevo_valor):

    
    Devueve TRUE si el dato es una fecha valida 
    
    >>> fecha_valida("25/11/2019")
    True
    
    >>> fecha_valida("")
    False
    
   
    try:
        datetime.strptime(nuevo_valor, '%d/%m/%Y')
        return True
    except:
        return False
"""
    
def reingresar_fecha(nuevo_valor):
    """ Muestra el mensaje de fecha incorrecta """
    Messagebox.showinfo(message="{} valor de fecha incorrecto ".
                        format(nuevo_valor), title="Fecha incorrecta")

def reingresar_mes_imputacion(nuevo_valor):
    """ Muestra el mensaje de mes incorrecto """
    Messagebox.showinfo(message="{} valor de mes_imputacion ".
                        format(nuevo_valor), title="Mes Imputación incorrecto")

def reingresar_anio_imputacion(nuevo_valor):
    """ Muestra el mensaje de año incorrecto """
    Messagebox.showinfo(message="{} valor de anio_imputacion ".
                        format(nuevo_valor), title="Año Imputación incorrecto")
"""
def mes_valido(mes):

     Valida numero de mes entero entre 1 y 12 
    if not mes:
        return False
    if mes.isdigit():
        return 0 < int(mes) < 13
    return False
"""
def anio_valido(anio):
    """ Valida año no mayor al actual """
    if not anio:
        return False
    if anio.isdigit():
        if int(anio) <= datetime.now().year:
            return True
    return False

def importe_valido(importe):
    """ Valida que el valor sea un importe """
    if not importe:
        return False
    try:
        float(importe)
    except ValueError:
        return False
    return True

def unidad_funcional_valida(p_unidad_funcional):
    """ Valida unidad funcional entre 1 y 4 """
    if not p_unidad_funcional:
        return True
    try:
        return 0 < int(p_unidad_funcional) < 5
    except ValueError:
        return False
    return True

def oprimir_enviar():
    """ Boton Enviar  """
    mensajes = ""

    if not fecha_valida(fecha.get()):
        mensajes = ("Valor de fecha inexistente o invalido:{}"
                    .format(fecha.get()))
    if not importe_valido(str_importe.get()):
        mensajes += ("\nValor de Importe inexistente o invalido:{}"
                     .format(str_importe.get()))
    if not str_concepto.get():
        mensajes += ("\nValor de concepto inexistente o invalido:{}"
                     .format(str_concepto.get()))
    if not anio_valido(anio_imputacion.get()):
        mensajes += ("\nValor de Año de imputación inexistente o invalido:{}"
                     .format(anio_imputacion.get()))
    if not mes_valido(mes_imputacion.get()):
        mensajes += ("\nValor de Año de imputación inexistente o invalido:{}"
                     .format(mes_imputacion.get()))
    if not unidad_funcional_valida(unidad_funcional.get()):
        mensajes += ("\nValor de dto inexistente o invalido:{}"
                     .format(unidad_funcional.get()))
    str_mensajes.set(mensajes)
    str_barra_estado.set("")
    if not mensajes:
        texto = txt_comentarios.get(1.0, "end-1c")
        mov = Movimiento(datetime.strptime(fecha.get(), '%d/%m/%Y'),
                         str_concepto.get()[0:100], str_nro_cpte.get(),
                         int_tipo_mov.get(), str_importe.get(),
                         anio_imputacion.get(), mes_imputacion.get(),
                         unidad_funcional.get(), texto[0:1023])
        conexion = conectar_BD(Datos_configuracion.db_server,
                               Datos_configuracion.db_name,
                               Datos_configuracion.user,
                               Datos_configuracion.password)
        mov.Grabar_en_bd(conexion)
        conexion.close()
        str_barra_estado.set("Ultimo movimiento registrado: " +
                             str_concepto.get().strip() + " importe: " +
                             str_importe.get().strip() +  " fecha: " +
                             fecha.get().strip())

# verificacion conexion la base
ventana = Tk()
Datos_configuracion = ConfiguracionExpensas()
conexion = conectar_BD(Datos_configuracion.db_server,
                       Datos_configuracion.db_name,
                       Datos_configuracion.user,
                       Datos_configuracion.password)
if not conexion:
    ventana.destroy()
    sys.exit()

conexion.close()


ventana.title("Carga de Expensas" + " - BD:" + Datos_configuracion.db_name)
ventana.resizable(1, 1)

marco = Frame(ventana)
marco.config(width=500, height=320)
marco.pack(fill="both", expand=1)

lbl_fecha = Label(marco, text="Fecha Comprobante:")
lbl_fecha.grid(column=0, row=0, sticky="E", padx=5, pady=5)
fecha = StringVar()
vcmd_fecha = (marco.register(fecha_valida), '%P')
icmd_fecha = (marco.register(reingresar_fecha), '%P')
txt_fecha = Entry(marco, width=10, textvariable=fecha, validate="focusout",
                  validatecommand=vcmd_fecha, invalidcommand=icmd_fecha)
txt_fecha.grid(column=1, row=0, sticky="W")

lbl_concepto = Label(marco, text="Concepto:")
lbl_concepto.grid(column=0, row=1, sticky="E", padx=5, pady=5)
str_concepto = StringVar()
txt_concepto = Entry(marco, width=40, textvariable=str_concepto)
txt_concepto.grid(column=1, row=1, sticky="W")


lbl_tipo = Label(marco, text="Tipo:")
lbl_tipo.grid(column=0, row=3, sticky="E", padx=5, pady=5)
int_tipo_mov = IntVar()
rad_tipo_1 = Radiobutton(marco, text='Debe', value=5, variable=int_tipo_mov)
rad_tipo_2 = Radiobutton(marco, text='Haber', value=6, variable=int_tipo_mov)
rad_tipo_1.grid(column=1, row=3, sticky="W")
rad_tipo_2.grid(column=2, row=3, sticky="W")
rad_tipo_1.invoke()

str_nro_cpte = StringVar()
lbl_nro_cpte = Label(marco, text="Nro Cpte:")
lbl_nro_cpte.grid(column=0, row=4, sticky="E", padx=5, pady=5)
txt_nro_cpte = Entry(marco, width=10, textvariable=str_nro_cpte)
txt_nro_cpte.grid(column=1, row=4, sticky="W")

str_importe = StringVar()
lbl_importe = Label(marco, text="Importe:")
lbl_importe.grid(column=0, row=5, sticky="E", padx=5, pady=5)
txt_importe = Entry(marco, width=15, textvariable=str_importe)
txt_importe.grid(column=1, row=5, sticky="W")

anio_imputacion = StringVar()
lbl_anio_imputacion = Label(marco, text="Año Imputación:")
lbl_anio_imputacion.grid(column=0, row=6, sticky="E", padx=5, pady=5)
txt_anio_imputacion = Entry(marco, width=4, textvariable=anio_imputacion)
txt_anio_imputacion.grid(column=1, row=6, sticky="W")

mes_imputacion = StringVar()
lbl_mes_imputacion = Label(marco, text="Mes Imputación:")
lbl_mes_imputacion.grid(column=0, row=7, sticky="E", padx=5, pady=5)
txt_mes_imputacion = Entry(marco, width=2, textvariable=mes_imputacion)
txt_mes_imputacion.grid(column=1, row=7, sticky="W")

unidad_funcional = StringVar()
lbl_unidad_funcional = Label(marco, text="Departamento:")
lbl_unidad_funcional.grid(column=0, row=8, sticky="E", padx=5, pady=5)
txt_unidad_funcional = Entry(marco, width=10, textvariable=unidad_funcional)
txt_unidad_funcional.grid(column=1, row=8, sticky="W")

comentarios = StringVar()
scrollbar = Scrollbar(marco)

lbl_comentarios = Label(marco, text="Comentarios:")
lbl_comentarios.grid(column=0, row=9, sticky="E", padx=5, pady=5)
txt_comentarios = Text(marco, width=40, height=4, yscrollcommand=scrollbar.set)
txt_comentarios.grid(column=1, row=9, sticky="W")
txt_comentarios.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt_comentarios.yview)


btn_enviar = Button(marco, text="Enviar", command=oprimir_enviar)
btn_enviar.grid(column=1, row=10)

str_mensajes = StringVar()
lbl_mensajes = Label(marco, justify=LEFT)
lbl_mensajes.grid(column=1, row=11, sticky="W")
lbl_mensajes.config(textvariable=str_mensajes, fg="red")

str_barra_estado = StringVar()
lbl_barra_estado = Label(marco, justify=LEFT)
lbl_barra_estado.grid(column=1, row=12, sticky="W")
lbl_barra_estado.config(textvariable=str_barra_estado, fg="grey")


ventana.mainloop()
