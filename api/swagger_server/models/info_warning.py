# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InfoWarning(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, details: List[str]=None):  # noqa: E501
        """InfoWarning - a model defined in Swagger

        :param details: The details of this InfoWarning.  # noqa: E501
        :type details: List[str]
        """
        self.swagger_types = {
            'details': List[str]
        }

        self.attribute_map = {
            'details': 'details'
        }

        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'InfoWarning':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Info_warning of this InfoWarning.  # noqa: E501
        :rtype: InfoWarning
        """
        return util.deserialize_model(dikt, cls)

    @property
    def details(self) -> List[str]:
        """Gets the details of this InfoWarning.


        :return: The details of this InfoWarning.
        :rtype: List[str]
        """
        return self._details

    @details.setter
    def details(self, details: List[str]):
        """Sets the details of this InfoWarning.


        :param details: The details of this InfoWarning.
        :type details: List[str]
        """

        self._details = details