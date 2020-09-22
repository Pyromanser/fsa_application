from fsa_backend.settings import env

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

# DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"
