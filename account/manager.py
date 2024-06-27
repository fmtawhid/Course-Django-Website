from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is requer")
        email = self.normalize_email(email)
        username = username
        user = self.model(email = email, username = username, **extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        return user
    


    def create_superuser(self, username, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, password, **extra_fields)

