from django.core.urlresolvers import reverse
from django.test import Client
from unittest import TestCase as UnitTestCase
from django.contrib.auth.models import User
from oauth2_provider.models import get_access_token_model, get_application_model
from django.utils import timezone
from datetime import timedelta
from tests import models


class ProfileCase(UnitTestCase):

    def setUp(self):
        self.userinfo = {
            'username':  'john',
            'email': 'lennon@thebeatles.com',
            'password': 'johnpassword', }
        self.user = User.objects.create_user(*self.userinfo.values())
        self.profile = models.Profile.objects.create(
            user=self.user, age=19, gender='male')

        App, Token = get_application_model(), get_access_token_model()
        self.app = App.objects.create(
            client_type=App.CLIENT_PUBLIC,
            user=self.user, name="test_client_credentials_app",
            authorization_grant_type=App.GRANT_CLIENT_CREDENTIALS,
        )

        self.token = Token.objects.create(
            user=self.user, scope="read write",
            expires=timezone.now() + timedelta(seconds=300),
            token="secret-access-token-key",
            application=self.app,
        )

        self.client = Client()

    def test_response(self):

        url = reverse('profile')
        response = self.client.get(
            url, HTTP_AUTHORIZATION="Bearer " + self.token.token, )

        self.assertEqual('application/json', response['Content-Type'])
        data = response.json()
        self.assertEqual(data['profile']['age'], 19)
