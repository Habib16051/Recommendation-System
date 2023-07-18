import os
from django.conf import settings


# DATABASES
###################################
if os.environ.get('SERVER_TYPE') == 'local':
    DATA_BASE_DIR = os.environ.get("DATA_BASE_DIR", settings.BASE_DIR)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(DATA_BASE_DIR, "db.sqlite3"),
        }
    }
    print("*******************************************")
    print("connecting to database ->>>{}".format(DATABASES['default']['NAME']))

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ.get("localhost"),
            "NAME": os.environ.get("habib"),
            "USER": os.environ.get("habib"),
            "PASSWORD": os.environ.get("123456"),
            "PORT": os.environ.get("5432"),

        }
    }
    print("*******************************************")
    print("connecting to database ->>>{}".format(DATABASES['default']['NAME']))
