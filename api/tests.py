import json

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase, APIClient

from api.serializers import UserSerializer
from .models import User, UserProfile


# -- Django Rest Framework --
class UserRequestTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.username = 'morphheus'
        self.first_name = 'Christian'
        self.last_name = 'Prada'
        self.password = 'admin'
        self.email = 'cprada87@gmail.com'
        self.title = 'Administrator'
        self.url = '/users/'
        self.pk = '3'

        self.user = User.objects.create_user(
            username=self.username, first_name=self.first_name, last_name=self.last_name,
            password=self.password, email=self.email
        )

        self.profile = UserProfile.objects.create(
            user=self.user, title=self.title
        )

    def login(self):
        return self.client.login(username=self.username, password=self.password, email=self.email)

    def test_login(self):
        response = self.login()
        if response:
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            obj_serializer = json.dumps(UserSerializer(instance=self.user).data)
            serializer_data = [json.loads(obj_serializer)]
            response_data = json.loads(response.content)
            self.assertEqual(serializer_data, response_data)

    def test_logout(self):
        response = self.login()
        if response:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.client.logout()

    def test_create_update(self):
        response = self.login()
        if response:
            self.client.post(self.url, {
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'password': self.password,
                'email': self.email,
            }, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete(self.url + self.pk + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TokenTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'morphheus'

    def test_auth(self):
        token = Token.objects.get(user__username=self.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
