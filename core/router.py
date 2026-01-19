import flet as ft
import re
from configs.routes import ROUTES
from controllers.auth_controller import AuthController

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = ROUTES
        self.auth_controller = AuthController()
        self.current_view = None

    def navigate(self, route_path):
        # 1. Conservamos la ruta tal cual
        full_path = str(route_path)
        print(f"DEBUG: [Router] Procesando: '{full_path}'")
        
        # 2. Rescate de Credenciales (Implicit o PKCE)
        found_session = False
        
        # Caso A: Implicit Flow (#access_token=...)
        if "access_token=" in full_path:
            try:
                access = re.search(r'access_token=([^&]+)', full_path)
                refresh = re.search(r'refresh_token=([^&]+)', full_path)
                if access:
                    print("DEBUG: [Router] ✅ TOKEN DETECTADO. Activando sesión...")
                    self.auth_controller.set_session(access.group(1), refresh.group(1) if refresh else None)
                    found_session = True
            except Exception as e:
                print(f"DEBUG: [Router] Error con token: {e}")

        # Caso B: PKCE Flow (?code=...)
        elif "code=" in full_path:
            try:
                code_match = re.search(r'code=([^&]+)', full_path)
                if code_match:
                    code = code_match.group(1)
                    print(f"DEBUG: [Router] ✅ CÓDIGO PKCE DETECTADO ({code[:5]}...). Intercambiando...")
                    res = self.auth_controller.exchange_code(code)
                    if res["success"]:
                        print("DEBUG: [Router] ✅ SESIÓN ACTIVADA VÍA PKCE.")
                        found_session = True
                    else:
                        print(f"DEBUG: [Router] ❌ Error PKCE: {res['error']}")
            except Exception as e:
                print(f"DEBUG: [Router] Error con código: {e}")

        # 3. Limpieza de vista
        # Si encontramos sesión, forzamos ir a cambio de password
        if found_session or "set-new-password" in full_path:
            base_route = "/change-password"
        else:
            base_route = full_path.split("?")[0].split("#")[0]
            if not base_route.startswith("/"): base_route = "/" + base_route

        print(f"DEBUG: [Router] Vista final: {base_route}")

        # 4. Renderizado
        if base_route in self.routes:
            self.page.controls.clear()
            self.page.route = base_route
            view_class = self.routes[base_route]
            self.current_view = view_class(self.page)
            self.page.add(self.current_view.render())
            self.page.update()
        else:
            self.page.go("/")
