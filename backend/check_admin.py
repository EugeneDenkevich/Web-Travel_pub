import os
import traceback
import subprocess


# Getting the User model from django
try:
    import django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()
    from django.contrib.auth.models import User
except Exception:
    print(traceback.format_exc())


def check_admin():
    """
    Creatung superuser if he doesn't exist.
      CREDENTIALS:
      - 'admin'
      - '123123'
    """
    admin = os.environ.get('DJANGO_ADMIN_USERNAME')
    try:
        admins = [user.username for user in User.objects.all()]
        if admin not in admins:
            sub = subprocess.run((f'python manage.py createsuperuser --username '
                                  f'{admin} --email admin@admin.com --noinput').split())
            return sub
    except Exception:
        print(traceback.format_exc())


check_admin()
