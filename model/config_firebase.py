import firebase_admin
from firebase_admin import db, credentials

#DEJAR LAS CREDENCIALES JSON FUERA DE LAS CARPETAS, SOLO DENTRO DE Sprint-2
class FirebaseConfig:
    #Configuración Singleton de Firebase
    _instance = None
    _initialized = False
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def initialize(self):
        if not self._initialized:
            cred = credentials.Certificate("Sprint-2/credentials.json")
            firebase_admin.initialize_app(cred, {"databaseURL": "https://proyecto-poo-b05c4-default-rtdb.firebaseio.com/"})
            self._initialized = True
    
    def get_reference(self, path: str = "/"):

        return db.reference(path)

