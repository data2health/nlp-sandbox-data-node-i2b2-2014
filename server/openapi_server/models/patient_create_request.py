# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PatientCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, identifier=None, gender=None):  # noqa: E501
        """PatientCreateRequest - a model defined in OpenAPI

        :param identifier: The identifier of this PatientCreateRequest.  # noqa: E501
        :type identifier: str
        :param gender: The gender of this PatientCreateRequest.  # noqa: E501
        :type gender: str
        """
        self.openapi_types = {
            'identifier': str,
            'gender': str
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'gender': 'gender'
        }

        self._identifier = identifier
        self._gender = gender

    @classmethod
    def from_dict(cls, dikt) -> 'PatientCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PatientCreateRequest of this PatientCreateRequest.  # noqa: E501
        :rtype: PatientCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identifier(self):
        """Gets the identifier of this PatientCreateRequest.

        An identifier for this patient  # noqa: E501

        :return: The identifier of this PatientCreateRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PatientCreateRequest.

        An identifier for this patient  # noqa: E501

        :param identifier: The identifier of this PatientCreateRequest.
        :type identifier: str
        """

        self._identifier = identifier

    @property
    def gender(self):
        """Gets the gender of this PatientCreateRequest.

        Gender of the patient  # noqa: E501

        :return: The gender of this PatientCreateRequest.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this PatientCreateRequest.

        Gender of the patient  # noqa: E501

        :param gender: The gender of this PatientCreateRequest.
        :type gender: str
        """
        allowed_values = ["male", "female", "other", "unknown"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender