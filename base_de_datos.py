# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:50:17 2019

@author: eduardo.vitcop
"""

import pyodbc
from tkinter  import messagebox as Messagebox

def conectar_BD(dir_server, nombre_bd, nombre_usuario, password):

    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                  SERVER=' + dir_server +';DATABASE=' + \
                                  nombre_bd+';UID='+ nombre_usuario +';PWD=' \
                                  + password)
        return conexion
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        Messagebox.showinfo(message= "Ocurrió un error al conectar a SQL Server:{} ".format(e),
                            title="Error de Datos")
        return False


def obtener_mov_mes(conexion, anio, mes):
    cursor = conexion.cursor()
    consulta = "SELECT [MovimientoID]\
                   ,[FechaMov]\
                   ,[Concepto]\
                   ,[TipoMovID]\
                   ,[NroComprobante]\
                   ,[DebeHaber]\
                   ,[Importe]\
                   ,[AnioImputacion]\
                   ,[MesImputacion]\
                   ,[UnidadFuncionalID]\
                   ,[Comentario]\
                   FROM [expensas].[dbo].[Movimiento]\
                   Where AnioImputacion = " + \
                   anio + " and MesImputacion = " + mes + \
                   " order by FechaMov"
    cursor.execute(consulta)
    movimientos = cursor.fetchall()
    return movimientos

def obtener_saldo_mes(conexion, anio, mes):
    cursor = conexion.cursor()
    consulta = "SELECT [SaldoTotal] from [expensas].[dbo].[SaldoMensual] " + \
               "where [mes] = " + mes + " and [Anio] = " + anio
    cursor.execute(consulta)
    saldoMes = 0
    data = cursor.fetchone()
    if data :
        saldoMes = data[0]
    return saldoMes
    #for movimiento in movimientos:
    #           print(movimiento)
"""
for row in cursor.columns(table='WORK_ORDER'):
    print row.column_name
    for field in row:
        print field
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT top 10 * from Movimiento ;")

            # Con fetchall traemos todas las filas
            movimientos = cursor.fetchall()

            # Recorrer e imprimir
            for movimiento in movimientos:
                print(movimiento)
    except Exception as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conexion.close()
"""

"""
    direccion_servidor = 'CARO_NB\MSSQLSERVER'
    nombre_bd = 'expensas'
    nombre_usuario = "sa"
    password = 'Carola24'
#conexion = conectar_BD('AR-NB-233\\SQLSERVEREV', 'expensas_copis', "sa" ,  'Carola24' )
#conexion.close()
"""