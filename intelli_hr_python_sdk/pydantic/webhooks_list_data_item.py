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

from intelli_hr_python_sdk.pydantic.webhooks_list_data_item_webhook_event import WebhooksListDataItemWebhookEvent

class WebhooksListDataItem(BaseModel):
    # The identifier string for the [Webhook](https://developers.intellihr.io/docs/v1/).
    id: typing.Optional[str] = Field(None, alias='id')

    # The [Webhook](https://developers.intellihr.io/docs/v1/) endpoint which the request will be sent to when the subscribed [Webhook Event](https://developers.intellihr.io/docs/v1/) is triggered.
    url: typing.Optional[str] = Field(None, alias='url')

    webhook_event: typing.Optional[WebhooksListDataItemWebhookEvent] = Field(None, alias='webhookEvent')

    # Specifies whether users can select this [Webhook](https://developers.intellihr.io/docs/v1/). When disabled, this [Webhook](https://developers.intellihr.io/docs/v1/) will not be sent.
    is_enabled: typing.Optional[bool] = Field(None, alias='isEnabled')

    # A customizable string which can be used to identify what system created this [Webhook](https://developers.intellihr.io/docs/v1/). [Webhooks](https://developers.intellihr.io/docs/v1/) created through the intelliHR application will have source: 'custom'.
    source: typing.Optional[str] = Field(None, alias='source')

    # When this record was created. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    # When this record was last updated. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
