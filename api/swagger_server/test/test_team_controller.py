# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.teams import Teams  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTeamController(BaseTestCase):
    """TeamController integration test stubs"""

    def test_create_team(self):
        """Test case for create_team

        Create a team
        """
        body = Team()
        response = self.client.open(
            '/team',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_team_by_id(self):
        """Test case for delete_team_by_id

        Delete Team
        """
        response = self.client.open(
            '/team/{teamid}'.format(teamid=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_teams(self):
        """Test case for get_all_teams

        Get all the teams
        """
        response = self.client.open(
            '/team',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_team_by_id(self):
        """Test case for get_team_by_id

        Get team by id
        """
        response = self.client.open(
            '/team/{teamid}'.format(teamid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_team_by_id(self):
        """Test case for modify_team_by_id

        Modify team
        """
        body = Team()
        response = self.client.open(
            '/team/{teamid}'.format(teamid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
