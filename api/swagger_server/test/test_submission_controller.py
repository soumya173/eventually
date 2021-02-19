# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.submission import Submission  # noqa: E501
from swagger_server.models.submissions import Submissions  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSubmissionController(BaseTestCase):
    """SubmissionController integration test stubs"""

    def test_create_submission(self):
        """Test case for create_submission

        Create a submission
        """
        body = Submission()
        response = self.client.open(
            '/submission',
            method='POST',
            data=json.dumps(body),
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submission_by_id(self):
        """Test case for delete_submission_by_id

        Delete submission
        """
        response = self.client.open(
            '/submission/{submissionid}'.format(submissionid=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submitted_file_by_id(self):
        """Test case for delete_submitted_file_by_id

        Delete submitted file
        """
        response = self.client.open(
            '/submission/{submissionid}/files'.format(submissionid=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_download_submission_by_id(self):
        """Test case for download_submission_by_id

        Download submission by id
        """
        response = self.client.open(
            '/submission/{submissionid}/files'.format(submissionid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_submissions(self):
        """Test case for get_all_submissions

        Get all the submissions
        """
        response = self.client.open(
            '/submission',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submission_by_id(self):
        """Test case for get_submission_by_id

        Get submission by id
        """
        response = self.client.open(
            '/submission/{submissionid}'.format(submissionid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_submission_by_id(self):
        """Test case for modify_submission_by_id

        Modify submission
        """
        body = Submission()
        response = self.client.open(
            '/submission/{submissionid}'.format(submissionid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upload_submission_file_by_id(self):
        """Test case for upload_submission_file_by_id

        Upload a submission file
        """
        data = dict(datafile=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/submission/{submissionid}/files'.format(submissionid=56),
            method='POST',
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
