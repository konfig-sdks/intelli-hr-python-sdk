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


class RequiredEmploymentConditionsMeta(TypedDict):
    pass

class OptionalEmploymentConditionsMeta(TypedDict, total=False):
    # The identifier string for the api request.
    requestId: str

class EmploymentConditionsMeta(RequiredEmploymentConditionsMeta, OptionalEmploymentConditionsMeta):
    pass
