import flet as ft
from core.i18n import I18n

class VerifyEmailView:
    def __init__(self, page: ft.Page):
        self.page = page

    def render(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=80),
                    ft.Icon(
                        ft.Icons.MARK_EMAIL_READ_ROUNDED,
                        size=100,
                        color=ft.Colors.BLUE_600
                    ),
                    ft.Container(height=30),
                    ft.Text(
                        I18n.t("auth.verify_email"),
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        I18n.t("auth.verification_pending"),
                        size=16,
                        color=ft.Colors.BLUE_GREY_400,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=40),
                    ft.Button(
                        content=ft.Text("Ir al Login", weight=ft.FontWeight.BOLD),
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_600,
                            padding=ft.Padding.all(20),
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                        width=250,
                        on_click=lambda _: self.page.data["router"].navigate("/login")
                    ),
                    ft.Container(expand=True),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=40,
            expand=True,
            bgcolor=ft.Colors.GREY_50
        )
