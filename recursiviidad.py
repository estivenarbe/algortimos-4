def palindromo(palabra):

    if len(palabra) <= 1:
        return True

    if palabra[0] == palabra[-1]:
        return palindromo(palabra[1:-1])
    else:
        return False
print(palindromo("reconocer"))


#recursiva cuantsd veces se repita un carscter en un texto

def contar(s, c):
    if len(s) == 0:
        return 0
    cuenta =1 if s[0] == c else 0
    return cuenta + contar(s[1:], c)

class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self,dato):
       nodo = nodo(dato)
       if self.cabeza == None:
           self.cabeza = nodo
       else:
           actual = self.cabeza
           while actual.siguiente != None:
               actual = actual.siguiente
           actual.siguiente = nodo

           #cual es la longitud de la lista
           #recursivo   


    def longitud(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo is None:
            return 0
        return 1 + self.longitud(nodo.siguiente)
 
