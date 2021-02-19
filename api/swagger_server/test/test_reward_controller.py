# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.reward import Reward  # noqa: E501
from swagger_server.models.rewards import Rewards  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRewardController(BaseTestCase):
    """RewardController integration test stubs"""

    def test_create_reward(self):
        """Test case for create_reward

        Create a reward
        """
        body = Reward()
        response = self.client.open(
            '/reward',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_reward_by_id(self):
        """Test case for delete_reward_by_id

        Delete Reward
        """
        response = self.client.open(
            '/reward/{rewardid}'.format(rewardid=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_rewards(self):
        """Test case for get_all_rewards

        Get all the rewards
        """
        response = self.client.open(
            '/reward',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reward_by_event_id(self):
        """Test case for get_reward_by_event_id

        Get reward by event id
        """
        response = self.client.open(
            '/reward/event/{eventid}'.format(eventid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reward_by_id(self):
        """Test case for get_reward_by_id

        Get reward by id
        """
        response = self.client.open(
            '/reward/{rewardid}'.format(rewardid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_reward_by_id(self):
        """Test case for modify_reward_by_id

        Modify reward
        """
        body = Reward()
        response = self.client.open(
            '/reward/{rewardid}'.format(rewardid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
