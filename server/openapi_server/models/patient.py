# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Patient(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, identifier=None, gender=None):  # noqa: E501
        """Patient - a model defined in OpenAPI

        :param id: The id of this Patient.  # noqa: E501
        :type id: str
        :param identifier: The identifier of this Patient.  # noqa: E501
        :type identifier: str
        :param gender: The gender of this Patient.  # noqa: E501
        :type gender: str
        """
        self.openapi_types = {
            'id': str,
            'identifier': str,
            'gender': str
        }

        self.attribute_map = {
            'id': 'id',
            'identifier': 'identifier',
            'gender': 'gender'
        }

        self._id = id
        self._identifier = identifier
        self._gender = gender

    @classmethod
    def from_dict(cls, dikt) -> 'Patient':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Patient of this Patient.  # noqa: E501
        :rtype: Patient
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Patient.

        The patient ID  # noqa: E501

        :return: The id of this Patient.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Patient.

        The patient ID  # noqa: E501

        :param id: The id of this Patient.
        :type id: str
        """

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this Patient.

        An identifier for this patient  # noqa: E501

        :return: The identifier of this Patient.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Patient.

        An identifier for this patient  # noqa: E501

        :param identifier: The identifier of this Patient.
        :type identifier: str
        """

        self._identifier = identifier

    @property
    def gender(self):
        """Gets the gender of this Patient.

        Gender of the patient  # noqa: E501

        :return: The gender of this Patient.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Patient.

        Gender of the patient  # noqa: E501

        :param gender: The gender of this Patient.
        :type gender: str
        """
        allowed_values = ["male", "female", "other", "unknown"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender
