from views.pages.welcome_view import WelcomeView
from views.pages.auth.login_view import LoginView
from views.pages.auth.register_view import RegisterView
from views.pages.auth.verify_email_view import VerifyEmailView
from views.pages.auth.forgot_password_view import ForgotPasswordView
from views.pages.auth.change_password_view import ChangePasswordView

ROUTES = {
    "/": WelcomeView,
    "/welcome": WelcomeView,
    "/login": LoginView,
    "/register": RegisterView,
    "/verify-email": VerifyEmailView,
    "/forgot-password": ForgotPasswordView,
    "/change-password": ChangePasswordView,
}
