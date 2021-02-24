# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.login_details import LoginDetails  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        body = User()
        response = self.client.open(
            '/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user_by_id(self):
        """Test case for delete_user_by_id

        Delete user
        """
        response = self.client.open(
            '/user/{userid}'.format(userid=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_users(self):
        """Test case for get_all_users

        Get all users
        """
        response = self.client.open(
            '/user',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        Get user by user id
        """
        response = self.client.open(
            '/user/{userid}'.format(userid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_user(self):
        """Test case for login_user

        Logs user into the system
        """
        body = LoginDetails()
        response = self.client.open(
            '/user/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_user(self):
        """Test case for logout_user

        Logs user into the system
        """
        response = self.client.open(
            '/user/logout/{userid}'.format(userid=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_user_by_id(self):
        """Test case for modify_user_by_id

        Update user
        """
        body = User()
        response = self.client.open(
            '/user/{userid}'.format(userid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
