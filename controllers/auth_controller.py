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

    def exchange_code(self, code):
        """
        Exchanges an auth code for a session (PKCE flow).
        """
        try:
            res = self.supabase.auth.exchange_code_for_session({"auth_code": code})
            return {"success": True, "session": res.session}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def send_reset_password_email(self, email):
        """
        Sends a password reset email to the user.
        """
        try:
            # Enviamos al BRIDGE que convierte el # en ?
            self.supabase.auth.reset_password_for_email(
                email, 
                options={"redirect_to": "http://localhost:3000/recovery.html"}
            )
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def update_password(self, new_password):
        """
        Updates the password for the currently logged-in user.
        """
        try:
            # Intentamos obtener el usuario actual para debug
            user = self.supabase.auth.get_user()
            if user:
                print(f"DEBUG: update_password - Usuario detectado: {user.user.email}")
            
            self.supabase.auth.update_user({"password": new_password})
            return {"success": True}
        except Exception as e:
            print(f"DEBUG: Error real de Supabase en update_password: {e}")
            return {"success": False, "error": str(e)}

    def set_session(self, access_token, refresh_token):
        """
        Sets the active session using tokens (used after password reset email).
        """
        try:
            self.supabase.auth.set_session(access_token, refresh_token)
            return {"success": True}
        except Exception as e:
            print(f"DEBUG: Error setting session: {e}")
            return {"success": False, "error": str(e)}
