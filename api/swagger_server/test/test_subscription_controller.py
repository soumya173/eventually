# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.subscription import Subscription  # noqa: E501
from swagger_server.models.subscriptions import Subscriptions  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSubscriptionController(BaseTestCase):
    """SubscriptionController integration test stubs"""

    def test_create_subscription(self):
        """Test case for create_subscription

        Create a subscription
        """
        body = Subscription()
        response = self.client.open(
            '/subscription',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_subscription_by_id(self):
        """Test case for delete_subscription_by_id

        Delete subscription
        """
        response = self.client.open(
            '/subscription/{subscriptionid}'.format(subscriptionid=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_subscriptions(self):
        """Test case for get_all_subscriptions

        Get all the subscriptions
        """
        response = self.client.open(
            '/subscription',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_subscription_by_id(self):
        """Test case for get_subscription_by_id

        Get subscription by id
        """
        response = self.client.open(
            '/subscription/{subscriptionid}'.format(subscriptionid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_subscription_by_id(self):
        """Test case for modify_subscription_by_id

        Modify subscription
        """
        body = Subscription()
        response = self.client.open(
            '/subscription/{subscriptionid}'.format(subscriptionid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
