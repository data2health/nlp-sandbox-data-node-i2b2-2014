# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dataset import Dataset
from openapi_server import util

from openapi_server.models.dataset import Dataset  # noqa: E501

class PageOfDatasetsAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datasets=None):  # noqa: E501
        """PageOfDatasetsAllOf - a model defined in OpenAPI

        :param datasets: The datasets of this PageOfDatasetsAllOf.  # noqa: E501
        :type datasets: List[Dataset]
        """
        self.openapi_types = {
            'datasets': List[Dataset]
        }

        self.attribute_map = {
            'datasets': 'datasets'
        }

        self._datasets = datasets

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfDatasetsAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfDatasets_allOf of this PageOfDatasetsAllOf.  # noqa: E501
        :rtype: PageOfDatasetsAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datasets(self):
        """Gets the datasets of this PageOfDatasetsAllOf.

        An array of datasets  # noqa: E501

        :return: The datasets of this PageOfDatasetsAllOf.
        :rtype: List[Dataset]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this PageOfDatasetsAllOf.

        An array of datasets  # noqa: E501

        :param datasets: The datasets of this PageOfDatasetsAllOf.
        :type datasets: List[Dataset]
        """

        self._datasets = datasets