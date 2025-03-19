import subprocess
import re
from fastapi import APIRouter


user = APIRouter()

produto = [
    {
        "producto": "laptop dell",
        "description": "laptop ultra slim 2023",
        "precio": 4560,
        "stock": 900,
    }
]


# ? CREATE ONE REGISTRO
# ? ****************************************************************************************/
@user.post("/user")
def create_User():
    return {"msj": "successfully", "pro": produto}


# ? CREATE ONE REGISTRO
# ? ****************************************************************************************/
@user.get("/user")
def get_All_User():

    # pro = "12"
    # cambio = int(pro)
    # print(cambio)
    def obtener_sujeto():
        try:
            # Ejecutar el comando y capturar la salida
            resultado = subprocess.run(
                ["certutil", "-silent", "-scinfo"], capture_output=True, text=True, check=True)

            # Buscar la línea que contiene "Sujeto"
            match = re.search(r"Sujeto: (.+)", resultado.stdout)

            if match:
                # Retorna solo el valor del sujeto
                return match.group(1).strip()
            else:
                return "No se encontró el sujeto en la salida."

        except subprocess.CalledProcessError as e:
            return f"Error ejecutando certutil: {e}"

# Llamar a la función
    sujeto = obtener_sujeto()
    print("Sujeto del certificado:", sujeto)

    return {"msj": "successfully", "pro": sujeto}


# ? CREATE ONE REGISTRO
# ? ****************************************************************************************/
@user.get("/productos")
def get_All_User():

    pro = "12"
    cambio = int(pro)
    print(cambio)
    return {"msj": "successfully", "pro": 1520

            }


# ? CREATE ONE REGISTRO
# ? ****************************************************************************************/
@user.get("/user/{id}")
def get_Id_User():
    return {"msj": "successfully", "pro": produto}
