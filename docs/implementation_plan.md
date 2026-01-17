# Implementation Plan: NewUserApp (Event-Based refinement)

This plan organizes the development of the NewUserApp project into distinct phases corresponding to major functional events, ensuring clarity and focused implementation.

---

## User Review Required

> [!IMPORTANT]
> - **Event Isolation**: Each phase represents a "Major Event" in the user journey.
> - **Mandatory Order**: Foundations (Phases 1-2) must be completed before functional events.
> - **Security Prerequisite**: Email confirmation is critical for the transition between Phase 3 and Phase 4.

---

## Proposed Changes

### Phase 1: Foundation (Environment & Supabase Setup)
- [NEW] `.env` configuration.
- [NEW] `requirements.txt`.
- [SETUP] Supabase project and `profiles` table schema.

### Phase 2: Framework Core & i18n
- [NEW] `core/database.py` (Supabase Connection).
- [NEW] `configs/languages/` (`es.json`, `en.json`).
- [MODIFY] `main.py` (Mobile-only window constraints).

### Phase 3: Event - Welcome / Onboarding
- [NEW] `views/pages/welcome_view.py`: UI premium con imagen de fondo y botón "Get Started".
- [MODIFY] `configs/routes.py`: Establecer `/welcome` como ruta inicial por defecto.

### Phase 4: Event - Login
- [NEW] `views/pages/auth/login_view.py`.
- [NEW] `controllers/auth_controller.py` (Shared logic for Sign In/Out).
- [UI] Set "Get Started" from Welcome to navigate here.
- [UI] Add "New here? Create an account" link navigating to Phase 5.

### Phase 5: Event - User Registration & Verification
- [NEW] `views/pages/auth/register_view.py`.
- [NEW] `views/pages/auth/verify_email_view.py`.
- [ACTION] Implement password strength validation and trigger email confirmation.
- [UI] Add "Already have an account? Login" link navigating back to Phase 4.
- [MODIFY] `core/router.py`: Implement middleware to block unverified users and redirect them to the pending verification screen.

### Phase 6: Events - Password Security (Recovery & Change)
- [NEW] `views/pages/auth/forgot_password_view.py`.
- [NEW] `views/pages/auth/change_password_view.py`.
- [MODIFY] `auth_controller.py`: Logic for `reset_password` and `update_password`.

### Phase 7: Event - Mandatory Profile Completion
- [NEW] `views/pages/profile/profile_completion_view.py`.
- [MODIFY] `core/router.py`: Logic check for complete profile.
- [NEW] `models/user_profile.py`.

### Phase 8: Event - Authorized Dashboard & Session management
- [NEW] `views/pages/profile/dashboard_view.py`.
- [ACTION] Implement Logout and session persistence.

### Phase 9: Final Validation & Testing
- [NEW] `tests/test_auth.py`.
- [NEW] `tests/test_ui_flows.py`.
- [ACTION] Final UI styling polish.

---

## Verification Plan

### Automated
- `pytest` execution for each controller logic block.

### Manual Verification
- **Flow A**: Register -> Try to Login -> Blocked -> Verify Email -> Login -> Redirected to Profile Completion -> Dashboard.
- **Flow B**: Forgot Password -> Reset from external link -> Successful Login.
- **Flow C**: Window resizing on desktop -> Should remain in mobile aspect ratio.
