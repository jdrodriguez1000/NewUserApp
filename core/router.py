import flet as ft

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            "/": self.go_welcome,
        }

    def navigate(self, route):
        if route in self.routes:
            self.routes[route]()
        else:
            print(f"Route {route} not found")

    def go_welcome(self):
        # This will be replaced by lazy loading from configs/routes.py in Phase 3
        print("Navigating to Welcome")
