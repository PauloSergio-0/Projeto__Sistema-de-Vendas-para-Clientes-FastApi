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
                    clientes.append(cliente)

                return clientes

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

    async def importar_produtos(self, file: UploadFile):
        if file.filename.endswith('.csv'):
            try:

                data = await file.read()
                decoded_data = data.decode('utf-8').splitlines()

                csv_reader = csv.DictReader(decoded_data)

                colunasEsperadas = {"ID", "Nome", "Código", "Categoria", "Preço"}
                if not colunasEsperadas.issubset(csv_reader.fieldnames):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Formato incorreto. Para fazer o upload de produtos, "
                               "o CSV deve conter informações do ID, nome, código, categoria e preço."
                    )

                produtos = []

                for linha in csv_reader:
                    produto = {
                        "id": linha["ID"],
                        "nome": linha["Nome"],
                        "codigo": linha["Código"],
                        "categoria": linha["Categoria"],
                        "preco": linha["Preço"]
                    }
                    produtos.append(produto)

                return produtos

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

    async def importar_vendas(self, file: UploadFile):
        if file.filename.endswith('.csv'):
            try:

                data = await file.read()
                decoded_data = data.decode('utf-8').splitlines()

                csv_reader = csv.DictReader(decoded_data)

                colunasEsperadas = {"ID do Cliente", "ID do Produto", "Quantidade", "Data da Venda"}
                if not colunasEsperadas.issubset(csv_reader.fieldnames):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Formato incorreto. Para fazer o upload de produtos, "
                               "o CSV deve conter informações do ID do cliente e produto, quantidade data da venda."
                    )

                vendas = []

                for linha in csv_reader:
                    venda = {
                        "id_do_cliente": linha["ID do Cliente"],
                        "id_do_produto": linha["ID do Produto"],
                        "quantidade": linha["Quantidade"],
                        "data_da_venda": linha["Data da Venda"]
                    }
                    vendas.append(venda)

                return vendas

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