import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.submission import Submission  # noqa: E501
from swagger_server.models.submissions import Submissions  # noqa: E501
from swagger_server import util


def create_submission(body):  # noqa: E501
    """Create a submission

    Create a submission # noqa: E501

    :param body: Created submission details
    :type body: dict | bytes

    :rtype: Submission
    """
    if connexion.request.is_json:
        body = Submission.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_submission_by_id(submissionid):  # noqa: E501
    """Delete submission

    Delete submission # noqa: E501

    :param submissionid: ID of the submission to delete
    :type submissionid: int

    :rtype: Submission
    """
    return 'do some magic!'


def delete_submitted_file_by_id(submissionid):  # noqa: E501
    """Delete submitted file

    Delete submitted file by id # noqa: E501

    :param submissionid: ID of the submitted file to delete
    :type submissionid: int

    :rtype: Info
    """
    return 'do some magic!'


def download_submission_by_id(submissionid):  # noqa: E501
    """Download submission by id

    Download submission by id # noqa: E501

    :param submissionid: ID of the submission to fetch
    :type submissionid: int

    :rtype: Submission
    """
    return 'do some magic!'


def get_all_submissions():  # noqa: E501
    """Get all the submissions

    Get all the submissions # noqa: E501


    :rtype: Submissions
    """
    return 'do some magic!'


def get_submission_by_id(submissionid):  # noqa: E501
    """Get submission by id

    Get submission by id # noqa: E501

    :param submissionid: ID of the submission to fetch
    :type submissionid: int

    :rtype: Submission
    """
    return 'do some magic!'


def modify_submission_by_id(submissionid, body):  # noqa: E501
    """Modify submission

    Modify submission # noqa: E501

    :param submissionid: ID of the submission to modify
    :type submissionid: int
    :param body: ID of the submission to modify
    :type body: dict | bytes

    :rtype: Submission
    """
    if connexion.request.is_json:
        body = Submission.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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
