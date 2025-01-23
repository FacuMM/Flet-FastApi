import flet as ft
import requests

API_URL = "http://localhost:8000/users"  # Cambia a la URL del backend

def main(page: ft.Page):
    page.title = "Login App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    username = ft.TextField(label="Usuario")
    password = ft.TextField(label="Contraseña", password=True)
    mensaje = ft.Text(value="", color="red")

    def registrar_usuario(e):
        data = {"username": username.value, "password": password.value}
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            mensaje.value = "Usuario registrado exitosamente"
            mensaje.color = "green"
        else:
            mensaje.value = "Error al registrar"
            mensaje.color = "red"
        page.update()

    page.add(
        ft.Column(
            controls=[
                username,
                password,
                ft.ElevatedButton("Registrar", on_click=registrar_usuario),
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
