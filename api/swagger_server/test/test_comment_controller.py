# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server.models.info import Info  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCommentController(BaseTestCase):
    """CommentController integration test stubs"""

    def test_create_comment(self):
        """Test case for create_comment

        Create a comment
        """
        body = Comment()
        response = self.client.open(
            '/comment',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_comment_by_id(self):
        """Test case for delete_comment_by_id

        Delete comment
        """
        response = self.client.open(
            '/comment/{commentid}'.format(commentid=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_comments(self):
        """Test case for get_all_comments

        Get all the comments
        """
        response = self.client.open(
            '/comment',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_comment_by_id(self):
        """Test case for get_comment_by_id

        Get comment by id
        """
        response = self.client.open(
            '/comment/{commentid}'.format(commentid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_comment_by_id(self):
        """Test case for modify_comment_by_id

        Modify comment
        """
        body = Comment()
        response = self.client.open(
            '/comment/{commentid}'.format(commentid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
