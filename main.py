from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os
from api.user import user_router

from typing import Union

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el valor de una variable de entorno.
port_server = int(os.getenv("PORT"))
print(f"{port_server}")




app = FastAPI()

# app.include_router(api.router, prefix="/api")
app.include_router(user_router.user, prefix="/api")

# corre uvicor con mi port
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port_server, reload=True)

# print(type(4))
# print(type(4.5))
# print(type("hola"))
# print(type(False))
# print(type([]))
# print(type({}))
# print(type(()))

