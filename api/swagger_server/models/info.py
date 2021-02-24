# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util
from .info_info import InfoInfo
from .info_critical import InfoCritical
from .info_warning import InfoWarning
from .info_error import InfoError


class Info(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, critical: InfoCritical=None, error: InfoError=None, warning: InfoWarning=None, info: InfoInfo=None):  # noqa: E501
        """Info - a model defined in Swagger

        :param critical: The critical of this Info.  # noqa: E501
        :type critical: InfoCritical
        :param error: The error of this Info.  # noqa: E501
        :type error: InfoError
        :param warning: The warning of this Info.  # noqa: E501
        :type warning: InfoWarning
        :param info: The info of this Info.  # noqa: E501
        :type info: InfoInfo
        """
        self.swagger_types = {
            'critical': InfoCritical,
            'error': InfoError,
            'warning': InfoWarning,
            'info': InfoInfo
        }

        self.attribute_map = {
            'critical': 'critical',
            'error': 'error',
            'warning': 'warning',
            'info': 'info'
        }

        self._critical = critical
        self._error = error
        self._warning = warning
        self._info = info

    @classmethod
    def from_dict(cls, dikt) -> 'Info':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Info of this Info.  # noqa: E501
        :rtype: Info
        """
        return util.deserialize_model(dikt, cls)

    @property
    def critical(self) -> InfoCritical:
        """Gets the critical of this Info.


        :return: The critical of this Info.
        :rtype: InfoCritical
        """
        return self._critical

    @critical.setter
    def critical(self, critical: InfoCritical):
        """Sets the critical of this Info.


        :param critical: The critical of this Info.
        :type critical: InfoCritical
        """

        self._critical = critical

    @property
    def error(self) -> InfoError:
        """Gets the error of this Info.


        :return: The error of this Info.
        :rtype: InfoError
        """
        return self._error

    @error.setter
    def error(self, error: InfoError):
        """Sets the error of this Info.


        :param error: The error of this Info.
        :type error: InfoError
        """

        self._error = error

    @property
    def warning(self) -> InfoWarning:
        """Gets the warning of this Info.


        :return: The warning of this Info.
        :rtype: InfoWarning
        """
        return self._warning

    @warning.setter
    def warning(self, warning: InfoWarning):
        """Sets the warning of this Info.


        :param warning: The warning of this Info.
        :type warning: InfoWarning
        """

        self._warning = warning

    @property
    def info(self) -> InfoInfo:
        """Gets the info of this Info.


        :return: The info of this Info.
        :rtype: InfoInfo
        """
        return self._info

    @info.setter
    def info(self, info: InfoInfo):
        """Sets the info of this Info.


        :param info: The info of this Info.
        :type info: InfoInfo
        """

        self._info = info
