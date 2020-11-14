# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.annotation_source import AnnotationSource
from openapi_server.models.text_annotation import TextAnnotation
from openapi_server.models.text_date_annotation_all_of import TextDateAnnotationAllOf
from openapi_server import util

from openapi_server.models.annotation_source import AnnotationSource  # noqa: E501
from openapi_server.models.text_annotation import TextAnnotation  # noqa: E501
from openapi_server.models.text_date_annotation_all_of import TextDateAnnotationAllOf  # noqa: E501

class TextDateAnnotation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, annotation_source=None, annotation_type=None, start=None, length=None, text=None, date_format=None):  # noqa: E501
        """TextDateAnnotation - a model defined in OpenAPI

        :param id: The id of this TextDateAnnotation.  # noqa: E501
        :type id: str
        :param annotation_source: The annotation_source of this TextDateAnnotation.  # noqa: E501
        :type annotation_source: AnnotationSource
        :param annotation_type: The annotation_type of this TextDateAnnotation.  # noqa: E501
        :type annotation_type: str
        :param start: The start of this TextDateAnnotation.  # noqa: E501
        :type start: int
        :param length: The length of this TextDateAnnotation.  # noqa: E501
        :type length: int
        :param text: The text of this TextDateAnnotation.  # noqa: E501
        :type text: str
        :param date_format: The date_format of this TextDateAnnotation.  # noqa: E501
        :type date_format: str
        """
        self.openapi_types = {
            'id': str,
            'annotation_source': AnnotationSource,
            'annotation_type': str,
            'start': int,
            'length': int,
            'text': str,
            'date_format': str
        }

        self.attribute_map = {
            'id': 'id',
            'annotation_source': 'annotationSource',
            'annotation_type': 'annotationType',
            'start': 'start',
            'length': 'length',
            'text': 'text',
            'date_format': 'dateFormat'
        }

        self._id = id
        self._annotation_source = annotation_source
        self._annotation_type = annotation_type
        self._start = start
        self._length = length
        self._text = text
        self._date_format = date_format

    @classmethod
    def from_dict(cls, dikt) -> 'TextDateAnnotation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextDateAnnotation of this TextDateAnnotation.  # noqa: E501
        :rtype: TextDateAnnotation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this TextDateAnnotation.

        The ID of the annotation  # noqa: E501

        :return: The id of this TextDateAnnotation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TextDateAnnotation.

        The ID of the annotation  # noqa: E501

        :param id: The id of this TextDateAnnotation.
        :type id: str
        """

        self._id = id

    @property
    def annotation_source(self):
        """Gets the annotation_source of this TextDateAnnotation.


        :return: The annotation_source of this TextDateAnnotation.
        :rtype: AnnotationSource
        """
        return self._annotation_source

    @annotation_source.setter
    def annotation_source(self, annotation_source):
        """Sets the annotation_source of this TextDateAnnotation.


        :param annotation_source: The annotation_source of this TextDateAnnotation.
        :type annotation_source: AnnotationSource
        """

        self._annotation_source = annotation_source

    @property
    def annotation_type(self):
        """Gets the annotation_type of this TextDateAnnotation.

        The type of the annotation  # noqa: E501

        :return: The annotation_type of this TextDateAnnotation.
        :rtype: str
        """
        return self._annotation_type

    @annotation_type.setter
    def annotation_type(self, annotation_type):
        """Sets the annotation_type of this TextDateAnnotation.

        The type of the annotation  # noqa: E501

        :param annotation_type: The annotation_type of this TextDateAnnotation.
        :type annotation_type: str
        """
        allowed_values = ["text_date", "text_person_name", "text_physical_address"]  # noqa: E501
        if annotation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `annotation_type` ({0}), must be one of {1}"
                .format(annotation_type, allowed_values)
            )

        self._annotation_type = annotation_type

    @property
    def start(self):
        """Gets the start of this TextDateAnnotation.

        The position of the first character  # noqa: E501

        :return: The start of this TextDateAnnotation.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TextDateAnnotation.

        The position of the first character  # noqa: E501

        :param start: The start of this TextDateAnnotation.
        :type start: int
        """

        self._start = start

    @property
    def length(self):
        """Gets the length of this TextDateAnnotation.

        The length of the annotation  # noqa: E501

        :return: The length of this TextDateAnnotation.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this TextDateAnnotation.

        The length of the annotation  # noqa: E501

        :param length: The length of this TextDateAnnotation.
        :type length: int
        """

        self._length = length

    @property
    def text(self):
        """Gets the text of this TextDateAnnotation.

        The string annotated  # noqa: E501

        :return: The text of this TextDateAnnotation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextDateAnnotation.

        The string annotated  # noqa: E501

        :param text: The text of this TextDateAnnotation.
        :type text: str
        """

        self._text = text

    @property
    def date_format(self):
        """Gets the date_format of this TextDateAnnotation.

        Date format (ISO 8601)  # noqa: E501

        :return: The date_format of this TextDateAnnotation.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this TextDateAnnotation.

        Date format (ISO 8601)  # noqa: E501

        :param date_format: The date_format of this TextDateAnnotation.
        :type date_format: str
        """

        self._date_format = date_format
