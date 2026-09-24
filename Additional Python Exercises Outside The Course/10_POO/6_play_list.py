#Clases, `__init__`, `self`, atributos, métodos.
#6. Cree una clase `Playlist` que permita agregar y quitar canciones (strings), y mostrar todas las canciones.

class Playlist():
    def __init__(self, lst):
        self.lst = lst

    def add(self, song):
        self.lst.append(song)

    def remove(self, song):
        if song in self.lst:
            self.lst.remove(song)

    def show_list(self):
        for song in self.lst:
            print(song)


playlist1 = Playlist(["Song 1", "Song 2", "Song 3"])
playlist1.add("Song 4")
playlist1.show_list()