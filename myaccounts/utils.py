from django.contrib.auth import get_user_model
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site


UIDB64 = r'(?P<uidb64>[0-9A-Za-z_\-]+)'
TOKEN = r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})'      # NOQA


def get_user_from_token(uidb64, token, token_generator=default_token_generator):
    UserModel = get_user_model()
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
        if token_generator.check_token(user, token):
            return user
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        pass


def create_user_token(user, token_generator=default_token_generator):
    return dict(
        uidb=urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        token=token_generator.make_token(user),
    )


def get_email_context(request):
    site = get_current_site(request)
    protocol = request.META.get('HTTP_X_FORWARDED_PROTOCOL', 'http')
    return dict(
        request=request, 
        protocol=protocol,
        site_name=site.name,
        domain=site.domain,
    )