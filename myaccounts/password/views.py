from django.contrib.auth import views as auth_views
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myaccounts import conf
from . import forms
import traceback
from logging import getLogger
logger = getLogger()


def reset_form(request):
    try:
        protocol = request.META.get('HTTP_X_FORWARDED_PROTOCOL', 'http')
        extra_email_context = {
            'request': request, 'protocol': protocol}

        return auth_views.password_reset(
            request,
            password_reset_form=forms.PasswordResetForm,    # Custom Form
            post_reset_redirect='password/reset/accepted',
            template_name='accounts/password/reset/form.html',
            extra_email_context=extra_email_context,
            **conf.PASSWORD_RESET_PARAMS)

    except:
        logger.error(traceback.format_exc())
        return render(
            request,
            'accounts/password/reset/error.html',
            dict(ex=_('Failed to send password reset error')))


def reset_accepted(request):
    return auth_views.password_reset_done(
        request,
        template_name='accounts/password/reset/accepted.html',
        extra_context=None)


def reset_confirm(request, uidb64, token):
    return auth_views.password_reset_confirm(
        request, uidb64=uidb64, token=token,
        template_name='accounts/password/reset/confirm.html',
        set_password_form=forms.PasswordResetConfirmForm,
        post_reset_redirect='password/reset/complete',
        extra_context=None)


def reset_complete(request):
    return auth_views.password_reset_complete(
        request,
        template_name='accounts/password/reset/complete.html',
        extra_context=None)


@login_required
def change_form(request):
    redir = request.GET.get('next', conf.LOGIN_REDIRECT_URL)

    return auth_views.password_change(
        request,
        template_name="accounts/password/change/form.html",
        post_change_redirect=redir,
        password_change_form=forms.PasswordChangeForm,
        extra_context=None)


@login_required
def change_complete(request):
    return self.render('accounts/password/change/complete.html')