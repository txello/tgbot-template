import dotenv
import os

class ENV:
    dotenv_path = os.path.join(os.path.dirname('.'), '.env')
    def read(key:str) -> str|None:
        return dotenv.get_key(ENV.dotenv_path,key)
    def set_key(key:str,value:str)->bool|any:
        return dotenv.set_key(ENV.dotenv_path,key,value)
    def unset_key(key:str) -> bool|any:
        return dotenv.unset_key(ENV.dotenv_path,key)
    def values() -> dict:
        return dict(dotenv.dotenv_values(ENV.dotenv_path))