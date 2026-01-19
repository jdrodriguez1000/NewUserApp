import flet as ft
import asyncio
import re
from core.i18n import I18n
from controllers.auth_controller import AuthController

class ChangePasswordView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_controller = AuthController()
        
        # UI Inputs
        self.password_input = ft.TextField(
            label=I18n.t("auth.new_password"),
            prefix_icon=ft.Icons.LOCK_OUTLINED,
            password=True,
            can_reveal_password=True,
            border_radius=12,
        )
        self.confirm_password_input = ft.TextField(
            label=I18n.t("auth.confirm_new_password"),
            prefix_icon=ft.Icons.LOCK_RESET_OUTLINED,
            password=True,
            can_reveal_password=True,
            border_radius=12,
        )
        self.status_text = ft.Text("", color=ft.Colors.RED)

    async def handle_change_password(self, e):
        password = self.password_input.value or ""
        confirm_password = self.confirm_password_input.value or ""
        
        if not password or len(password) < 8:
            self.password_input.error_text = I18n.t("auth.error_password_security")
            self.page.update()
            return
        
        if password != confirm_password:
            self.confirm_password_input.error_text = I18n.t("auth.error_password_match")
            self.page.update()
            return

        e.control.disabled = True
        self.page.update()

        print("DEBUG: [ChangePassword] Iniciando flujo de actualización...")
        
        # Intentamos obtener usuario (Supabase debería detectarlo si el token está en el navegador)
        try:
            res = self.auth_controller.update_password(password)
            if res["success"]:
                self.show_message(I18n.t("auth.password_changed_success"), color=ft.Colors.GREEN_700)
                await asyncio.sleep(2)
                self.page.data["router"].navigate("/login")
            else:
                self.show_error(f"Error: {res['error']}")
                e.control.disabled = False
                self.page.update()
        except Exception as ex:
            self.show_error(f"Error fatal: {ex}")
            e.control.disabled = False
            self.page.update()

    def show_error(self, message):
        snack = ft.SnackBar(content=ft.Text(str(message)), bgcolor=ft.Colors.RED_700)
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def show_message(self, message, color=ft.Colors.BLUE_700):
        snack = ft.SnackBar(content=ft.Text(str(message)), bgcolor=color)
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def render(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=40),
                    ft.Icon(ft.Icons.LOCK_OPEN_ROUNDED, size=80, color=ft.Colors.BLUE_600),
                    ft.Text(I18n.t("auth.change_password_title"), size=28, weight=ft.FontWeight.BOLD),
                    ft.Text(I18n.t("auth.change_password_subtitle"), color=ft.Colors.GREY_700),
                    ft.Container(height=20),
                    self.password_input,
                    self.confirm_password_input,
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        content=ft.Text(I18n.t("auth.change_password_button"), weight=ft.FontWeight.BOLD),
                        on_click=self.handle_change_password,
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_600,
                            shape=ft.RoundedRectangleBorder(radius=12),
                            elevation=4,
                        ),
                        height=50,
                        width=320,
                    ),
                    ft.Container(expand=True),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            expand=True,
            alignment=ft.Alignment(0, 0)
        )
