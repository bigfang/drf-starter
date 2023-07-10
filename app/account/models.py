from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from common.models import TimestampMixin, DeleteMixin


class User(AbstractUser, TimestampMixin, DeleteMixin):
    first_name = None
    last_name = None

    REQUIRED_FIELDS: list[str] = ['email']

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self) -> None:
        pass

    def get_short_name(self) -> None:
        pass


class UserToken(User):
    class Meta:
        proxy = True

    @property
    def token(self) -> dict[str, str] | None:
        pass
