import tkinter as tk

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


class Admin:
    def __init__(self):
        self.usuario = "usuario"

    def Ventana_Principal(self, root):
        root.configure(bg="SystemButtonFace")
        root.title("Barra de Herramientas")

        # Crear una barra de herramientas
        barra = tk.Menu(root)
        root.config(menu=barra)

        # Agregar botones a la barra de herramientas
        barra.add_command(label="Opción 1", command=self.opcion1)
        barra.add_command(label="Opción 2", command=self.opcion2)
        barra.add_command(label="Opción 3", command=self.opcion3)
        barra.add_command(label="Opción 4", command=self.opcion4)

        # Etiqueta para mostrar la opción seleccionada
        self.label = tk.Label(root, text="Seleccione una opción")
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
        self.usuario = entry_usuario.get()
        self.contraseña = entry_contraseña.get()
        pass


def login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

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
            bg=color_principal,
        )


root = tk.Tk()
root.title("Inicio de sesión")
root.geometry("300x200")

# Colores
color_principal = "#FF6D60"
color_secundario = "#F7D060"
color_terciario = "#F3E99F"
color_cuarto = "#98D8AA"

root.configure(bg=color_principal)

# Etiquetas
label_title = tk.Label(
    root, text="Inicio de sesión", font=("Arial", 16), bg=color_principal, fg="white"
)
label_title.pack(pady=10)

label_username = tk.Label(root, text="Usuario:",
                          bg=color_principal, fg="white")
label_username.pack()

# Entradas de texto
entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_password = tk.Label(root, text="Contraseña:",
                          bg=color_principal, fg="white")
label_password.pack()

entry_contraseña = tk.Entry(root, show="*")
entry_contraseña.pack()

label_status = tk.Label(root, text="", bg=color_principal, fg="white")
label_status.pack(pady=5)

# Botón
button_login = tk.Button(
    root,
    text="Iniciar sesión",
    command=login,
    bg=color_secundario,
    fg="white",
    activebackground=color_cuarto,
    activeforeground="white",
)
button_login.pack(pady=10)

root.mainloop()
