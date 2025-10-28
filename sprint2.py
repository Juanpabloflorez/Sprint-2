import firebase_admin
from firebase_admin import db,credentials

cred=credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://proyecto-poo-b05c4-default-rtdb.firebaseio.com/"})

ref = db.reference("/")
usuarios = db.reference("Usuarios")

# Cambios a composición de tarea: agregarTarea, actualizartarea
# Base de datos: sprint 2
# Codigo: sprint 2

def crearUsuario():
    user = input("Crea el nombre de tu nueva cuenta: ")
    password = input("Crea una contraseña para tu nueva cuenta: ")
    ref.child("Usuarios").child(user).set({"Password: ": password})
    print("Usuario creado exitosamente")


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
        print("Bienvenido,",user)


def agregarTarea(user):
    tarea = input("Ingrese el nombre de su nueva tarea: ")

    importancia = int(input("Ingrese un valor del 1 al 3 para establecer la importancia de la tarea (1 minima, 2 medio, 3 maxima): "))
    while importancia != 1 and importancia != 2 and importancia != 3:
        importancia=int(input("Nivel de importancia incoherente (rango de 1 a 3): "))
    
    categoria = int(input("Ingrese un valor del 1 al 3 para establecer la categoria de la tarea (1 personal, 2 estudios, 3 trabajo): "))
    if categoria == 1:
        categoria = "personal"
    elif categoria == 2:
        categoria = "estudios"
    elif categoria == 3:
        categoria = "trabajo"
    
    tiempo=int(input("¿Cual es el tiempo límite de tu tarea (En días)?: "))
    while tiempo < 0:
        tiempo=int(input("Ingrese numeros mayores a 0 para saber cual es la fecha límite de tu tarea: "))

    ref.child("Usuarios").child(user).child("Tareas").child(tarea).set({"importancia de la Tarea": importancia, "Categoria": categoria, "Tiempo": tiempo, "Estado": "No completada"})
    print("Tarea creada exitosamente")


def actualizarTarea(user):
    tarea=input("Ingrese el nombre de la tarea: ")

    opcion=int(input("Editor de tarea: 1: Nombre, 2: Importancia, 3: Categoría, 4: Tiempo, 5: Estado"))

    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        opcion=int(input("Opcion no valida: 1: Nombre, 2: Importancia, 3: Categoría, 4: Tiempo"))

    if opcion == 1:
        nombreNuevo = input("Ingrese el nuevo nombre de la tarea: ")
        tareaOriginal = ref.child("Usuarios").child(user).child("Tareas").child(tarea).get()
        ref.child("Usuarios").child(user).child("Tareas").child(nombreNuevo).set(tareaOriginal)
        tareaOriginal = ref.child("Usuarios").child(user).child("Tareas").child(tarea).delete()
        print("Nombre de la tarea cambiado a: ",nombreNuevo)

    elif opcion == 2:
        importancia=int(input("Ingrese un valor del 1 al 3 para establecer la importancia de la tarea (1 minima, 2 media, 3 maxima): "))
        while importancia != 1 and importancia != 2 and importancia != 3:
            importancia=int(input("Nivel de importancia incoherente (rango de 1 a 3): "))
        ref.child("Usuarios").child(user).child("Tareas").child(tarea).set({"importancia de la Tarea": importancia})
        if importancia == 1:
            print("Importancia cambiada a minima")
        elif importancia == 2:
            print("Importancia cambiada a media")
        elif importancia == 3:
            print("Importancia cambiada a maxima")

    elif opcion == 3:
        categoria = int(input("Ingrese un valor del 1 al 3 para establecer la categoria de la tarea (1 personal, 2 estudios, 3 trabajo): "))

        while categoria != 1 and opcion != 2 and opcion != 3:
            categoria=int(input("Opcion no valida. Ingrese un valor del 1 al 3 para establecer la categoria de la tarea (1 personal, 2 estudios, 3 trabajo): "))

        ref.child("Usuarios").child(user).child("Tareas").child(tarea).update({"Categoria": categoria})
        if categoria == 1:
            print("categoria cambiada a personal")
        elif categoria == 2:
            print("categoria cambiada a estudios")
        elif categoria == 3:
            print("categoria cambiada a trabajo")

    elif opcion == 4:
        tiempo=int(input("¿Cual es el tiempo límite de tu tarea (En días)?"))
        while tiempo < 0:
            tiempo=int(input("Ingrese numeros mayores a 0 para saber cual es la fecha límite de tu tarea"))

        ref.child("Usuarios").child(user).child("Tareas").child(tarea).update({"Tiempo": tiempo})
        print("Tiempo cambiado a: ", tiempo)
        

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


def marcarCompletada(user):
    tarea=input("Ingrese el nombre de la tarea: ")
    ref.child("Usuarios").child(user).child("Tareas").child(tarea).update({"Estado: Completada"})
    print(tarea,"completado/a")


def main():
    leerTareas("Ivan")

if __name__ == "__main__":
    main()





