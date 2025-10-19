import firebase_admin
from firebase_admin import db,credentials

cred=credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://proyecto-poo-b05c4-default-rtdb.firebaseio.com/"})

ref = db.reference("/")
usuarios = db.reference("Usuarios")

def crearTarea():
    ref.child("Usuarios").child("Jairo").set({"Password": "4321"})
    ref.child("Usuarios").child("Jairo").child("Tareas").child("1").set({"Titulo": "POO","importanciaTarea": 2})

def proponerImportancia(user):
    get = usuarios.get()
    tarea=input("Ingrese el numero de su tarea: ")

    importancia=int(input("Ingrese un valor del 1 al 3 para establecer la importancia de la tarea: "))
    while importancia != 1 and importancia != 2 and importancia != 3:
        importancia=input("Nivel de importancia incoherente (rango de 1 a 3)")
    ref.child("Usuarios").child(user).child("Tareas").child(tarea).set({"importanciaTarea": importancia})

def login():
    user=input("Ingrese su usuario: ")
    get = usuarios.get()
    if get is None:
        print("No existen usuarios")
    elif user not in get:
        print("El usuario",user,"no existe")
    else:
        print("El usuario existe: ",user)
        password=input("Ingrese su contraseña: ")
        while password not in get[user]["Password"]:
            password=input("Contraseña incorrecta, intente nuevamente")
        leerTareas(user)

def leerTareas(user):
    tarea=int(input("Ingrese una tarea: "))
    get = usuarios.get()
    datos = get[user]["Tareas"][tarea]
    print(f"Tarea {tarea}:")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")


def main():
    proponerImportancia("Jairo")

if __name__ == "__main__":
    main()