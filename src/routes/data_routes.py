from fastapi import FastAPI, UploadFile, APIRouter, File

router = APIRouter()

@router.get("/ola")
async def ola():
    return {"menssagem": "olá".encode("utf-8")}
