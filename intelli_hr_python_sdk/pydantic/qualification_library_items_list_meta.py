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

from intelli_hr_python_sdk.pydantic.qualification_library_items_list_meta_pagination import QualificationLibraryItemsListMetaPagination

class QualificationLibraryItemsListMeta(BaseModel):
    # The point in time at which the data in this response is accurate. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    as_at: typing.Optional[str] = Field(None, alias='asAt')

    pagination: typing.Optional[QualificationLibraryItemsListMetaPagination] = Field(None, alias='pagination')

    # The identifier string for the api request.
    request_id: typing.Optional[str] = Field(None, alias='requestId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
