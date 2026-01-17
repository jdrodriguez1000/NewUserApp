import flet as ft
from core.i18n import I18n
import os

def main(page: ft.Page):
    # Window Configuration (Stricter Mobile-Only aesthetic)
    page.window.width = 390
    page.window.height = 844
    page.window.maximizable = False
    page.window.always_on_top = True
    
    # Debug absolute path and multiple assignment
    icon_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets", "icon.ico"))
    page.window_icon = icon_abs_path
    if hasattr(page, "window"):
        page.window.icon = icon_abs_path
    
    print(f"DEBUG: Icon path: {icon_abs_path}")
    
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Initialize I18n
    I18n.load_translations("en")
    page.title = "NewUserApp"

    # Initialize Router
    from core.router import Router
    router = Router(page)
    
    # Store router in page for global access if needed
    page.data = {"router": router}
    
    # Navigate to initial route
    router.navigate("/")

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
