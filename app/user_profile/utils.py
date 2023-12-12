from django.contrib.auth.models import User


def is_email_duplicate(previous_email, new_email):
    # Return True when email already exists
    return previous_email != new_email and User.objects.filter(email=new_email)