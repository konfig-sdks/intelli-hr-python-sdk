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

from intelli_hr_python_sdk.pydantic.position_titles_list_data import PositionTitlesListData
from intelli_hr_python_sdk.pydantic.position_titles_list_links import PositionTitlesListLinks
from intelli_hr_python_sdk.pydantic.position_titles_list_meta import PositionTitlesListMeta

class PositionTitlesList(BaseModel):
    data: typing.Optional[PositionTitlesListData] = Field(None, alias='data')

    meta: typing.Optional[PositionTitlesListMeta] = Field(None, alias='meta')

    links: typing.Optional[PositionTitlesListLinks] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
