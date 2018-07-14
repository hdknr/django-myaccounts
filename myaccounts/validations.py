from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .exceptions import UserExistsException
from .utils import available_username


def validate_usernname(username, username_validators=None):
    errors = []
    if username_validators:
        for validator in username_validators:
            try:
                validator.validate(username)
            except ValidationError as error:
                errors.append(error)

    if not available_username(username):
        errors.append(UserExistsException(username)) 

    if errors:
        raise ValidationError(errors)


def validate_credentials(user, password, username_validators=None, password_validators=None):
    password_validation.validate_password(password, user, password_validators=password_validators)
    validate_usernname(user.username, username_validators=username_validators)
