from django.utils.translation import ugettext_lazy as _


class UserExistsException(Exception):
    def __init__(self, user, message=''):
        message = _('User {user} already exists. {message}').format(
            user=user, message=message)
        super().__init__(message)