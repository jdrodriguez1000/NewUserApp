# NewUserApp

A user registration and management application built with **Flet** and the **Fleting** micro-framework, using **Supabase** as the backend.

## 🚀 Overview

This application implements a complete user management flow, including:
- User registration with email verification.
- Secure login.
- Profile management with additional user data.
- Password change and recovery.
- Mobile-first design (iPhone 17 dimensions).

## 🛠️ Tech Stack

- **Frontend**: Flet (Python)
- **Framework**: Fleting
- **Backend**: Supabase (Auth, PostgreSQL, RLS)

## 📁 Structure

- `core/`: Framework infrastructure.
- `views/`: UI views and layouts.
- `controllers/`: Logic handlers.
- `models/`: Data structures.
- `configs/`: App configurations and translations.

## ⚙️ Setup

1. Create a virtual environment: `python -m venv .venv`
2. Activate it: `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Configure `.env` with Supabase credentials.
5. Run the app: `python main.py`
