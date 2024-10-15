import csv
import os

from fastapi import UploadFile, HTTPException, status
from data.data_memo import Data_Memory

class DataProcessor:
    def __init__(self):
        self.data_save = Data_Memory

    async def upload_clientes(self, file: UploadFile):

        if file.filename.endswith('.csv'):
            try:

                data = await file.read()
                decoded_data = data.decode('utf-8').splitlines()

                csv_reader = csv.DictReader(decoded_data)

                clientes = []

                for linha in csv_reader:
                    cliente = {
                        "ID": linha["ID"],
                        "Nome": linha["Nome"],
                        "Endereco": linha["Endereço"],
                        "Contato": linha["Contato"]
                    }
                    clientes.append(cliente)
                    
                self.data_save.clientes = clientes
                
                return {"clientes": "Adicianados com sucesso"}

            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Falha ao processar o arquivo CSV: {str(e)}"
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Apenas arquivos CSV são aceitos"
            )


    async def exportar_cliente(self):
        if self.data_save.clientes:
            try:
            
                return {self.data_save.clientes}
            
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Falha ao enviar o arquivo CSV: {str(e)}"
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Apenas arquivos CSV são aceitos"
            )
            
    