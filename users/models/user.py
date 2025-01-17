from django.db import models
from django.http import QueryDict
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password, email):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError("The given phone_number must be set")
        phone_number = User.normalize_username(phone_number)
        user = User(phone_number=phone_number, user_type=User.UserType.ADMIN, email=email)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Gender(models.TextChoices):
        MALE = 'MALE', _('Male')
        FEMALE = 'FEMALE', _('Female')
        OTHERS = 'OTHERS', _('Others')
    
    class UserType(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        SUPERVISOR = 'SUPERVISOR', _('Supervisor')
        SURVEYOR = 'SURVEYOR', _('Surveyor')
 
    profile_photo = models.OneToOneField("files_manager.File", on_delete=models.DO_NOTHING, null=True)
    user_type = models.CharField(_("user type"), max_length=20, choices=UserType.choices)
    name = models.CharField(_("name"), max_length=200)
    gender = models.CharField(_("gender"), max_length=20, choices=Gender.choices)
    phone_number = PhoneNumberField(_("phone number"), null=False, blank=False, unique=True)
    email = models.EmailField('email adress', unique=True)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )    
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    last_updated = models.DateTimeField(_("last updated"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users"


class AnonymousUser:
    user_id = None
    username = ""
    is_active = False
    user_type = None
    assigned_blocks = User.objects.none()
    assigned_projects = User.objects.none()

    def __str__(self):
        return "AnonymousUser"

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __hash__(self):
        return 1  # instances always return the same hash value

    def __int__(self):
        raise TypeError(
            "Cannot cast AnonymousUser to int. Are you trying to use it in place of "
            "User?"
        )

    def save(self):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def delete(self):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def set_password(self, raw_password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def check_password(self, raw_password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    @property
    def is_anonymous(self):
        return True

    @property
    def is_authenticated(self):
        return False

    def get_username(self):
        return self.username
