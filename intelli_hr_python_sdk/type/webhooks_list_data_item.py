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

from intelli_hr_python_sdk.type.webhooks_list_data_item_webhook_event import WebhooksListDataItemWebhookEvent

class RequiredWebhooksListDataItem(TypedDict):
    pass

class OptionalWebhooksListDataItem(TypedDict, total=False):
    # The identifier string for the [Webhook](https://developers.intellihr.io/docs/v1/).
    id: str

    # The [Webhook](https://developers.intellihr.io/docs/v1/) endpoint which the request will be sent to when the subscribed [Webhook Event](https://developers.intellihr.io/docs/v1/) is triggered.
    url: str

    webhookEvent: WebhooksListDataItemWebhookEvent

    # Specifies whether users can select this [Webhook](https://developers.intellihr.io/docs/v1/). When disabled, this [Webhook](https://developers.intellihr.io/docs/v1/) will not be sent.
    isEnabled: bool

    # A customizable string which can be used to identify what system created this [Webhook](https://developers.intellihr.io/docs/v1/). [Webhooks](https://developers.intellihr.io/docs/v1/) created through the intelliHR application will have source: 'custom'.
    source: str

    # When this record was created. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    createdAt: str

    # When this record was last updated. This date will follow the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6).
    updatedAt: str

class WebhooksListDataItem(RequiredWebhooksListDataItem, OptionalWebhooksListDataItem):
    pass
