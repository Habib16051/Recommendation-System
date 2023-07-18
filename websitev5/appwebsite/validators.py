from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_email_guest(value):
    """
    Let's validate the email passed from guest user"
    """
    if not "@" in value:
        errmsg = "Sorry, the email submitted is invalid. All emails have to be registered on this domain only."
        raise ValidationError(errmsg)
