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


RequiredWebhooksListLinks = TypedDict("RequiredWebhooksListLinks", {
    })

OptionalWebhooksListLinks = TypedDict("OptionalWebhooksListLinks", {
    # The current page URL
    "self": str,

    # The first page URL
    "first": str,

    # The previous page URL
    "prev": str,

    # The next page URL
    "next": str,

    # The last page URL
    "last": str,
    }, total=False)

class WebhooksListLinks(RequiredWebhooksListLinks, OptionalWebhooksListLinks):
    pass
