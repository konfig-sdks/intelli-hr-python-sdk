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


class WebhookEventLinksLinks(BaseModel):
    # Link on the public api to get more information on this piece of data.
    self_: typing.Optional[str] = Field(None, alias='self')

    # Link on the public api to get more information on this piece of data.
    self_encoded: typing.Optional[str] = Field(None, alias='selfEncoded')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
