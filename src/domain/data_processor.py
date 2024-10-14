import csv
import os

from fastapi import UploadFile, HTTPException, status


class DataProcessor:
    def __init__(self):
        pass

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