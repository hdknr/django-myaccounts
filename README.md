# django-myaccounts

- based on python social auth(https://github.com/python-social-auth)

## settings.py


auth.py:

~~~py
AUTH = dict(
    CONTEXT_PROCESSORS=[
        'social_django.context_processors.backends',
        'social_django.context_processors.login_redirect',
    ],    
    APPS=[
        'social_django',        # Social Login
        'oauth2_provider',      # OAuth2 Provider
        'corsheaders',          # OAuth2 Provider
        'myaccounts',
    ],
    AUTHENTICATION_BACKENDS=[
        'social_core.backends.facebook.FacebookOAuth2',     # Facebook
        'oauth2_provider.backends.OAuth2Backend',           # OAuth2 Provider
    ],
    MIDDLEWARE=[
      'corsheaders.middleware.CorsMiddleware',              # OAuth2 Provider     
      'oauth2_provider.middleware.OAuth2TokenMiddleware',   # OAuth2 Provider         
    ],
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
]
#
SOCIAL_AUTH_FACEBOOK_KEY = '3399274742020431'
SOCIAL_AUTH_FACEBOOK_SECRET = '7021391e076a9af1a9f641c82ad1fd052'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email',
}
~~~

settings.py:

~~~py
from django.conf import global_settings
from .auth import *     # NOQA
...
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ....
            ] + AUTH['CONTEXT_PROCESSORS'],
        },
    },
]
INSTALLED_APPS += [
    ....
] + AUTH['APPS']

AUTHENTICATION_BACKENDS = AUTH['AUTHENTICATION_BACKENDS'] + global_settings.AUTHENTICATION_BACKENDS  # NOQA

~~~

## urls.py

~~~py
from myaccounts import urls as accounts_urls

urlpatterns = [
    ...
    url(r'^accounts/', include(accounts_urls)),
]

~~~
