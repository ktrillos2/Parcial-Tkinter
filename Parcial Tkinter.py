import tkinter as tk
import re
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime

usuarios = [
    ["admin@email.com", "admin123", "admin", ["", "", True, "", ""]],
    ["cajero1@email.com", "cajero1", "cajero",
        ["prueba", "123456789", True, "", ""]],
    ["cajero2@email.com", "cajero2", "cajero",
        ["prueba2", "1234567891", True, "", ""]],
    [
        "angel@gmail.com",
        "contra",
        "usuario",
        ["angel", "123456789", True, "3144098545", "Mz A lote 1"],
        0,
    ],
    [
        "keiner@gmail.com",
        "contra",
        "usuario",
        ["angel", "1234567893", True, "3222244572", "Mz A lote 1"],
        0,
    ],
]

facturas = [
    [
        1,
        "keiner@gmail.com",
        "21/03/2023",
        {
            "tipo": "Ensalada de frutas",
            "tamaño": "para compartir sin helado",
            "sabor": ["Ensalada de frutas sin helado"],
            "precio": 10200,
        },"caja",
        {"Total": 10200},
    ],
    [
        2,
        "Andres",
        "26/03/2023",
        {
            "tipo": "Fresas",
            "tamaño": "Fresas con helado",
            "sabor": ["vainilla chips"],
            "precio": 8400,
        },"caja",
        {"Total": 8400},
    ],
    [
        3,
        "Felipe",
        "21/03/2023",
        {
            "tipo": "Granizados",
            "tamaño": "Granizado 16 onz",
            "sabor": ["fresa"],
            "precio": 8400,
        },"online",
        {"Total": 8400},
    ],
    [
        4,
        "Felipe",
        "12/01/2023",
        {
            "tipo": "Banana split",
            "tamaño": "Banana split",
            "sabor": ["fresa", "ron con pasas"],
            "precio": 13200,
        },"onlinecaja",
        {"Total": 13200},
    ],
    [
        5,
        "Felipe",
        "10/04/2023",
        {
            "tipo": "Banana split",
            "tamaño": "Banana split",
            "sabor": ["fresa", "ron con pasas"],
            "precio": 13200,
        },"caja",
        {"Total": 13200},
    ],
    [
        6,
        "Andres",
        "12/08/2019",
        {
            "tipo": "Ensalada de frutas",
            "tamaño": "para compartir con helado",
            "sabor": ["vainilla chips", "tropical de agua"],
            "precio": 14500,
        },"online",
        {"Total": 14500},
    ],
    [
        7,
        "Andres",
        "12/08/2019",
        {
            "tipo": "Ensalada de frutas",
            "tamaño": "para compartir con helado",
            "sabor": ["vainilla chips", "tropical de agua"],
            "precio": 14500,
        },"caja",
        {"Total": 14500},
    ],
    [
        8,
        "Tomas",
        "12/03/2021",
        {
            "tipo": "Vasos",
            "tamaño": "Doble",
            "sabor": ["vainilla chips", "cereza"],
            "precio": 8400,
        },
        {
            "tipo": "Litro de helado",
            "tamaño": "Litro de helado",
            "sabor": ["vainilla chips"],
            "precio": 27000,
        },"caja",
        {"Total": 35400},
    ],
    [
        9,
        "Andres",
        "19/04/2022",
        {
            "tipo": "Copas infantiles",
            "tamaño": "Fiesta",
            "sabor": ["maracuya en leche", "nata"],
            "precio": 8800,
        },"online",
        {"Total": 8800},
    ],
    [
        10,
        "Felipe",
        "18/02/2023",
        {
            "tipo": " Malteadas",
            "tamaño": "Malteada 12 onz",
            "sabor": ["maracuya en leche"],
            "precio": 6400,
        },"onlinecaja",
        {"Total": 6400},
    ],
    [
        11,
        "Tomas",
        "25/03/2023",
        {
            "tipo": "Banana split",
            "tamaño": "Banana split",
            "sabor": ["frutos rojos", "chicle"],
            "precio": 13200,
        },"caja",
        {"Total": 13200},
    ],
    [
        12,
        "Tomas",
        "01/01/2021",
        {
            "tipo": "Copas infantiles",
            "tamaño": "piñata",
            "sabor": ["crocante"],
            "precio": 10800,
        },"online",
        {"Total": 10800},
    ],
    [
        13,
        "Tomas",
        "06/04/2022",
        {
            "tipo": "Granizados",
            "tamaño": "Granizado 16 onz",
            "sabor": ["fresa"],
            "precio": 8400,
        },"caja",
        {"Total": 8400},
    ],
    [
        14,
        "Felipe",
        "30/04/2022",
        {
            "tipo": "Ensalada de frutas",
            "tamaño": "para compartir con helado",
            "sabor": ["tropical de agua", "maracuya en agua"],
            "precio": 14500,
        },"online",
        {"Total": 14500},
    ],
    [
        15,
        "Andres",
        "12/02/2023",
        {
            "tipo": "Conos",
            "tamaño": "Doble",
            "sabor": ["maracuya en agua", "tropical de agua"],
            "precio": 8400,
        },"onlinecaja",
        {"Total": 8400},
    ],
]

