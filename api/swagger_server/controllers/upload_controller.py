import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server import util


def upload_submission_file_by_id(submissionid, datafile):  # noqa: E501
    """Upload a submission file

    Upload a  submission file # noqa: E501

    :param submissionid: ID of the submission to modify
    :type submissionid: int
    :param datafile: Submission File
    :type datafile: werkzeug.datastructures.FileStorage

    :rtype: Info
    """
    return 'do some magic!'
