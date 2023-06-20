import tkinter as tk
import tkinter.simpledialog
from tkinter import ttk
import re
import datetime
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Menu
import datetime

lista = []
filas = []  # pedidos_ pendientes
pedidos_aceptados = []  # pedidos_entregar

facturas_pendientes = []  # pedidos_pendientes
facutras_entregar = []  # pedidos_entregar

facturas = []

productos_dobles = ["Vaso Doble", "Cono Doble", "Copa infantil fiesta", "Copa infantil Chips", "Banana split", "Ensalada de frutas personal",
                    "Ensalada de frutas con helado"]  # ignora esta wea

productos_Triples = ["Vaso Triple", "Super cono", "Mega cono", "Copa infantil piñata", "Copa exotica",
                     "Copa De la casa", "Copa peach melba", "Copa Tropical", "Copa caramelo", "Ron o amaretto", "Sunday"]  # ignora esta wea

sabores = ["maracuya en agua", "tropical de agua", "chicle", "frutos rojos", "arequipe", "nata", "crocante", "maracuya en leche", "cereza", "fresa", "vainilla chips",
           "brownie", "galleta oreo", "leche klim", "chocolate", "MyM", "queso", "vainilla", "ron con pasas", "nucita", "stracciatella"]  # ignore tambien esta wea


pending_orders = []
entregar_orders = []