# Colores
color_principal = "#FF6D60"
color_secundario = "#F7D060"
color_terciario = "#F3E99F"
color_cuarto = "#98D8AA"

usuario = ""
contraseña = ""


class Admin:
    def __init__(self, root):
        self.root = root
        self.facturas_table = None
        pass

    def volver(self):
        self.root.destroy()  # Destruir la ventana actual
        main = Inicio()  # Crear una nueva instancia de la clase Inicio
        main.root.mainloop()

    def herramientas(self):
        self.root.configure(bg=color_terciario)
        self.root.title("Barra de Herramientas")

        # Crear una barra de herramientas
        barra = tk.Menu(self.root)
        self.root.config(menu=barra)

        # Agregar botones a la barra de herramientas
        cajero_menu = tk.Menu(barra, tearoff=0)
        cajero_menu.add_command(label="Ver Cajeros", command=self.Cajeros)
        cajero_menu.add_command(label="Agregar Cajero",
                                command=self.AgregarCajero)
        productos_menu = tk.Menu(barra, tearoff=0)
        productos_menu.add_command(label="Ver Productos", command=self.Productos)
        productos_menu.add_command(label="Modificar Productos", command=self.ModificarProductos)
        productos_menu.add_command(label="Agregar Productos", command=self.AgregarProductos)

        # Agregar opción de "Ver Facturas"
        facturas_menu = tk.Menu(barra, tearoff=0)
        facturas_menu.add_command(label="Ver Facturas", command=self.VerFacturas)
        facturas_menu.add_command(label="Ver Facturas por Fecha", command=self.VerFacturasPorFecha)
        facturas_menu.add_command(label="Ver Facturas por Cajero", command=self.VerFacturasPorCajero)


        barra.add_cascade(label="Cajero", menu=cajero_menu)
        barra.add_cascade(label="Productos", menu=productos_menu)
        barra.add_cascade(label="Facturas", menu=facturas_menu)
        barra.add_command(label="Opción 4", command=self.opcion4)

        # Crear un botón de regresar
        image = Image.open("BotonVolver.png")  # Ruta de la imagen corregida
        nuevo_tamaño = (40, 40)
        imagen_nueva = image.resize(nuevo_tamaño)
        background_image = ImageTk.PhotoImage(imagen_nueva)
        button_regresar = tk.Button(
            self.root,
            image=background_image,
            command=lambda: self.volver(),
            bg=color_terciario,
        )
        button_regresar.image = background_image  # Mantener una referencia a la imagen
        button_regresar.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

    def Ventana_Principal(self):
        self.herramientas()
        self.Cajeros()

    def Cajeros(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()

        # Filtrar los usuarios que tengan el rol "cajero"
        cajeros = [cajero for cajero in usuarios if cajero[2] == "cajero"]

        # Crear la tabla de cajeros
        table_frame = tk.Frame(
            self.root, bg=color_terciario, bd=1, relief=tk.SOLID)
        table_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título de la tabla
        titulo = tk.Label(
            table_frame, text="Cajeros", font=("Arial", 14, "bold"), bg=color_terciario
        )
        titulo.grid(row=0, column=0, columnspan=5, pady=10)

        # Encabezados de las columnas
        nombre_label = tk.Label(
            table_frame, text="Nombre", font=("Arial", 12, "bold"), bg=color_terciario
        )
        nombre_label.grid(row=1, column=0, padx=(30, 5), pady=5)

        correo_label = tk.Label(
            table_frame, text="Correo", font=("Arial", 12, "bold"), bg=color_terciario
        )
        correo_label.grid(row=1, column=1, padx=(20, 5), pady=5)

        documento_label = tk.Label(
            table_frame, text="Documento", font=("Arial", 12, "bold"), bg=color_terciario
        )
        documento_label.grid(row=1, column=2, padx=(20, 10), pady=5)

        eliminar_label = tk.Label(
            table_frame, text="Eliminar", font=("Arial", 12, "bold"), bg=color_terciario
        )
        eliminar_label.grid(row=1, column=3, padx=10, pady=5)

        editar_label = tk.Label(
            table_frame, text="Editar", font=("Arial", 12, "bold"), bg=color_terciario
        )
        editar_label.grid(row=1, column=4, padx=10, pady=5)

        # Mostrar datos de los cajeros en la tabla
        for i, cajero in enumerate(cajeros, start=2):
            nombre = cajero[3][0]
            correo = cajero[0]
            documento = cajero[3][1]

            nombre_label = tk.Label(
                table_frame, text=nombre, bg=color_terciario)
            nombre_label.grid(row=i, column=0, padx=(20, 5), pady=5)

            correo_label = tk.Label(
                table_frame, text=correo, bg=color_terciario)
            correo_label.grid(row=i, column=1, padx=(20, 5), pady=5)

            documento_label = tk.Label(
                table_frame, text=documento, bg=color_terciario)
            documento_label.grid(row=i, column=2, padx=(20, 5), pady=5)

            eliminar_button = tk.Button(
                table_frame,
                text="Eliminar",
                command=lambda c=cajero: self.eliminar_cajero(c),
                bg="red",
            )
            eliminar_button.grid(row=i, column=3, padx=5, pady=5)

            editar_button = tk.Button(
                table_frame,
                text="Editar",
                command=lambda c=cajero: self.editar_cajero(c),
                bg="yellow",
            )
            editar_button.grid(row=i, column=4, padx=5, pady=5)

    def AgregarCajero(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()

        # Crear el formulario de agregar cajero
        form_frame = tk.Frame(self.root, bg=color_terciario, bd=0)
        form_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título del formulario
        titulo = tk.Label(
            form_frame,
            text="Agregar Cajero",
            font=("Arial", 14, "bold"),
            bg=color_terciario,
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Campos del formulario
        nombre_label = tk.Label(
            form_frame, text="Nombre:", font=("Arial", 12), bg=color_terciario
        )
        nombre_label.grid(row=1, column=0, padx=5, pady=5)
        nombre_entry = tk.Entry(form_frame, font=("Arial", 12))
        nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        numero_doc_label = tk.Label(
            form_frame,
            text="Número de Documento:",
            font=("Arial", 12),
            bg=color_terciario,
        )
        numero_doc_label.grid(row=2, column=0, padx=5, pady=5)
        numero_doc_entry = tk.Entry(form_frame, font=("Arial", 12))
        numero_doc_entry.grid(row=2, column=1, padx=5, pady=5)

        correo_label = tk.Label(
            form_frame, text="Correo:", font=("Arial", 12), bg=color_terciario
        )
        correo_label.grid(row=3, column=0, padx=5, pady=5)
        correo_entry = tk.Entry(form_frame, font=("Arial", 12))
        correo_entry.grid(row=3, column=1, padx=5, pady=5)

        contrasena_label = tk.Label(
            form_frame, text="Contraseña:", font=("Arial", 12), bg=color_terciario
        )
        contrasena_label.grid(row=4, column=0, padx=5, pady=5)
        contrasena_entry = tk.Entry(form_frame, font=("Arial", 12), show="*")
        contrasena_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botón de añadir nuevo cajero
        nuevo_cajero_button = tk.Button(
            form_frame,
            text="Añadir Nuevo Cajero",
            command=lambda: self.nuevo_cajero(
                nombre_entry.get(),
                correo_entry.get(),
                contrasena_entry.get(),
                numero_doc_entry.get(),
            ),
            bg=color_principal,
            fg="white",
        )
        nuevo_cajero_button.grid(
            row=5, column=0, columnspan=2, padx=5, pady=10, ipadx=10
        )

    def nuevo_cajero(self, nombre, correo, contrasena, numero_documento):

        # Verificar campos vacíos
        if nombre == "" or numero_documento == "" or correo == "" or contrasena == "":
            messagebox.showerror(
                "Error", "Por favor, complete todos los campos.")
            return

        # Verificar correo válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "El correo ingresado es inválido.")
            return

        # Verificar documento válido
        if not numero_documento.isdigit() or len(numero_documento) < 9 or len(numero_documento) > 10:
            messagebox.showerror(
                "Error", "El número de documento ingresado es inválido.")
            return

        # Verificar duplciados de documento y correo
        for usuario in usuarios:
            if usuario[0] == correo:
                messagebox.showerror("Error", "El correo ya está en uso.")
                return
            if usuario[3][1] == numero_documento:
                messagebox.showerror(
                    "Error", "El número de documento ya existe.")
                return

        nuevo_cajero = [correo, contrasena, "cajero",
                        [nombre, numero_documento, True, "", ""]]
        usuarios.append(nuevo_cajero)
        print("Nuevo cajero agregado:", nuevo_cajero)

    def es_correo_valido(self, correo):
        # Expresión regular para validar el correo electrónico
        patron_correo = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron_correo, correo)

    def es_documento_valido(self, documento):
        # Expresión regular para validar el número de documento
        patron_documento = r"^\d{9,10}$"
        return re.match(patron_documento, documento)

    def eliminar_cajero(self, cajero):
        usuarios.remove(cajero)  # Eliminar el cajero del arreglo de usuarios

        # Destruir la tabla de cajeros si ya existe
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

        # Volver a crear la tabla de cajeros sin el cajero eliminado
        self.Cajeros()

    def editar_cajero(self, cajero):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()

        # Crear el formulario de editar cajero
        form_frame = tk.Frame(self.root, bg=color_terciario, bd=0)
        form_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título del formulario
        titulo = tk.Label(
            form_frame,
            text="Editar Cajero",
            font=("Arial", 14, "bold"),
            bg=color_terciario,
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Obtener los datos del cajero seleccionado
        correo = cajero[0]
        contrasena = cajero[1]
        nombre = cajero[3][0]
        documento = cajero[3][1]

        # Campos del formulario
        nombre_label = tk.Label(
            form_frame, text="Nombre:", font=("Arial", 12), bg=color_terciario
        )
        nombre_label.grid(row=1, column=0, padx=5, pady=5)
        nombre_entry = tk.Entry(form_frame, font=("Arial", 12))
        # Rellenar el campo con el nombre del cajero
        nombre_entry.insert(tk.END, nombre)
        nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        numero_doc_label = tk.Label(
            form_frame,
            text="Número de Documento:",
            font=("Arial", 12),
            bg=color_terciario,
        )
        numero_doc_label.grid(row=2, column=0, padx=5, pady=5)
        numero_doc_entry = tk.Entry(form_frame, font=("Arial", 12))
        # Rellenar el campo con el documento del cajero
        numero_doc_entry.insert(tk.END, documento)
        numero_doc_entry.grid(row=2, column=1, padx=5, pady=5)

        correo_label = tk.Label(
            form_frame, text="Correo:", font=("Arial", 12), bg=color_terciario
        )
        correo_label.grid(row=3, column=0, padx=5, pady=5)
        correo_entry = tk.Entry(form_frame, font=("Arial", 12))
        # Rellenar el campo con el correo del cajero
        correo_entry.insert(tk.END, correo)
        correo_entry.grid(row=3, column=1, padx=5, pady=5)

        contrasena_label = tk.Label(
            form_frame, text="Contraseña:", font=("Arial", 12), bg=color_terciario
        )
        contrasena_label.grid(row=4, column=0, padx=5, pady=5)
        contrasena_entry = tk.Entry(form_frame, font=("Arial", 12), show="*")
        # Rellenar el campo con la contraseña del cajero
        contrasena_entry.insert(tk.END, contrasena)
        contrasena_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botón de actualizar cajero
        actualizar_cajero_button = tk.Button(
            form_frame,
            text="Actualizar Cajero",
            font=("Arial", 12, "bold"),
            bg="green",
            command=lambda: self.actualizar_cajero(
                cajero, nombre_entry.get(), numero_doc_entry.get(
                ), correo_entry.get(), contrasena_entry.get()
            ),
        )
        actualizar_cajero_button.grid(row=5, column=0, columnspan=2, pady=10)

    def actualizar_cajero(self, cajero, nombre, correo, contrasena, numero_documento):
        # Verificar campos vacíos
        if nombre == "" or numero_documento == "" or correo == "" or contrasena == "":
            messagebox.showerror(
                "Error", "Por favor, complete todos los campos.")
            return

        # Verificar correo válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "El correo ingresado es inválido.")
            return

        # Verificar documento válido
        if not numero_documento.isdigit() or len(numero_documento) < 9 or len(numero_documento) > 10:
            messagebox.showerror(
                "Error", "El número de documento ingresado es inválido.")
            return

        # Verificar duplicados de documento y correo
        for usuario in usuarios:
            if usuario != cajero:
                if usuario[0] == correo:
                    messagebox.showerror("Error", "El correo ya está en uso.")
                    return
                if usuario[3][1] == numero_documento:
                    messagebox.showerror(
                        "Error", "El número de documento ya existe.")
                    return

        # Actualizar los datos del cajero
        cajero[0] = correo
        cajero[1] = contrasena
        cajero[3][0] = nombre
        cajero[3][3] = numero_documento

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Cajero actualizado correctamente.")

        # Destruir el formulario de editar cajero y recrear la tabla de cajeros
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
        self.Cajeros()
        
    def Productos(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()

        # Crear la tabla de productos
        table_frame = tk.Frame(
            self.root, bg=color_terciario, bd=1, relief=tk.SOLID)
        table_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título de la tabla
        titulo = tk.Label(
            table_frame, text="Productos", font=("Arial", 14, "bold"), bg=color_terciario
        )
        titulo.grid(row=0, column=0, columnspan=5, pady=10)

        # Encabezados de las columnas
        # ...

        # Mostrar datos de los productos en la tabla
        # ...
        
    def ModificarProductos(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()

        # Crear el formulario para modificar productos
        form_frame = tk.Frame(
            self.root, bg=color_terciario, bd=1, relief=tk.SOLID)
        form_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título del formulario
        titulo = tk.Label(
            form_frame, text="Modificar Productos", font=("Arial", 14, "bold"), bg=color_terciario
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Campos de entrada para modificar productos
        # ...

    def AgregarProductos(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()

        # Crear el formulario para agregar productos
        form_frame = tk.Frame(
            self.root, bg=color_terciario, bd=1, relief=tk.SOLID)
        form_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título del formulario
        titulo = tk.Label(
            form_frame, text="Agregar Productos", font=("Arial", 14, "bold"), bg=color_terciario
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Campos de entrada para agregar productos
        # ...

    def VerFacturas(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()
        # Crear la tabla de facturas dentro de un widget Canvas
        canvas = tk.Canvas(self.root, bg=color_terciario, highlightbackground=color_terciario)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Crear un scrollbar y asociarlo al widget Canvas
        scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configurar el scrollbar para que controle el widget Canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Crear un frame dentro del widget Canvas para contener la tabla
        table_frame = tk.Frame(canvas, bg=color_terciario,highlightbackground="black", highlightthickness=1)
        canvas.create_window((30, 0), window=table_frame, anchor=tk.NW)

        # Agregar la tabla de facturas al frame
        # ... código para crear y mostrar la tabla de facturas ...
        # Crear la tabla de facturas

        # Título de la tabla
        titulo = tk.Label(
            table_frame, text="Facturas", font=("Arial", 14, "bold"), bg=color_terciario
        )
        titulo.grid(row=0, column=0, columnspan=7)

        # Encabezados de las columnas
        id_label = tk.Label(
            table_frame, text="ID", font=("Arial", 12, "bold"), bg=color_terciario
        )
        id_label.grid(row=1, column=0, padx=(30, 10), pady=5)

        correo_label = tk.Label(
            table_frame, text="Correo", font=("Arial", 12, "bold"), bg=color_terciario
        )
        correo_label.grid(row=1, column=1, padx=(20, 10), pady=5)

        fecha_label = tk.Label(
            table_frame, text="Fecha", font=("Arial", 12, "bold"), bg=color_terciario
        )
        fecha_label.grid(row=1, column=2, padx=(20, 10), pady=5)

        tipo_label = tk.Label(
            table_frame, text="Tipo", font=("Arial", 12, "bold"), bg=color_terciario
        )
        tipo_label.grid(row=1, column=3, padx=(20, 10), pady=5)

        sabores_label = tk.Label(
            table_frame, text="Sabores", font=("Arial", 12, "bold"), bg=color_terciario
        )
        sabores_label.grid(row=1, column=5, padx=(20, 10), pady=5)

        precio_label = tk.Label(
            table_frame, text="Precio", font=("Arial", 12, "bold"), bg=color_terciario
        )
        precio_label.grid(row=1, column=6, padx=(20, 10), pady=5)

        # Mostrar datos de las facturas en la tabla
        for i, factura in enumerate(facturas, start=2):
            factura_id = factura[0]
            correo = factura[1]
            fecha = factura[2]
            tipo = factura[3]["tipo"]
            tamaño = factura[3]["tamaño"]
            sabores = ", ".join(factura[3]["sabor"])
            precio = factura[3]["precio"]

            id_label = tk.Label(
                table_frame, text=factura_id, bg=color_terciario)
            id_label.grid(row=i, column=0, padx=(20, 10), pady=5)

            correo_label = tk.Label(
                table_frame, text=correo, bg=color_terciario)
            correo_label.grid(row=i, column=1, padx=(20, 10), pady=5)

            fecha_label = tk.Label(
                table_frame, text=fecha, bg=color_terciario)
            fecha_label.grid(row=i, column=2, padx=(20, 10), pady=5)

            tipo_label = tk.Label(
                table_frame, text=tipo, bg=color_terciario)
            tipo_label.grid(row=i, column=3, padx=(20, 10), pady=5)

            sabores_label = tk.Label(
                table_frame, text=sabores, bg=color_terciario)
            sabores_label.grid(row=i, column=5, padx=(20, 10), pady=5)

            precio_label = tk.Label(
                table_frame, text=precio, bg=color_terciario)
            precio_label.grid(row=i, column=6, padx=(20, 10), pady=5)

    def VerFacturasPorFecha(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()

        # Crear el formulario de búsqueda por fecha
        form_frame = tk.Frame(self.root, bg=color_terciario, bd=0)
        form_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título del formulario
        titulo = tk.Label(
            form_frame,
            text="Buscar Facturas por Fecha",
            font=("Arial", 14, "bold"),
            bg=color_terciario,
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Campo de fecha
        fecha_label = tk.Label(
            form_frame, text="Fecha (DD/MM/AAAA):", font=("Arial", 12), bg=color_terciario
        )
        fecha_label.grid(row=1, column=0, padx=5, pady=5)
        fecha_entry = tk.Entry(form_frame, font=("Arial", 12))
        fecha_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botón de búsqueda
        buscar_button = tk.Button(
            form_frame,
            text="Buscar",
            command=lambda: self.buscar_facturas_por_fecha(fecha_entry.get()),
            bg=color_secundario,
        )
        buscar_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def buscar_facturas_por_fecha(self, fecha):
        # Verificar que se haya ingresado una fecha válida
        if not fecha:
            messagebox.showerror("Error", "Ingrese una fecha válida.")
            return

        # Convertir la fecha ingresada a un objeto datetime
        try:
            fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        except ValueError:
            messagebox.showerror("Error", "Fecha ingresada inválida.")
            return

        # Filtrar las facturas por fecha
        facturas_filtradas = [
            factura for factura in facturas if factura[2] == fecha.strftime("%d/%m/%Y")
        ]

        # Mostrar las facturas filtradas en una tabla
        # Crear la tabla de facturas
        table_frame = tk.Frame(
            self.root, bg=color_terciario, bd=1, relief=tk.SOLID)
        table_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título de la tabla
        titulo = tk.Label(
            table_frame, text="Facturas por Fecha", font=("Arial", 14, "bold"), bg=color_terciario
        )
        titulo.grid(row=0, column=0, columnspan=5, pady=10)

        # Encabezados de las columnas
        headers = ["ID", "Cliente", "Fecha", "Detalles", "Tipo Pago", "Total"]
        for col, header in enumerate(headers):
            label = tk.Label(table_frame, text=header, font=("Arial", 12, "bold"), bg=color_terciario)
            label.grid(row=1, column=col, padx=5, pady=5)

        # Mostrar las facturas en la tabla
        for row, factura in enumerate(facturas_filtradas, start=2):
            for col, value in enumerate(factura):
                label = tk.Label(table_frame, text=value, font=("Arial", 12), bg=color_terciario)
                label.grid(row=row, column=col, padx=5, pady=5)

    def VerFacturasPorCajero(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.herramientas()
        pass

    def opcion3(self):
        self.label.config(text="Has seleccionado la opción 3")

    def opcion4(self):
        self.label.config(text="Has seleccionado la opción 4")



class Cajero:
    def __init__(self) -> None:
        pass


class Usuario:
    def __init__(self) -> None:
        pass

    def volver_inicio_sesion(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.mostrar_ventana_inicio_sesion()  
 
    def Ventana_Usuario(self):
        self.root.configure(bg=color_terciario)
        self.root.title("Barra de Herramientas")

        # Crear una barra de herramientas
        barra = tk.Menu(self.root)
        self.root.config(menu=barra)

        # Agregar botones a la barra de herramientas
        cajero_menu = tk.Menu(barra, tearoff=0)
        compra = tk.Menu(barra, tearoff=1)
        cajero_menu.add_command(label="Modificar Usuario")
        compra.add_command(label="Compra en Linea")
        compra.add_command(label="Pagar en caja")
        compra.add_command(label="Todo en caja")

        barra.add_cascade(label="Usuario", menu=cajero_menu)
        barra.add_cascade(label="Comprar", menu=compra)

        # Crear un botón de regresar
        image = Image.open("BotonVolver.png")
        nuevo_tamaño = (40, 40)
        imagen_nueva = image.resize(nuevo_tamaño)
        background_image = ImageTk.PhotoImage(imagen_nueva)
        button_regresar = tk.Button(
            self.root,
            image=background_image,
            command=lambda: self.volver_inicio_sesion(),
            bg=color_terciario
        )
        button_regresar.image = background_image
        button_regresar.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)
                
    



class Inicio:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.Inicio_sesion()
        pass

    def login(self, root, label_status, usuario, contraseña):
        encontrado = False
        habilitado = False
        for i in usuarios:
            for j in range(len(i[3])):
                if i[0] == usuario and i[1] == contraseña and i[3][2]:
                    habilitado = True
        for i in usuarios:
            if i[0] == usuario and i[1] == contraseña and habilitado == True:
                encontrado = True
                if i[2] == "admin":
                    for widget in root.winfo_children():
                        widget.destroy()
                    Admin(root).Ventana_Principal()
                    break
                if i[2] == "cajero":
                    label_status.config(
                        text="Inicio de sesión exitoso", fg="green", bg=color_terciario
                    )
                    break
                if i[2] == "usuario":
                    label_status.config(
                        text="Inicio de sesión exitoso", fg="green", bg=color_terciario
                    )
                    break
        if not encontrado:
            label_status.config(
                text="Usuario no existe, ¿desea registrarse?",
                fg="red",
            )

            button_frame = tk.Frame(root)
            button_frame.pack()

            button_si = tk.Button(
                button_frame,
                text="Si",
                bg=color_secundario,
                fg="black",
            )
            button_si.pack(side="left", padx=5, ipadx=10)

            button_no = tk.Button(
                button_frame,
                text="No",
                command=lambda: self.Opcion_no(),
                bg=color_secundario,
                fg="black",
            )
            button_no.pack(side="left", padx=5, ipadx=8)

            self.button_login.destroy()

    # Crear un formulario de registro similar al de crear cajero
        form_frame = tk.Frame(self.root)
        form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Título del formulario
        titulo = tk.Label(
            form_frame, text="Registro", font=("Arial", 14, "bold")
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Etiquetas y campos de entrada
        correo_label = tk.Label(
            form_frame, text="Correo:", font=("Arial", 12, "bold")
        )
        correo_label.grid(row=1, column=0, padx=5, pady=5)
        correo_entry = tk.Entry(form_frame, font=("Arial", 12))
        correo_entry.grid(row=1, column=1, padx=5, pady=5)

        contrasena_label = tk.Label(
            form_frame, text="Contraseña:", font=("Arial", 12, "bold")
        )
        contrasena_label.grid(row=2, column=0, padx=5, pady=5)
        contrasena_entry = tk.Entry(form_frame, show="*", font=("Arial", 12))
        contrasena_entry.grid(row=2, column=1, padx=5, pady=5)

        nombre_label = tk.Label(
            form_frame, text="Nombre:", font=("Arial", 12, "bold")
        )
        nombre_label.grid(row=3, column=0, padx=5, pady=5)
        nombre_entry = tk.Entry(form_frame, font=("Arial", 12))
        nombre_entry.grid(row=3, column=1, padx=5, pady=5)

        cedula_label = tk.Label(
            form_frame, text="Cédula:", font=("Arial", 12, "bold")
        )
        cedula_label.grid(row=4, column=0, padx=5, pady=5)
        cedula_entry = tk.Entry(form_frame, font=("Arial", 12))
        cedula_entry.grid(row=4, column=1, padx=5, pady=5)

        telefono_label = tk.Label(
            form_frame, text="Teléfono:", font=("Arial", 12, "bold")
        )
        telefono_label.grid(row=5, column=0, padx=5, pady=5)
        telefono_entry = tk.Entry(form_frame, font=("Arial", 12))
        telefono_entry.grid(row=5, column=1, padx=5, pady=5)

        direccion_label = tk.Label(
            form_frame, text="Dirección:", font=("Arial", 12, "bold")
        )
        direccion_label.grid(row=6, column=0, padx=5, pady=5)
        direccion_entry = tk.Entry(form_frame, font=("Arial", 12))
        direccion_entry.grid(row=6, column=1, padx=5, pady=5)

        # Botón de registro
        crear_button = tk.Button(
            form_frame,
            text="Crear",
            font=("Arial", 12),
            command=lambda: self.registrar_usuario(
                correo_entry.get(),
                contrasena_entry.get(),
                nombre_entry.get(),
                cedula_entry.get(),
                telefono_entry.get(),
                direccion_entry.get()
            
            ),
        )
        crear_button.grid(row=7, column=1, padx=5, pady=5)

        # Botón de volver
        volver_button = tk.Button(
            form_frame,
            text="Volver",
            font=("Arial", 12),
            command=lambda: self.Opcion_no()
        )
        volver_button.grid(row=7, column=0, padx=5, pady=5)

    def mostrar_ventana_principal(self):
        # Destruir los botones de registro
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        # Crear los botones de la ventana principal
        btn_nuevo_usuario = tk.Button(
            self.root,
            text="Nuevo Usuario",
            font=("Arial", 12),
            command=self.Registro
        )
        btn_nuevo_usuario.pack(pady=10)

        btn_salir = tk.Button(
            self.root,
            text="Salir",
            font=("Arial", 12),
            command=self.root.quit
        )
        btn_salir.pack()

    def registrar_usuario(self, correo, contrasena, nombre, cedula, telefono, direccion):
        if not correo or not contrasena or not nombre or not cedula or not telefono or not direccion:
            messagebox.showwarning("Campos Incompletos", "Por favor complete todos los campos.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showwarning("Correo Inválido", "Por favor ingrese un correo válido.")
            return
        if nombre == "" or cedula == "" or correo == "" or contrasena == "":
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        if not telefono.isdigit() or len(telefono) != 10:
            messagebox.showerror("Error", "Por favor, marque un número valido.")
            return

        # Verificar correo válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "El correo ingresado es inválido.")
            return

        # Verificar documento válido
        if not cedula.isdigit() or len(cedula) < 9 or len(cedula) > 10:
            messagebox.showerror("Error", "El número de documento ingresado es inválido.")
            return
        
        #Verificar duplciados de documento y correo
        for usuario in usuarios:
            if usuario[0] == correo:
                messagebox.showerror("Error", "El correo ya está en uso.")
                return
            if usuario[3][1] == cedula:
                messagebox.showerror("Error", "El número de documento ya existe.")
                return
            if len(usuario) > 3 and usuario[3][3] == telefono:
                messagebox.showerror("Error", "El telefono ya esta en uso")
                return
        usuarios.append([correo, contrasena, "usuario", [nombre, cedula, True, telefono, direccion]])
        messagebox.showinfo("Registro Exitoso", "El usuario ha sido registrado exitosamente.")
        
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Inicio_sesion()

    def Opcion_no(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Inicio_sesion()

    def Inicio_sesion(self):
        self.root.configure(bg="SystemButtonFace")
        # Cargar la imagen del icono
        # Ruta de la imagen del ícono
        icon_photo = tk.PhotoImage(file="Icono.png")

        # Establecer la imagen como icono de la ventana
        self.root.iconphoto(True, icon_photo)
        self.root.title("Inicio de sesión")
        self.root.geometry("800x600")
        # Crear la imagen de fondo
        self.image = Image.open("./Logo.png")
        self.background_image = ImageTk.PhotoImage(self.image)
        # Crear el widget Label con la imagen de fondo
        self.background_label = tk.Label(
            self.root, image=self.background_image)
        self.background_label.place(x=0, y=-150, relwidth=1, relheight=1)
        self.label_username = tk.Label(
            self.root, text="Usuario", fg="black", font=("Arial", 11, "bold")
        )
        self.label_username.pack(pady=(250, 0))
        # Entradas de texto
        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.pack(pady=5)
        self.entry_usuario.focus()
        self.label_password = tk.Label(
            self.root, text="Contraseña", fg="black", font=("Arial", 11, "bold")
        )
        self.label_password.pack()
        self.entry_contraseña = tk.Entry(self.root, show="*")
        self.entry_contraseña.pack(pady=5)
        self.label_status = tk.Label(self.root, text="", fg="black")
        self.label_status.pack(pady=5)
        # Botón
        self.button_login = tk.Button(
            self.root,
            text="Iniciar sesión",
            command=lambda: self.login(
                self.root,
                self.label_status,
                self.entry_usuario.get(),
                self.entry_contraseña.get(),
            ),
            bg=color_secundario,
            fg="black",
        )
        self.button_login.pack(ipadx=5, ipady=5)
        self.root.bind(
            "<Return>",
            lambda event: self.login(
                self.root,
                self.label_status,
                self.entry_usuario.get(),
                self.entry_contraseña.get(),
            ),
        )


main = Inicio()
main.root.mainloop()
