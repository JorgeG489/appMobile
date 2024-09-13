from flet import *

def main(page: Page):
    # Crear los TextField y el botón dentro de la función main
    text_field_username = TextField(
        label="Nombre de usuario",
        width=300,
        bgcolor="white",
        border_color="black",
        border_radius=5,
        color="black"
    )

    text_field_password = TextField(
        label="Contraseña",
        width=300,
        password=True,
        bgcolor="white",
        border_color="black",
        border_radius=5,
    )

    # Crear el contenedor para el formulario de inicio de sesión
    login_container = Container(
        width=400,
        height=300,
        margin=20,
        padding=20,
        bgcolor="#6F78F2",
        border_radius=15,
        alignment=alignment.center,
        content=Column(
            controls=[
                Text("Iniciar sesión", size=24, weight="bold", color="white"),
                text_field_username,
                text_field_password,
                ElevatedButton(
                    text="Iniciar sesión",
                    on_click=lambda e: on_login_click(e, text_field_username, text_field_password, page),
                    bgcolor="#4C5BCA",
                    color="white",
                ),
            ],
            spacing=15
        )
    )
    
    # Agregar el contenedor a la página
    page.add(login_container)

def on_login_click(e, text_field_username, text_field_password, page):
    # Obtener el valor de los campos de texto
    user_input = text_field_username.value
    password_input = text_field_password.value
    
    # Verificar las credenciales
    if user_input == "admin" and password_input == "admin":
        # Limpiar la página y mostrar la página principal
        page.controls.clear()
        show_main_page(page)
    else:
        # Mostrar mensaje de error
        page.add(Text("Credenciales incorrectas", color="red"))

def show_main_page(page: Page):
    # Crear una nueva vista para la página principal
    main_container = Container(
        width=400,
        height=300,
        margin=20,
        padding=20,
        bgcolor="#4CAF50",  # Fondo general del contenedor
        border_radius=15,
        alignment=alignment.center,
        content=Column(
            controls=[
                Text("Bienvenido a la página principal", size=24, weight="bold", color="white"),
                ElevatedButton(
                    text="Cerrar sesión",
                    on_click=lambda e: show_login_page(page),
                    bgcolor="#f44336",
                    color="white",
                ),
            ],
            spacing=15
        )
    )
    
    # Agregar el contenedor a la página
    page.add(main_container)

def show_login_page(page: Page):
    # Limpiar la página y volver a mostrar el formulario de inicio de sesión
    page.controls.clear()
    main(page)

# Inicia la aplicación
app(target=main, view=AppView.FLET_APP)
