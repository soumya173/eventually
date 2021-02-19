# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Comment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, comment: str=None, commented_at: str=None, user_id: int=None, submission_id: int=None, rating: int=None):  # noqa: E501
        """Comment - a model defined in Swagger

        :param id: The id of this Comment.  # noqa: E501
        :type id: int
        :param comment: The comment of this Comment.  # noqa: E501
        :type comment: str
        :param commented_at: The commented_at of this Comment.  # noqa: E501
        :type commented_at: str
        :param user_id: The user_id of this Comment.  # noqa: E501
        :type user_id: int
        :param submission_id: The submission_id of this Comment.  # noqa: E501
        :type submission_id: int
        :param rating: The rating of this Comment.  # noqa: E501
        :type rating: int
        """
        self.swagger_types = {
            'id': int,
            'comment': str,
            'commented_at': str,
            'user_id': int,
            'submission_id': int,
            'rating': int
        }

        self.attribute_map = {
            'id': 'id',
            'comment': 'comment',
            'commented_at': 'commented_at',
            'user_id': 'user_id',
            'submission_id': 'submission_id',
            'rating': 'rating'
        }

        self._id = id
        self._comment = comment
        self._commented_at = commented_at
        self._user_id = user_id
        self._submission_id = submission_id
        self._rating = rating

    @classmethod
    def from_dict(cls, dikt) -> 'Comment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Comment of this Comment.  # noqa: E501
        :rtype: Comment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Comment.


        :return: The id of this Comment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Comment.


        :param id: The id of this Comment.
        :type id: int
        """

        self._id = id

    @property
    def comment(self) -> str:
        """Gets the comment of this Comment.


        :return: The comment of this Comment.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this Comment.


        :param comment: The comment of this Comment.
        :type comment: str
        """

        self._comment = comment

    @property
    def commented_at(self) -> str:
        """Gets the commented_at of this Comment.


        :return: The commented_at of this Comment.
        :rtype: str
        """
        return self._commented_at

    @commented_at.setter
    def commented_at(self, commented_at: str):
        """Sets the commented_at of this Comment.


        :param commented_at: The commented_at of this Comment.
        :type commented_at: str
        """

        self._commented_at = commented_at

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Comment.


        :return: The user_id of this Comment.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Comment.


        :param user_id: The user_id of this Comment.
        :type user_id: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def submission_id(self) -> int:
        """Gets the submission_id of this Comment.


        :return: The submission_id of this Comment.
        :rtype: int
        """
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id: int):
        """Sets the submission_id of this Comment.


        :param submission_id: The submission_id of this Comment.
        :type submission_id: int
        """
        if submission_id is None:
            raise ValueError("Invalid value for `submission_id`, must not be `None`")  # noqa: E501

        self._submission_id = submission_id

    @property
    def rating(self) -> int:
        """Gets the rating of this Comment.


        :return: The rating of this Comment.
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating: int):
        """Sets the rating of this Comment.


        :param rating: The rating of this Comment.
        :type rating: int
        """

        self._rating = rating
