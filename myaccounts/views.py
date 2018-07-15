from django.contrib.auth import views as auth_views


def login(request, template_name="accounts/auth/login.html", *args, **kwargs):
    return auth_views.login(request, template_name=template_name)


def logout(request):
    return auth_views.logout(request)