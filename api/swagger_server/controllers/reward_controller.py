import connexion
import six

from swagger_server.models.info import Info  # noqa: E501
from swagger_server.models.reward import Reward  # noqa: E501
from swagger_server.models.rewards import Rewards  # noqa: E501
from swagger_server import util


def create_reward(body):  # noqa: E501
    """Create a reward

    Create a reward # noqa: E501

    :param body: Created reward details
    :type body: dict | bytes

    :rtype: Reward
    """
    if connexion.request.is_json:
        body = Reward.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_reward_by_id(rewardid):  # noqa: E501
    """Delete Reward

    Delete reward # noqa: E501

    :param rewardid: ID of the reward to delete
    :type rewardid: int

    :rtype: Reward
    """
    return 'do some magic!'


def get_all_rewards():  # noqa: E501
    """Get all the rewards

    Get all the rewards # noqa: E501


    :rtype: Rewards
    """
    return 'do some magic!'


def get_reward_by_event_id(eventid):  # noqa: E501
    """Get reward by event id

    Get reward by event id # noqa: E501

    :param eventid: ID of the event to fetch
    :type eventid: int

    :rtype: Rewards
    """
    return 'do some magic!'


def get_reward_by_id(rewardid):  # noqa: E501
    """Get reward by id

    Get reward by id # noqa: E501

    :param rewardid: ID of the reward to fetch
    :type rewardid: int

    :rtype: Reward
    """
    return 'do some magic!'


def modify_reward_by_id(rewardid, body):  # noqa: E501
    """Modify reward

    Modify reward # noqa: E501

    :param rewardid: ID of the reward to modify
    :type rewardid: int
    :param body: ID of the reward to modify
    :type body: dict | bytes

    :rtype: Reward
    """
    if connexion.request.is_json:
        body = Reward.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
