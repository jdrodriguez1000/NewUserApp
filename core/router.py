import flet as ft

from configs.routes import ROUTES
from controllers.auth_controller import AuthController

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = ROUTES
        self.auth_controller = AuthController()
        self.current_view = None

    def navigate(self, route_path):
        # Verification Middleware Logic
        is_auth_route = route_path in ["/login", "/register", "/verify-email", "/welcome", "/"]
        
        if not is_auth_route:
            if not self.auth_controller.is_user_verified():
                print("Access denied: User not verified")
                route_path = "/verify-email"

        if route_path in self.routes:
            # Clear current contents
            self.page.controls.clear()
            
            # Instantiate the view
            view_class = self.routes[route_path]
            self.current_view = view_class(self.page)
            
            # Add the view to the page
            self.page.add(self.current_view.render())
            self.page.update()
        else:
            print(f"Route {route_path} not found")

    def go_welcome(self):
        self.navigate("/welcome")
