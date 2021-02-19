import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user_by_id(userid):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param userid: The name that needs to be deleted
    :type userid: int

    :rtype: User
    """
    return 'do some magic!'


def get_user_by_id(userid):  # noqa: E501
    """Get user by user id

     # noqa: E501

    :param userid: The id that needs to be fetched.
    :type userid: int

    :rtype: User
    """
    return 'do some magic!'


def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: User
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: Info
    """
    return 'do some magic!'


def modify_user_by_id(userid, body):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param userid: id that need to be updated
    :type userid: int
    :param body: Update user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
