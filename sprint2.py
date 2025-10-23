import firebase_admin
from firebase_admin import db,credentials

cred=credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://proyecto-poo-b05c4-default-rtdb.firebaseio.com/"})

ref = db.reference("/")
usuarios = db.reference("Usuarios")

def crearUsuario():
    user = input("Crea el nombre de tu nueva cuenta: ")
    password = input("Crea una contraseña para tu nueva cuenta: ")
    ref.child("Usuarios").child(user).set({"Password: ": password})

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


def agregarTarea(user):
    tarea = input("Ingrese el nombre de su nueva tarea: ")
    importancia = int(input("Ingrese un valor del 1 al 3 para establecer la importancia de la tarea (1 minima, 2 medio, 3 maxima): "))
    while importancia != 1 and importancia != 2 and importancia != 3:
        importancia=int(input("Nivel de importancia incoherente (rango de 1 a 3): "))
    categoria = int(input("Ingrese un valor del 1 al 3 para establecer la categoria de la tarea (1 personal, 2 estudios, 3 trabajo): "))

    ref.child("Usuarios").child(user).child("Tareas").child(tarea).set({"importancia de la Tarea": importancia, "Categoria: ": categoria})


def actualizarTarea(user):
    opcion=int(input("Ingrese 1 para editar el nombre de la tarea, 2 para editar la importancia, 3 para editar la categoria: "))

    while opcion != 1 and opcion != 2 and opcion != 3:
        opcion=int(input("Opcion no valida. Ingrese 1 para editar el nombre de la tarea, 2 para editar la importancia: "))

    if opcion == 1:
        tarea=input("Ingrese el nombre original de la tarea: ")
        nombreNuevo = input("Ingrese el nuevo nombre: ")
        tareaOriginal = ref.child("Usuarios").child(user).child("Tareas").child(tarea).get()
        ref.child("Usuarios").child(user).child("Tareas").child(nombreNuevo).set(tareaOriginal)
        tareaOriginal = ref.child("Usuarios").child(user).child("Tareas").child(tarea).delete()

    elif opcion == 2:
        importancia=int(input("Ingrese un valor del 1 al 3 para establecer la importancia de la tarea: "))
        while importancia != 1 and importancia != 2 and importancia != 3:
            importancia=int(input("Nivel de importancia incoherente (rango de 1 a 3): "))
        ref.child("Usuarios").child(user).child("Tareas").child(tarea).set({"importancia de la Tarea": importancia})

    elif opcion == 3:
        categoria = int(input("Ingrese un valor del 1 al 3 para establecer la categoria de la tarea (1 personal, 2 estudios, 3 trabajo): "))

        while categoria != 1 and opcion != 2 and opcion != 3:
            categoria=int(input("Opcion no valida. Ingrese un valor del 1 al 3 para establecer la categoria de la tarea (1 personal, 2 estudios, 3 trabajo): "))

        ref.child("Usuarios").child(user).child("Tareas").child(tarea).update({"Categoria: ": categoria})
        



def eliminarTarea(user):
    tarea=input("Ingrese el nombre original de la tarea: ")
    ref.child("Usuarios").child(user).child("Tareas").child(tarea).delete()
    print(f"Tarea: ",tarea,"ha sido eliminada")
        

def leerTareas(user):
    tareas=ref.child("Usuarios").child(user).child("Tareas").get()

    if tareas:
        for clave, datos in tareas.items():
            print(f"Tarea ID: {clave}")
            print(f"Datos: {datos}")
    else:
        print("No hay tareas registradas.")


def main():
    agregarTarea("Jairo")

if __name__ == "__main__":
    main()
