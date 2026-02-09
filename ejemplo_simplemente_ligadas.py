class nodo :
    def __init__(self, nombre, cdeula):
        self.nombre = nombre
        self.cdeula = cdeula
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregarNodoAlFinal(self, nombre, cedula):
        nuevo_nodo = nodo(nombre, cedula)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente

            actual.siguiente = nuevo_nodo
        
        print("Nodo agregado al final de la lista correctamente")

    def mostrar(self):
        actual = self.cabeza
        while actual != None:
            print(f"Nombre: {actual.nombre}, Cédula: {actual.cdeula}")
            actual = actual.siguiente

lista = Lista()
lista.agregarNodoAlFinal("Juan", "12345678")
lista.mostrar()

                
        
