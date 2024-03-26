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


class WorkTypesListMetaPagination(BaseModel):
    # Total items count
    total: typing.Optional[int] = Field(None, alias='total')

    # Number of items for current page
    count: typing.Optional[int] = Field(None, alias='count')

    # Items per page limit
    per_page: typing.Optional[int] = Field(None, alias='per_page')

    # Current page
    current_page: typing.Optional[int] = Field(None, alias='current_page')

    # Total number of pages
    total_pages: typing.Optional[int] = Field(None, alias='total_pages')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
