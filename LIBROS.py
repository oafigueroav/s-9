# Clase Libro: representa un libro en la librería

class Libro:
    def __init__(self, id_libro, titulo, autor, cantidad, precio):
        self._id = id_libro
        self._titulo = titulo
        self._autor = autor
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_autor(self, autor):
        self._autor = autor

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id}, Título: {self._titulo}, Autor: {self._autor}, Cantidad: {self._cantidad}, Precio: {self._precio}"
