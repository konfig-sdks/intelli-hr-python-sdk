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


class RequiredBusinessUnitsMeta(TypedDict):
    pass

class OptionalBusinessUnitsMeta(TypedDict, total=False):
    # The point in time for which this response is for. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    asAt: str

    # The identifier string for the api request.
    requestId: str

class BusinessUnitsMeta(RequiredBusinessUnitsMeta, OptionalBusinessUnitsMeta):
    pass
