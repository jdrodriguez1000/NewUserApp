from core.database import db

class AuthController:
    def __init__(self):
        self.supabase = db

    def login(self, email, password):
        """
        Authenticates a user with email and password.
        Returns the user data and session on success, or an error message on failure.
        """
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            return {"success": True, "data": response}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def logout(self):
        """
        Signs out the current user.
        """
        try:
            self.supabase.auth.sign_out()
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def register(self, email, password):
        """
        Creates a new user account and triggers email verification.
        """
        try:
            response = self.supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            return {"success": True, "data": response}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_session(self):
        """
        Retrieves the current active session.
        """
        return self.supabase.auth.get_session()

    def is_user_verified(self):
        """
        Checks if the current session's user is verified.
        """
        session = self.get_session()
        if session and session.user:
            return session.user.email_confirmed_at is not None
        return False
