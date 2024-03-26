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


class RepresentativeTypesData(BaseModel):
    # The identifier string for the [Representative Type](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of this [Representative Type](https://developers.intellihr.io/docs/v1/)
    name: typing.Optional[str] = Field(None, alias='name')

    # Type of Object this [Representative Type](https://developers.intellihr.io/docs/v1/) relates to.
    model_type: typing.Optional[Literal["BUSINESS_UNIT", "LOCATION"]] = Field(None, alias='modelType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
