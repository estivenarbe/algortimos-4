#menu en el que se pueda escuchar musica , saber cuanto dura la cancion, si quiere pasar a la siguiente cancion, retroceder, que cancion quiere escuchar

class Cancion:
    def __init__(self, titulo, artista, tipo):
        self.titulo = titulo
        self.artista = artista
        self.tipo = tipo  # Normal o Favorita
        self.siguiente = None


class Playlist:
    def __init__(self):
        self.primera = None

    #  Agregar canción normal (recursivo)
    def agregar_cancion(self, titulo, artista):
        nueva = Cancion(titulo, artista, "Normal")

        if self.primera is None:
            self.primera = nueva
        else:
            self._agregar_recursivo(self.primera, nueva)

    def _agregar_recursivo(self, nodo_actual, nueva):
        if nodo_actual.siguiente is None:
            nodo_actual.siguiente = nueva
        else:
            self._agregar_recursivo(nodo_actual.siguiente, nueva)

    #  Agregar canción favorita (al inicio)
    def agregar_favorita(self, titulo, artista):
        nueva = Cancion(titulo, artista, "Favorita")
        nueva.siguiente = self.primera
        self.primera = nueva

    #  Mostrar playlist
    def mostrar_playlist(self):
        if self.primera is None:
            print("\nLa playlist está vacía.")
            return

        actual = self.primera
        print("\n🎶 PLAYLIST 🎶")
        while actual:
            print(f"Título: {actual.titulo} | Artista: {actual.artista} | Tipo: {actual.tipo}")
            actual = actual.siguiente
        print("----------------------")

    #  Reproducir canción (elimina la primera)
    def reproducir(self):
        if self.primera is None:
            print("\nNo hay canciones para reproducir.")
        else:
            actual = self.primera
            self.primera = self.primera.siguiente
            print(f"\nReproduciendo: {actual.titulo} - {actual.artista}")

    # Eliminar canción por título (RECURSIVO)
    def eliminar_cancion(self, titulo):
        self.primera = self._eliminar_recursivo(self.primera, titulo)

    def _eliminar_recursivo(self, nodo_actual, titulo):

        # Caso base: lista vacía
        if nodo_actual is None:
            print("\nCanción no encontrada.")
            return None

        # Caso cuando encuentra la canción
        if nodo_actual.titulo.lower() == titulo.lower():
            print(f"\nCanción eliminada: {nodo_actual.titulo}")
            return nodo_actual.siguiente

        # Caso recursivo
        nodo_actual.siguiente = self._eliminar_recursivo(
            nodo_actual.siguiente, titulo)

        return nodo_actual


#  PROGRAMA PRINCIPAL

playlist = Playlist()

while True:
    print("\n🎵 REPRODUCTOR DE MÚSICA 🎵")
    print("1. Agregar canción")
    print("2. Agregar canción favorita")
    print("3. Mostrar playlist")
    print("4. Reproducir canción")
    print("5. Eliminar canción por título")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        titulo = input("Título: ")
        artista = input("Artista: ")
        playlist.agregar_cancion(titulo, artista)

    elif opcion == "2":
        titulo = input("Título: ")
        artista = input("Artista: ")
        playlist.agregar_favorita(titulo, artista)

    elif opcion == "3":
        playlist.mostrar_playlist()

    elif opcion == "4":
        playlist.reproducir()

    elif opcion == "5":
        titulo = input("Título de la canción a eliminar: ")
        playlist.eliminar_cancion(titulo)

    elif opcion == "0":
        print("Saliendo del reproductor...")
        break

    else:
        print("Opción inválida.")