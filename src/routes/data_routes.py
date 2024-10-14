from fastapi import UploadFile, APIRouter, File

from src.domain.data_processor import DataProcessor

router = APIRouter()

data_processor = DataProcessor()

@router.post("/importar-clientes/")
async def importar_clientes(file : UploadFile = File(...)):
    return await data_processor.upload_clientes(file)
