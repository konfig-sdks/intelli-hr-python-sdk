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


class TrainingTypesData(BaseModel):
    # The identifier string for the [Training Type](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # User friendly name given to the [Training Type](https://developers.intellihr.io/docs/v1/).
    name: typing.Optional[str] = Field(None, alias='name')

    # Indicates if this [Training Type](https://developers.intellihr.io/docs/v1/) will be used as a default when creating a [Training](https://developers.intellihr.io/docs/v1/) record.
    is_default: typing.Optional[bool] = Field(None, alias='isDefault')

    # Specifies whether users can select this Training Type in dropdowns
    is_enabled: typing.Optional[bool] = Field(None, alias='isEnabled')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
