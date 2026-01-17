import flet as ft
from core.i18n import I18n

def main(page: ft.Page):
    # Window Configuration (Mobile-Only aesthetic)
    page.window_width = 390
    page.window_height = 844
    page.window_resizable = False
    page.window_always_on_top = True
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Initialize I18n
    I18n.load_translations("es")

    page.title = "NewUserApp"
    
    # Initial placeholder view (until WelcomeView is implemented)
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(I18n.t("welcome.title"), size=32, weight="bold"),
                    ft.Text(I18n.t("welcome.description"), text_align=ft.TextAlign.CENTER),
                    ft.Button(I18n.t("welcome.get_started"))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            padding=20,
            alignment=ft.Alignment.CENTER
        )
    )
    page.update()

if __name__ == "__main__":
    ft.run(main)
