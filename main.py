import firebase_admin
from firebase_admin import db,credentials

cred=credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://proyecto-poo-b05c4-default-rtdb.firebaseio.com/"})

ref = db.reference("/")

def crearTarea():
    ref.child("Tareas de Jairo").child("2").set({"Titulo": "Codigo","importanciaTarea": 2})

def leerTareas():
    tareas = ref.get()
    if tareas:
        for clave, datos in tareas.items():
            print(f"ID: {clave}")
            for campo, valor in datos.items():
                print(f"  {campo}: {valor}")
    else:
        print("No hay tareas registradas.")

def actualizarTarea():
    ref.child("Tareas de Jairo").child("2").update({"importanciaTarea": 3})

def eliminarTarea():
    ref.child("Tareas de Jairo").child("2").delete()

def main():
    crearTarea()

if __name__ == "__main__":
    main()