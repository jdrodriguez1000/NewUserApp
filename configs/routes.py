from views.pages.welcome_view import WelcomeView
from views.pages.auth.login_view import LoginView

ROUTES = {
    "/": WelcomeView,
    "/welcome": WelcomeView,
    "/login": LoginView,
}
