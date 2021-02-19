# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.submission import Submission  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDownloadController(BaseTestCase):
    """DownloadController integration test stubs"""

    def test_download_submission_by_id(self):
        """Test case for download_submission_by_id

        Download submission by id
        """
        response = self.client.open(
            '/submission/{submissionid}/files'.format(submissionid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
