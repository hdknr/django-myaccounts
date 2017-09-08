# coding: utf-8
from django.template.response import TemplateResponse
from django.contrib.auth import views as auth_views


def login(request):
    template_name = "accounts/auth/login.html",
    context = {}
    return TemplateResponse(request, template_name, context)


def logout(request):
    return auth_views.logout(request)
