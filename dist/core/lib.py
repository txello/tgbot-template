from aiohttp import web

class register:
    data = []
    data_webhook = []
    
    @staticmethod
    def __apps(x):
        register.data.append(x)
        return x
    
    @staticmethod
    def __webhooks(url, method, data_model=None):
        def decorator(function):
            register.data_webhook.append([function, method, url, data_model])
            return function
        return decorator
    
    
           
    apps = lambda x: register.__apps(x)
    webhooks = lambda url, method, data_model=None: register.__webhooks(url, method, data_model)