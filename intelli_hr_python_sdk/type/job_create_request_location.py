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


class RequiredJobCreateRequestLocation(TypedDict):
    pass

class OptionalJobCreateRequestLocation(TypedDict, total=False):
    # The identifier string for the [Location](https://developers.intellihr.io/docs/v1/).
    id: str

    # Name given to this [Location](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: str

    # The address of this location.
    address: str

class JobCreateRequestLocation(RequiredJobCreateRequestLocation, OptionalJobCreateRequestLocation):
    pass
