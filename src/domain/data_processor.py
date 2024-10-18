import csv
import os

from fastapi import UploadFile, HTTPException, status
from service.api_flask import APIFlask

class DataProcessor:
    def __init__(self):
        pass

    async def upload_clientes(self, file: UploadFile):

        if file.filename.endswith('.csv'):
            try:

                data = await file.read()
                decoded_data = data.decode('utf-8').splitlines()

                csv_reader = csv.DictReader(decoded_data)

                colunasEsperadas = {"ID", "Nome", "Endereço", "Contato"}
                if not colunasEsperadas.issubset(csv_reader.fieldnames):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Formato incorreto. Para fazer o upload de clientes, "
                               "o CSV deve conter informações do ID, nome, endereço e contato."
                    )

                clientes = []

                for linha in csv_reader:
                    cliente = {
                        "id": linha["ID"],
                        "nome": linha["Nome"],
                        "endereco": linha["Endereço"],
                        "contato": linha["Contato"]
                    }
                    APIFlask.send_data(data = cliente, type_data = "Cliente")
                    # clientes.append(cliente)

                return {"clientes": clientes}

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