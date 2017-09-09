# coding: utf-8
from rest_framework import decorators
from oauth2_provider.decorators import protected_resource
from corekit.responses import JsonResponse


@decorators.api_view(['POST', 'GET', ])
@protected_resource()
def profile(request):
    user = getattr(request, 'resource_owner', getattr(request, 'user', None))
    if not user:
        return JsonResponse({})

    if not request.user.is_authenticated():
        return JsonResponse({'username': 'AnonymousUser', })

    # TODO: 'profile' objects must be configurable
    profile = getattr(user, 'profile', {})

    # User Info Response
    data = {
        'user_id': user.id,
        'email': user.email,
        'date_joined': user.date_joined,
        'profile': profile,
        'endpoint_name': 'accounts.api.profile',
    }
    return JsonResponse(data)
