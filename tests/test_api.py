import os

from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app as web_app
from app.config import DATABASE_URL, IS_TEST
from scripts.create_db import main as create_db


class APITestCase(TestCase):

    def setUp(self):
        if not IS_TEST:
            raise Exception('Please setup `IS_TEST=True` os variable')

        create_db()
        self.client = TestClient(web_app)

    def tearDown(self):
        os.remove(DATABASE_URL.replace('sqlite:///', ''))

    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
        body = response.json()
        self.assertEqual(body, {'detail': 'Not Found'})

    def test_create_user(self):
        user_data = {
            'user': {
                'email': 'test@mail.com',
                'password': '123',
                'first_name': 'John',
                'last_name': 'Doe',
                'nickname': 'joe07'
            }
        }

        response = self.client.post('/api/user', json=user_data)
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body, {'user_id': 1})
