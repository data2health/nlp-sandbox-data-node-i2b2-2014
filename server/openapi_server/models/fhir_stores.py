# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.fhir_store import FhirStore
from openapi_server import util

from openapi_server.models.fhir_store import FhirStore  # noqa: E501

class FhirStores(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fhir_stores=None):  # noqa: E501
        """FhirStores - a model defined in OpenAPI

        :param fhir_stores: The fhir_stores of this FhirStores.  # noqa: E501
        :type fhir_stores: List[FhirStore]
        """
        self.openapi_types = {
            'fhir_stores': List[FhirStore]
        }

        self.attribute_map = {
            'fhir_stores': 'fhirStores'
        }

        self._fhir_stores = fhir_stores

    @classmethod
    def from_dict(cls, dikt) -> 'FhirStores':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FhirStores of this FhirStores.  # noqa: E501
        :rtype: FhirStores
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fhir_stores(self):
        """Gets the fhir_stores of this FhirStores.

        A list of FHIR stores  # noqa: E501

        :return: The fhir_stores of this FhirStores.
        :rtype: List[FhirStore]
        """
        return self._fhir_stores

    @fhir_stores.setter
    def fhir_stores(self, fhir_stores):
        """Sets the fhir_stores of this FhirStores.

        A list of FHIR stores  # noqa: E501

        :param fhir_stores: The fhir_stores of this FhirStores.
        :type fhir_stores: List[FhirStore]
        """

        self._fhir_stores = fhir_stores
