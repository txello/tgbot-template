class register:
    data = []
    data_webhook = []
    def __apps(x):
        register.data.append(x.__name__)
        return x
    
    def __webhooks(url, method):
        def decorator(function):
            register.data_webhook.append([function.__name__, method, url])
            return function
        return decorator
           
    apps = lambda x: register.__apps(x)
    webhooks = lambda url, method: register.__webhooks(url, method)