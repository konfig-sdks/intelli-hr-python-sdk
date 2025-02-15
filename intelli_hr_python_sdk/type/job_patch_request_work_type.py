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


class RequiredJobPatchRequestWorkType(TypedDict):
    pass

class OptionalJobPatchRequestWorkType(TypedDict, total=False):
    # The identifier string for the [Work Type](https://developers.intellihr.io/docs/v1/) to which this [Job](https://developers.intellihr.io/docs/v1/) belongs.
    id: str

    # The name of the [Work Type](https://developers.intellihr.io/docs/v1/). Enum: `Permanent`, `Fixed Contract`, `Unpaid`, `Temporary/Casual`, `Independent Contract`.
    name: str

class JobPatchRequestWorkType(RequiredJobPatchRequestWorkType, OptionalJobPatchRequestWorkType):
    pass
