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

from intelli_hr_python_sdk.pydantic.custom_fields_response import CustomFieldsResponse

class JobsDataLocation(BaseModel):
    # The identifier string for the [Location](tag/Locations) of this [Job](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # Name given to this [Location](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: typing.Optional[str] = Field(None, alias='name')

    # The address of this location.
    address: typing.Optional[str] = Field(None, alias='address')

    # Code given to this [Location](https://developers.intellihr.io/docs/v1/).
    code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='code')

    # The custom field values for this [Location](https://developers.intellihr.io/docs/v1/)
    custom_fields: typing.Optional[CustomFieldsResponse] = Field(None, alias='customFields')

    # Link on the public api to get more information on this piece of data.
    link: typing.Optional[str] = Field(None, alias='link')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
