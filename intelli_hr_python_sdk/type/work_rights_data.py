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


class RequiredWorkRightsData(TypedDict):
    pass

class OptionalWorkRightsData(TypedDict, total=False):
    # The identifier string for the [Work Right](https://developers.intellihr.io/docs/v1/).
    id: str

    # Name given to this [Work Right](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: str

    # The identifier string for the Country.
    countryId: str

    # The name value of the assigned Country.
    country: str

class WorkRightsData(RequiredWorkRightsData, OptionalWorkRightsData):
    pass
