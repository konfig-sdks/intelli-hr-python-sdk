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

from intelli_hr_python_sdk.pydantic.webhook_event_basic import WebhookEventBasic
from intelli_hr_python_sdk.pydantic.webhook_event_update_attributes import WebhookEventUpdateAttributes

WebhookEventPersonUpdated = typing.Union[WebhookEventBasic,WebhookEventUpdateAttributes,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
