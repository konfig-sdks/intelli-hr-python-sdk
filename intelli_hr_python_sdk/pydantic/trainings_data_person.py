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


class TrainingsDataPerson(BaseModel):
    # The identifier string for the [Person](https://developers.intellihr.io/docs/v1/) of the [Training](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # The name of the [Person](https://developers.intellihr.io/docs/v1/) who did the [Training](https://developers.intellihr.io/docs/v1/).
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    # A manually entered employee number that identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.
    employee_number: typing.Optional[typing.Union[none_type, str]] = Field(None, alias='employeeNumber')

    # An autogenerated number that uniquely identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.
    auto_increment_intellihr_id: typing.Optional[typing.Union[int, float]] = Field(None, alias='autoIncrementIntellihrId')

    # Link on the public api to get more information on this piece of data.
    link: typing.Optional[str] = Field(None, alias='link')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
