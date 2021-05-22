# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 00:50:57 2020

@author: eduardo.vitcop
"""
from tkinter  import messagebox as Messagebox

class Movimiento:
    """ clase que representa un movimiento de expensas """

    def __init__(self, fecha, concepto, numero, tipo_mov, importe,
                 anio_imputacion, mes_imputacion, unidad_funcional, comentario):
        self.fecha = fecha
        self.concepto = concepto
        if not numero:
            self.numero = None
        else:
            self.numero = numero
        self.tipo_mov = tipo_mov
        if self.tipo_mov == 6:
            self.debe_haber = "H"
        else:
            self.debe_haber = "D"
        self.importe = importe
        self.anio_imputacion = anio_imputacion
        self.mes_imputacion = mes_imputacion
        if not unidad_funcional:
            self.unidad_funcional = None
        else:
            self.unidad_funcional = int(unidad_funcional)
        if not comentario:
            self.comentario = None
        else:
            self.comentario = comentario

    def __str__(self):
        return ('fecha:\t\t\t{} \n concepto:\t\t{} \n tipo:\t\t\t{} \n numero:\t\t{} \n debe_haber:\t\t{} \n importe:\t\t{} \n anio_imputacion:\t{} \n mes_imputacion:\t{} \n unidad_funcional:\t{} \n comentario:\t\t{} \n'.format(self.fecha,
                self.concepto, self.tipo_mov, self.numero, self.debe_haber,
                self.importe, self.anio_imputacion, self.mes_imputacion,
                self.unidad_funcional, self.comentario))

    def Grabar_en_bd(self, conexion):
        """ inserta los valores del objeto en la base de datos """
        consulta = "INSERT INTO movimiento (FechaMov, Concepto, TipoMovID, NroComprobante, DebeHaber, Importe, AnioImputacion, MesImputacion, UnidadFuncionalID, Comentario) "
        consulta += "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        try:
            with conexion.cursor() as cursor:
                cursor.execute(consulta, self.fecha, self.concepto, self.tipo_mov,
                               self.numero, self.debe_haber, self.importe,
                               self.anio_imputacion, self.mes_imputacion,
                               self.unidad_funcional, self.comentario)
        except Exception as err:
            print("Ocurrió un error al insertar: {}".format(err))
            conexion.close()
            return False
            Messagebox.showinfo(message="Ocurrió un error al conectar a SQL Server: ".format(err),  
                                title="Error de Datos")
        return True
    
   
        
        