from settings.config import Config
from fastapi import HTTPException
import requests

class APIFlask:
    def __init__(self):
        self.cliente = Config.URL_CLIENTE
        self.produto = Config.URL_PRODUTO
        self.venda = Config.URL_VENDA
        
    # será enviado o json  para a url de acordo com o tipo de dados (cliente, produto  ou venda)
    
    def send_data(self, data, type_data): 
        
        if type_data == "cliente":            
            url = self.cliente
            
        elif type_data == "produto":            
            url = self.produto
            
        elif type_data == "venda":
            url = self.venda
        else:
            raise HTTPException(status_code=400, detail="Tipo não autorizado")
        
        try:
            

            response = requests.post(url, json=data)

            response.raise_for_status()
            
        except requests.exceptions.HTTPError as e :
            raise HTTPException(status_code=response.status_code, detail=str(e))