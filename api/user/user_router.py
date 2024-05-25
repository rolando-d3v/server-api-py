from fastapi import APIRouter

user = APIRouter()

produto = [
    {
        "producto": "laptop dell",
        "description": "laptop ultra slim 2023",
        "precio": 4560,
        "stock": 10,
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

    pro = "12"
    cambio = int(pro)
    print(cambio)
    return {"msj": "successfully", "pro": produto}



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
