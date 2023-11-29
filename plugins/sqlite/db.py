from typing import Any
from sqlite3 import Connection,Cursor

import sqlite3

class SQLITE:
    def __init__(self,file,**args) -> None:
        self.__connect:Connection|Any = dict(**{'database':file},**args)
        self.__cursor:Cursor|Any
        self.__commit:bool
    def connect(self) -> Connection:
        self.__connect = sqlite3.connect(**self.__connect)
        return self.__connect
    def cursor(self,commit=False) -> Cursor:
        self.__cursor = self.__connect.cursor()
        self.__commit = commit
        return self.__cursor
    def close(self) -> None|Any:
        self.__connect = self.__connect.close()
        return self.__connect
    
    def query(self,query,args=None) -> Cursor|Any:
        self.__cursor.execute(query) if args == None else self.__cursor.execute(query,args)
        if self.__commit: self.__connect.commit()
        return self.__cursor
    def commit(self) -> None|Any:
        return self.__connect.commit()