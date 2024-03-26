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


class JobCreateRequestPerson(BaseModel):
    # The identifier string for the [Person](https://developers.intellihr.io/docs/v1/) to locate in the system.
    id: typing.Optional[str] = Field(None, alias='id')

    # The name of the [Person](https://developers.intellihr.io/docs/v1/) in intelliHR to search for. Note that the search accounts for differences in name order automatically.
    name: typing.Optional[str] = Field(None, alias='name')

    # The email address flagged as primary for the [Person](https://developers.intellihr.io/docs/v1/) within the system.
    primary_email_address: typing.Optional[str] = Field(None, alias='primaryEmailAddress')

    # A manually entered employee number that identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.
    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    # An autogenerated number that uniquely identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.
    auto_increment_intellihr_id: typing.Optional[str] = Field(None, alias='autoIncrementIntellihrId')

    # WARNING: This property is deprecated
    # An autogenerated number that uniquely identifies a [Person](https://developers.intellihr.io/docs/v1/) in intelliHR. It may be hidden in the system's UI depending upon your tenant's configuration.
    auto_incrementing_intellihr_id: typing.Optional[str] = Field(None, alias='autoIncrementingIntellihrId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
