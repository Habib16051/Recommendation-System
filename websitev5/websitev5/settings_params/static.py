import os
from django.conf import settings

STATIC_URL = os.environ.get("STATIC_URL", '/static/')
# STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE")
STATICFILES_DIRS = [os.path.join(settings.BASE_DIR, 'appwebsite', 'static'),]
STATIC_ROOT = os.environ.get("STATIC_ROOT") or os.path.join(
    settings.BASE_DIR, "static")


print("STATIC_URL ->>{}".format(STATIC_URL))
# print("STATICFILES_STORAGE ->>{}".format(STATICFILES_STORAGE))
print("STATIC_ROOT ->>{}".format(STATIC_ROOT))
