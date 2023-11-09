from typing import List,Any
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from typing import Generator
from mysql.connector.types import RowType
from mysql.connector import MySQLConnection
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.errors import InternalError
class MYSQL:
    def __init__(self,*vars) -> None:
        '''
        Параметры:
        host = 'Адрес подключения'
        user = 'Имя пользователя'
        password = 'Пароль'
        database = 'Имя Базы данных'
        port = 'Порт'(По умолчанию)
        '''
        self.vars = list(vars)
        self.__connect:MySQLConnection|PooledMySQLConnection|Any
        self.__cursor:MySQLCursor|Any
        self.__commit:bool = False
        
    def connect(self) -> MySQLConnection|PooledMySQLConnection|Any:
        connect = mysql.connector.connect(
            host=self.vars[0],
            user=self.vars[1],
            password=self.vars[2],
            database=self.vars[3],
            port=self.vars[4] if len(self.vars) == 5 else '3306'
        )
        self.__connect = connect
        return self.__connect
    
    def cursor(self,commit=False) -> MySQLCursor|Any:
        self.__cursor = self.__connect.cursor()
        if commit: self.__commit = commit
        return self.__cursor
    
    def query(self,query:str,params:tuple=None) -> Generator[MySQLCursor,None,None]|None:
        if params == None: self.__cursor.execute(query)
        else: self.__cursor.execute(query,params)
        try:
            if self.__commit: self.__connect.commit()
        except InternalError: pass
    
    def fetchall(self) -> List[RowType]:
        return self.__cursor.fetchall()
    
    def fetchmany(self,size:int = None) -> List[RowType]:
        return self.__cursor.fetchmany()
    
    def fetchone(self) -> RowType|None:
        return self.__cursor.fetchone()
    
    def close(self) -> None:
        return self.__connect.close()