# -*- coding: utf-8 -*-

# DRIVER PARA EL MANEJO DE LA INFORMACION DE BASE DE DATOS POSTGIS
# DESARROLLADO POR : FRANCISCO CONTRERAS

import psycopg2
import psycopg2.errors
import psycopg2.extras

from qgis.core import *
from qgis.utils import iface

import os
import json


class DataBaseDriver():

    
    """Database driver class. Config enviroment variables:
    --- DBCATASTRO_DBNAME
    --- DBCATASTRO_HOST
    --- DBCATASTRO_USER
    --- DBCATASTRO_PASSWORD
    --- DBCATASTRO_PORT

    

    """
    AS_DICT = psycopg2.extras.RealDictCursor
    def __init__(self) -> None:
        #! CONFIGURAR LAS VARIABLES DE ENTORNO DENTRO DE LA PC DEL CLIENTE
        os.environ['DBCATASTRO_DBNAME'] = 'bdcatastro'
        os.environ['DBCATASTRO_HOST'] = 'localhost'
        os.environ['DBCATASTRO_USER'] = 'postgres'
        os.environ['DBCATASTRO_PASSWORD'] = '23826405'
        os.environ['DBCATASTRO_PORT'] = '5432'

        self.params = {
            'dbname': os.getenv('DBCATASTRO_DBNAME'),
            'host' : os.getenv('DBCATASTRO_HOST'),
            'user' : os.getenv('DBCATASTRO_USER'),
            'password': os.getenv('DBCATASTRO_PASSWORD'),
            'port': os.getenv('DBCATASTRO_PORT')
        }   

        # print(self.params)

        pass

    def dbParams(self): 
        return self.params

    def connection(self):
        """DataBaseDriver connection function

        Returns:
            connection: data base connection handle
        """        
        # conn = psycopg2.connect('dbname={} user={} host={} password={}'.format(self.params['dbname'], self.params['user'],self.params['host'],self.params['password']))
        conn = psycopg2.connect(
                dbname=self.params['dbname'],
                user=self.params['user'],
                password=self.params['password'],
                host=self.params['host'],
                port=self.params['port']
                )
        return conn
    def testConnection(self): 
        """DataBaseDriver testConnection function, if connection: print database version
        """
     
        conn = self.connection() 
        cur = conn.cursor()
        cur.execute('select version()')
        print(cur.fetchone())
        
        pass


    def create(self,sql):
        """Function for Input queries

        Args:
             sql (str): SQL query for read information of Database
        """

        with self.connection() as conn: 
            try:
                cur = conn.cursor()
                cur.execute(sql) 
                conn.commit()
                self.showMessage("Información Guardada en la Base de Datos Correctamente",3,3)


            
            except Exception as ex:
                self.showMessage("Algo ha ocurrido, revisar Consola Python!",2,3)
                print(ex)
                conn.rollback()




        pass
    
    def read(self,sql,multi=True,as_dict=True):
        """ Function for Read-only queries

        Args:
            sql (str): SQL query for read information of Database
            multi (bool, optional): Parameter to Fetch multi rows of Single row. Defaults to True.

        Returns:
            json: results in json format
        """        
        
        with self.connection() as conn: 
            try: 
                if as_dict:
                    cur = conn.cursor(cursor_factory = self.AS_DICT) 
                else:
                    cur = conn.cursor() 
                    
                cur.execute(sql)
                if multi:
                    r = cur.fetchall()
                else: 
                    r = cur.fetchone()
                
                # return json.dumps(r).encode('latin1')
                return r
            except Exception as ex: 
                print(ex) 
        pass
    def update(self,sql):
        """Function for Update queries

        Args:
            sql (str): SQL query for read information of Database
        """
        with self.connection() as conn: 
            try: 
                cur = conn.cursor() 
                cur.execute(sql) 
                conn.commit() 
                self.showMessage("Información Actualizada en la Base de Datos Correctamente",3,15)
            except Exception as ex:
                self.showMessage("Algo ha ocurrido, revisar Consola Python!",2,3)
                print(ex)
        pass


    def delete(self,sql,msg=True): 
        """Function for Delete queries

        Args:
            sql (str): SQL query for read information of Database
        """ 
        with self.connection() as conn: 
            try: 
                cur = conn.cursor() 
                cur.execute(sql) 
                print(sql)
                conn.commit()
                if msg:
                    self.showMessage("Información Actualizada en la Base de Datos Correctamente",3,15)
            except Exception as ex:
                self.showMessage("Algo ha ocurrido, revisar Consola Python!",2,3)
                print(ex)      
        

    def showMessage(self,text:str,level:int=0,duration:int=3):
        """
        Args:
            text (str)
            level (int, optional): LOGGIN LEVEL :
    
            0-Info

            1-Warning

            2-Critical

            3-Success

            duration (int, optional): Defaults to 3.
        """        
        iface.messageBar().pushMessage(text, level=level, duration=duration)
        QgsMessageLog.logMessage(text, level=level)

    