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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class JobCreateRequestEmploymentCondition(BaseModel):
    # The identifier string for the [Employment Condition](https://developers.intellihr.io/docs/v1/) of this Remuneration Schedule.
    id: typing.Optional[str] = Field(None, alias='id')

    # Name given to this [Employment Condition](https://developers.intellihr.io/docs/v1/).
    name: typing.Optional[str] = Field(None, alias='name')

    # Award name can be different from the name presented to a user. Usually used for the legal name of the award.
    award_name: typing.Optional[str] = Field(None, alias='awardName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
