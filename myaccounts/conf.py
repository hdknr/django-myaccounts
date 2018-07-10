from django.conf import settings

# False: Django default behavior, 
# True:  password_reset_mail signnal fired to application
SIGNAL_MAIL = getattr(
    settings, 'MYACCOUNTS_SIGNAL_MAIL', False
) 

PASSWORD_RESET_PARAMS = getattr(
    settings, 'MYACCOUNTS_PASSWORD_RESET_PARAMS',
    dict(
        subject_template_name='accounts/password/reset_subject.txt',
        email_template_name='accounts/password/reset_email.txt',
        html_email_template_name=None,
        from_email=settings.DEFAULT_FROM_EMAIL,
        # token_generator=default_token_generator,      # Django default
        # use_https=False,                              # Django default
    )
)

