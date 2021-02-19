import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.teams import Teams  # noqa: E501
from swagger_server import util


def create_team(body):  # noqa: E501
    """Create a team

    Create a team # noqa: E501

    :param body: Created evenet details
    :type body: dict | bytes

    :rtype: Team
    """
    if connexion.request.is_json:
        body = Team.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_team_by_id(teamid):  # noqa: E501
    """Delete Team

    Delete team # noqa: E501

    :param teamid: ID of the event to delete
    :type teamid: int

    :rtype: Team
    """
    return 'do some magic!'


def get_all_teams():  # noqa: E501
    """Get all the teams

    Get all the teams # noqa: E501


    :rtype: Teams
    """
    return 'do some magic!'


def get_team_by_id(teamid):  # noqa: E501
    """Get team by id

    Get team by id # noqa: E501

    :param teamid: ID of the event to fetch
    :type teamid: int

    :rtype: Team
    """
    return 'do some magic!'


def modify_team_by_id(teamid, body):  # noqa: E501
    """Modify team

    Modify team # noqa: E501

    :param teamid: ID of the team to modify
    :type teamid: int
    :param body: ID of the event to modify
    :type body: dict | bytes

    :rtype: Team
    """
    if connexion.request.is_json:
        body = Team.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
