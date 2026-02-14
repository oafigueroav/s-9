from servicios.gestion_libreria import GestionLibreria
from modelos.libro import Libro

def menu():
    libreria = GestionLibreria()

    while True:
        print("\n--- Menú de Gestión de Librería ---")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Actualizar libro")
        print("4. Buscar libro")
        print("5. Listar librería")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_libro = input("Ingrese ID: ")
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            libro = Libro(id_libro, titulo, autor, cantidad, precio)
            libreria.añadir_libro(libro)

        elif opcion == "2":
            id_libro = input("Ingrese ID del libro a eliminar: ")
            libreria.eliminar_libro(id_libro)

        elif opcion == "3":
            id_libro = input("Ingrese ID del libro a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            libreria.actualizar_libro(id_libro, cantidad, precio)

        elif opcion == "4":
            titulo = input("Ingrese título o parte del título a buscar: ")
            libreria.buscar_libro(titulo)

        elif opcion == "5":
            libreria.mostrar_libreria()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
