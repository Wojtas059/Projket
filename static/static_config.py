from pathlib import Path

STATIC_DIR = Path(__file__).resolve().parent

KIVY_DIR = STATIC_DIR / "kivy"
KIVY_ADMIN_DIR = KIVY_DIR / "kivy_admin_builder"
KIVY_CLIENT_DIR = KIVY_DIR / "kivy_bulider"
KIVY_CSV_DIR = KIVY_DIR / "kivy_csv_builder"
MUSCLES_FILE = STATIC_DIR / "muscles informations" / "Muscles.txt"
MOVIES_DIR = STATIC_DIR / "movies"
PICTURES_DIR = STATIC_DIR / "pictures"
DATABASE_FILE = STATIC_DIR / "database" / "database.db"
CSV_DIR = STATIC_DIR / "csv_saves"
