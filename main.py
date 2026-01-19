import flet as ft
from core.i18n import I18n
import os
import warnings
import asyncio

# Suppress warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

async def main(page: ft.Page):
    # Configuración Base
    page.window_width = 390
    page.window_height = 844
    page.theme_mode = ft.ThemeMode.LIGHT
    I18n.load_translations("es")
    page.title = "NewUserApp"

    from core.router import Router
    router = Router(page)
    page.data = {"router": router}

    # Esta función recibirá la URL completa del navegador, incluyendo el #
    async def on_window_event(e):
        if e.data:
            print(f"DEBUG: [App] Evento de ventana: {e.data}")
            # Si el evento trae la URL (depende de la versión de Flet)
            if "access_token" in e.data:
                router.navigate(e.data)

    page.on_window_event = on_window_event

    def on_route_change(e):
        # Intentamos capturar la ruta. Si Flet 0.8.x la limpia, 
        # confiaremos en el router.navigate con la URL sucia que detectemos.
        print(f"DEBUG: [App] Flet Route: '{page.route}'")
        router.navigate(page.route)

    page.on_route_change = on_route_change
    
    # PEQUEÑO TRUCO: Inyectamos un script que re-navega a la misma URL
    # pero asegurándose de que Flet vea el fragmento #
    await asyncio.sleep(0.5)
    
    # Navegación inicial
    print(f"DEBUG: [App] Iniciando con: '{page.route}'")
    router.navigate(page.route if page.route else "/")

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", port=3000, view=ft.AppView.WEB_BROWSER)
