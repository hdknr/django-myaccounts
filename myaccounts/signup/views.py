from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
from myaccounts import utils
import traceback
from logging import getLogger
logger = getLogger()


def activate(request, uidb64, token):
    user = utils.get_user_from_token(uidb64, token)
    user.is_active = True
    user.save()
    return redirect('login')