import os


# EMAIL CONFIG
####################################################
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")

DEVELOPMENT_ONLY_EMAIL_RECIPIENTS=['contact@legoio.com',]
# SUPPORT_EMAIL = DEVELOPMENT_ONLY_EMAIL_RECIPIENTS
print("user-->>{} pass-->>{}".format(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD))
