from pathlib import Path
import os
import dj_database_url

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: Secret key and debug mode
SECRET_KEY = os.environ.get(
    "SECRET_KEY"
)  # Load from environment variable:contentReference[oaicite:8]{index=8}
DEBUG = False  # Never True in production:contentReference[oaicite:9]{index=9}

# Allowed hosts for this site
ALLOWED_HOSTS = [
    "wattthevolt.onrender.com",
    "www.wattthevolt.onrender.com",
    "wattthevolt.com",
    "www.wattthevolt.com",
]

# Trusted origins for CSRF (required for secure HTTPS requests)
CSRF_TRUSTED_ORIGINS = [
    "https://wattthevolt.onrender.com",
    "https://www.wattthevolt.onrender.com",
    "https://wattthevolt.com",
    "https://www.wattthevolt.com",
]

# Security settings for HTTPS
SECURE_SSL_REDIRECT = (
    True  # Redirect HTTP to HTTPS:contentReference[oaicite:10]{index=10}
)
SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)  # Honor the X-Forwarded-Proto header:contentReference[oaicite:11]{index=11}
SESSION_COOKIE_SECURE = (
    True  # Cookies only sent over HTTPS:contentReference[oaicite:12]{index=12}
)
CSRF_COOKIE_SECURE = (
    True  # CSRF cookie only sent over HTTPS:contentReference[oaicite:13]{index=13}
)
# HTTP Strict Transport Security (HSTS) – enforce SSL
SECURE_HSTS_SECONDS = (
    31536000  # 1 year (recommended):contentReference[oaicite:14]{index=14}
)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow preload listing

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",  # Include the blog app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # WhiteNoise for static files:contentReference[oaicite:15]{index=15}
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "life_long_blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # You can add templates directories here if needed
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "life_long_blog.wsgi.application"

# Database configuration (PostgreSQL on Render or SQLite fallback)
DATABASES = {
    "default": dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',  # Use SQLite if no DATABASE_URL:contentReference[oaicite:16]{index=16}
        conn_max_age=600,  # persistent connections
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static and media files
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

if not DEBUG:
    # In production, collect static files here (Render-specific):contentReference[oaicite:17]{index=17}
    STATIC_ROOT = BASE_DIR / "staticfiles"
    # Use WhiteNoise compressed manifest storage for static files:contentReference[oaicite:18]{index=18}
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        }
    }

# Directory for user-uploaded media files
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
