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


class RequiredRepresentativeTypesListDataItem(TypedDict):
    pass

class OptionalRepresentativeTypesListDataItem(TypedDict, total=False):
    # The identifier string for the [Representative Type](https://developers.intellihr.io/docs/v1/).
    id: str

    # Name of this [Representative Type](https://developers.intellihr.io/docs/v1/)
    name: str

    # Type of Object this [Representative Type](https://developers.intellihr.io/docs/v1/) relates to.
    modelType: str

class RepresentativeTypesListDataItem(RequiredRepresentativeTypesListDataItem, OptionalRepresentativeTypesListDataItem):
    pass
