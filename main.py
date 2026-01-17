import flet as ft
from core.i18n import I18n

def main(page: ft.Page):
    # Window Configuration (Stricter Mobile-Only aesthetic)
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False
    page.window.maximizable = False
    page.window.always_on_top = True
    page.window.icon = "icon.png"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Initialize I18n
    I18n.load_translations("en")

    page.title = "NewUserApp"
    
    # Initial placeholder view (until WelcomeView is implemented)
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        I18n.t("welcome.title"), 
                        size=36, 
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.BLUE_900
                    ),
                    ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                    ft.Text(
                        I18n.t("welcome.description"), 
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.BLUE_GREY_700
                    ),
                    ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                    ft.Button(
                        content=ft.Text(I18n.t("welcome.get_started"), size=18, weight=ft.FontWeight.W_500),
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_600,
                            padding=ft.Padding.all(20),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            elevation=4, # Simulate elevation that would have come from ElevatedButton
                        ),
                        width=280,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            padding=40,
            alignment=ft.Alignment.CENTER,
            bgcolor=ft.Colors.GREY_50
        )
    )
    page.update()

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
