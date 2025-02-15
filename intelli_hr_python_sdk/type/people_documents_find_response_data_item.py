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


class RequiredPeopleDocumentsFindResponseDataItem(TypedDict):
    pass

class OptionalPeopleDocumentsFindResponseDataItem(TypedDict, total=False):
    # The identifier string for the [People Document](https://developers.intellihr.io/docs/v1/).
    id: str

    # The filename of the document. This will be used for display name. Includes extension.
    filename: str

    # A downloadable Url of the document.
    downloadUrlAbsolute: str

    # The extension of the document, not including the dot
    extension: str

    # The size in bytes. We use this to validate the upload was successful so must match the actual file size
    size: int

    # The size in bytes. We use this to validate the upload was successful so must match the actual file size
    humanReadableSize: str

    # The upload status of this [Document](https://developers.intellihr.io/docs/v1/). Enum: `SUCCESS`, `PENDING`, `FAILED`.
    uploadStatus: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class PeopleDocumentsFindResponseDataItem(RequiredPeopleDocumentsFindResponseDataItem, OptionalPeopleDocumentsFindResponseDataItem):
    pass
