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


class RequiredTrainingsCreateRequestType(TypedDict):
    pass

class OptionalTrainingsCreateRequestType(TypedDict, total=False):
    # The identifier string for the [Training Type](https://developers.intellihr.io/docs/v1/) of the [Training](https://developers.intellihr.io/docs/v1/).
    id: str

    # User friendly name given to the [Training Type](https://developers.intellihr.io/docs/v1/) of the [Training](https://developers.intellihr.io/docs/v1/).
    name: str

class TrainingsCreateRequestType(RequiredTrainingsCreateRequestType, OptionalTrainingsCreateRequestType):
    pass
