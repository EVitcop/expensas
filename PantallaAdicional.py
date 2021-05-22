# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:09:38 2020

@author: eduardo.vitcop
"""
import tkinter as tk
from base_de_datos import conectar_BD
from base_de_datos import obtener_mov_mes
from base_de_datos import obtener_saldo_mes
from configuracion_expensas import ConfiguracionExpensas

def mostrar_movimientos(table,anio,mes):   
        ##table = tk.Frame(marco)
       ## table.pack(side="top", fill="both", expand=True)
        print(mes)
        print(anio)
        Datos_configuracion = ConfiguracionExpensas()
        conexion = conectar_BD(Datos_configuracion.db_server,
                               Datos_configuracion.db_name,
                               Datos_configuracion.user,
                               Datos_configuracion.password)
        if not conexion:
            table.destroy()
            sys.exit()    
        if mes == 1 :
            mes_ant = 12
            anio_ant = anio - 1
        else:
            mes_ant = mes - 1
            anio_ant = anio     
        saldoAnterior = obtener_saldo_mes(conexion, str(anio_ant) , str(mes_ant))
        print(saldoAnterior)
        # obtener set de datos de la consulta y dejarlo en una tupla
        data = obtener_mov_mes(conexion, str(anio), str(mes))
        conexion.close()
        table.widgets = {}
        # Inicializa acumuladores
        row = 0
        totalDebe = 0
        totalHaber = 0
        # Titulos Grilla
        lbl_fecha = tk.Label(table, text="Fecha")
        lbl_fecha.grid(column=1, row=0, sticky="", padx=5, pady=5)
        lbl_concepto = tk.Label(table, text="Concepto")
        lbl_concepto.grid(column=2, row=0, sticky="", padx=5, pady=5)
        lbl_debe = tk.Label(table, text="Debe")
        lbl_debe.grid(column=3, row=0, sticky="", padx=5, pady=5)
        lbl_haber = tk.Label(table, text="Haber")
        lbl_haber.grid(column=4, row=0, sticky="", padx=5, pady=5)
        lbl_cpte = tk.Label(table, text="Cpte.")
        lbl_cpte.grid(column=5, row=0, sticky="", padx=5, pady=5)
        lbl_UF = tk.Label(table, text="UF")
        lbl_UF.grid(column=6, row=0, sticky="", padx=5, pady=5)
        lbl_comentario = tk.Label(table, text="Comentario")
        lbl_comentario.grid(column=7, row=0, sticky="", padx=5, pady=5)
        # Saldo Anterior
        row += 1
        lbl_saldoAnterior = tk.Label(table, text="saldoAnterior") 
        lbl_saldoAnterior.grid(column=2, row=row, sticky="E", padx=5, pady=5)
        if saldoAnterior >= 0 :
             impHaber = saldoAnterior
             impDebe = ''
             totalHaber += saldoAnterior
        else:
            impDebe = saldoAnterior
            impHaber = ''
            totalDebe += saldoAnterior 
        lbl_debe = tk.Label(table, text=impDebe)
        lbl_debe.grid(column=3, row=row, sticky="W")
        lbl_haber = tk.Label(table, text=impHaber)
        lbl_haber.grid(column=4, row=row, sticky="W")   
        # populacion tabla con los movimientos del mes
        for ID, fechMov, Concepto, tipoMov, NroCpte, DH, importe, anio, mes, Dto, Comentario in (data):
            row += 1
            fecha = fechMov.strftime('%d/%m/%Y')
            if DH == 'D':
                impHaber = ''
                impDebe = importe
                totalDebe += importe
            elif DH == 'H':
                impHaber = importe
                impDebe = ''
                totalHaber += importe
            table.widgets[ID] = {
                "ID": tk.Label(table, text=ID),
                "fechMov": tk.Label(table, text=fecha),
                "Concepto": tk.Label(table, text=Concepto),
                "Debe": tk.Label(table, text=impDebe),
                "Haber": tk.Label(table, text=impHaber),
                "NroCpte": tk.Label(table, text=NroCpte),
                "Dto": tk.Label(table, text=Dto),
                "Comentario": tk.Label(table, text=Comentario),
                #"start_time": tk.Label(table, text=start_time),
                #"end_time": tk.Label(table, text=start_time)
            }

          ##  self.widgets[ID]["ID"].grid(row=row, column=0, sticky="nsew")
            table.widgets[ID]["fechMov"].grid(row=row, column=1, sticky="nsew")
            table.widgets[ID]["Concepto"].grid(row=row, column=2, sticky="nsew")
            table.widgets[ID]["Debe"].grid(row=row, column=3, sticky="nsew")
            table.widgets[ID]["Haber"].grid(row=row, column=4, sticky="nsew")
            table.widgets[ID]["NroCpte"].grid(row=row, column=5, sticky="nsew")
            table.widgets[ID]["Dto"].grid(row=row, column=6, sticky="nsew")
            table.widgets[ID]["Comentario"].grid(row=row, column=7, sticky="nsew")
            #self.widgets[rowid]["start_time"].grid(row=row, column=5, sticky="nsew")
            #self.widgets[rowid]["end_time"].grid(row=row, column=6, sticky="nsew")
        
        # ultima linea
        row += 1
        lbl_total = tk.Label(table, text="Total.")
        lbl_total.grid(column=2, row=row, sticky="E", padx=5, pady=5)
        lbl_totalDebe = tk.Label(table, text=totalDebe)
        lbl_totalDebe.grid(column=3, row=row, sticky="W")
        lbl_totalHaber = tk.Label(table, text=totalHaber)
        lbl_totalHaber.grid(column=4, row=row, sticky="W")
        lbl_totalSaldo = tk.Label(table, text=(totalHaber - totalDebe))
        lbl_totalSaldo.grid(column=7, row=row, sticky="W")

        
        table.grid_columnconfigure(1, weight=1)
        table.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        table.grid_rowconfigure(row+1, weight=1)

def mostrar_cabecera(marco, marco_cuerpo):
        anio = 2021
        mes = 2
        lbl_mes = tk.Label(marco, text="Mes:")
        lbl_mes.grid(column=1, row=0, sticky="", padx=5, pady=5)
        txt_mes = tk.Entry(marco, width=2, textvariable=mes)
        txt_mes.grid(column=2, row=0, sticky="W")
        lbl_anio = tk.Label(marco, text="Año:")
        lbl_anio.grid(column=3, row=0, sticky="", padx=5, pady=5)
        txt_anio = tk.Entry(marco, width=4, textvariable=anio)
        txt_anio.grid(column=4, row=0, sticky="W")
        btn_enviar = tk.Button(marco, text="Ejecutar", command=mostrar_movimientos(marco_cuerpo,anio,mes))
        btn_enviar.grid(column=5, row=0)

if __name__ == "__main__":
    root =tk.Tk() # create root window
    root.title("Basic GUI Layout with Grid")
    root.maxsize(900, 600) # width x height
    root.config(bg="skyblue")
    marco_cabecera = tk.Frame(root, width=1200, height= 400, bg='grey')
    marco_cabecera.grid(row=0, column=0, padx=10, pady=5)
    marco_cuerpo = tk.Frame(root, width=1200, height= 400, bg='grey')
    marco_cuerpo.grid(row=1, column=0, padx=10, pady=5)
    mostrar_cabecera(marco_cabecera,marco_cuerpo)
    anio = 2021
    mes = 2
    lbl_mes = tk.Label(marco_cabecera, text="Mes:")
    lbl_mes.grid(column=1, row=0, sticky="", padx=5, pady=5)
    txt_mes = tk.Entry(marco_cabecera, width=2, textvariable=mes)
    txt_mes.grid(column=2, row=0, sticky="W")
    lbl_anio = tk.Label(marco_cabecera, text="Año:")
    lbl_anio.grid(column=3, row=0, sticky="", padx=5, pady=5)
    txt_anio = tk.Entry(marco_cabecera, width=4, textvariable=anio)
    txt_anio.grid(column=4, row=0, sticky="W")
    btn_enviar = tk.Button(marco_cabecera, text="Ejecutar", command=mostrar_movimientos(marco_cuerpo,anio,mes))
    btn_enviar.grid(column=5, row=0)
    root.mainloop()