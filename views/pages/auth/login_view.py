import flet as ft
from core.i18n import I18n
from controllers.auth_controller import AuthController

class LoginView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_controller = AuthController()
        self.email_input = ft.TextField(
            label=I18n.t("auth.email"),
            prefix_icon=ft.Icons.EMAIL_OUTLINED,
            keyboard_type=ft.KeyboardType.EMAIL,
            border_radius=12,
        )
        self.password_input = ft.TextField(
            label=I18n.t("auth.password"),
            prefix_icon=ft.Icons.LOCK_OUTLINED,
            password=True,
            can_reveal_password=True,
            border_radius=12,
        )

    def handle_login(self, _):
        email = self.email_input.value
        password = self.password_input.value
        
        if not email or not password:
            self.page.snack_bar = ft.SnackBar(ft.Text(I18n.t("common.error")))
            self.page.snack_bar.open = True
            self.page.update()
            return

        result = self.auth_controller.login(email, password)
        if result["success"]:
            # Redirect to Dashboard (Phase 8 logic)
            print("Login successful")
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text(f"{I18n.t('common.error')}: {result['error']}"))
            self.page.snack_bar.open = True
            self.page.update()

    def render(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=40),
                    # App Logo (Smaller)
                    ft.Image(src="icon.png", width=80, height=80, border_radius=15),
                    ft.Text(
                        I18n.t("auth.login"),
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    ),
                    ft.Text(
                        "Bienvenido de nuevo",
                        size=16,
                        color=ft.Colors.BLUE_GREY_400
                    ),
                    ft.Container(height=30),
                    self.email_input,
                    ft.Container(height=15),
                    self.password_input,
                    ft.Container(
                        content=ft.TextButton(
                            I18n.t("auth.forgot_password"),
                            on_click=lambda _: print("Navigate to Forgot Password")
                        ),
                        alignment=ft.Alignment.CENTER_RIGHT
                    ),
                    ft.Container(height=30),
                    ft.Button(
                        content=ft.Text(I18n.t("auth.login"), weight=ft.FontWeight.BOLD),
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_600,
                            padding=ft.Padding.all(20),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            elevation=4,
                        ),
                        width=320,
                        on_click=self.handle_login
                    ),
                    ft.Container(expand=True),
                    ft.Row(
                        [
                            ft.Text(I18n.t("auth.no_account")),
                            ft.TextButton(
                                I18n.t("auth.register"),
                                on_click=lambda _: self.page.data["router"].navigate("/register")
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Container(height=20),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            expand=True,
            bgcolor=ft.Colors.GREY_50
        )
