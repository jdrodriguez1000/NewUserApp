import flet as ft
from core.i18n import I18n
from controllers.auth_controller import AuthController

class RegisterView:
    def __init__(self, page: ft.Page):
        print("DEBUG: RegisterView Initialized - v6.0 (FINAL)")
        self.page = page
        self.auth_controller = AuthController()
        
        # UI Inputs
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
            hint_text="Mínimo 8 caracteres",
        )
        self.confirm_password_input = ft.TextField(
            label="Confirmar Contraseña",
            prefix_icon=ft.Icons.LOCK_RESET_OUTLINED,
            password=True,
            can_reveal_password=True,
            border_radius=12,
        )

    def handle_register(self, e):
        print("\n=== REGISTRO: Botón pulsado (v6.0) ===")
        
        # Reset visual state
        self.email_input.error_text = None
        self.password_input.error_text = None
        self.confirm_password_input.error_text = None
        self.email_input.border_color = None
        self.password_input.border_color = None
        self.confirm_password_input.border_color = None
        self.page.update()

        # Capture values
        email = (self.email_input.value or "").strip()
        password = self.password_input.value or ""
        confirm_password = self.confirm_password_input.value or ""
        
        has_error = False

        # Validations
        error_msg = ""
        
        if not email or not password or not confirm_password:
            error_msg = I18n.t("auth.error_required_fields")
            if not email:
                self.email_input.error_text = I18n.t("auth.error_required_fields")
                self.email_input.border_color = ft.Colors.RED_700
            if not password:
                self.password_input.error_text = I18n.t("auth.error_required_fields")
                self.password_input.border_color = ft.Colors.RED_700
            if not confirm_password:
                self.confirm_password_input.error_text = I18n.t("auth.error_required_fields")
                self.confirm_password_input.border_color = ft.Colors.RED_700
            has_error = True
        elif "@" not in email:
            error_msg = I18n.t("auth.error_invalid_email")
            self.email_input.error_text = I18n.t("auth.error_invalid_email")
            self.email_input.border_color = ft.Colors.RED_700
            has_error = True
        elif len(password) < 8:
            error_msg = I18n.t("auth.error_password_security")
            self.password_input.error_text = I18n.t("auth.error_password_security")
            self.password_input.border_color = ft.Colors.RED_700
            has_error = True
        elif password != confirm_password:
            error_msg = I18n.t("auth.error_password_match")
            self.confirm_password_input.error_text = I18n.t("auth.error_password_match")
            self.confirm_password_input.border_color = ft.Colors.RED_700
            has_error = True

        if has_error:
            print(f"DEBUG: Errores detectados: {error_msg}")
            self.show_error(error_msg)
            return

        # Success flow
        print("DEBUG: Todo OK. Registrando en Supabase...")
        e.control.disabled = True
        self.page.update()

        result = self.auth_controller.register(email, password)
        
        if result["success"]:
            print("DEBUG: Registro Exitoso")
            self.page.data["router"].navigate("/verify-email")
        else:
            print(f"DEBUG: Error de Supabase: {result['error']}")
            e.control.disabled = False
            
            # Detectar si es un error de "usuario ya existe"
            error_text = str(result["error"])
            friendly_error = error_text
            
            if "already registered" in error_text.lower() or "already exists" in error_text.lower():
                friendly_error = I18n.t("auth.error_email_exists")
                self.email_input.border_color = ft.Colors.RED_700
                self.email_input.update()
            
            self.show_error(friendly_error)
            self.page.update()

    def show_error(self, message):
        print(f"DEBUG: Mostrando SnackBar vía overlay (v6.3): {message}")
        
        # In this Flet version, floating controls must be in the overlay
        snack = ft.SnackBar(
            content=ft.Text(str(message), color=ft.Colors.WHITE),
            bgcolor=ft.Colors.RED_700,
            action="ENTENDIDO",
        )
        
        # Add to overlay if not already there
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def render(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=40),
                    ft.Image(src="icon.png", width=80, height=80, border_radius=15),
                    ft.Text(
                        I18n.t("auth.register"),
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    ),
                    ft.Text(
                        "Crea una cuenta para empezar",
                        size=16,
                        color=ft.Colors.BLUE_GREY_400
                    ),
                    ft.Container(height=30),
                    self.email_input,
                    ft.Container(height=15),
                    self.password_input,
                    ft.Container(height=15),
                    self.confirm_password_input,
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        content=ft.Text(I18n.t("auth.register"), weight=ft.FontWeight.BOLD),
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_600,
                            padding=ft.Padding.all(20),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            elevation=4,
                        ),
                        width=320,
                        on_click=self.handle_register
                    ),
                    ft.Container(expand=True),
                    ft.Row(
                        [
                            ft.Text(I18n.t("auth.already_have_account")),
                            ft.TextButton(
                                I18n.t("auth.login"),
                                on_click=lambda _: self.page.data["router"].navigate("/login")
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
