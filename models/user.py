from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """
    Manager for User model to handle user creation.
    """

    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates and returns a regular user.
        """
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Creates and returns a superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model for storing user details.
    """
    username = models.CharField(max_length=80, unique=True, null=False)
    email = models.EmailField(max_length=120, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)  # Stored as hashed
    is_active = models.BooleanField(default=True)  # Active user flag
    is_staff = models.BooleanField(default=False)  # For admin dashboard access

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """String representation of the User instance."""
        return self.username

    def as_dict(self):
        """
        Serialize the user object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

