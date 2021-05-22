# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 17:31:05 2020

@author: eduardo.vitcop

Modulo que contiene la clase configuracion_expensas
"""
import json
class ConfiguracionExpensas:
    """Clase que toma los disitntos valores para de la aplicacion desde el archivo expensas_config.json"""

    def __init__(self):
        """Inicializa la clase tomando los valores desde el archivo expensas_config.json"""
        try:
            with open('expensas_config.json', 'r') as file:
                config = json.load(file)
        except Exception as err:
            print("Ocurrió un error al abrir archvivo de configuración: ", err)
        self.db_server = config.get('DB_SERVER', '')
        self.db_name = config.get('DB_NAME', ' ')
        self.user = config.get('DB_USER', '')
        self.password = config.get("DB_PASSWORD", '')
