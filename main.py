from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os
from api.user import user_router

from typing import Union

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el valor de una variable de entorno.
port_server = os.getenv("PORT")
print(f"{port_server}")

app = FastAPI()

# app.include_router(api.router, prefix="/api")
app.include_router(user_router.user, prefix="/api")


# corre uvicor con mi port
if __name__ == "__main__":
    uvicorn.run("main:app", port=port_server, reload=True)

print(type(4))
print(type(4.5))
print(type("hola"))
print(type(False))
print(type([]))
print(type({}))
print(type(()))


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# from smartcard.System import readers
# from smartcard.util import toHexString
# from smartcard.CardConnection import CardConnection
# from smartcard.Exceptions import CardConnectionException

# # Obtener la lista de lectores
# r = readers()
# if not r:
#     print("No se encontraron lectores de tarjetas inteligentes")
#     exit()

# # Seleccionar el primer lector
# reader = r[0]

# try:
#     # Conectar al lector
#     connection = reader.createConnection()
#     connection.connect()

#     # Comando APDU para leer el número de DNI
#     apdu_command = [0xa0, 0x00, 0x00, 0x00, 0x62, 0x03, 0x01, 0xc, 0x01, 0x01]
#     # apdu_command = [0x00, 0xA4, 0x04, 0x00, 0x08, 0xA0, 0x00, 0x00, 0x00, 0x54, 0x48, 0x01, 0x00]

#     # Enviar el comando APDU
#     data, sw1, sw2 = connection.transmit(apdu_command)
#     print(data)
#     print(sw1)
#     print(0x11)
#     print(0xFF)
#     print(0xFF)

#     # Verificar la respuesta
#     if sw1 == 0x11 and sw2 == 0x00:
#         # Extraer el número de DNI de los datos recibidos
#         dni_number = toHexString(data)[-8:].decode('utf-8')
#         print("Número de DNI:", dni_number)
#     else:
#         print("Error al leer el número de DNI:", sw1, sw2)


# except CardConnectionException as e:
#     print("Error de conexión:", e)

# finally:
#     # Desconectar del lector
#     connection.disconnect()
