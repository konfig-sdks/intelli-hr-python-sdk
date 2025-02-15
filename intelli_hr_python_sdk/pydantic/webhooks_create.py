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


class WebhooksCreate(BaseModel):
    # The [Webhook](https://developers.intellihr.io/docs/v1/) endpoint which the request will be sent to when the subscribed [Webhook Event](https://developers.intellihr.io/docs/v1/) is triggered.
    url: str = Field(alias='url')

    # The slug of the [Webhook Event](https://developers.intellihr.io/docs/v1/).
    webhook_event: str = Field(alias='webhookEvent')

    # Specifies whether users can select this [Webhook](https://developers.intellihr.io/docs/v1/). When disabled, this [Webhook](https://developers.intellihr.io/docs/v1/) will not be sent.
    is_enabled: typing.Optional[bool] = Field(None, alias='isEnabled')

    # A customizable string which can be used to identify what system created this [Webhook](https://developers.intellihr.io/docs/v1/). [Webhooks](https://developers.intellihr.io/docs/v1/) created through the intelliHR application will have source: 'custom'.
    source: typing.Optional[str] = Field(None, alias='source')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
