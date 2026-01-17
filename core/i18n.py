import json
import os

class I18n:
    _translations = {}
    _current_language = "es"

    @classmethod
    def load_translations(cls, lang="es"):
        cls._current_language = lang
        file_path = os.path.join("configs", "languages", f"{lang}.json")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                cls._translations = json.load(f)
        except Exception as e:
            print(f"Error loading translations: {e}")
            cls._translations = {}

    @classmethod
    def t(cls, key_path):
        keys = key_path.split(".")
        value = cls._translations
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return key_path  # Return the key itself if not found
        return value

    @classmethod
    def set_language(cls, lang):
        cls.load_translations(lang)

# Initialize with default language
I18n.load_translations("es")
