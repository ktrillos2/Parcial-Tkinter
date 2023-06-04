import tkinter as tk
from PIL import ImageTk, Image

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
    def __init__(self):
        pass

    def volver(self, root):
        for widget in root.winfo_children():
            widget.destroy()
        Inicio_sesion()

    def Ventana_Principal(self, root):
        root.configure(bg=color_terciario)
        root.title("Barra de Herramientas")

        # Crear una barra de herramientas
        barra = tk.Menu(root)
        root.config(menu=barra)

        # Agregar botones a la barra de herramientas
        barra.add_command(label="Opción 1", command=self.opcion1)
        barra.add_command(label="Opción 2", command=self.opcion2)
        barra.add_command(label="Opción 3", command=self.opcion3)
        barra.add_command(label="Opción 4", command=self.opcion4)

        # Crear un botón de regresar
        image = Image.open("./BotonVolver.png")
        nuevo_tamaño = (40, 40)
        imagen_nueva = image.resize(nuevo_tamaño)
        background_image = ImageTk.PhotoImage(imagen_nueva)
        button_regresar = tk.Button(
            root,
            text="Volver",
            image=background_image,
            command=lambda: self.volver(root),
        )
        button_regresar.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

        # Etiqueta para mostrar la opción seleccionada
        self.label = tk.Label(root, text="Seleccione una opción",bg=color_terciario)
        self.label.pack(padx=10, pady=10)

        root.mainloop()

    def opcion1(self):
        self.label.config(text="Has seleccionado la opción 1.")

    def opcion2(self):
        self.label.config(text="Has seleccionado la opción 2.")

    def opcion3(self):
        self.label.config(text="Has seleccionado la opción 3.")

    def opcion4(self):
        self.label.config(text="Has seleccionado la opción 4.")


class Cajero:
    def __init__(self) -> None:
        pass


class Usuario:
    def __init__(self) -> None:
        pass


def login(root, label_status, usuario, contraseña):

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
                Admin().Ventana_Principal(root)
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


def Inicio_sesion():
    root.configure(bg="SystemButtonFace")
    # Crear la imagen de fondo
    image = Image.open("./Logo.png")
    background_image = ImageTk.PhotoImage(image)
    # Crear el widget Label con la imagen de fondo
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=-150, relwidth=1, relheight=1)
    label_username = tk.Label(
        root, text="Usuario", fg="black", font=("Arial", 11, "bold")
    )
    label_username.pack(pady=(250, 0))
    # Entradas de texto
    entry_usuario = tk.Entry(root)
    entry_usuario.pack()
    label_password = tk.Label(
        root, text="Contraseña", fg="black", font=("Arial", 11, "bold")
    )
    label_password.pack()
    entry_contraseña = tk.Entry(root, show="*")
    entry_contraseña.pack()
    label_status = tk.Label(root, text="", fg="black")
    label_status.pack(pady=5)
    # Botón
    button_login = tk.Button(
        root,
        text="Iniciar sesión",
        command=lambda: login(root, label_status, entry_usuario, entry_contraseña),
        bg=color_secundario,
        fg="black",
        activebackground=color_cuarto,
        activeforeground="white",
    )
    button_login.pack(pady=5, ipadx=5, ipady=5)
    root.mainloop()


root = tk.Tk()
# Cargar la imagen del icono
icon_image = Image.open("./Icono.png")
icon_photo = ImageTk.PhotoImage(icon_image)

# Establecer la imagen como icono de la ventana
root.iconphoto(True, icon_photo)
root.title("Inicio de sesión")
root.geometry("800x600")
# Crear la imagen de fondo
image = Image.open("./Logo.png")
background_image = ImageTk.PhotoImage(image)
# Crear el widget Label con la imagen de fondo
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=-150, relwidth=1, relheight=1)
label_username = tk.Label(root, text="Usuario", fg="black", font=("Arial", 11, "bold"))
label_username.pack(pady=(250, 0))
# Entradas de texto
entry_usuario = tk.Entry(root)
entry_usuario.focus()
entry_usuario.pack()
label_password = tk.Label(
    root, text="Contraseña", fg="black", font=("Arial", 11, "bold")
)
label_password.pack()
entry_contraseña = tk.Entry(root, show="*")
entry_contraseña.pack()
label_status = tk.Label(root, text="", fg="black")
label_status.pack(pady=5)
# Botón
button_login = tk.Button(
    root,
    text="Iniciar sesión",
    command=lambda: login(root, label_status, entry_usuario.get(), entry_contraseña.get()),
    bg=color_secundario,
    fg="black",
)
button_login.pack(pady=5, ipadx=5, ipady=5)
root.bind(
    "<Return>", lambda event: login(root, label_status, entry_usuario.get(), entry_contraseña.get())
)
root.mainloop()
