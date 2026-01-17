class AppState:
    device = "mobile"  # Forced for this app
    language = "es"
    user = None
    session_active = False

    @classmethod
    def set_user(cls, user_data):
        cls.user = user_data
        cls.session_active = True if user_data else False
