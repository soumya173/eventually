import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.submission import Submission  # noqa: E501
from swagger_server import util


def download_submission_by_id(submissionid):  # noqa: E501
    """Download submission by id

    Download submission by id # noqa: E501

    :param submissionid: ID of the submission to fetch
    :type submissionid: int

    :rtype: Submission
    """
    return 'do some magic!'
