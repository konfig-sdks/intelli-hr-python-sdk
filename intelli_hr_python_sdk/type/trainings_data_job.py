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


class RequiredTrainingsDataJob(TypedDict):
    pass

class OptionalTrainingsDataJob(TypedDict, total=False):
    # The identifier string for the [Job](https://developers.intellihr.io/docs/v1/) of the [Training](https://developers.intellihr.io/docs/v1/).
    id: str

    # The name of the [Persons](https://developers.intellihr.io/docs/v1/) [Job](https://developers.intellihr.io/docs/v1/) who did the [Training](https://developers.intellihr.io/docs/v1/).
    name: str

    # The [Jobs](https://developers.intellihr.io/docs/v1/) effective start date. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    startDate: str

    # The [Jobs](https://developers.intellihr.io/docs/v1/) effective end date. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    endDate: typing.Union[str, none_type]

    # The Status Schema. Enum: `Past Job`, `Future Job`, `Ending Job`, `Current Job`.
    jobStatus: str

    # Link on the public api to get more information on this piece of data.
    link: str

class TrainingsDataJob(RequiredTrainingsDataJob, OptionalTrainingsDataJob):
    pass
