# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class NoteCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text=None, note_type=None, patient_id=None):  # noqa: E501
        """NoteCreateRequest - a model defined in OpenAPI

        :param text: The text of this NoteCreateRequest.  # noqa: E501
        :type text: str
        :param note_type: The note_type of this NoteCreateRequest.  # noqa: E501
        :type note_type: str
        :param patient_id: The patient_id of this NoteCreateRequest.  # noqa: E501
        :type patient_id: str
        """
        self.openapi_types = {
            'text': str,
            'note_type': str,
            'patient_id': str
        }

        self.attribute_map = {
            'text': 'text',
            'note_type': 'noteType',
            'patient_id': 'patientId'
        }

        self._text = text
        self._note_type = note_type
        self._patient_id = patient_id

    @classmethod
    def from_dict(cls, dikt) -> 'NoteCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NoteCreateRequest of this NoteCreateRequest.  # noqa: E501
        :rtype: NoteCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self):
        """Gets the text of this NoteCreateRequest.

        The content of the clinical note  # noqa: E501

        :return: The text of this NoteCreateRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this NoteCreateRequest.

        The content of the clinical note  # noqa: E501

        :param text: The text of this NoteCreateRequest.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def note_type(self):
        """Gets the note_type of this NoteCreateRequest.

        The note type (LOINC concept)  # noqa: E501

        :return: The note_type of this NoteCreateRequest.
        :rtype: str
        """
        return self._note_type

    @note_type.setter
    def note_type(self, note_type):
        """Sets the note_type of this NoteCreateRequest.

        The note type (LOINC concept)  # noqa: E501

        :param note_type: The note_type of this NoteCreateRequest.
        :type note_type: str
        """
        if note_type is None:
            raise ValueError("Invalid value for `note_type`, must not be `None`")  # noqa: E501

        self._note_type = note_type

    @property
    def patient_id(self):
        """Gets the patient_id of this NoteCreateRequest.

        The ID of the FHIR patient  # noqa: E501

        :return: The patient_id of this NoteCreateRequest.
        :rtype: str
        """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        """Sets the patient_id of this NoteCreateRequest.

        The ID of the FHIR patient  # noqa: E501

        :param patient_id: The patient_id of this NoteCreateRequest.
        :type patient_id: str
        """
        if patient_id is None:
            raise ValueError("Invalid value for `patient_id`, must not be `None`")  # noqa: E501
        if patient_id is not None and len(patient_id) > 60:
            raise ValueError("Invalid value for `patient_id`, length must be less than or equal to `60`")  # noqa: E501
        if patient_id is not None and len(patient_id) < 3:
            raise ValueError("Invalid value for `patient_id`, length must be greater than or equal to `3`")  # noqa: E501
        if patient_id is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', patient_id):  # noqa: E501
            raise ValueError("Invalid value for `patient_id`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._patient_id = patient_id
