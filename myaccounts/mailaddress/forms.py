from django import forms
from myaccounts import conf, signals, models
from myaccounts.utils import create_user_token


class VerificationForm(forms.Form):
    address = forms.EmailField(required=True)
        
    def save(self, user, context):
        keys = dict(
            user=user,
            address=self.cleaned_data['address'],
        )
        qs = models.MailAddress.objects.filter(**keys)
        instance = qs.first() if qs.update(is_verified=False) > 0 \
            else models.MailAddress.objects.create(is_verified=False, **keys)

        context.update(create_user_token(user))
        context['mailaddress'] = instance
        signals.mailaddress_verify_mail.send(
            sender=self, context=context, mailaddress=instance)

        return instance