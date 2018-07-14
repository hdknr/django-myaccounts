from django.contrib.auth import forms as auth_forms     #
from myaccounts import conf, signals


class PasswordResetForm(auth_forms.PasswordResetForm):

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        # Not called if the user has NO email.

        if conf.SIGNAL_MAIL:
            # Application will send an email
            signals.password_reset_mail.send(
                sender=self,
                subject_template_name=subject_template_name,
                email_template_name=email_template_name,
                context=context, 
                to_mail=to_email,
                html_email_template_name=html_email_template_name)
            return

        # Django sends an email
        super(PasswordResetForm, self).send_mail(
            subject_template_name, email_template_name,
            context, from_email, to_email,
            html_email_template_name=html_email_template_name)


class SetPasswordForm(auth_forms.SetPasswordForm):

    def save(self, *args, **kwargs):
        self.user.is_active = True    
        return super(PasswordResetConfirmForm, self).save(*args, **kwargs)


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    pass
