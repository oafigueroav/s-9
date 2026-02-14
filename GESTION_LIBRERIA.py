from modelos.libro import Libro

class GestionLibreria:
    def __init__(self):
        self.libros = []

    def añadir_libro(self, libro):
        for l in self.libros:
            if l.get_id() == libro.get_id():
                print("❌ Error: El ID ya existe en la librería.")
                return
        self.libros.append(libro)
        print("✅ Libro añadido correctamente.")

    def eliminar_libro(self, id_libro):
        for l in self.libros:
            if l.get_id() == id_libro:
                self.libros.remove(l)
                print("✅ Libro eliminado correctamente.")
                return
        print("❌ Error: Libro no encontrado.")

    def actualizar_libro(self, id_libro, cantidad=None, precio=None):
        for l in self.libros:
            if l.get_id() == id_libro:
                if cantidad is not None:
                    l.set_cantidad(cantidad)
                if precio is not None:
                    l.set_precio(precio)
                print("✅ Libro actualizado correctamente.")
                return
        print("❌ Error: Libro no encontrado.")

    def buscar_libro(self, titulo):
        resultados = [l for l in self.libros if titulo.lower() in l.get_titulo().lower()]
        if resultados:
            print("🔎 Resultados de búsqueda:")
            for l in resultados:
                print(l)
        else:
            print("❌ No se encontraron coincidencias.")

    def mostrar_libreria(self):
        if not self.libros:
            print("📚 La librería está vacía.")
        else:
            print("📋 Libros disponibles:")
            for l in self.libros:
                print(l)
