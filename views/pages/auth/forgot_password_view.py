import flet as ft
from core.i18n import I18n
from controllers.auth_controller import AuthController

class ForgotPasswordView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_controller = AuthController()
        
        # UI Inputs
        self.email_input = ft.TextField(
            label=I18n.t("auth.email"),
            prefix_icon=ft.Icons.EMAIL_OUTLINED,
            keyboard_type=ft.KeyboardType.EMAIL,
            border_radius=12,
        )

    def handle_reset_request(self, e):
        email = (self.email_input.value or "").strip()
        
        if not email:
            self.email_input.error_text = I18n.t("auth.error_required_fields")
            self.email_input.update()
            return
            
        if "@" not in email:
            self.email_input.error_text = I18n.t("auth.error_invalid_email")
            self.email_input.update()
            return

        self.email_input.error_text = None
        e.control.disabled = True
        self.page.update()

        result = self.auth_controller.send_reset_password_email(email)
        
        if result["success"]:
            self.show_message(I18n.t("auth.password_reset_success"), color=ft.Colors.GREEN_700)
            # After success, we could redirect or keep them there
        else:
            self.show_error(str(result["error"]))
            e.control.disabled = False
            self.page.update()

    def show_error(self, message):
        snack = ft.SnackBar(
            content=ft.Text(str(message), color=ft.Colors.WHITE),
            bgcolor=ft.Colors.RED_700,
            action="OK",
        )
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def show_message(self, message, color=ft.Colors.BLUE_700):
        snack = ft.SnackBar(
            content=ft.Text(str(message), color=ft.Colors.WHITE),
            bgcolor=color,
            action="OK",
        )
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def render(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=40),
                    ft.Icon(ft.Icons.LOCK_RESET_ROUNDED, size=80, color=ft.Colors.BLUE_600),
                    ft.Text(
                        I18n.t("auth.reset_password"),
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        I18n.t("auth.instructions_forgot"),
                        size=16,
                        color=ft.Colors.BLUE_GREY_400,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=30),
                    self.email_input,
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        content=ft.Text(I18n.t("auth.send_email"), weight=ft.FontWeight.BOLD),
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_600,
                            padding=ft.Padding.all(20),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            elevation=4,
                        ),
                        width=320,
                        on_click=self.handle_reset_request
                    ),
                    ft.Container(expand=True),
                    ft.TextButton(
                        I18n.t("auth.back_to_login"),
                        on_click=lambda _: self.page.data["router"].navigate("/login")
                    ),
                    ft.Container(height=20),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            expand=True,
            bgcolor=ft.Colors.GREY_50
        )
