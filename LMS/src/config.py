from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


@dataclass(frozen=True)
class AppConfig:
    db_host: str
    db_user: str
    db_password: str
    db_name: str
    db_port: int
    log_level: str
    default_admin_email: str
    default_admin_password: str
    default_admin_name: str

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            db_host=os.getenv("DB_HOST", "localhost"),
            db_user=os.getenv("DB_USER", "root"),
            db_password=os.getenv("DB_PASSWORD", ""),
            db_name=os.getenv("DB_NAME", "learntrack_lms"),
            db_port=int(os.getenv("DB_PORT", "3306")),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            default_admin_email=os.getenv(
                "DEFAULT_ADMIN_EMAIL", "admin@learntrack.local"
            ),
            default_admin_password=os.getenv("DEFAULT_ADMIN_PASSWORD", "Admin@12345"),
            default_admin_name=os.getenv("DEFAULT_ADMIN_NAME", "System Admin"),
        )


CONFIG = AppConfig.from_env()
REPORTS_DIR = BASE_DIR / "reports"
CERTIFICATES_DIR = BASE_DIR / "certificates"
LOGS_DIR = BASE_DIR / "logs"
SQL_DIR = BASE_DIR / "sql"

for directory in (REPORTS_DIR, CERTIFICATES_DIR, LOGS_DIR):
    directory.mkdir(parents=True, exist_ok=True)
