import flet as ft

from configs.routes import ROUTES

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = ROUTES
        self.current_view = None

    def navigate(self, route_path):
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
