from django.contrib.auth import views as auth_views
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myaccounts import conf, models
from myaccounts.utils import get_user_from_token, get_email_context
from . import forms
import traceback
from logging import getLogger
logger = getLogger()


@login_required
def verify_form(request):
    context = get_email_context(request)
    form = forms.VerificationForm(request.POST or None)
    if form.is_valid():
        form.save(request.user, context)        # Send Email
        return redirect('mailaddress-verify-accepted')

    context = dict(
        form=form,
    )
    return render(request, 'accounts/mailaddress/verify_form.html', context)


@login_required
def verify_accepted(request):
    return render(request, 'accounts/mailaddress/verify_accepted.html')


@login_required
def verify_confirm(request, id, uidb64, token):

    instance = models.MailAddress.objects.filter(
        user=request.user, id=id).first()

    if not instance or request.user != get_user_from_token(uidb64, token):
        return render(request, 'accounts/mailaddress/verify_error.html')

    instance.is_verified = True
    instance.save()
    return redirect('mailaddress-verify-complete', id=instance.id)


@login_required
def reset_complete(request, id):
    instance = models.MailAddress.objects.filter(user=request.user, id=id).first()
    if not instance:
        return render('accounts/mailaddress/verify_error.html')
    context = {'mailaddress': instance}
    return render(request, 'accounts/mailaddress/verify_complete.html', context)


@login_required
def index(request):
    context = dict(
        mailaddresses=request.user.mailaddress_set.all(),
    )
    return render(request, 'accounts/mailaddress/index.html', context)
    