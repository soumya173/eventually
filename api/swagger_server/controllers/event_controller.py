import connexion
import six

from swagger_server.models.event import Event  # noqa: E501
from swagger_server.models.events import Events  # noqa: E501
from swagger_server.models.info import Info  # noqa: E501
from swagger_server import util


def create_event(body):  # noqa: E501
    """Create a event

    Create a event # noqa: E501

    :param body: Created evenet details
    :type body: dict | bytes

    :rtype: Event
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_event_by_id(eventid):  # noqa: E501
    """Delete event

    Delete event # noqa: E501

    :param eventid: ID of the event to delete
    :type eventid: int

    :rtype: Event
    """
    return 'do some magic!'


def get_active_event():  # noqa: E501
    """Get active event

    Get active event # noqa: E501


    :rtype: Events
    """
    return 'do some magic!'


def get_all_events():  # noqa: E501
    """Get all the events

    Get all the events # noqa: E501


    :rtype: Events
    """
    return 'do some magic!'


def get_event_by_id(eventid):  # noqa: E501
    """Get event by id

    Get event by id # noqa: E501

    :param eventid: ID of the event to fetch
    :type eventid: int

    :rtype: Event
    """
    return 'do some magic!'


def get_subscribed_event(user_id):  # noqa: E501
    """Get subscribed event

    Get subscribed event # noqa: E501

    :param user_id: 
    :type user_id: int

    :rtype: Events
    """
    return 'do some magic!'


def get_upcoming_event():  # noqa: E501
    """Get upcoming event

    Get upcoming event # noqa: E501


    :rtype: Events
    """
    return 'do some magic!'


def modify_event_by_id(eventid, body):  # noqa: E501
    """Modify event

    Modify event # noqa: E501

    :param eventid: ID of the event to modify
    :type eventid: int
    :param body: ID of the event to modify
    :type body: dict | bytes

    :rtype: Event
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def search_events_by_keyword(keyword):  # noqa: E501
    """Search events by keyword

    Search events by keyword # noqa: E501

    :param keyword: 
    :type keyword: str

    :rtype: Events
    """
    return 'do some magic!'
