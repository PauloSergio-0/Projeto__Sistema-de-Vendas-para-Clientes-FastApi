from settings.config import Config

class APIFlask:
    def __init__(self):
        self.cliente = Config.URL_CLIENTE
        self.