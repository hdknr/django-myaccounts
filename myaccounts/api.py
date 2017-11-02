# coding: utf-8
from rest_framework import decorators
from rest_framework.response import Response
from oauth2_provider.decorators import protected_resource
from .renderers import JSONRenderer


@decorators.api_view(['POST', 'GET', ])
@decorators.renderer_classes((JSONRenderer, ))
@protected_resource()
def profile(request):
    user = getattr(request, 'resource_owner', getattr(request, 'user', None))
    if not user:
        return JsonResponse({})

    if not request.user.is_authenticated():
        return Response({'username': 'AnonymousUser', })

    # TODO: 'profile' objects must be configurable
    profile = getattr(user, 'profile', {})

    # User Info Response
    data = {
        'user_id': user.id,
        'email': user.email,
        'date_joined': user.date_joined,
        'profile': profile,
        'endpoint_name': 'accounts.api.profile', }
    return Response(data)
