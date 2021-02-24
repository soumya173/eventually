# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.event import Event  # noqa: E501
from swagger_server.models.events import Events  # noqa: E501
from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.teams import Teams  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEventController(BaseTestCase):
    """EventController integration test stubs"""

    def test_create_event(self):
        """Test case for create_event

        Create a event
        """
        body = Event()
        response = self.client.open(
            '/event',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_event_by_id(self):
        """Test case for delete_event_by_id

        Delete event
        """
        response = self.client.open(
            '/event/{eventid}'.format(eventid=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_active_event(self):
        """Test case for get_active_event

        Get active event
        """
        response = self.client.open(
            '/event/active',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_events(self):
        """Test case for get_all_events

        Get all the events
        """
        response = self.client.open(
            '/event',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_event_by_id(self):
        """Test case for get_event_by_id

        Get event by id
        """
        response = self.client.open(
            '/event/{eventid}'.format(eventid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_subscribed_event(self):
        """Test case for get_subscribed_event

        Get subscribed event
        """
        response = self.client.open(
            '/event/subscribed/{user_id}'.format(user_id=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_teams_by_eveid(self):
        """Test case for get_teams_by_eveid

        Get teams by id
        """
        response = self.client.open(
            '/event/{eventid}/teams'.format(eventid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_upcoming_event(self):
        """Test case for get_upcoming_event

        Get upcoming event
        """
        response = self.client.open(
            '/event/upcoming',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_event_by_id(self):
        """Test case for modify_event_by_id

        Modify event
        """
        body = Event()
        response = self.client.open(
            '/event/{eventid}'.format(eventid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_events_by_keyword(self):
        """Test case for search_events_by_keyword

        Search events by keyword
        """
        response = self.client.open(
            '/event/search/{keyword}'.format(keyword='keyword_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
