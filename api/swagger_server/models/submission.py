# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Submission(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, event_id: int=None, title: str=None, team_id: int=None, video_file: str=None, submitted_at: str=None, views: int=None):  # noqa: E501
        """Submission - a model defined in Swagger

        :param id: The id of this Submission.  # noqa: E501
        :type id: int
        :param event_id: The event_id of this Submission.  # noqa: E501
        :type event_id: int
        :param title: The title of this Submission.  # noqa: E501
        :type title: str
        :param team_id: The team_id of this Submission.  # noqa: E501
        :type team_id: int
        :param video_file: The video_file of this Submission.  # noqa: E501
        :type video_file: str
        :param submitted_at: The submitted_at of this Submission.  # noqa: E501
        :type submitted_at: str
        :param views: The views of this Submission.  # noqa: E501
        :type views: int
        """
        self.swagger_types = {
            'id': int,
            'event_id': int,
            'title': str,
            'team_id': int,
            'video_file': str,
            'submitted_at': str,
            'views': int
        }

        self.attribute_map = {
            'id': 'id',
            'event_id': 'event_id',
            'title': 'title',
            'team_id': 'team_id',
            'video_file': 'video_file',
            'submitted_at': 'submitted_at',
            'views': 'views'
        }

        self._id = id
        self._event_id = event_id
        self._title = title
        self._team_id = team_id
        self._video_file = video_file
        self._submitted_at = submitted_at
        self._views = views

    @classmethod
    def from_dict(cls, dikt) -> 'Submission':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Submission of this Submission.  # noqa: E501
        :rtype: Submission
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Submission.


        :return: The id of this Submission.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Submission.


        :param id: The id of this Submission.
        :type id: int
        """

        self._id = id

    @property
    def event_id(self) -> int:
        """Gets the event_id of this Submission.


        :return: The event_id of this Submission.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: int):
        """Sets the event_id of this Submission.


        :param event_id: The event_id of this Submission.
        :type event_id: int
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def title(self) -> str:
        """Gets the title of this Submission.


        :return: The title of this Submission.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Submission.


        :param title: The title of this Submission.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def team_id(self) -> int:
        """Gets the team_id of this Submission.


        :return: The team_id of this Submission.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id: int):
        """Sets the team_id of this Submission.


        :param team_id: The team_id of this Submission.
        :type team_id: int
        """
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def video_file(self) -> str:
        """Gets the video_file of this Submission.


        :return: The video_file of this Submission.
        :rtype: str
        """
        return self._video_file

    @video_file.setter
    def video_file(self, video_file: str):
        """Sets the video_file of this Submission.


        :param video_file: The video_file of this Submission.
        :type video_file: str
        """

        self._video_file = video_file

    @property
    def submitted_at(self) -> str:
        """Gets the submitted_at of this Submission.


        :return: The submitted_at of this Submission.
        :rtype: str
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at: str):
        """Sets the submitted_at of this Submission.


        :param submitted_at: The submitted_at of this Submission.
        :type submitted_at: str
        """

        self._submitted_at = submitted_at

    @property
    def views(self) -> int:
        """Gets the views of this Submission.


        :return: The views of this Submission.
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views: int):
        """Sets the views of this Submission.


        :param views: The views of this Submission.
        :type views: int
        """

        self._views = views