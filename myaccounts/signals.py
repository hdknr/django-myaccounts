import django.dispatch


password_reset_mail_args = [
    "subject_template_name",
    "email_template_name",
    "context",
    "to_mail",
    "html_email_template_name",
]

password_reset_mail = django.dispatch.Signal(providing_args=password_reset_mail_args)