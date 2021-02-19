import connexion
import six

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server.models.info import Info  # noqa: E501
from swagger_server import util


def create_comment(body):  # noqa: E501
    """Create a comment

    Create a comment # noqa: E501

    :param body: Created comment details
    :type body: dict | bytes

    :rtype: Comment
    """
    if connexion.request.is_json:
        body = Comment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_comment_by_id(commentid):  # noqa: E501
    """Delete comment

    Delete comment # noqa: E501

    :param commentid: ID of the comment to delete
    :type commentid: int

    :rtype: Comment
    """
    return 'do some magic!'


def get_all_comments():  # noqa: E501
    """Get all the comments

    Get all the comments # noqa: E501


    :rtype: Comments
    """
    return 'do some magic!'


def get_comment_by_id(commentid):  # noqa: E501
    """Get comment by id

    Get comment by id # noqa: E501

    :param commentid: ID of the comment to fetch
    :type commentid: int

    :rtype: Comments
    """
    return 'do some magic!'


def modify_comment_by_id(commentid, body):  # noqa: E501
    """Modify comment

    Modify comment # noqa: E501

    :param commentid: ID of the comment to modify
    :type commentid: int
    :param body: ID of the comment to modify
    :type body: dict | bytes

    :rtype: Comment
    """
    if connexion.request.is_json:
        body = Comment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
