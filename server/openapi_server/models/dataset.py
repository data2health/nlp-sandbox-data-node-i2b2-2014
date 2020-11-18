# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Dataset(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None):  # noqa: E501
        """Dataset - a model defined in OpenAPI

        :param name: The name of this Dataset.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Dataset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dataset of this Dataset.  # noqa: E501
        :rtype: Dataset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Dataset.

        Resource name of the dataset, of the form datasets/{datasetId}  # noqa: E501

        :return: The name of this Dataset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dataset.

        Resource name of the dataset, of the form datasets/{datasetId}  # noqa: E501

        :param name: The name of this Dataset.
        :type name: str
        """

        self._name = name