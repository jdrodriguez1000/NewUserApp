import flet as ft
from core.i18n import I18n

class WelcomeView:
    def __init__(self, page: ft.Page):
        self.page = page

    def render(self):
        return ft.Stack(
            [
                # Background Image
                ft.Image(
                    src="welcome_bg.png",
                    width=self.page.window.width,
                    height=self.page.window.height,
                    fit="cover",
                ),
                # Overlay Gradient/Darken
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.BLACK45,
                ),
                # Content
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(height=100), # Spacer
                            # Logo placeholder or Icon
                            ft.Container(
                                content=ft.Image(src="icon.png", width=100, height=100, border_radius=20),
                                alignment=ft.Alignment.CENTER,
                                margin=ft.Margin.only(bottom=20)
                            ),
                            ft.Text(
                                "NewUserApp",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            ft.Text(
                                I18n.t("welcome.title"),
                                size=28,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(height=20),
                            ft.Text(
                                I18n.t("welcome.description"),
                                size=16,
                                color=ft.Colors.WHITE70,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(expand=True),
                            # Get Started Button
                            ft.Container(
                                content=ft.Button(
                                    content=ft.Row(
                                        [
                                            ft.Text(I18n.t("welcome.get_started"), size=18, weight=ft.FontWeight.BOLD),
                                            ft.Icon(ft.Icons.ARROW_FORWARD_ROUNDED),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        tight=True,
                                    ),
                                    style=ft.ButtonStyle(
                                        color=ft.Colors.WHITE,
                                        bgcolor=ft.Colors.BLUE_600,
                                        padding=ft.Padding.all(25),
                                        shape=ft.RoundedRectangleBorder(radius=15),
                                        elevation=10,
                                    ),
                                    on_click=lambda _: print("Navigate to Register"),
                                    width=320,
                                ),
                                alignment=ft.Alignment.CENTER,
                                margin=ft.Margin.only(bottom=60)
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=30,
                    expand=True,
                ),
            ],
            expand=True,
        )
