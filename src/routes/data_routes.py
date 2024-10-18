from fastapi import UploadFile, APIRouter, File

from domain.data_processor import DataProcessor

router = APIRouter()

data_processor = DataProcessor()

@router.post("/importar-clientes/")
async def importar_clientes(file : UploadFile = File(...)):
    return await data_processor.upload_clientes(file)

@router.post("/importar-produtos/")
async def importar_produtos(file : UploadFile = File(...)):
    return await data_processor.importar_produtos(file)

@router.post("/importar-vendas/")
async def importar_vendas(file : UploadFile = File(...)):
    return await data_processor.importar_vendas(file)