from django.test import TestCase
from django.contrib.auth import get_user_model
from django_urls import reverse

from rest_frameowrk.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    '''Test the users API (public)'''
    
    def setUp(self):
        self.client = APIClient()
    def test_create_valid_user_successful(self):
        '''Test creating user with valid payload is successful'''
        payload = {
            'email': 'test@aaron.com',
            'password': 'test123',
            'name': 'Test Name'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)