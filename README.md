
 Sistema de Gestión de Librería
 Descripción
Este proyecto implementa un sistema de gestión de libros para una librería, utilizando Programación Orientada a Objetos (POO) en Python.
El sistema permite añadir, actualizar, eliminar, buscar y listar libros mediante un menú interactivo en consola.
Arquitectura del proyecto
libreria/
├── modelos/
│   └── libro.py              # Clase Libro (representa cada libro)
├── servicios/
│   └── gestion_libreria.py   # Clase gestión librería (gestiona la colección de libros)
└── main.py      # Punto de entrada con menú en consola

 Explicación del código
1. modelos/libro.py
•	Clase Libro: representa la entidad principal del sistema.
•	Atributos: 
o	ID_libro: identificador único del libro.
o	titulo: nombre del libro.
o	autor: autor del libro.
o	cantidad: número de ejemplares disponibles.
o	precio: costo del libro.
•	Métodos: 
o	Constructor __init__: inicializa los atributos.
o	Getters y Setters: permiten acceder y modificar los atributos de forma controlada.
o	__str__: devuelve una representación legible del libro para mostrar en consola.
 Esta parte encapsula la información de cada libro y asegura que se pueda manipular de forma ordenada.

2. servicios/gestion_libreria.py
•	Clase GestionLibreria: maneja la colección de libros.
•	Atributo principal: 
o	libros: lista que almacena objetos de tipo Libro.
•	Métodos: 
o	añadir_libro: agrega un libro validando que el ID no esté repetido.
o	eliminar_libro: elimina un libro por su ID.
o	actualizar_libro: permite modificar cantidad y/o precio de un libro.
o	buscar_libro: busca libros por coincidencias parciales en el título.
o	mostrar_libreria: lista todos los libros disponibles.
 Esta parte centraliza la lógica de negocio y evita que el menú interactúe directamente con la lista de libros.
3. main.py
•	Contiene el menú interactivo en consola.
•	Permite al usuario ejecutar las operaciones: 
1.	Añadir libro.
2.	Eliminar libro.
3.	Actualizar libro.
4.	Buscar libro.
5.	Listar librería.
6.	Salir.
•	Utiliza la clase GestionLibreria para realizar las operaciones y la clase Libro para crear nuevos registros.
En este archivo es el punto de entrada del sistema y conecta la interfaz de usuario con la lógica de negocio.
 Ejemplo de uso
Menú principal:
--- Menú de Gestión de Librería ---
1. Añadir libro
2. Eliminar libro
3. Actualizar libro
4. Buscar libro
5. Listar librería
6. Salir
Ejemplo de flujo:
1.	Añadir libro:
2.	Ingrese ID: L001
3.	Ingrese título: Cien Años de Soledad
4.	Ingrese autor: Gabriel García Márquez
5.	Ingrese cantidad: 5
6.	Ingrese precio: 20.00
7.	 Libro añadido correctamente.
8.	Listar librería:
9.	Libros disponibles:
10.	ID: L001, Título: Cien Años de Soledad, Autor: Gabriel García Márquez, Cantidad: 5, Precio: 20.0


