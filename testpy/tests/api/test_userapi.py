import json
import unittest
from unittest import mock
from fastapi.testclient import TestClient
from api.routes import app
from schema.user import User
from core.logger import logger

ENDPOINT = '/user'
SUCCESS_MSG = '"success"'


class TestUserAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.user = {
            '_id': {'$oid': 'dscvf'},
            'name': 'mXFqF'
        }
        self.user_list = [self.user]
        self.client = TestClient(app)
        logger.disabled = True

    @mock.patch('api.userapi.userservice.fetch_user')
    def test_api_fetch_user(self, mock_fetch):

        mock_fetch.return_value = self.user_list

        response = self.client.get(ENDPOINT)
        response_content = json.loads(response.content.decode('utf-8'))

        assert response.status_code == 200
        assert response_content == self.user_list

    @mock.patch('api.userapi.userservice.insert_user')
    def test_api_insert_user(self, mock_insert):

        mock_insert.return_value = self.user_list

        response = self.client.post(ENDPOINT, data = json.dumps(self.user))
        response_content = response.content.decode('utf-8')

        assert response_content == SUCCESS_MSG
        assert mock_insert.called

    @mock.patch('api.userapi.userservice.update_user')
    def test_api_update_user(self, mock_update):

        mock_update.return_value = self.user_list

        response = self.client.put(f'{ENDPOINT}/dfghv', data = json.dumps(self.user))
        response_content = response.content.decode('utf-8')

        assert response_content == SUCCESS_MSG
        assert mock_update.called

    @mock.patch('api.userapi.userservice.delete_user')
    def test_api_delete_user(self, mock_delete):

        mock_delete.return_value = self.user_list

        response = self.client.delete(f'{ENDPOINT}/dfghv')
        response_content = response.content.decode('utf-8')

        assert response.status_code == 200
        assert response_content == SUCCESS_MSG
        assert mock_delete.called
