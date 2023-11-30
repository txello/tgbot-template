class register:
    data = []
    def __apps(x):
        register.data.append(x.__name__)
        return x
    apps = lambda x: register.__apps(x)