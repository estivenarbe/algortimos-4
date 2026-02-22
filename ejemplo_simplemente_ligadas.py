class nodo :
    def __init__(self, nombre, cedula, prioridad):
        self.nombre = nombre
        self.cedula = cedula
        self.prioridad = prioridad
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregarNodoAlFinal(self, nombre, cedula):
        nuevo_nodo = nodo(nombre, cedula)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        elif self.cabeza.prioridad > prioridad:
            nuevo_nodo.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente

            actual.siguiente = nuevo_nodo
        
        print("Nodo agregado al final de la lista correctamente")

    def mostrar(self):
        actual = self.cabeza
        while actual != None:
            print(f"Nombre: {actual.nombre}, Cédula: {actual.cedula}")
            actual = actual.siguiente

lista = Lista()
lista.agregarNodoAlFinal("Juan", "12345678")
lista.agregarNodoAlFinal("María", "87654321")
lista.mostrar()

                
        
