import tkinter as tk
import re
from tkinter import messagebox
from PIL import Image, ImageTk


usuarios = [
    ["admin@email.com", "admin123", "admin", ["", "", True, "", ""]],
    ["cajero1@email.com", "cajero1", "cajero", ["prueba", "123456789", True, "", ""]],
    ["cajero2@email.com", "cajero2", "cajero", ["prueba2", "1234567891", True, "", ""]],
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
        pass

    def volver(self):
        self.root.destroy()  # Destruir la ventana actual
        main = Inicio()  # Crear una nueva instancia de la clase Inicio
        main.root.mainloop()

    def Ventana_Principal(self):
        self.root.configure(bg=color_terciario)
        self.root.title("Barra de Herramientas")

        # Crear una barra de herramientas
        barra = tk.Menu(self.root)
        self.root.config(menu=barra)

        # Agregar botones a la barra de herramientas
        cajero_menu = tk.Menu(barra, tearoff=0)
        cajero_menu.add_command(label="Ver Cajeros", command=self.Cajeros)
        cajero_menu.add_command(label="Agregar Cajero", command=self.AgregarCajero)

        barra.add_cascade(label="Cajero", menu=cajero_menu)
        barra.add_command(label="Opción 2", command=self.opcion2)
        barra.add_command(label="Opción 3", command=self.opcion3)
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

        self.Cajeros()

    def Cajeros(self):
        # Destruir el formulario de agregar cajero si ya existe
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

        # Filtrar los usuarios que tengan el rol "cajero"
        cajeros = [cajero for cajero in usuarios if cajero[2] == "cajero"]

        # Crear la tabla de cajeros
        table_frame = tk.Frame(self.root, bg=color_terciario, bd=1, relief=tk.SOLID)
        table_frame.pack(padx=10, pady=(100, 10), ipadx=10, ipady=10)

        # Título de la tabla
        titulo = tk.Label(
            table_frame, text="Cajeros", font=("Arial", 14, "bold"), bg=color_terciario
        )
        titulo.grid(row=0, column=0, columnspan=4, pady=10)

        # Encabezados de las columnas
        correo_label = tk.Label(
            table_frame, text="Correo", font=("Arial", 12, "bold"), bg=color_terciario
        )
        correo_label.grid(row=1, column=0, padx=5, pady=5)

        eliminar_label = tk.Label(
            table_frame, text="Eliminar", font=("Arial", 12, "bold"), bg=color_terciario
        )
        eliminar_label.grid(row=1, column=2, padx=5, pady=5)

        editar_label = tk.Label(
            table_frame, text="Editar", font=("Arial", 12, "bold"), bg=color_terciario
        )
        editar_label.grid(row=1, column=3, padx=5, pady=5)

        # Mostrar datos de los cajeros en la tabla
        for i, cajero in enumerate(cajeros, start=2):
            correo = cajero[0]

            correo_label = tk.Label(table_frame, text=correo, bg=color_terciario)
            correo_label.grid(row=i, column=0, padx=(20, 5), pady=5)

            eliminar_button = tk.Button(
                table_frame,
                text="Eliminar",
                command=lambda c=cajero: self.eliminar_cajero(c),
                bg="red",
            )
            eliminar_button.grid(row=i, column=2, padx=5, pady=5)

            editar_button = tk.Button(
                table_frame,
                text="Editar",
                command=lambda c=cajero: self.editar_cajero(c),
                bg="blue",
            )
            editar_button.grid(row=i, column=3, padx=5, pady=5)


    def AgregarCajero(self):
        # Destruir la tabla de cajeros si ya existe
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

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
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Verificar correo válido
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "El correo ingresado es inválido.")
            return

        # Verificar documento válido
        if not numero_documento.isdigit() or len(numero_documento) < 9 or len(numero_documento) > 10:
            messagebox.showerror("Error", "El número de documento ingresado es inválido.")
            return
        
        #Verificar duplciados de documento y correo
        for usuario in usuarios:
            if usuario[0] == correo:
                messagebox.showerror("Error", "El correo ya está en uso.")
                return
            if usuario[3][1] == numero_documento:
                messagebox.showerror("Error", "El número de documento ya existe.")
                return

        nuevo_cajero = [correo, contrasena, "cajero", [nombre, "", True, numero_documento, ""]]
        usuarios.append(nuevo_cajero)
        print("Nuevo cajero agregado:", nuevo_cajero)

    def opcion2(self):
        self.label.config(text="Has seleccionado la opción 2")

    def opcion3(self):
        self.label.config(text="Has seleccionado la opción 3")

    def opcion4(self):
        self.label.config(text="Has seleccionado la opción 4")

    def es_correo_valido(self,correo):
        # Expresión regular para validar el correo electrónico
        patron_correo = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron_correo, correo)

    def es_documento_valido(self,documento):
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
        # Lógica para editar un cajero del arreglo de usuarios
        print("Editar cajero:", cajero)


class Cajero:
    def __init__(self) -> None:
        pass


class Usuario:
    def __init__(self, root) -> None:
        self.root=root
        pass
    def Ventana_Usuario(self):
        self.root.configure(bg=color_terciario)
        self.root.title("Barra de Herramientas")

        # Crear una barra de herramientas
        barra = tk.Menu(self.root)
        self.root.config(menu=barra)

        # Agregar botones a la barra de herramientas
        cajero_menu = tk.Menu(barra, tearoff=0)
        compra= tk.Menu(barra, tearoff=1)
        cajero_menu.add_command(label="Modificar Usuario",)
        compra.addcomand(label="Compra en Linea")
        compra.addcomand(label="Pagar en caja")
        compra.addcomand(label="Todo en caja")

        barra.add_cascade(label="Usuario", menu=cajero_menu)
        barra.add_cascade(label="Comprar", menu=compra)
        

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
                    for widget in root.winfo_children():
                        widget.destroy()
                    Usuario(root).Ventana_Usuario()
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
        self.background_label = tk.Label(self.root, image=self.background_image)
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
    def VentanaPrincipal(self):
        self.root.destroy()
        root = tk.Tk()
        app = Admin(root)
        app.Ventana_Principal()
        root.mainloop()


main = Inicio()
main.root.mainloop()