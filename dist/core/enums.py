from enum import Enum

class WebMethod(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
    HEAD = 'head'
    OPTIONS = 'options'
