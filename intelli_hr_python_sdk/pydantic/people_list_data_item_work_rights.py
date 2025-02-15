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


class PeopleListDataItemWorkRights(BaseModel):
    # The type of the working rights
    name: typing.Optional[str] = Field(None, alias='name')

    # The country where the working rights are valid
    country: typing.Optional[str] = Field(None, alias='country')

    # The date the working rights are expiring
    expiration_date: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='expirationDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
