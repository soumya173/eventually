import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.subscription import Subscription  # noqa: E501
from swagger_server.models.subscriptions import Subscriptions  # noqa: E501
from swagger_server import util


def create_subscription(body):  # noqa: E501
    """Create a subscription

    Create a subscription # noqa: E501

    :param body: Created subscription details
    :type body: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_subscription_by_id(subscriptionid):  # noqa: E501
    """Delete subscription

    Delete subscription # noqa: E501

    :param subscriptionid: ID of the subscription to delete
    :type subscriptionid: int

    :rtype: Subscription
    """
    return 'do some magic!'


def get_all_subscriptions():  # noqa: E501
    """Get all the subscriptions

    Get all the subscriptions # noqa: E501


    :rtype: Subscriptions
    """
    return 'do some magic!'


def get_subscription_by_id(subscriptionid):  # noqa: E501
    """Get subscription by id

    Get subscription by id # noqa: E501

    :param subscriptionid: ID of the subscription to fetch
    :type subscriptionid: int

    :rtype: Subscriptions
    """
    return 'do some magic!'


def modify_subscription_by_id(subscriptionid, body):  # noqa: E501
    """Modify subscription

    Modify subscription # noqa: E501

    :param subscriptionid: ID of the subscription to modify
    :type subscriptionid: int
    :param body: ID of the subscription to modify
    :type body: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
