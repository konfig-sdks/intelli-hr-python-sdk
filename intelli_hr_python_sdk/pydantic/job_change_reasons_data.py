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


class JobChangeReasonsData(BaseModel):
    # The identifier string for the [Job Change Reason](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # Name given to this [Job Change Reason](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: typing.Optional[str] = Field(None, alias='name')

    # Specifies whether users can select this [Job Change Reason](https://developers.intellihr.io/docs/v1/) in dropdowns.
    is_enabled: typing.Optional[bool] = Field(None, alias='isEnabled')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
