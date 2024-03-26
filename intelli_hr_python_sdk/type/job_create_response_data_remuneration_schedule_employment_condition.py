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


class RequiredJobCreateResponseDataRemunerationScheduleEmploymentCondition(TypedDict):
    pass

class OptionalJobCreateResponseDataRemunerationScheduleEmploymentCondition(TypedDict, total=False):
    # The identifier string for the [Employment Condition](https://developers.intellihr.io/docs/v1/) of this Remuneration Schedule.
    id: str

    # Name given to this [Employment Condition](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: str

    # Award name can be different from the name presented to a user. Usually used for the legal name of the award.
    awardName: typing.Union[str, none_type]

    # Link on the public api to get more information on this piece of data.
    link: str

class JobCreateResponseDataRemunerationScheduleEmploymentCondition(RequiredJobCreateResponseDataRemunerationScheduleEmploymentCondition, OptionalJobCreateResponseDataRemunerationScheduleEmploymentCondition):
    pass