categories = {
    "Vasos": [
        {
            "title": "Vaso Sencillo",
            "image_path": "./vasos1.png",
            "description": "Delicioso vaso de helado con 1 bola",
            "price": "$5,500"
        },
        {
            "title": "Vaso Doble",
            "image_path": "./vasos2.png",
            "description": "Delicioso vaso de helado con 2 bolas",
            "price": "$8,400"
        },
        {
            "title": "Vaso Triple",
            "image_path": "./vasos3.png",
            "description": "Delicioso vaso de helado con 3 bolas",
            "price": "$10,800"
        }

    ], "Conos": [
        {
            "title": "Cono pequeño ",
            "image_path": "./HeladoP.png",
            "description": "Delicioso cono de helado con 1 bola pequeña",
            "price": "$4,200"
        },
        {
            "title": "Cono mediano ",
            "image_path": "./HeladoM.png",
            "description": "Delicioso cono de helado con 1 bola mediana",
            "price": "$5,500"

        },
        {
            "title": "Cono Doble ",
            "image_path": "./HeladoD.png",
            "description": "Delicioso cono de helado con 2 bolas ",
            "price": "$8,400"

        },
        {
            "title": "Super cono ",
            "image_path": "./SuperCono.png",
            "description": "Delicioso cono de helado con 3 bolas con barquillo",
            "price": "$10,800"

        },
        {
            "title": "Mega cono ",
            "image_path": "./MegaCono.png",
            "description": "Sorprendente cono de helado con 4 bolas con barquillo y galleta",
            "price": "$14,000"

        }
    ], "Granizados": [{
        "title": "Granizado 12 onz",
        "image_path": "./Granizado12.png",
        "description": "Granizado refrescante de 12 onz",
        "price": "6,400"
    },
        {
            "title": "Granizado 16 onz",
            "image_path": "./Granizado16.png",
            "description": "Granizado refrescante de 12 onz",
            "price": "$8,400"
    }
    ], "Salpicon/copa chocolate": [{
        "title": "Salpicon",
        "image_path": "./Salpicon.png",
        "description": "Tropical salpicon con helado con frutas frescas",
        "price": "$9,000"
    },
        {
            "title": "Copa chocolate",
            "image_path": "./CopaChocolate.png",
            "description": "clasica copa de helado con chocolate ",
            "price": "$5,000"
    }
    ], "Copas infantiles": [{
        "title": "Copa infantil Mickey",
        "image_path": "./Mickey.png",
        "description": "Divertido helado con forma de mickey",
        "price": "$6,400"
    },
        {
            "title": "Copa infantil piñata",
            "image_path": "./Piñata.png",
            "description": "Divertido helado perfecto para los cumpleaños con gorro incluido",
            "price": "$10,800"
    },
        {
            "title": "Copa infantil fiesta",
            "image_path": "./CopaFiesta.png",
            "description": "Helado Listo si quieres salir de fiesta ",
            "price": "$8,800"
    },
        {
            "title": "Copa infantil Chips",
            "image_path": "./Chips.png",
            "description": "Helado casual con chispas de chocolate",
            "price": "$8,800"
    }

    ], "Malteada": [{
        "title": "Malteada 12 Onz",
        "image_path": "./Malteadap.png",
        "description": "Deliciosa malteada de 12 onz",
        "price": "$10,000"
    },
        {
            "title": "Malteada 16 Onz",
            "image_path": "./Malteadag.png",
            "description": "Deliciosa malteada de 16z onz",
            "price": "$12,000"
    }
    ], "Fresas": [{
        "title": "Fresas Con crema",
        "image_path": "./FresasC.png",
        "description": "Fresas dulces con crema",
        "price": "$11,400"
    },
        {
            "title": "Fresa Con helado ",
            "image_path": "./FresasH.png",
            "description": "Fresas dulces con helado ",
            "price": "$13,200"
    }
    ], "Banana split/ Brownie con helado": [{
        "title": "Brownie con helado",
        "image_path": "./Brownie.png",
        "description": "Dulce brownie con helado para disfrutar",
        "price": "$10,200"
    },
        {
            "title": "Banana split",
            "image_path": "./bananasplit.png",
            "description": "Delicioso barco de banana con helado",
            "price": "$13,200"
    }
    ], "Ensalada de frutas": [{
        "title": "Ensalada de frutas personal",
        "image_path": "./Ensalada.png",
        "description": "Tropical pequeña ensalada de frutas con helado",
        "price": "$10,800"
    },
        {
        "title": "Ensalada de frutas con helado",
        "image_path": "./EnsaladaGH.png",
        "description": "Tropical ensalada de frutas con helado",
        "price": "$14,500"
    }, {
            "title": "Ensalada de sin helado",
            "image_path": "./EnsaladaG.png",
            "description": "Tropical ensalada de frutas ",
            "price": "$10,200"
    },
    ], "Copas": [{
        "title": "Copa exotica",
        "image_path": "./CopasExotica.png",
        "description": "Copa con un toque exotico ",
        "price": "$10,800"
    },
        {
            "title": "Sundae",
            "image_path": "./copasundae.png",
            "description": "Copa perfecta para el medio dia con añadicion de galleta ",
            "price": "$10,800"
    }, {
            "title": "Ron o amaretto",
            "image_path": "./Coparon.png",
            "description": "Copa con un toque ron pa los que les gusta el alcohol  ",
            "price": "$10,800"
    },
        {
            "title": "Copa caramelo",
            "image_path": "./Copacaramelo.png",
            "description": "Copa con salsa de caramelo ",
            "price": "$10,800"
    },
        {
            "title": "Copa Tropical",
            "image_path": "./copatropical.png",
            "description": "Copa con salsa de fresa ",
            "price": "$10,800"
    },
        {
            "title": "Copa peach melba",
            "image_path": "./peachmelba.png",
            "description": "Copa con duraznos en una cama de galleta y helado ",
            "price": "$10,800"
    },
        {
            "title": "Copa De la casa",
            "image_path": "./copacasa.png",
            "description": "Recomendado por nosotros la copa de la casa con doble racion de crema chantilly ",
            "price": "$10,800"
    },

    ], "Litro de helado": [{
        "title": "litro de helado ",
        "image_path": "Litro de Helado.png",
        "description": "Por si te quedas con los antojos, lleva tu litro de helado.",
        "price": "$27,000"
    }
    ], "Paletas": [{
        "title": "Leche Klym ",
        "image_path": "./Paletalecheklim.png",
        "description": "Deliciosa paleta con sabor a Leche Klym.",
        "price": "$6,000"
    },
        {
        "title": "Maracuya ",
        "image_path": "./Paletamaracuya.png",
        "description": "Deliciosa paleta con sabor a maracuya.",
        "price": "$6,000"
    },
        {
        "title": "Fresas con Chocolate ",
        "image_path": "./Paletafresasc.png",
        "description": "Deliciosa paleta con sabor a fresas y chocolate.",
        "price": "$6,000"
    },
        {
        "title": "MYM ",
        "image_path": "./paletamym.png",
        "description": "Deliciosa paleta con sabor a MyM.",
        "price": "$6,000"
    },
        {
        "title": "Chantilly",
        "image_path": "./Paletachantilly.png",
        "description": "Deliciosa paleta con sabor a chantilly.",
        "price": "$6,000"
    },
        {
        "title": "Ron con Pasas ",
        "image_path": "./Paletasron.png",
        "description": "Deliciosa paleta con sabor a Ron con Pasas.",
        "price": "$6,000"
    },
        {
        "title": "Nucita ",
        "image_path": "./Paletanucita.png",
        "description": "Deliciosa paleta con sabor a Nucita.",
        "price": "$6,000"
    },
        {
        "title": "Frutos Rojos ",
        "image_path": "./paletafrutosrojos.png",
        "description": "Deliciosa paleta con sabor a Leche Klym.",
        "price": "$6,000"
    },
        {
        "title": "Chocomani ",
        "image_path": "./paletaChocomany.png",
        "description": "Deliciosa paleta con sabor a chocolate con mani.",
        "price": "$6,000"
    },
        {
        "title": "Oreo ",
        "image_path": "./Paletaoreo.png",
        "description": "Deliciosa paleta con sabor a oreo.",
        "price": "$6,000"
    },
        {
        "title": "Chocolate ",
        "image_path": "./paletachocolate.png",
        "description": "Deliciosa paleta con sabor a chocolate.",
        "price": "$6,000"
    },
        {
        "title": "Queso ",
        "image_path": "./paletaqueso.png",
        "description": "Deliciosa paleta con sabor a queso.",
        "price": "$6,000"
    }
    ]
}

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
        "cajero1@email.com",
        "21/03/2023",
        {
            "tamaño": "para compartir sin helado",
            "sabor": ["Ensalada de frutas sin helado"],
            "precio": 10200,
        },
        "caja",
        {"Total": 10200},
    ],
    [
        2,
        "Andres",
        "26/03/2023",
        {
            "tamaño": "Fresas con helado",
            "sabor": ["vainilla chips"],
            "precio": 8400,
        },
        "caja",
        {"Total": 8400},
    ],
    [
        3,
        "Felipe",
        "21/03/2023",
        {
            "tamaño": "Granizado 16 onz",
            "sabor": ["fresa"],
            "precio": 8400,
        },
        "online",
        {"Total": 8400},
    ],
    [
        4,
        "Felipe",
        "12/01/2023",
        {
            "tamaño": "Banana split",
            "sabor": ["fresa", "ron con pasas"],
            "precio": 13200,
        },
        "onlinecaja",
        {"Total": 13200},
    ],
    [
        5,
        "Felipe",
        "10/04/2023",
        {
            "tamaño": "Banana split",
            "sabor": ["fresa", "ron con pasas"],
            "precio": 13200,
        },
        "caja",
        {"Total": 13200},
    ],
    [
        6,
        "Andres",
        "12/08/2019",
        {
            "tamaño": "para compartir con helado",
            "sabor": ["vainilla chips", "tropical de agua"],
            "precio": 14500,
        },
        "online",
        {"Total": 14500},
    ],
    [
        7,
        "Andres",
        "12/08/2019",
        {
            "tamaño": "para compartir con helado",
            "sabor": ["vainilla chips", "tropical de agua"],
            "precio": 14500,
        },
        "caja",
        {"Total": 14500},
    ],
    [
        8,
        "Tomas",
        "12/03/2021",
        [
            {
                "tamaño": "Doble",
                "sabor": ["vainilla chips", "cereza"],
                "precio": 8400,
            },
            {
                "tamaño": "Litro de helado",
                "sabor": ["vainilla chips"],
                "precio": 27000,
            },
        ],
        "caja",
        {"Total": 35400},
    ],
    [
        9,
        "Andres",
        "19/04/2022",
        {
            "tamaño": "Fiesta",
            "sabor": ["maracuya en leche", "nata"],
            "precio": 8800,
        },
        "online",
        {"Total": 8800},
    ],
    [
        10,
        "Felipe",
        "18/02/2023",
        {
            "tamaño": "Malteada 12 onz",
            "sabor": ["maracuya en leche"],
            "precio": 6400,
        },
        "onlinecaja",
        {"Total": 6400},
    ],
    [
        11,
        "Tomas",
        "25/03/2023",
        {
            "tamaño": "Banana split",
            "sabor": ["frutos rojos", "chicle"],
            "precio": 13200,
        },
        "caja",
        {"Total": 13200},
    ],
    [
        12,
        "Tomas",
        "01/01/2021",
        {
            "tamaño": "piñata",
            "sabor": ["crocante"],
            "precio": 10800,
        },
        "online",
        {"Total": 10800},
    ],
    [
        13,
        "Tomas",
        "06/04/2022",
        {
            "tamaño": "Granizado 16 onz",
            "sabor": ["fresa"],
            "precio": 8400,
        },
        "caja",
        {"Total": 8400},
    ],
    [
        14,
        "Felipe",
        "30/04/2022",
        {
            "tamaño": "para compartir con helado",
            "sabor": ["tropical de agua", "maracuya en agua"],
            "precio": 14500,
        },
        "online",
        {"Total": 14500},
    ],
    [
        15,
        "Andres",
        "12/02/2023",
        {
            "tamaño": "Doble",
            "sabor": ["maracuya en agua", "tropical de agua"],
            "precio": 8400,
        },
        "onlinecaja",
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
id=len(facturas)+1

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
        productos_menu.add_command(
            label="Ver Productos", command=self.Productos)
        productos_menu.add_command(
            label="Agregar Productos", command=self.AgregarProductos
        )

        # Agregar opción de "Ver Facturas"
        facturas_menu = tk.Menu(barra, tearoff=0)
        facturas_menu.add_command(
            label="Ver Facturas", command=self.VerFacturas)
        facturas_menu.add_command(
            label="Ver Facturas por Fecha", command=self.VerFacturasPorFecha
        )
        facturas_menu.add_command(
            label="Ver Facturas por Cajero", command=self.VerFacturasPorCajero
        )

        barra.add_cascade(label="Cajero", menu=cajero_menu)
        barra.add_cascade(label="Productos", menu=productos_menu)
        barra.add_cascade(label="Facturas", menu=facturas_menu)

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
            table_frame,
            text="Documento",
            font=("Arial", 12, "bold"),
            bg=color_terciario,
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
                fg="white",
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
        # Destruir la tabla de cajeros si ya existe
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
        if (
            not numero_documento.isdigit()
            or len(numero_documento) < 9
            or len(numero_documento) > 10
        ):
            messagebox.showerror(
                "Error", "El número de documento ingresado es inválido."
            )
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

        nuevo_cajero = [
            correo,
            contrasena,
            "cajero",
            [nombre, numero_documento, True, "", ""],
        ]
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
        # Destruir la tabla de cajeros si ya existe
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
                cajero,
                nombre_entry.get(),
                numero_doc_entry.get(),
                correo_entry.get(),
                contrasena_entry.get(),
            ),
        )
        actualizar_cajero_button.grid(row=5, column=0, columnspan=2, pady=10)

    def actualizar_cajero(self, cajero, nombre, numero_documento, correo, contrasena):
        # Verificar campos vacíos
        if nombre == "" or numero_documento == "" or correo == "" or contrasena == "":
            messagebox.showerror(
                "Error", "Por favor, complete todos los campos.")
            return

        # Verificar correo válido}
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", correo):
            messagebox.showerror("Error", "El correo ingresado es inválido.")
            return

        # Verificar documento válido
        if (
            not numero_documento.isdigit()
            or len(numero_documento) < 9
            or len(numero_documento) > 10
        ):
            messagebox.showerror(
                "Error", "El número de documento ingresado es inválido."
            )
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
        cajero[3][1] = numero_documento

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Cajero actualizado correctamente.")

        # Destruir el formulario de editar cajero y recrear la tabla de cajeros
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
        self.Cajeros()

    def Productos(self):
        # Destruir el formulario de agregar producto si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()

        self.herramientas()

        # Crear un frame para contener la tabla de productos
        table_frame = tk.Frame(
            self.root, bg=color_terciario, bd=1, relief=tk.SOLID)
        table_frame.pack(padx=20, pady=20)

        # Título de la tabla
        titulo = tk.Label(
            table_frame,
            text="Productos",
            font=("Arial", 14, "bold"),
            bg=color_terciario,
        )
        titulo.grid(row=0, column=0, columnspan=5, pady=10)

        # Crear un frame para contener los encabezados de las columnas
        header_frame = tk.Frame(table_frame, bg=color_terciario)
        header_frame.grid(row=1, column=0, columnspan=5, sticky="nsew")

        # Encabezados de las columnas
        headers = ["Imagen", "Producto", "Descripción", "Precio", "Acciones"]
        for index, header in enumerate(headers):
            label = tk.Label(
                header_frame,
                text=header,
                font=("Arial", 12, "bold"),
                bg=color_terciario,
            )
            label.grid(row=0, column=index, padx=30, pady=5)

        # Crear un canvas para el desplazamiento vertical
        canvas = tk.Canvas(
            table_frame, bg=color_terciario, bd=0, highlightthickness=0, relief=tk.SOLID
        )
        canvas.grid(row=2, column=0, columnspan=5, sticky="nsew")

        # Crear un scrollbar para el canvas
        scrollbar = tk.Scrollbar(
            table_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.grid(row=2, column=5, sticky="ns")

        # Configurar el canvas para usar el scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>", lambda e: canvas.configure(
                scrollregion=canvas.bbox("all"))
        )

        # Crear un frame dentro del canvas para contener los elementos de la tabla
        content_frame = tk.Frame(canvas, bg=color_terciario)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        if not any(
            categories.values()
        ):  # Verificar si no hay productos en ninguna categoría
            # Mostrar mensaje de que no hay productos disponibles
            no_products_label = tk.Label(
                content_frame,
                text="No hay productos disponibles",
                font=("Arial", 12, "bold"),
                bg=color_terciario,
                justify="center",
                width=50,
            )
            no_products_label.pack(pady=10, padx=(10, 0))
        else:
            # Mostrar datos de los productos en la tabla
            row_index = 0  # Índice de fila inicial para mostrar los productos
            for category, products in categories.items():
                if products:  # Verificar si la categoría tiene productos asociados
                    # Mostrar el nombre de la categoría en una fila separada
                    category_label = tk.Label(
                        content_frame,
                        text=category,
                        font=("Arial", 12, "bold"),
                        bg=color_terciario,
                    )
                    category_label.grid(
                        row=row_index, column=0, columnspan=5, pady=(10, 5)
                    )
                    row_index += 1

                    for index, product in enumerate(products):
                        # Mostrar la imagen en la primera columna
                        image_path = product["image_path"]
                        image = Image.open(image_path)
                        image = image.resize((100, 100))
                        image_tk = ImageTk.PhotoImage(image)
                        image_label = tk.Label(
                            content_frame, image=image_tk, bg=color_terciario
                        )
                        image_label.image = image_tk
                        image_label.grid(
                            row=row_index, column=0, padx=5, pady=5)

                        # Mostrar información de cada producto en las columnas restantes
                        product_data = [
                            product["title"],
                            product["description"],
                            product["price"],
                        ]
                        for column_index, data in enumerate(product_data, start=1):
                            if column_index == 2:  # Descripción del producto
                                if (
                                    len(data) > 100
                                ):  # Verificar si la descripción supera el ancho máximo
                                    data = (
                                        data[:100] + "..."
                                    )  # Cortar el texto y agregar los 3 puntos al final

                                data_label = tk.Label(
                                    content_frame,
                                    text=data,
                                    bg=color_terciario,
                                    wraplength=140,  # Ancho máximo del texto
                                    justify="left",  # Alinear el texto a la izquierda
                                )
                                data_label.grid(
                                    row=row_index, column=column_index, padx=10, pady=5
                                )
                            else:
                                data_label = tk.Label(
                                    content_frame, text=data, bg=color_terciario
                                )
                                data_label.grid(
                                    row=row_index, column=column_index, padx=10, pady=5
                                )

                        # Agregar botones de eliminar y editar en la última columna
                        delete_button = tk.Button(
                            content_frame,
                            text="Eliminar",
                            bg="red",
                            fg="white",
                            command=lambda category=category, index=index: self.eliminar_producto(
                                category, index
                            ),
                        )
                        delete_button.grid(
                            row=row_index, column=4, padx=5, pady=5)

                        edit_button = tk.Button(
                            content_frame,
                            text="Editar",
                            bg="yellow",
                            command=lambda category=category, index=index: self.editar_producto(
                                category, index
                            ),
                        )
                        edit_button.grid(
                            row=row_index, column=5, padx=5, pady=5)

                        row_index += 1
                else:
                    continue

        # Configurar el desplazamiento del canvas
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Configurar el tamaño del contenido en el canvas
        content_frame.update_idletasks()
        canvas.configure(width=content_frame.winfo_width(), height=400)

        # Centrar la tabla en la pantalla
        table_frame.pack(padx=20, pady=0)

    def eliminar_producto(self, category, index):
        # Ajustar el índice para tener en cuenta las categorías y productos anteriores
        row_index = 2  # Índice de fila inicial de los productos

        for cat, prods in categories.items():
            if cat == category:
                # Encontrar el índice de fila correcto para el producto en la categoría actual
                row_index += index
                break
            # +1 para contar la fila de nombre de categoría
            row_index += len(prods) + 1

        # Eliminar el producto del arreglo de categorías
        categories[category].pop(index)

        # Destruir la tabla existente y volver a construirla
        self.Productos()

    def editar_producto(self, category, index):
        # Obtener el producto que se desea editar
        product = categories[category][index]

        # Crear una nueva ventana para el formulario de edición
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar Producto")
        edit_window.configure(bg=color_principal)
        edit_window.grab_set()

        # Obtener la imagen del producto
        image_path = product["image_path"]
        image = Image.open(image_path)
        image = image.resize((100, 100))
        image_tk = ImageTk.PhotoImage(image)

        # Crear un Label para mostrar la imagen del producto
        image_label = tk.Label(edit_window, image=image_tk)
        image_label.image = image_tk
        image_label.pack(side="left", padx=10, pady=10)

        # Crear un formulario de edición dentro de la ventana
        form_frame = tk.Frame(edit_window, bg=color_principal)
        form_frame.pack(padx=20, pady=20)

        # Título de la ventana de edición
        titulo = tk.Label(
            form_frame,
            text="Editar Producto",
            font=("Arial", 14, "bold"),
            bg=color_principal,
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Etiquetas y campos de entrada para editar los datos del producto
        title_label = tk.Label(
            form_frame, text="Producto:", bg=color_principal)
        title_label.grid(row=1, column=0, pady=5)
        title_entry = tk.Entry(form_frame, width=30)
        title_entry.grid(row=1, column=1, pady=5)
        title_entry.insert(0, product["title"])

        description_label = tk.Label(
            form_frame, text="Descripción:", bg=color_principal
        )
        description_label.grid(row=2, column=0, pady=5)
        description_entry = tk.Entry(form_frame, width=30)
        description_entry.grid(row=2, column=1, pady=5)
        description_entry.insert(0, product["description"])

        price_label = tk.Label(form_frame, text="Precio:", bg=color_principal)
        price_label.grid(row=3, column=0, pady=5)
        price_entry = tk.Entry(form_frame, width=30)
        price_entry.grid(row=3, column=1, pady=5)
        price_entry.insert(
            0, re.sub(r"\D", "", product["price"])
        )  # Eliminar cualquier carácter no numérico del precio

        # Función para guardar los cambios realizados en el formulario
        def guardar_cambios():
            # Obtener los valores actualizados del formulario
            updated_title = title_entry.get()
            updated_description = description_entry.get()
            updated_price = re.sub(
                r"\D", "", price_entry.get()
            )  # Eliminar cualquier carácter no numérico del precio

            # Agregar el símbolo "$" al inicio del precio actualizado
            updated_price = f"${updated_price}"

            # Actualizar los datos del producto en el arreglo de categorías
            categories[category][index]["title"] = updated_title
            categories[category][index]["description"] = updated_description
            categories[category][index]["price"] = updated_price

            # Cerrar la ventana de edición
            edit_window.destroy()

            # Actualizar la vista de la tabla de productos
            self.Productos()

        # Función para validar que solo se ingresen números en el campo de precio
        def validate_price_entry(text):
            return re.match(r"^\d*$", text) is not None

        # Configurar validación de entrada para el campo de precio
        vcmd = (edit_window.register(validate_price_entry), "%P")
        price_entry.configure(validate="key", validatecommand=vcmd)

        # Botón para guardar los cambios
        save_button = tk.Button(
            form_frame,
            text="Guardar Cambios",
            bg=color_secundario,
            fg="black",
            command=guardar_cambios,
        )
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def AgregarProductos(self):
        # Destruir el formulario de agregar producto si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()

        self.herramientas()

        # Crear el formulario para agregar productos
        form_frame = tk.Frame(self.root, bg=color_terciario, relief=tk.SOLID)
        form_frame.pack(padx=10, pady=(100, 10), ipady=10)

        # Título del formulario
        titulo = tk.Label(
            form_frame,
            text="Agregar Productos",
            font=("Arial", 14, "bold"),
            bg=color_terciario,
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Función para mostrar el formulario de nueva categoría
        def mostrar_formulario_nueva_categoria():
            # Destruir el formulario anterior si existe
            if hasattr(self, "form_frame_content"):
                self.form_frame_content.destroy()

            # Crear el formulario para la nueva categoría
            self.form_frame_content = tk.Frame(
                self.root, bg=color_terciario, bd=1, relief=tk.SOLID
            )
            self.form_frame_content.pack(pady=(50), ipadx=10, ipady=10)

            # Campo de entrada para el nombre de la categoría nueva
            label_new_category = tk.Label(
                self.form_frame_content, text="Nombre de categoría:"
            )
            label_new_category.config(bg=color_terciario)
            label_new_category.grid(
                row=0, column=0, sticky=tk.E, padx=10, pady=10)

            entry_new_category = tk.Entry(self.form_frame_content)
            entry_new_category.grid(row=0, column=1)

            # Función para agregar la nueva categoría
            def agregar_categoria_nueva():
                nueva_categoria = entry_new_category.get().strip()
                if nueva_categoria:
                    categories[nueva_categoria] = []
                    messagebox.showinfo(
                        "Éxito", "Categoría agregada correctamente.")
                    entry_new_category.delete(0, tk.END)
                else:
                    messagebox.showerror(
                        "Error", "Por favor, ingrese el nombre de la categoría nueva."
                    )

            # Botón para agregar la categoría nueva
            btn_add_category = tk.Button(
                self.form_frame_content,
                text="Agregar Categoría",
                command=agregar_categoria_nueva,
                bg=color_principal,
            )
            btn_add_category.grid(row=1, column=0, columnspan=2, pady=10)

        # Función para mostrar el formulario de categoría existente
        def mostrar_formulario_categoria_existente():
            # Destruir el formulario anterior si existe
            if hasattr(self, "form_frame_content"):
                self.form_frame_content.destroy()

            # Crear el formulario para la categoría existente
            self.form_frame_content = tk.Frame(
                self.root, bg=color_terciario, bd=1, relief=tk.SOLID
            )
            self.form_frame_content.pack(pady=(50), ipadx=10, ipady=10)

            # Campo de selección de categoría existente
            label_category = tk.Label(
                self.form_frame_content, text="Categoría existente:", bg=color_terciario
            )
            label_category.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)

            categories_list = list(categories.keys())
            selected_category = tk.StringVar(self.form_frame_content)
            selected_category.set(categories_list[0])

            combo_category = tk.OptionMenu(
                self.form_frame_content, selected_category, *categories_list
            )
            combo_category.grid(row=0, column=1, padx=10, pady=10)

            label_title = tk.Label(
                self.form_frame_content, text="Título:", bg=color_terciario
            )
            label_title.grid(row=1, column=0, sticky=tk.E, pady=2)

            entry_title = tk.Entry(self.form_frame_content)
            entry_title.grid(row=1, column=1)

            label_description = tk.Label(
                self.form_frame_content, text="Descripción:", bg=color_terciario
            )
            label_description.grid(row=2, column=0, sticky=tk.E, pady=2)

            entry_description = tk.Entry(self.form_frame_content)
            entry_description.grid(row=2, column=1)

            label_price = tk.Label(
                self.form_frame_content, text="Precio:", bg=color_terciario
            )
            label_price.grid(row=3, column=0, sticky=tk.E, pady=2)

            entry_price = tk.Entry(self.form_frame_content)
            entry_price.grid(row=3, column=1)

            # Función para agregar el producto al arreglo de categorías
            def agregar_producto():
                categoria_seleccionada = selected_category.get()
                if categoria_seleccionada:
                    title = entry_title.get().strip()
                    description = entry_description.get().strip()
                    price = entry_price.get().strip()

                    if not title or not description or not price:
                        messagebox.showerror(
                            "Error", "Por favor, complete todos los campos."
                        )
                        return

                    # Validar el formato del precio
                    if not price.isnumeric():
                        messagebox.showerror(
                            "Error", "Por favor, ingrese un precio válido."
                        )
                        return

                    price = "${:,.0f}".format(int(price))

                    producto = {
                        "title": title,
                        "image_path": "./Cono.png",
                        "description": description,
                        "price": price,
                    }
                    categories[categoria_seleccionada].append(producto)
                    messagebox.showinfo(
                        "Éxito", "Producto agregado correctamente.")
                    entry_title.delete(0, tk.END)
                    entry_description.delete(0, tk.END)
                    entry_price.delete(0, tk.END)
                else:
                    messagebox.showerror(
                        "Error", "Por favor, seleccione una categoría existente."
                    )

            # Botón para agregar el producto
            btn_add_product = tk.Button(
                self.form_frame_content,
                text="Agregar Producto",
                command=agregar_producto,
                bg=color_principal,
            )
            btn_add_product.grid(row=4, column=0, columnspan=2, pady=10)

        # Botones para seleccionar categoría nueva o existente
        btn_nueva_categoria = tk.Button(
            form_frame,
            text="Crear categoría nueva",
            command=mostrar_formulario_nueva_categoria,
        )
        btn_nueva_categoria.grid(row=1, column=0, padx=5)

        btn_existente_categoria = tk.Button(
            form_frame,
            text="Usar categoría existente",
            command=mostrar_formulario_categoria_existente,
        )
        btn_existente_categoria.grid(row=1, column=1, padx=5)

    def VerFacturas(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()

        self.herramientas()
        # Crear la tabla de facturas dentro de un widget Canvas
        canvas = tk.Canvas(
            self.root, bg=color_terciario, highlightbackground=color_terciario
        )
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=60, pady=20)

        # Crear un scrollbar y asociarlo al widget Canvas
        scrollbar = tk.Scrollbar(
            self.root, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configurar el scrollbar para que controle el widget Canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>", lambda e: canvas.configure(
                scrollregion=canvas.bbox("all"))
        )

        # Crear un frame dentro del widget Canvas para contener la tabla
        table_frame = tk.Frame(
            canvas,
            bg=color_terciario,
            highlightbackground="black",
            highlightthickness=1,
        )
        canvas.create_window((30, 0), window=table_frame, anchor=tk.NW)

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

        total_label = tk.Label(
            table_frame, text="Total", font=("Arial", 12, "bold"), bg=color_terciario
        )
        total_label.grid(row=1, column=4, padx=(20, 10), pady=5)

        detalles_label = tk.Label(
            table_frame, text="Detalles", font=("Arial", 12, "bold"), bg=color_terciario
        )
        detalles_label.grid(row=1, column=5, padx=(20, 10), pady=5)

        # Mostrar datos de las facturas en la tabla
        for i, factura in enumerate(facturas, start=2):
            factura_id = factura[0]
            correo = factura[1]
            fecha = factura[2]
            detalles = factura[3]
            total = factura[5]["Total"]

            id_label = tk.Label(
                table_frame, text=factura_id, bg=color_terciario)
            id_label.grid(row=i, column=0, padx=(20, 10), pady=5)

            correo_label = tk.Label(
                table_frame, text=correo, bg=color_terciario)
            correo_label.grid(row=i, column=1, padx=(20, 10), pady=5)

            fecha_label = tk.Label(table_frame, text=fecha, bg=color_terciario)
            fecha_label.grid(row=i, column=2, padx=(20, 10), pady=5)

            total_label = tk.Label(table_frame, text=total, bg=color_terciario)
            total_label.grid(row=i, column=4, padx=(20, 10), pady=5)

            detalles_label = tk.Button(
                table_frame,
                text="Mirar detalles",
                bg="yellow",
                command=lambda detalles1=detalles: self.mostrar_detalles(
                    detalles1),
            )
            detalles_label.grid(row=i, column=5, padx=(20, 10), pady=5)

        # Mostrar datos de las facturas en la tabla
        # ...

        # Puedes implementar la lógica para mostrar las facturas en la tabla según tus necesidades

    def mostrar_detalles(self, detalles1):
        ventana_hija = tk.Toplevel(self.root)
        ventana_hija.title("Detalles de la Factura")

        # Configurar el estilo de la ventana hija
        ventana_hija.configure(bg=color_terciario)
        ventana_hija.geometry("600x400")
        icon_photo = tk.PhotoImage(file="Icono.png")
        # Establecer la imagen como icono de la ventana
        ventana_hija.iconphoto(False, icon_photo)

        # Hacer que la ventana hija sea modal
        ventana_hija.grab_set()

        # Etiqueta de título
        titulo_label = tk.Label(
            ventana_hija,
            text="Detalles de las Facturas",
            font=("Arial", 14, "bold"),
            bg=color_terciario,
        )
        titulo_label.pack(pady=10)

        # Crear el árbol de la tabla
        tabla = ttk.Treeview(ventana_hija, height=10)
        tabla.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Configurar columnas
        tabla["columns"] = ("Tamaño", "Sabores", "Precio")

        # Formatear los encabezados de columna
        tabla.heading("Tamaño", text="Tamaño")
        tabla.heading("Sabores", text="Sabores")
        tabla.heading("Precio", text="Precio")

        # Ajustar el ancho de las columnas
        tabla.column("Tamaño", width=120)
        tabla.column("Sabores", width=150)
        tabla.column("Precio", width=50)

        # Ajustar el alto de las filas
        tabla["show"] = "headings"
        tabla.configure(style="Treeview")

        # Mostrar los detalles de la factura en la tabla
        if isinstance(detalles1, dict):
            # Caso en que detalles1 es un diccionario
            tamaño = detalles1["tamaño"]
            sabores = ", ".join(detalles1["sabor"])
            precio = detalles1["precio"]
            tabla.insert("", "end", values=(tamaño, sabores, precio))
        elif isinstance(detalles1, list):
            # Caso en que detalles1 es una lista de diccionarios
            for detalle in detalles1:
                tamaño = detalle["tamaño"]
                sabores = ", ".join(detalle["sabor"])
                precio = detalle["precio"]
                tabla.insert("", "end", values=(tamaño, sabores, precio))

        # Configurar scrollbar para la tabla
        scrollbar = ttk.Scrollbar(
            ventana_hija, orient="vertical", command=tabla.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tabla.configure(yscrollcommand=scrollbar.set)

        # Centrar el texto en las celdas de la tabla
        for column in tabla["columns"]:
            tabla.column(column, anchor="center")

        # Botón de cierre de la ventana hija
        cerrar_boton = tk.Button(
            ventana_hija,
            text="Cerrar",
            command=ventana_hija.destroy,
            font=("Arial", 12),
        )
        cerrar_boton.pack(pady=10)

        self.root.wait_window(ventana_hija)

    def VerFacturasPorFecha(self):
        # Destruir la tabla de cajeros si ya existe
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
            form_frame,
            text="Fecha (DD/MM/AAAA):",
            font=("Arial", 12),
            bg=color_terciario,
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
        self.root.bind(
            "<Return>", lambda event: self.buscar_facturas_por_fecha(
                fecha_entry.get())
        )

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

        # Crear una nueva ventana para mostrar las facturas
        ventana_facturas = tk.Toplevel(self.root)
        ventana_facturas.title("Facturas por Fecha")
        ventana_facturas.configure(bg=color_terciario)

        icon_photo = tk.PhotoImage(file="Icono.png")
        # Establecer la imagen como icono de la ventana
        ventana_facturas.iconphoto(False, icon_photo)
        # Hacer que la ventana hija sea modal
        ventana_facturas.grab_set()

        # Crear el marco de la tabla de facturas
        table_frame = tk.Frame(
            ventana_facturas, bg=color_terciario, bd=1, relief=tk.SOLID
        )
        table_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

        # Título de la tabla
        titulo = tk.Label(
            table_frame,
            text="Facturas por Fecha",
            font=("Arial", 14, "bold"),
            bg=color_terciario,
        )
        titulo.grid(row=0, column=0, columnspan=5, pady=10)

        # Encabezados de las columnas
        headers = ["ID", "Cliente", "Fecha", "Detalles", "Tipo Pago", "Total"]
        for col, header in enumerate(headers):
            label = tk.Label(
                table_frame, text=header, font=("Arial", 12, "bold"), bg=color_terciario
            )
            label.grid(row=1, column=col, padx=5, pady=5)

        # Mostrar las facturas en la tabla
        for col, header in enumerate(headers):
            table_frame.grid_columnconfigure(col, weight=1)

        for row, factura in enumerate(facturas_filtradas, start=2):
            for col, value in enumerate(factura):
                if col == 3:  # Columna de detalles
                    detalles_button = tk.Button(
                        table_frame,
                        text="Ver Detalles",
                        command=lambda detalles1=factura[3]: self.mostrar_detalles(
                            detalles1
                        ),
                        font=("Arial", 10),
                        bg="yellow",
                    )
                    detalles_button.grid(
                        row=row, column=col, padx=5, pady=5, sticky="nsew"
                    )
                elif col == 5:  # Columna de Total
                    label = tk.Label(
                        table_frame,
                        text=value["Total"],
                        font=("Arial", 12),
                        bg=color_terciario,
                    )
                    label.grid(row=row, column=col, padx=5,
                               pady=5, sticky="nsew")
                else:
                    label = tk.Label(
                        table_frame, text=value, font=("Arial", 12), bg=color_terciario
                    )
                    label.grid(row=row, column=col, padx=5,
                               pady=5, sticky="nsew")

        self.root.wait_window(ventana_facturas)

    def VerFacturasPorCajero(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.herramientas()

        # Crear un Frame para contener los elementos de la interfaz
        frame = tk.Frame(self.root, bg=color_terciario)
        frame.pack(padx=20, pady=20)

        # Crear el título "Buscar facturas por cajero"
        titulo_label = tk.Label(frame, text="Buscar facturas por cajero", font=("Arial", 16, "bold"), bg=color_terciario)
        titulo_label.pack(pady=10)

        # Crear el Label y el Combobox para seleccionar el usuario del cajero
        usuario_label = tk.Label(frame, text="Selecciona el usuario del cajero:", font=("Arial", 12, "bold"), bg=color_terciario)
        usuario_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Obtener la lista de usuarios cajeros
        cajeros = [usuario[0] for usuario in usuarios if usuario[2] == "cajero"]

        # Variable para almacenar el usuario seleccionado
        selected_usuario = tk.StringVar()

        # Crear el Combobox para seleccionar el usuario del cajero
        usuario_combobox = ttk.Combobox(frame, textvariable=selected_usuario, values=cajeros, state="readonly")
        usuario_combobox.pack(side=tk.LEFT, padx=10, pady=10)
        usuario_combobox.current(0)  # Establecer el valor predeterminado

        no_existe_label = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg=color_terciario)

        def mostrar_facturas():
            no_existe_label.config(text="")
            no_existe_label.pack_forget()
            cajero_usuario = selected_usuario.get()

            cajero_existente = False
            facturas_cajero = []

            # Buscar facturas correspondientes al cajero
            for usuario in usuarios:
                if usuario[0] == cajero_usuario:
                    cajero_existente = True
                    for factura in facturas:
                        if factura[1] == cajero_usuario:
                            facturas_cajero.append(factura)
                    break

            if cajero_existente:
                # Destruir los elementos anteriores
                for widget in frame.winfo_children():
                    widget.destroy()

                # Crear la tabla de facturas filtradas por cajero
                tabla_frame = tk.Frame(frame, bg=color_terciario, highlightbackground="black", highlightthickness=1)
                tabla_frame.pack(padx=60, pady=20)

                titulo = tk.Label(tabla_frame, text="Facturas", font=("Arial", 16, "bold"), bg=color_terciario)
                titulo.grid(row=0, column=0, columnspan=7)

                # Encabezados de las columnas
                id_label = tk.Label(tabla_frame, text="ID", font=("Arial", 12, "bold"), bg=color_terciario)
                id_label.grid(row=1, column=0, padx=(30, 10), pady=5)

                correo_label = tk.Label(tabla_frame, text="Correo", font=("Arial", 12, "bold"), bg=color_terciario)
                correo_label.grid(row=1, column=1, padx=(20, 10), pady=5)

                fecha_label = tk.Label(tabla_frame, text="Fecha", font=("Arial", 12, "bold"), bg=color_terciario)
                fecha_label.grid(row=1, column=2, padx=(20, 10), pady=5)

                total_label = tk.Label(tabla_frame, text="Total", font=("Arial", 12, "bold"), bg=color_terciario)
                total_label.grid(row=1, column=4, padx=(20, 10), pady=5)

                detalles_label = tk.Label(tabla_frame, text="Detalles", font=("Arial", 12, "bold"), bg=color_terciario)
                detalles_label.grid(row=1, column=5, padx=(20, 10), pady=5)

                # Mostrar facturas del cajero en la tabla
                for i, factura in enumerate(facturas_cajero, start=2):
                    factura_id = factura[0]
                    correo = factura[1]
                    fecha = factura[2]
                    detalles = factura[3]
                    total = factura[5]["Total"]

                    id_label = tk.Label(tabla_frame, text=factura_id, bg=color_terciario)
                    id_label.grid(row=i, column=0, padx=(20, 10), pady=5)

                    correo_label = tk.Label(tabla_frame, text=correo, bg=color_terciario)
                    correo_label.grid(row=i, column=1, padx=(20, 10), pady=5)

                    fecha_label = tk.Label(tabla_frame, text=fecha, bg=color_terciario)
                    fecha_label.grid(row=i, column=2, padx=(20, 10), pady=5)

                    total_label = tk.Label(tabla_frame, text=total, bg=color_terciario)
                    total_label.grid(row=i, column=4, padx=(20, 10), pady=5)

                    detalles_label = tk.Button(
                        tabla_frame,
                        text="Mirar detalles",
                        bg="yellow",
                        command=lambda detalles1=detalles: self.mostrar_detalles(detalles1),
                    )
                    detalles_label.grid(row=i, column=5, padx=(20, 10), pady=5)
                    # Destruir el mensaje anterior de cajero no existe
                    no_existe_label.config(text="")
                    no_existe_label.pack_forget()

            else:
                no_existe_label.config(text="El cajero no existe")
                no_existe_label.pack(padx=20, pady=20, anchor="center")

        # Crear un botón para mostrar las facturas del cajero
        mostrar_button = tk.Button(frame, text="Mostrar Facturas", bg=color_secundario, command=mostrar_facturas)
        mostrar_button.pack(pady=10)

        # Establecer el fondo de la ventana y de los elementos
        self.root.config(bg=color_terciario)
        frame.config(bg=color_terciario)
        titulo_label.config(bg=color_terciario)
        usuario_label.config(bg=color_terciario)
        usuario_combobox.config(style="TCombobox")



class Cajero:
    def __init__(self, root):
        self.products = []
        self.root = root
        self.current_category = None
        self.carrito = None
        self.create_menu()
        self.usuario = None

        # Configurar la ventana principal
        self.root.title("Cajero")
        self.root.config(bg=color_terciario)

        # Configurar el carrito
        self.carrito = ttk.Treeview(
            self.root,
            columns=("Producto", "Sabores", "Cantidad", "Precio")
        )
        self.carrito.heading("#0", text="Producto")
        self.carrito.heading("#1", text="Sabores")
        self.carrito.heading("#2", text="Cantidad")
        self.carrito.heading("#3", text="Precio")

    def Ventana_principal(self, usuario):
        if usuario is not None:
            self.usuario = usuario
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_menu()

        # Configurar la ventana principal
        self.root.title("Cajero")
        self.root.config(bg=color_terciario)

        # Crear widgets
        self.category_frame = ttk.Frame(self.root)
        self.product_frame = ttk.Frame(self.root)
        self.details_frame = None
        self.selected_category_label = ttk.Label(self.root, text="")

        # Configurar el marco de categorías
        self.category_frame.grid(row=1, column=1, padx=20, pady=10)

        # Mostrar la etiqueta de categoría seleccionada
        self.selected_category_label.grid(
            row=2, column=0, padx=10, pady=5, sticky="w")

        # Crear botones para las categorías
        for i, category in enumerate(categories.keys()):
            category_button = ttk.Button(
                self.category_frame,
                text=category,
                command=lambda c=category: self.show_category(c)
            )
            category_button.grid(row=i, column=0, padx=10, pady=5)

        # Configurar el marco de productos
        self.product_frame.grid(row=2, column=0, padx=20, pady=10)

        # Iniciar la interfaz gráfica mostrando las categorías
        self.show_categories()

        # Crear el marco del carrito
        self.carrito_frame = ttk.Frame(self.root)
        self.carrito_frame.grid(row=0, column=1, padx=20, pady=10)

        # Crear la etiqueta del título del carrito
        carrito_label = ttk.Label(
            self.carrito_frame, text="Carrito de Compras")
        carrito_label.grid(row=0, column=0, padx=10, pady=5)

        # Crear el Treeview del carrito
        self.carrito = ttk.Treeview(
            self.carrito_frame,
            columns=("Producto", "Sabores", "Cantidad", "Precio")
        )
        self.carrito.grid(row=1, column=0, padx=10, pady=5)
        self.carrito.heading("#0", text="Producto")
        self.carrito.heading("#1", text="Sabores")
        self.carrito.heading("#2", text="Cantidad")
        self.carrito.heading("#3", text="Precio")

        # Crear el botón de eliminar
        eliminar_button = ttk.Button(
            self.carrito_frame,
            text="Eliminar Producto",
            command=self.remove_selected_product
        )
        eliminar_button.grid(row=2, column=0, padx=10, pady=5)

        # Crear la etiqueta y el cuadro de texto del total
        total_label = ttk.Label(self.carrito_frame, text="Total:")
        total_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.total_textbox = ttk.Entry(self.carrito_frame, state="readonly")
        self.total_textbox.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        realizar_compra_button = ttk.Button(
            self.carrito_frame,
            text="Realizar compra",
            command=self.show_pending_orders
        )
        realizar_compra_button.grid(row=2, column=1, padx=10, pady=5)

    def show_categories(self, canvas=None):
        self.current_category = None
        if canvas != None:
            canvas.destroy()

        if self.details_frame:
            self.details_frame.grid_remove()
        self.category_frame.grid()
        self.product_frame.grid_remove()
        self.selected_category_label.configure(text="")
        self.root.config(bg=color_terciario)

    def add_to_cart(self, product, quantity, flavor1, flavor2=None, flavor3=None):
        if not quantity.isdigit() or int(quantity) == 0:
            messagebox.showerror("Error", "Por favor, selecciona una cantidad válida.")
        elif flavor1 == "":
            messagebox.showerror("Error", "Por favor, selecciona un sabor.")
        else:
            product_title = product["title"]
            if product_title in productos_dobles:
                if flavor2 is None or flavor2 == "":
                    messagebox.showerror(
                        "Error", "Por favor, selecciona un segundo sabor para el Producto 2.")
                    return
                self.products.append(
                    (product_title, quantity, flavor1, flavor2))
            elif product_title in productos_Triples:
                if flavor3 is None or flavor3 == "":
                    messagebox.showerror(
                        "Error", "Por favor, selecciona un tercer sabor.")
                    return
                self.products.append(
                    (product_title, quantity, flavor1, flavor2, flavor3))
            else:
                self.products.append((product_title, quantity, flavor1))

            messagebox.showinfo("Éxito", "Producto agregado al carrito.")
            self.show_categories()
            self.carrito_compras()

    def show_category(self, category):
        self.root.config(bg=color_terciario)
        self.current_category = category
        self.selected_category_label.configure(text=category)

        for widget in self.product_frame.winfo_children():
            widget.destroy()

        products = categories[category]

        # Crear un lienzo para el marco de productos
        canvas = tk.Canvas(self.product_frame, width=600)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear una barra de desplazamiento para el lienzo (vertical)
        scrollbar_y = ttk.Scrollbar(self.product_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear una barra de desplazamiento para el lienzo (horizontal)
        scrollbar_x = ttk.Scrollbar(self.product_frame, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configurar el lienzo para utilizar las barras de desplazamiento
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Crear un marco para contener los widgets de productos
        product_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=product_frame, anchor="nw")

        for i, product in enumerate(products):
            title_label = ttk.Label(product_frame, text=product["title"])
            title_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            image = Image.open(product["image_path"])
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(product_frame, image=photo)
            image_label.image = photo
            image_label.grid(row=i, column=1, padx=10, pady=5)

            description_label = ttk.Label(product_frame, text=product["description"])
            description_label.grid(row=i, column=2, padx=10, pady=5, sticky="w")

            price_label = ttk.Label(product_frame, text="Precio: " + product["price"])
            price_label.grid(row=i, column=3, padx=10, pady=5, sticky="w")

            buy_button = ttk.Button(
                product_frame,
                text="Comprar",
                command=lambda p=product: self.show_details(p),
            )
            buy_button.grid(row=i, column=4, padx=10, pady=5)

        # Vincular las barras de desplazamiento al lienzo
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        canvas.bind("<Shift-MouseWheel>", lambda e: canvas.xview_scroll(int(-1 * (e.delta / 120)), "units"))

        self.product_frame.grid()
        self.category_frame.grid_remove()

        back_button = ttk.Button(
            product_frame,
            text="Volver al menú principal",
            command=lambda: self.show_categories(canvas),
        )
        back_button.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    def show_details(self, product):
        self.category_frame.grid_forget()
        self.product_frame.grid_forget()
        self.details_frame = ttk.Frame(self.root)
        self.details_frame.grid(row=0, column=0, padx=20, pady=10)
        title_label = ttk.Label(
            self.details_frame,
            text="Title: " + product["title"] +
            " - Price: " + product["price"],
        )
        title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        image = Image.open(product["image_path"])
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(self.details_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        quantity_label = ttk.Label(self.details_frame, text="Quantity:")
        quantity_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        quantity_spinbox = ttk.Spinbox(self.details_frame, from_=1, to=10)
        quantity_spinbox.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        flavor1_label = ttk.Label(self.details_frame, text="Flavor 1:")
        flavor1_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        flavor_combobox1 = ttk.Combobox(
            self.details_frame, values=[
                   sabores[0], sabores[1], sabores[2],sabores[3], sabores[4], sabores[5], sabores[6], sabores[7],
                   sabores[8], sabores[9], sabores[10], sabores[11], sabores[12], sabores[13], sabores[14], sabores[15],
                   sabores[16], sabores[17], sabores[18], sabores[19], sabores[20]]
        )
        flavor_combobox1.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        flavor_combobox2 = None
        print(product, "producto de")
        flavor2_label = ttk.Label(self.details_frame, text="Flavor 2:")
        flavor2_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        flavor_combobox2 = ttk.Combobox(
            self.details_frame, values=[
               sabores[0], sabores[1], sabores[2],sabores[3], sabores[4], sabores[5], sabores[6], sabores[7],
               sabores[8], sabores[9], sabores[10], sabores[11], sabores[12], sabores[13], sabores[14], sabores[15],
               sabores[16], sabores[17], sabores[18], sabores[19], sabores[20]]
        )
        flavor_combobox2.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        flavor_combobox3 = None
        flavor3_label = None
        flavor3_label = ttk.Label(self.details_frame, text="Flavor 3:")
        flavor3_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        flavor_combobox3 = ttk.Combobox(
            self.details_frame, values=[
               sabores[0], sabores[1], sabores[2],sabores[3], sabores[4], sabores[5], sabores[6], sabores[7],
               sabores[8], sabores[9], sabores[10], sabores[11], sabores[12], sabores[13], sabores[14], sabores[15],
               sabores[16], sabores[17], sabores[18], sabores[19], sabores[20]]
        )
        flavor_combobox3.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        add_to_cart_button = ttk.Button(
            self.details_frame,
            text="Add to Cart",
            command=lambda: self.add_to_cart(
                product,
                quantity_spinbox.get(),
                flavor_combobox1.get(),
                flavor_combobox2.get() if flavor_combobox2 else None,
                flavor_combobox3.get() if flavor_combobox3 else None
            ),
        )
        add_to_cart_button.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        back_button = ttk.Button(
            self.details_frame, text="Back to menu", command=self.show_categories
        )
        back_button.grid(row=6, column=1, padx=10, pady=5, sticky="e")

    def ver_facturas(self):
        # Eliminar todos los widgets de la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_menu()
        self.root.config(bg=color_terciario)

        # Crear la tabla de facturas dentro de un widget Canvas
        canvas = tk.Canvas(
            self.root,
            bg=color_terciario,
            highlightbackground=color_terciario,
            width=480,
            height=520,
        )
        canvas.grid(row=1, column=1, sticky="nsew", padx=60, pady=20)

        # Crear un scrollbar y asociarlo al widget Canvas
        scrollbar = tk.Scrollbar(
            self.root, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")

        # Configurar el scrollbar para que controle el widget Canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))

        # Crear un frame dentro del widget Canvas para contener la tabla
        table_frame = tk.Frame(
            canvas,
            bg=color_terciario,
            highlightbackground="black",
            highlightthickness=1,
        )
        canvas.create_window((0, 0), window=table_frame, anchor=tk.NW)

        # Título de la tabla
        titulo = tk.Label(
            table_frame, text="Facturas", font=("Arial", 14, "bold"), bg=color_terciario
        )
        titulo.grid(row=0, column=0, columnspan=6)

        # Encabezados de las columnas
        id_label = tk.Label(
            table_frame, text="ID", font=("Arial", 12, "bold"), bg=color_terciario
        )
        id_label.grid(row=1, column=0, padx=(30, 10), pady=5, sticky="w")

        correo_label = tk.Label(
            table_frame, text="Correo", font=("Arial", 12, "bold"), bg=color_terciario
        )
        correo_label.grid(row=1, column=1, padx=(20, 10), pady=5, sticky="w")

        fecha_label = tk.Label(
            table_frame, text="Fecha", font=("Arial", 12, "bold"), bg=color_terciario
        )
        fecha_label.grid(row=1, column=2, padx=(20, 10), pady=5, sticky="w")

        total_label = tk.Label(
            table_frame, text="Total", font=("Arial", 12, "bold"), bg=color_terciario
        )
        total_label.grid(row=1, column=4, padx=(20, 10), pady=5, sticky="w")

        detalles_label = tk.Label(
            table_frame, text="Detalles", font=("Arial", 12, "bold"), bg=color_terciario
        )
        detalles_label.grid(row=1, column=5, columnspan=2,
                            pad1x=(20, 10), pady=5, sticky="w")

        # Mostrar datos de las facturas en la tabla
        for i, factura in enumerate(facturas, start=2):
            factura_id = factura[0]
            correo = factura[1]
            fecha = factura[2]
            detalles = factura[3]
            total = factura[5]["Total"]

            id_label = tk.Label(
                table_frame, text=factura_id, bg=color_terciario)
            id_label.grid(row=i, column=0, padx=(20, 10), pady=5, sticky="w")

            correo_label = tk.Label(
                table_frame, text=correo, bg=color_terciario)
            correo_label.grid(row=i, column=1, padx=(
                20, 10), pady=5, sticky="w")

            fecha_label = tk.Label(table_frame, text=fecha, bg=color_terciario)
            fecha_label.grid(row=i, column=2, padx=(
                20, 10), pady=5, sticky="w")

            total_label = tk.Label(table_frame, text=total, bg=color_terciario)
            total_label.grid(row=i, column=4, padx=(
                20, 10), pady=5, sticky="w")

            detalles_label = tk.Button(
                table_frame,
                text="Mirar detalles",
                bg="yellow",
                command=lambda detalles1=detalles: Admin(
                    self.root).mostrar_detalles(detalles1),
            )
            detalles_label.grid(
                row=i, column=5, columnspan=2, padx=(20, 10), pady=5, sticky="w"
            )

    def carrito_compras(self):
        self.carrito.delete(*self.carrito.get_children())
        self.root.config(bg=color_terciario)

        for product in self.products:
            product_title = product[0]
            quantity = int(product[1])
            flavors = ", ".join(product[2:])
            price = self.get_product_price(product_title)
            total_price = quantity * price
            self.carrito.insert(
                "", "end", text=product_title, values=(flavors, quantity, total_price)
            )

        total = self.calculate_total()
        self.total_textbox.configure(state="normal")
        self.total_textbox.delete(0, "end")
        self.total_textbox.insert(0, total)
        self.total_textbox.configure(state="readonly")

    def get_product_price(self, product_title):
        for category in categories.values():
            for product in category:
                if product["title"] == product_title:
                    price = product["price"]
                    price = price.replace("$", "").replace(",", "")
                    return int(price)

    def calculate_total(self):
        total = 0
        for product in self.products:
            product_title = product[0]
            quantity = int(product[1])
            price = self.get_product_price(product_title)
            total += quantity * price
        return total

    def remove_selected_product(self):
        selection = self.carrito.selection()
        if selection:
            item = self.carrito.item(selection)
            product_title = item["text"]
            for i, product in enumerate(self.products):
                if product[0] == product_title:
                    del self.products[i]
                    break
            self.carrito.delete(selection)

            total = self.calculate_total()
            self.total_textbox.configure(state="normal")
            self.total_textbox.delete(0, "end")
            self.total_textbox.insert(0, total)
            self.total_textbox.configure(state="readonly")
        else:
            messagebox.showerror("Error", "Please select a product to remove.")

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        self.root.config(bg=color_terciario)
        # Crea el menú "Pedidos pendientes"

        # Crea el menú "Pedidos para entregar"
        entregar_menu = Menu(menubar, tearoff=0)
        entregar_menu.add_command(label="Ver pedidos para entregar")
        menubar.add_cascade(label="Pedidos para entregar", menu=entregar_menu)

        # Crea el menú "Facturas"
        facturas_menu = Menu(menubar, tearoff=0)
        facturas_menu.add_command(label="Ver facturas")
        menubar.add_cascade(label="Facturas", menu=facturas_menu)

        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        pendientes_menu = Menu(menubar, tearoff=0)
        pendientes_menu.add_command(
            label="Ver pedidos pendientes", command=self.view_pending_orders
        )
        pendientes_menu.add_command(
            label="Ver pedidos para entregar", command=self.view_entregar_orders
        )
        pendientes_menu.add_command(
            label="Ver Facturas", command=self.ver_facturas)

        menubar.add_cascade(label="Pedidos", menu=pendientes_menu)

        # Create the "Volver arriba" button
        image = Image.open("BotonVolver.png")
        nuevo_tamaño = (40, 40)
        imagen_nueva = image.resize(nuevo_tamaño)
        background_image = ImageTk.PhotoImage(imagen_nueva)
        button_regresar = tk.Button(
            self.root,
            image=background_image,
            command=lambda: Admin(self.root).volver(),
            bg=color_terciario,
        )
        button_regresar.image = background_image
        button_regresar.grid(row=0, column=0)

    def create_invoice(self, paymenth_method):
        filas_adicionales = []
        invoice = ""
        total = 0
        Producto_Factura_Individual = []
        Producto_Factura_Conjunta = []
        Producto_Factura_Conjunta_Filtro = []
        Producto_Factura_Total = []
        productos = []
        for item in self.carrito.get_children():
            product = self.carrito.item(item)
            product_title = product["text"]
            flavors = product["values"][0]
            quantity = product["values"][1]
            total_price = product["values"][2]
            Producto_Factura_Individual.append(product_title)
            Producto_Factura_Individual.append(flavors)
            Producto_Factura_Individual.append(quantity)
            Producto_Factura_Individual.append(total_price)
            Producto_Factura_Conjunta.append(Producto_Factura_Individual)
            total += total_price
            invoice += f"Product: {product_title}\n"
            invoice += f"Flavors: {flavors}\n"
            invoice += f"Quantity: {quantity}\n"
            invoice += f"Total Price: {total_price}\n"
            invoice += "------------------------\n"
            producto = {"tamaño": product_title,
                        "sabor": flavors, "precio": total_price}
            productos.append(producto)
        invoice += f"Total: {total}\n"
        Producto_Factura_Conjunta_Filtro.append(Producto_Factura_Conjunta[0])
        Producto_Factura_Total.append(Producto_Factura_Conjunta_Filtro)
        Producto_Factura_Total.append(total)

        print(Producto_Factura_Total, "aquí es")
        lista.append(invoice)
        print(lista)

        filas_adicionales.append(len(facturas)+1)
        filas_adicionales.append(self.usuario[0])
        filas_adicionales.append(datetime.date.today().strftime("%d/%m/%Y"))
        filas_adicionales.append(productos)
        filas_adicionales.append(paymenth_method)
        filas_adicionales.append({"Total": total})
        print(filas_adicionales)
        filas.append(filas_adicionales)
        print(filas)

        return invoice

    def clear_cart(self):
        self.carrito.delete(*self.carrito.get_children())
        self.root.config(bg=color_terciario)
        self.total_textbox.configure(state="normal")
        self.total_textbox.delete(0, "end")
        self.total_textbox.configure(state="readonly")

    def show_pending_orders(self):
        if self.carrito.get_children():
            answer = messagebox.askyesno(
                "Confirmation", "Do you want to create an invoice for pending orders?"
            )
            if answer:
                payment_method = ""
                payment_answer = messagebox.askyesno(
                    "Payment Method", "Will the payment be in cash (online)?"
                )
                if payment_answer:
                    payment_method = "online"
                else:
                    payment_method = "caja"

                invoice = self.create_invoice(payment_method)
                pending_orders.append(invoice)
                messagebox.showinfo("Pending Orders", invoice)
                self.clear_cart()

        else:
            messagebox.showinfo("No Pending Orders",
                                "There are no pending orders.")

    def view_pending_orders(self):
        if pending_orders:
            orders = "\n".join(pending_orders)
            messagebox.showinfo("Pending Orders", orders)
            self.actualizar_tabla(self.root)
        else:
            messagebox.showinfo("No Pending Orders",
                                "There are no pending orders.")

    # ----- Pedidos pendientes
    def actualizar_tabla(self, root):
        # Eliminar todos los widgets de la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_menu()
        # Crear títulos de la tabla
        titulos = [
            "ID",
            "Correo",
            "Fecha",
            "Detalles",
            "Tipo de pago",
            "Total",
            "Aceptar Pedido",
            "Cancelar Pedido",
        ]
        for i, titulo in enumerate(titulos):
            label = tk.Label(root, text=titulo)
            label.grid(row=0, column=i, padx=5, pady=5)

        # Crear contenido de la tabla
        for i, fila in enumerate(filas):
            for j, valor in enumerate(fila):
                if j == 3:
                    detalles = ""
                    for obj in valor:
                        detalles += f"tamaño: {obj['tamaño']}\n"
                        detalles += f"sabor: {obj['sabor']}\n"
                        detalles += f"precio: {obj['precio']}\n"
                    btn_detalles = ttk.Button(
                        root,
                        text="Detalles",
                        command=lambda detalles=detalles: messagebox.showinfo(
                            "Detalles", detalles),
                    )
                    btn_detalles.grid(row=i + 1, column=j, padx=5, pady=5)
                elif j == 5:
                    if isinstance(valor, dict):
                        valor_dict = dict(valor)
                        value = valor_dict.get("Total", "")
                        label = ttk.Label(root, text=value)
                        label.grid(row=i + 1, column=j, padx=5, pady=5)
                else:
                    if isinstance(valor, dict):
                        if j == 4:
                            valor = valor.get("tamaño", "")
                        elif j == 5:
                            valor = valor.get("precio", "")
                    label = ttk.Label(root, text=valor)
                    label.grid(row=i + 1, column=j, padx=5, pady=5)

            # Crear botones de pedido
            seccion_pedido = ttk.Frame(root)
            seccion_pedido.grid(row=i + 1, column=6,
                                columnspan=2, padx=5, pady=5)

            btn_aceptar = ttk.Button(
                seccion_pedido,
                text="Aceptar Pedido",
                command=lambda fila=fila: self.aceptar_pedido(fila),
            )
            btn_cancelar = ttk.Button(
                seccion_pedido,
                text="Cancelar Pedido",
                command=lambda fila=fila: self.cancelar_pedido(fila),
            )

            btn_aceptar.pack(side="left", padx=5, pady=5)
            btn_cancelar.pack(side="left", padx=5, pady=5)

        # Obtener el número de filas actuales
        num_filas_actuales = len(filas)

        # Botón "volver menu"
        btn_volver_menu = ttk.Button(
            root, text="Volver al menú", command=lambda: self.remover_ver_pedidos()
        )
        btn_volver_menu.grid(
            row=num_filas_actuales + 1, column=0, columnspan=8, padx=5, pady=5
        )

    def aceptar_pedido(self, fila):
        # Lógica para aceptar el pedido
        pedidos_aceptados.append(
            fila
        )  # Guardar los datos de la fila en la lista de pedidos aceptados
        filas.remove(
            fila
        )  # Remover la fila de la lista de filas  # Actualizar la tabla en la interfaz
        print("Pedido aceptado")
        print(filas)
        print(pedidos_aceptados)
        self.actualizar_tabla(self.root)

    def cancelar_pedido(self, fila):
        # Lógica para cancelar el pedido
        filas.remove(fila)  # Remover la fila de la lista de filas

        print("Pedido cancelado")
        print(filas)
        self.actualizar_tabla(self.root)

    def ver_detalles(self, detalles):
        # Imprimir los detalles del pedido
        messagebox.showinfo("Pending Orders", detalles)

    # ------ pedidos para entregar
    def view_entregar_orders(self):
        if pending_orders:
            orders = "\n".join(pending_orders)
            messagebox.showinfo("Pending Orders", orders)

            self.actualizar_tabla2(self.root)
        else:
            messagebox.showinfo("No Pending Orders",
                                "There are no pending orders.")

    def actualizar_tabla2(self, root):
        # Eliminar todos los widgets de la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_menu()
        # Crear títulos de la tabla
        titulos = [
            "ID",
            "Correo",
            "Fecha",
            "Detalles",
            "Tipo de pago",
            "Total",
            "Aceptar Pedido",
            "Cancelar Pedido",
        ]
        for i, titulo in enumerate(titulos):
            label = tk.Label(root, text=titulo)
            label.grid(row=0, column=i, padx=5, pady=5)

        # Crear contenido de la tabla
        for i, fila in enumerate(pedidos_aceptados):
            for j, valor in enumerate(fila):
                if j == 3:
                    detalles = ""
                    for obj in valor:
                        detalles += f"tamaño: {obj['tamaño']}\n"
                        detalles += f"sabor: {obj['sabor']}\n"
                        detalles += f"precio: {obj['precio']}\n"
                    btn_detalles = ttk.Button(
                        root,
                        text="Detalles",
                        command=lambda detalles=detalles: messagebox.showinfo(
                            "Detalles", detalles),
                    )
                    btn_detalles.grid(row=i + 1, column=j, padx=5, pady=5)
                elif j == 5:
                    if isinstance(valor, dict):
                        valor_dict = dict(valor)
                        value = valor_dict.get("Total", "")
                        label = ttk.Label(root, text=value)
                        label.grid(row=i + 1, column=j, padx=5, pady=5)
                else:
                    if isinstance(valor, dict):
                        if j == 4:
                            valor = valor.get("tamaño", "")
                        elif j == 5:
                            valor = valor.get("precio", "")
                    label = ttk.Label(root, text=valor)
                    label.grid(row=i + 1, column=j, padx=5, pady=5)

            # Crear botones de pedido
            seccion_pedido = ttk.Frame(root)
            seccion_pedido.grid(row=i + 1, column=6,
                                columnspan=2, padx=5, pady=5)

            btn_aceptar = ttk.Button(
                seccion_pedido,
                text="Entregar pedido",
                command=lambda fila=fila: self.aceptar_pedido2(fila),
            )

            btn_aceptar.pack(side="left", padx=5, pady=5)

        # Obtener el número de filas actuales
        num_filas_actuales = len(filas)

        # Botón "volver menu"
        btn_volver_menu = ttk.Button(
            root, text="Volver al menu", command=lambda: self.remover_ver_pedidos()
        )
        btn_volver_menu.grid(
            row=num_filas_actuales + 2, column=0, columnspan=6, padx=5, pady=5
        )

    def aceptar_pedido2(self, fila):
        print(fila, "hola aqui es")
        # Lógica para aceptar el pedido
        facturas.append(
            fila
        )  # Guardar los datos de la fila en la lista de pedidos aceptados
        pedidos_aceptados.remove(
            fila
        )  # Remover la fila de la lista de filas  # Actualizar la tabla en la interfaz
        print("Pedido aceptado")
        print(filas)
        print(pedidos_aceptados)
        print(facturas)
        self.actualizar_tabla(self.root)

    def ver_detalles2(self, detalles):
        # Imprimir los detalles del pedido
        messagebox.showinfo("Pending Orders", detalles)

    def remover_ver_pedidos(self):
        self.Ventana_principal(None)


class Usuario:
    def __init__(self, root):
        self.root = root
        self.usuario = None
        self.metodoPago=""
        self.products = []
        # Configure the cart
        self.carrito_treeview = ttk.Treeview(
            self.root,
            columns=("Producto", "Sabores", "Cantidad", "Precio")
        )
        self.carrito_treeview.heading("#0", text="Producto")
        self.carrito_treeview.heading("#1", text="Sabores")
        self.carrito_treeview.heading("#2", text="Cantidad")
        self.carrito_treeview.heading("#3", text="Precio")

    def Ventana_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.herramientas()
        # Configure the main window
        self.root.title("Usuario")
        self.root.config(bg=color_terciario)

        # Create widgets
        self.category_frame = ttk.Frame(self.root)
        self.product_frame = ttk.Frame(self.root)
        self.details_frame = None
        self.selected_category_label = ttk.Label(self.root, text="")

        # Configure the category frame
        self.category_frame.pack(side=tk.LEFT, padx=20, pady=10)

        # Show the selected category label
        self.selected_category_label.pack(
            side=tk.TOP, padx=10, pady=5, anchor="w")

        # Create buttons for the categories
        for i, category in enumerate(categories.keys()):
            category_button = ttk.Button(
                self.category_frame,
                text=category,
                command=lambda c=category: self.show_category(c)
            )
            category_button.pack(side=tk.TOP, padx=10, pady=5)

        # Configure the product frame
        self.product_frame.pack(side=tk.LEFT, padx=20, pady=10)

        # Start the GUI by showing the categories
        self.show_categories()

        # Create the carrito frame
        self.carrito_frame = ttk.Frame(self.root)
        self.carrito_frame.pack(side=tk.RIGHT, padx=20, pady=10)

        # Create the carrito title label
        carrito_label = ttk.Label(
            self.carrito_frame, text="Carrito de Compras")
        carrito_label.pack(side=tk.TOP, padx=10, pady=5)

        self.carrito_treeview = ttk.Treeview(
            self.carrito_frame,
            columns=("Producto", "Sabores", "Cantidad", "Precio")
        )
        self.carrito_treeview.pack(side=tk.TOP, padx=10, pady=5)
        self.carrito_treeview.heading("#0", text="Producto")
        self.carrito_treeview.heading("#1", text="Sabores")
        self.carrito_treeview.heading("#2", text="Cantidad")
        self.carrito_treeview.heading("#3", text="Precio")

        # Create the eliminar button
        eliminar_button = ttk.Button(
            self.carrito_frame,
            text="Eliminar Producto",
            command=self.remove_selected_product
        )
        eliminar_button.pack(side=tk.TOP, padx=10, pady=5)

        # Create the total label and textbox
        total_label = ttk.Label(self.carrito_frame, text="Total:")
        total_label.pack(side=tk.TOP, padx=10, pady=5, anchor="e")
        self.total_textbox = ttk.Entry(self.carrito_frame, state="readonly")
        self.total_textbox.pack(side=tk.TOP, padx=10, pady=5, anchor="w")

        # Create the combobox for payment method
        metodo_pago_label = ttk.Label(self.carrito_frame, text="Método de Pago:")
        metodo_pago_label.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        self.metodo_pago_combobox = ttk.Combobox(
            self.carrito_frame,
            values=["Caja", "Online", "OnlineCaja"]
        )
        self.metodo_pago_combobox.pack(side=tk.TOP, padx=10, pady=5, anchor="w")

        realizar_compra_button = ttk.Button(
            self.carrito_frame,
            text="Realizar compra",
            command=self.checkout
        )
        realizar_compra_button.pack(side=tk.TOP, padx=10, pady=5)

    def checkout(self):
        metodo_pago = self.metodo_pago_combobox.get()
        if metodo_pago:
            self.metodoPago = metodo_pago
            self.show_pending_orders()
        else:
            messagebox.showinfo("Error", "Debes seleccionar un método de pago.")

        
        
    def show_category(self, category):
        self.root.config(bg=color_terciario)
        self.current_category = category
        self.selected_category_label.configure(text=category)

        # Destroy existing widgets in the product frame
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        # Create a canvas for the product frame
        canvas = tk.Canvas(self.product_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar for the canvas
        scrollbar = ttk.Scrollbar(self.product_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the products
        inner_frame = ttk.Frame(canvas)

        # Add the inner frame to the canvas
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        products = categories[category]
        for i, product in enumerate(products):
            title_label = ttk.Label(inner_frame, text=product["title"])
            title_label.pack(padx=10, pady=5, anchor="w")

            image = Image.open(product["image_path"])
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(inner_frame, image=photo)
            image_label.image = photo
            image_label.pack(padx=10, pady=5)

            description_label = ttk.Label(
                inner_frame, text=product["description"])
            description_label.pack(padx=10, pady=5, anchor="w")

            price_label = ttk.Label(
                inner_frame, text="Price: " + product["price"])
            price_label.pack(padx=10, pady=5, anchor="w")

            buy_button = ttk.Button(
                inner_frame,
                text="Buy",
                command=lambda p=product: self.show_details(p),
            )
            buy_button.pack(padx=10, pady=5)

        # Update the scroll region of the canvas
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Show the product frame and hide the category frame
        self.product_frame.pack()
        self.category_frame.pack_forget()

        back_button = ttk.Button(
            self.product_frame,
            text="Back to main menu",
            command=lambda:self.show_categories(canvas),
            width=30
        )
        back_button.pack(padx=8, pady=5, anchor="w")

    def show_details(self, product):
        self.category_frame.pack_forget()
        self.product_frame.pack_forget()

        self.details_frame = ttk.Frame(self.root)
        self.details_frame.pack(padx=20, pady=10)

        title_label = ttk.Label(
            self.details_frame,
            text="Title: " + product["title"] +
            " - Price: " + product["price"],
        )
        title_label.pack(padx=10, pady=5, anchor="w")

        image = Image.open(product["image_path"])
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(self.details_frame, image=photo)
        image_label.image = photo
        image_label.pack(padx=10, pady=5)

        quantity_label = ttk.Label(self.details_frame, text="Quantity:")
        quantity_label.pack(padx=10, pady=5, anchor="w")

        quantity_spinbox = ttk.Spinbox(self.details_frame, from_=1, to=10)
        quantity_spinbox.pack(padx=10, pady=5, anchor="w")

        flavor1_label = ttk.Label(self.details_frame, text="Flavor 1:")
        flavor1_label.pack(padx=10, pady=5, anchor="w")

        flavor_combobox1 = ttk.Combobox(
            self.details_frame, values=[
                   sabores[0], sabores[1], sabores[2],sabores[3], sabores[4], sabores[5], sabores[6], sabores[7],
                   sabores[8], sabores[9], sabores[10], sabores[11], sabores[12], sabores[13], sabores[14], sabores[15],
                   sabores[16], sabores[17], sabores[18], sabores[19], sabores[20]]
        )
        flavor_combobox1.pack(padx=10, pady=5, anchor="w")

        if product["title"] == "Product 2" and self.current_category == "Category 1":
            flavor2_label = ttk.Label(self.details_frame, text="Flavor 2:")
            flavor2_label.pack(padx=10, pady=5, anchor="w")

            flavor_combobox2 = ttk.Combobox(
                self.details_frame, values=[
                   sabores[0], sabores[1], sabores[2],sabores[3], sabores[4], sabores[5], sabores[6], sabores[7],
                   sabores[8], sabores[9], sabores[10], sabores[11], sabores[12], sabores[13], sabores[14], sabores[15],
                   sabores[16], sabores[17], sabores[18], sabores[19], sabores[20]]
            )
            flavor_combobox2.pack(padx=10, pady=5, anchor="w")

        add_to_cart_button = ttk.Button(
            self.details_frame,
            text="Add to cart",
            command=lambda: self.add_to_cart(
                product,
                quantity_spinbox.get(),
                flavor_combobox1.get(),
                flavor_combobox2.get() if "flavor_combobox2" in locals() else None,
            ),
        )
        add_to_cart_button.pack(padx=10, pady=5, anchor="w")

        back_button = ttk.Button(
            self.details_frame, text="Back to menu", command=self.show_categories
        )
        back_button.pack(padx=10, pady=5, anchor="e")

    def add_to_cart(self, product, quantity, flavor1, flavor2=None, flavor3=None):
        if not quantity.isdigit() or int(quantity) == 0:
            messagebox.showerror("Error", "Please select a valid quantity.")
        elif flavor1 == "":
            messagebox.showerror("Error", "Please select a flavor.")
        else:
            product_title = product["title"]
            if product_title in productos_dobles:
                if flavor2 is None or flavor2 == "":
                    messagebox.showerror(
                        "Error", "Please select a second flavor for Product 2.")
                    return
                self.products.append(
                    (product_title, quantity, flavor1, flavor2))
            elif product_title in productos_Triples:
                if flavor3 is None or flavor3 == "":
                    messagebox.showerror(
                        "Error", "Please select a third flavor ")
                    return
                self.products.append(
                    (product_title, quantity, flavor1, flavor2, flavor3))
            else:
                self.products.append((product_title, quantity, flavor1))

            messagebox.showinfo("Success", "Product added to cart!")
            self.show_categories()
            self.carrito_compras()

    def carrito_compras(self):
        self.carrito_treeview.delete(*self.carrito_treeview.get_children())
        self.root.config(bg=color_terciario)

        for product in self.products:
            product_title = product[0]
            quantity = int(product[1])
            flavors = ", ".join(product[2:])
            price = self.get_product_price(product_title)
            total_price = quantity * price
            self.carrito_treeview.insert(
                "", "end", text=product_title, values=(flavors, quantity, total_price)
            )

        total = self.calculate_total()
        self.total_textbox.configure(state="normal")
        self.total_textbox.delete(0, "end")
        self.total_textbox.insert(0, total)
        self.total_textbox.configure(state="readonly")

    def get_product_price(self, product_title):
        for category in categories.values():
            for product in category:
                if product["title"] == product_title:
                    price = product["price"]
                    price = price.replace("$", "").replace(",", "")
                    return int(price)

    def remove_selected_product(self):
        selection = self.carrito_treeview.selection()
        if selection:
            item = self.carrito_treeview.item(selection)
            product_title = item["text"]
            for i, product in enumerate(self.products):
                if product[0] == product_title:
                    del self.products[i]
                    break
            self.carrito_treeview.delete(selection)

            total = self.calculate_total()
            self.total_textbox.configure(state="normal")
            self.total_textbox.delete(0, "end")
            self.total_textbox.insert(0, total)
            self.total_textbox.configure(state="readonly")
        else:
            messagebox.showerror("Error", "Please select a product to remove.")

    def calculate_total(self):
        total = 0
        for product in self.products:
            product_title = product[0]
            quantity = int(product[1])
            price = self.get_product_price(product_title)
            total += quantity * price
        return total

    def show_categories(self, canvas=None):
        self.current_category = None
        if canvas!=None:
            canvas.destroy()
        if self.details_frame:
            self.details_frame.pack_forget()

        self.category_frame.pack()
        self.product_frame.pack_forget()
        self.selected_category_label.configure(text="")
        self.root.config(bg=color_terciario)

    def herramientas(self):
        self.root.configure(bg=color_terciario)
        self.root.title("Usuario")

        # Crear una barra de herramientas
        barra = tk.Menu(self.root)
        self.root.config(menu=barra)

        # Agregar botones a la barra de herramientas
        usuario_menu = tk.Menu(barra, tearoff=0)
        compra = tk.Menu(barra, tearoff=0)
        pedido = tk.Menu(barra, tearoff=0)
        usuario_menu.add_command(
            label="Modificar Usuario",
            command=lambda usuario=self.usuario: self.editar_usuario(usuario),
        )
        compra.add_command(label="Compra en Linea",
                           command=self.Ventana_principal)
        pedido.add_command(label="Pedidos", command=self.view_pending_orders)
        barra.add_cascade(label="Usuario", menu=usuario_menu)
        barra.add_cascade(label="Comprar", menu=compra)
        barra.add_cascade(label="Pedidos", menu=pedido)
        # Crear un botón de regresar
        image = Image.open("BotonVolver.png")
        nuevo_tamaño = (40, 40)
        imagen_nueva = image.resize(nuevo_tamaño)
        background_image = ImageTk.PhotoImage(imagen_nueva)
        button_regresar = tk.Button(
            self.root,
            image=background_image,
            command=lambda: self.volver(),
            bg=color_terciario,
        )
        button_regresar.image = background_image
        button_regresar.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

    def volver_inicio_sesion(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.mostrar_ventana_inicio_sesion()

    def show_pending_orders(self):
        if self.carrito_treeview.get_children():
            answer = messagebox.askyesno(
                "Confirmation", "Do you want to create an invoice for pending orders?"
            )
            if answer:
                

                invoice = self.create_invoice(self.metodoPago)
                pending_orders.append(invoice)
                messagebox.showinfo("Pending Orders", invoice)
                self.clear_cart()
        else:
            messagebox.showinfo("No Pending Orders",
                                "There are no pending orders.")

    def clear_cart(self):
        self.carrito_treeview.delete(*self.carrito_treeview.get_children())
        self.root.config(bg=color_terciario)
        self.total_textbox.configure(state="normal")
        self.total_textbox.delete(0, "end")
        self.total_textbox.configure(state="readonly")

    def create_invoice(self, paymenth_method):
        filas_adicionales = []
        invoice = ""
        total = 0
        Producto_Factura_Individual = []
        Producto_Factura_Conjunta = []
        Producto_Factura_Conjunta_Filtro = []
        Producto_Factura_Total = []
        productos = []
        for item in self.carrito_treeview.get_children():
            product = self.carrito_treeview.item(item)
            product_title = product["text"]
            flavors = product["values"][0]
            quantity = product["values"][1]
            total_price = product["values"][2]
            Producto_Factura_Individual.append(product_title)
            Producto_Factura_Individual.append(flavors)
            Producto_Factura_Individual.append(quantity)
            Producto_Factura_Individual.append(total_price)
            Producto_Factura_Conjunta.append(Producto_Factura_Individual)
            total += total_price
            invoice += f"Product: {product_title}\n"
            invoice += f"Flavors: {flavors}\n"
            invoice += f"Quantity: {quantity}\n"
            invoice += f"Total Price: {total_price}\n"
            invoice += "------------------------\n"
            producto = {"tamaño": product_title,
                        "sabor": flavors, "precio": total_price}
            productos.append(producto)
        invoice += f"Total: {total}\n"
        Producto_Factura_Conjunta_Filtro.append(Producto_Factura_Conjunta[0])
        Producto_Factura_Total.append(Producto_Factura_Conjunta_Filtro)
        Producto_Factura_Total.append(total)

        print(Producto_Factura_Total, "aquí es")
        lista.append(invoice)
        print(lista)

        filas_adicionales.append(len(facturas)+1)
        filas_adicionales.append(self.usuario[0])
        filas_adicionales.append(datetime.date.today().strftime("%d/%m/%Y"))
        filas_adicionales.append(productos)
        filas_adicionales.append(paymenth_method)
        filas_adicionales.append({"Total": total})
        print(filas_adicionales) 
        filas.append(filas_adicionales)
        print(filas)

        return invoice

    def view_pending_orders(self):
        if pending_orders:
            orders = "\n".join(pending_orders)
            messagebox.showinfo("Pending Orders", orders)
            self.actualizar_tabla(self.root)
        else:
            messagebox.showinfo("No Pending Orders",
                                "There are no pending orders.")

    # ----- Pedidos pendientes
    def actualizar_tabla(self, root):
        # Eliminar todos los widgets de la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        self.herramientas()

        # Crear títulos de la tabla
        titulos = [
            "ID",
            "Correo",
            "Fecha",
            "Detalles",
            "Tipo de pago",
            "Total",
            "Cancelar Pedido",
        ]
        
        # Crear un contenedor para los títulos
        titulo_frame = ttk.Frame(root)
        titulo_frame.pack()

        for i, titulo in enumerate(titulos):
            label = ttk.Label(titulo_frame, text=titulo, background=color_terciario)
            label.pack(side="left", padx=5, pady=5)

        # Crear contenido de la tabla
        for fila in filas:
            fila_frame = ttk.Frame(root)
            fila_frame.pack()

            for j, valor in enumerate(fila):
                if j == 3:
                    detalles = ""
                    for obj in valor:
                        detalles += f"tamaño: {obj['tamaño']}\n"
                        detalles += f"sabor: {obj['sabor']}\n"
                        detalles += f"precio: {obj['precio']}\n"
                    btn_detalles = ttk.Button(
                        fila_frame,
                        text="Detalles",
                        command=lambda detalles=detalles: messagebox.showinfo(
                            "Detalles", detalles),
                        style="TButton",
                    )
                    btn_detalles.pack(side="left", padx=5, pady=5)
                elif j == 5:
                    if isinstance(valor, dict):
                        valor_dict = dict(valor)
                        value = valor_dict.get("Total", "")
                        label = ttk.Label(fila_frame, text=value, background=color_terciario)
                        label.pack(side="left", padx=5, pady=5)
                else:
                    if isinstance(valor, dict):
                        if j == 4:
                            valor = valor.get("tamaño", "")
                        elif j == 5:
                            valor = valor.get("precio", "")
                    label = ttk.Label(fila_frame, text=valor, background=color_terciario)
                    label.pack(side="left", padx=5, pady=5)

            # Crear botones de pedido
            seccion_pedido = ttk.Frame(fila_frame)
            seccion_pedido.pack(side="left", padx=5, pady=5)

            btn_cancelar = ttk.Button(
                seccion_pedido,
                text="Cancelar Pedido",
                command=lambda fila=fila: self.cancelar_pedido(fila),
                style="TButton",
            )
            btn_cancelar.pack(side="left", padx=5, pady=5)

        # Botón "volver menu"
        btn_volver_menu = ttk.Button(
            root,
            text="Volver al menú",
            command=lambda: self.remover_ver_pedidos(),
            style="TButton",
        )
        btn_volver_menu.pack(padx=5, pady=5)

        # Establecer colores a los botones
        style = ttk.Style()
        style.configure("TButton", background=color_secundario)
        style.configure("TButton.TLabel", background=color_principal)



    def aceptar_pedido(self, fila):
        # Lógica para aceptar el pedido
        pedidos_aceptados.append(
            fila
        )  # Guardar los datos de la fila en la lista de pedidos aceptados
        filas.remove(
            fila
        )  # Remover la fila de la lista de filas  # Actualizar la tabla en la interfaz
        print("Pedido aceptado")
        print(filas)
        print(pedidos_aceptados)
        self.actualizar_tabla(self.root)

    def cancelar_pedido(self, fila):
        # Lógica para cancelar el pedido
        filas.remove(fila)  # Remover la fila de la lista de filas

        # Sumar 1 a la posición 4 del usuario correspondiente
        for usuario in usuarios:
            if usuario[0] == self.usuario[0]:
                usuario[4] += 1

        print("Pedido cancelado")
        self.actualizar_tabla(self.root)

    def ver_detalles(self, detalles):
        # Imprimir los detalles del pedido
        messagebox.showinfo("Pending Orders", detalles)

    # ------ pedidos para entregar
    def view_entregar_orders(self):
        if pending_orders:
            orders = "\n".join(pending_orders)
            messagebox.showinfo("Pending Orders", orders)

            self.actualizar_tabla2(self.root)
        else:
            messagebox.showinfo("No Pending Orders",
                                "There are no pending orders.")

    def actualizar_tabla2(self, root):
        # Eliminar todos los widgets de la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_menu()
        # Crear títulos de la tabla
        titulos = ["Correo", "Fecha", "Detalles", "Total", "Entregar pedido"]
        for i, titulo in enumerate(titulos):
            label = tk.Label(root, text=titulo)
            label.grid(row=0, column=i, padx=5, pady=5)

        # Crear contenido de la tabla
        for i, fila in enumerate(pedidos_aceptados):
            for j, valor in enumerate(pedidos_aceptados):
                if j == 2:
                    btn_detalles = ttk.Button(
                        root,
                        text="Detalles",
                        command=lambda detalles=valor: self.ver_detalles2(
                            detalles),
                    )
                    btn_detalles.grid(row=i + 1, column=j, padx=5, pady=5)
                else:
                    label = ttk.Label(root, text=valor)
                    label.grid(row=i + 1, column=j, padx=5, pady=5)

            # Crear botones de pedido
            seccion_pedido = ttk.Frame(root)
            seccion_pedido.grid(row=i + 1, column=4,
                                columnspan=2, padx=5, pady=5)

            btn_aceptar = ttk.Button(
                seccion_pedido,
                text="Entregar pedido",
                command=lambda fila=fila: self.aceptar_pedido2(fila),
            )

            btn_aceptar.pack(side="left", padx=5, pady=5)

        # Obtener el número de filas actuales
        num_filas_actuales = len(filas)

        # Botón "volver menu"
        btn_volver_menu = ttk.Button(
            root, text="Volver al menu", command=lambda: self.remover_ver_pedidos()
        )
        btn_volver_menu.grid(
            row=num_filas_actuales + 1, column=0, columnspan=6, padx=5, pady=5
        )

    def aceptar_pedido2(self, fila):
        # Lógica para aceptar el pedido
        facturas.append(
            fila
        )  # Guardar los datos de la fila en la lista de pedidos aceptados
        pedidos_aceptados.remove(
            fila
        )  # Remover la fila de la lista de filas  # Actualizar la tabla en la interfaz
        print("Pedido aceptado")
        print(filas)
        print(pedidos_aceptados)
        print(facturas)
        self.actualizar_tabla(self.root)

    def ver_detalles2(self, detalles):
        # Imprimir los detalles del pedido
        messagebox.showinfo("Pending Orders", detalles)

    def remover_ver_pedidos(self):
        self.Ventana_principal()

    def Ventana_Usuario(self, usuario1):
        self.usuario = usuario1
        self.root.configure(bg=color_terciario)
        self.root.title("Usuario")

        # Crear una barra de herramientas
        barra = tk.Menu(self.root)
        self.root.config(menu=barra)

        # Agregar botones a la barra de herramientas
        usuario_menu = tk.Menu(barra, tearoff=0)
        compra = tk.Menu(barra, tearoff=0)
        pedido = tk.Menu(barra, tearoff=0)
        usuario_menu.add_command(
            label="Modificar Usuario",
            command=lambda usuario=usuario1: self.editar_usuario(usuario),
        )
        compra.add_command(label="Compra en Linea",
                           command=self.Ventana_principal)
        pedido.add_command(label="Ver pedidos pendientes",
                           command=self.show_pending_orders)
        barra.add_cascade(label="Usuario", menu=usuario_menu)
        barra.add_cascade(label="Comprar", menu=compra)
        barra.add_cascade(label="Pedidos", menu=pedido)
        # Crear un botón de regresar
        image = Image.open("BotonVolver.png")
        nuevo_tamaño = (40, 40)
        imagen_nueva = image.resize(nuevo_tamaño)
        background_image = ImageTk.PhotoImage(imagen_nueva)
        button_regresar = tk.Button(
            self.root,
            image=background_image,
            command=lambda: self.volver(),
            bg=color_terciario,
        )
        button_regresar.image = background_image
        button_regresar.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)
        self.Ventana_principal()

    def volver(self):
        self.root.destroy()  # Destruir la ventana actual
        main = Inicio()  # Crear una nueva instancia de la clase Inicio
        main.root.mainloop()

    def editar_usuario(self, usuario1):
        # Destruir la tabla de cajeros si ya existe
        for widget in self.root.winfo_children():
            widget.destroy()

        self.Ventana_Usuario(usuario1)

        # Crear el formulario de editar cajero
        form_frame = tk.Frame(self.root, bg=color_terciario, bd=0)
        form_frame.pack(
            side=tk.TOP, padx=10, pady=(100, 10), ipadx=10, ipady=10, anchor="center"
        )

        # Título del formulario
        titulo = tk.Label(
            form_frame,
            text="Editar usuario",
            font=("Arial", 14, "bold"),
            bg=color_terciario,
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Obtener los datos del cajero seleccionado
        correo = usuario1[0]
        contrasena = usuario1[1]
        nombre = usuario1[3][0]
        documento = usuario1[3][1]
        telefono = usuario1[3][3]
        direccion = usuario1[3][4]

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
        # Rellenar el campo con el documento del usuario
        numero_doc_entry.insert(tk.END, documento)
        numero_doc_entry.grid(row=2, column=1, padx=5, pady=5)

        correo_label = tk.Label(
            form_frame, text="Correo:", font=("Arial", 12), bg=color_terciario
        )
        correo_label.grid(row=3, column=0, padx=5, pady=5)
        correo_entry = tk.Entry(form_frame, font=("Arial", 12))
        # Rellenar el campo con el correo del usuario
        correo_entry.insert(tk.END, correo)
        correo_entry.grid(row=3, column=1, padx=5, pady=5)

        contrasena_label = tk.Label(
            form_frame, text="Contraseña:", font=("Arial", 12), bg=color_terciario
        )
        contrasena_label.grid(row=4, column=0, padx=5, pady=5)
        contrasena_entry = tk.Entry(form_frame, font=("Arial", 12))
        # Rellenar el campo con la contraseña del cajero
        contrasena_entry.insert(tk.END, contrasena)
        contrasena_entry.grid(row=4, column=1, padx=5, pady=5)

        telefono_label = tk.Label(
            form_frame, text="Telefono:", font=("Arial", 12), bg=color_terciario
        )
        telefono_label.grid(row=5, column=0, padx=5, pady=5)
        telefono_entry = tk.Entry(form_frame, font=("Arial", 12))
        # Rellenar el campo con el correo del cajero
        telefono_entry.insert(tk.END, telefono)
        telefono_entry.grid(row=5, column=1, padx=5, pady=5)
        # Botón de actualizar cajero
        direccion_label = tk.Label(
            form_frame, text="Direccion:", font=("Arial", 12), bg=color_terciario
        )
        direccion_label.grid(row=6, column=0, padx=5, pady=5)
        direccion_entry = tk.Entry(form_frame, font=("Arial", 12))
        # Rellenar el campo con el correo del cajero
        direccion_entry.insert(tk.END, direccion)
        direccion_entry.grid(row=6, column=1, padx=5, pady=5)

        actualizar_usuario_button = tk.Button(
            form_frame,
            text="Actualizar Usuario",
            font=("Arial", 12, "bold"),
            bg="green",
            command=lambda: self.actualizar_usuario(
                usuario1,
                nombre_entry.get(),
                numero_doc_entry.get(),
                correo_entry.get(),
                contrasena_entry.get(),
                telefono_entry.get(),
                direccion_entry.get(),
            ),
        )
        actualizar_usuario_button.grid(row=7, column=0, columnspan=2, pady=10)

    def actualizar_usuario(
        self,
        usuario1,
        nombre,
        numero_documento,
        correo,
        contrasena,
        telefono,
        direccion,
    ):
        # Verificar campos vacíos
        if (
            nombre == ""
            or numero_documento == ""
            or correo == ""
            or contrasena == ""
            or telefono == ""
            or direccion == ""
        ):
            messagebox.showerror(
                "Error", "Por favor, complete todos los campos.")
            return

        # Verificar correo válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "El correo ingresado es inválido.")
            return
        if not telefono.isdigit() or len(telefono) != 10:
            messagebox.showerror(
                "Error", "Por favor, marque un telefono valido.")
            return
        # Verificar documento válido
        if (
            not numero_documento.isdigit()
            or len(numero_documento) < 9
            or len(numero_documento) > 10
        ):
            messagebox.showerror(
                "Error", "El número de documento ingresado es inválido."
            )
            return

        # Verificar duplicados de documento y correo
        for comprobar in usuarios:
            if comprobar != usuario1:
                if comprobar[0] == correo:
                    messagebox.showerror("Error", "El correo ya está en uso.")
                    return
                if comprobar[3][1] == numero_documento:
                    messagebox.showerror(
                        "Error", "El número de documento ya existe.")
                    return
                if comprobar[3][3] == telefono:
                    messagebox.showerror(
                        "Error", "El número de telefono ya existe ")
        # Actualizar los datos del cajero
        usuario1[0] = correo
        usuario1[1] = contrasena
        usuario1[3][0] = nombre
        usuario1[3][1] = numero_documento
        usuario1[3][3] = telefono
        usuario1[3][4] = direccion

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")

        # Destruir el formulario de editar cajero y recrear la tabla de cajeros
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
        self.Ventana_Usuario(usuario1)

    def Opcion_no(self, usuario1):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.Ventana_Usuario(usuario1)


class Inicio:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.usuario = Usuario(self.root)
        self.Inicio_sesion()
        # self.Pruebas()
        pass

    def Pruebas(self):
        self.root.configure(bg="SystemButtonFace")
        # Cargar la imagen del icono
        # Ruta de la imagen del ícono
        self.root.title("Inicio de sesión")
        self.root.geometry("800x600")
        icon_photo = tk.PhotoImage(file="Icono.png")
        # Establecer la imagen como icono de la ventana

        self.root.iconphoto(False, icon_photo)
        # Crear la imagen de fondo
        self.image = Image.open("./Logo.png")
        self.background_image = ImageTk.PhotoImage(self.image)
        # Crear el widget Label con la imagen de fondo
        self.background_label = tk.Label(
            self.root, image=self.background_image)
        self.background_label.place(x=0, y=-150, relwidth=1, relheight=1)

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
                    for widget in root.winfo_children():
                        widget.destroy()
                    Cajero(root).Ventana_principal(i)
                    break
                if i[2] == "usuario":
                    if len(i) > 4 and i[4] > 3:
                        label_baneado = tk.Label(root, text="¡Estás baneado!")
                        label_baneado.pack(padx=5, pady=5)
                    else:
                        for widget in root.winfo_children():
                            widget.destroy()
                        self.usuario.Ventana_Usuario(i)
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
                command=self.Registro,
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

    def Registro(self):
        # Destruir los botones de registro
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        # Crear un formulario de registro similar al de crear cajero
        form_frame = tk.Frame(self.root)
        form_frame.place(relx=0.5, rely=0.62, anchor=tk.CENTER)

        # Título del formulario
        titulo = tk.Label(form_frame, text="Registro",
                          font=("Arial", 14, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Etiquetas y campos de entrada
        correo_label = tk.Label(
            form_frame, text="Correo:", font=("Arial", 12, "bold"))
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
            form_frame, text="Nombre:", font=("Arial", 12, "bold"))
        nombre_label.grid(row=3, column=0, padx=5, pady=5)
        nombre_entry = tk.Entry(form_frame, font=("Arial", 12))
        nombre_entry.grid(row=3, column=1, padx=5, pady=5)

        cedula_label = tk.Label(
            form_frame, text="Cédula:", font=("Arial", 12, "bold"))
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
                direccion_entry.get(),
            ),
        )
        crear_button.grid(row=7, column=2, padx=5, pady=5)

        # Botón de volver
        volver_button = tk.Button(
            form_frame,
            text="Volver",
            font=("Arial", 12),
            command=lambda: self.Opcion_no(),
        )
        volver_button.grid(row=7, column=0, padx=5, pady=5)

    def mostrar_ventana_principal(self):
        # Destruir los botones de registro
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        # Crear los botones de la ventana principal
        btn_nuevo_usuario = tk.Button(
            self.root, text="Nuevo Usuario", font=("Arial", 12), command=self.Registro
        )
        btn_nuevo_usuario.pack(pady=10)

        btn_salir = tk.Button(
            self.root, text="Salir", font=("Arial", 12), command=self.root.quit
        )
        btn_salir.pack()

    def registrar_usuario(
        self, correo, contrasena, nombre, cedula, telefono, direccion
    ):
        if (
            not correo
            or not contrasena
            or not nombre
            or not cedula
            or not telefono
            or not direccion
        ):
            messagebox.showwarning(
                "Campos Incompletos", "Por favor complete todos los campos."
            )
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showwarning(
                "Correo Inválido", "Por favor ingrese un correo válido."
            )
            return
        if nombre == "" or cedula == "" or correo == "" or contrasena == "":
            messagebox.showerror(
                "Error", "Por favor, complete todos los campos.")
            return
        if not telefono.isdigit() or len(telefono) != 10:
            messagebox.showerror(
                "Error", "Por favor, marque un telefono valido.")
            return

        # Verificar correo válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "El correo ingresado es inválido.")
            return

        # Verificar documento válido
        if not cedula.isdigit() or len(cedula) < 9 or len(cedula) > 10:
            messagebox.showerror(
                "Error", "El número de documento ingresado es inválido."
            )
            return

        # Verificar duplciados de documento y correo
        for usuario in usuarios:
            if usuario[0] == correo:
                messagebox.showerror("Error", "El correo ya está en uso.")
                return
            if usuario[3][1] == cedula:
                messagebox.showerror(
                    "Error", "El número de documento ya existe.")
                return
            if len(usuario) > 3 and usuario[3][3] == telefono:
                messagebox.showerror("Error", "El telefono ya esta en uso")
                return
        usuarios.append(
            [correo, contrasena, "usuario", [
                nombre, cedula, True, telefono, direccion], 0]
        )
        messagebox.showinfo(
            "Registro Exitoso", "El usuario ha sido registrado exitosamente."
        )

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
        self.root.title("Inicio de sesión")
        self.root.geometry("800x600")
        icon_photo = tk.PhotoImage(file="Icono.png")
        # Establecer la imagen como icono de la ventana

        self.root.iconphoto(False, icon_photo)
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
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        self.root.mainloop()


main = Inicio()
main.root.mainloop()
