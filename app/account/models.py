from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from common.models import TimestampMixin, DeleteMixin


class User(AbstractUser, TimestampMixin, DeleteMixin):
    first_name = None
    last_name = None

    REQUIRED_FIELDS: list[str] = ['email']

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def token(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def get_full_name(self) -> str:
        return None

    def get_short_name(self) -> str:
        return None
