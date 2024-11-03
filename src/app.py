from fastapi import FastAPI

from routes import init_routes

import uvicorn

app = FastAPI()

init_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port =  8000)
