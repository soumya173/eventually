# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUploadController(BaseTestCase):
    """UploadController integration test stubs"""

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
