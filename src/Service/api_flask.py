from settings.config import Config
import requests
class APIFlask:
    def __init__(self):
        self.cliente = Config.URL_CLIENTE
        self.produto = Config.URL_PRODUTO
        self.venda = Config.URL_VENDA
        
        
    def send_data(self, data, type_data):
        if type_data == "cliente":
            url = self.cliente
        elif type_data == "produto":
            url = self.produto
        elif type_data == "venda":
            url = self.venda
        else:
            raise {'Error': "tipo não autorizado"}
        try:
            response = requests.post(url, json= data)
        
            response.raise_for_status()
        except Exception as e :
            raise {"error": f"{(str(e))}"}