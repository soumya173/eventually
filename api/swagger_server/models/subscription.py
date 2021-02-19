# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Subscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, user_id: int=None, event_id: int=None):  # noqa: E501
        """Subscription - a model defined in Swagger

        :param id: The id of this Subscription.  # noqa: E501
        :type id: int
        :param user_id: The user_id of this Subscription.  # noqa: E501
        :type user_id: int
        :param event_id: The event_id of this Subscription.  # noqa: E501
        :type event_id: int
        """
        self.swagger_types = {
            'id': int,
            'user_id': int,
            'event_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'user_id',
            'event_id': 'event_id'
        }

        self._id = id
        self._user_id = user_id
        self._event_id = event_id

    @classmethod
    def from_dict(cls, dikt) -> 'Subscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Subscription of this Subscription.  # noqa: E501
        :rtype: Subscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Subscription.


        :return: The id of this Subscription.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Subscription.


        :param id: The id of this Subscription.
        :type id: int
        """

        self._id = id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Subscription.


        :return: The user_id of this Subscription.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Subscription.


        :param user_id: The user_id of this Subscription.
        :type user_id: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def event_id(self) -> int:
        """Gets the event_id of this Subscription.


        :return: The event_id of this Subscription.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: int):
        """Sets the event_id of this Subscription.


        :param event_id: The event_id of this Subscription.
        :type event_id: int
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id
