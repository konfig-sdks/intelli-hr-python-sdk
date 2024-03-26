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


class JobCreateRequestBusinessEntity(BaseModel):
    # The identifier string for the [Business Entity](https://developers.intellihr.io/docs/v1/) to which this [Job](https://developers.intellihr.io/docs/v1/) belongs.
    id: typing.Optional[str] = Field(None, alias='id')

    # Name given to this [Business Entity](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: typing.Optional[str] = Field(None, alias='name')

    # Legal name of [Business Entity](https://developers.intellihr.io/docs/v1/). Usually used for administrative tasks.
    legal_name: typing.Optional[str] = Field(None, alias='legalName')

    # Legally registered [Business Entity](https://developers.intellihr.io/docs/v1/) number, e.g. in Australia this might be the ABN, or in America the RN.
    number: typing.Optional[str] = Field(None, alias='number')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
