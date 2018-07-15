from myaccounts.utils import get_email_context, create_user_token
from myaccounts.signals import activation_mail


def send_activation_mail(user, email=None, context=None, request=None):
    context = context or get_email_context(request)
    context.update(create_user_token(user))
    context['user'] = user
    context['email'] = email or user.email
    activation_mail.send(sender=user, email=context['email'], context=context)