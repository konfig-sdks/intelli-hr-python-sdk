# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredPeopleDocumentsPatchRequest(TypedDict):
    pass

class OptionalPeopleDocumentsPatchRequest(TypedDict, total=False):
    # The filename of the document. This will be used for display name. Includes extension.
    filename: str

    # The upload status of this [Document](https://developers.intellihr.io/docs/v1/). Enum: `SUCCESS`, `PENDING`, `FAILED`.
    uploadStatus: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class PeopleDocumentsPatchRequest(RequiredPeopleDocumentsPatchRequest, OptionalPeopleDocumentsPatchRequest):
    pass
