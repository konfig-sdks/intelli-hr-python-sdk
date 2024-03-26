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


class RequiredCustomFieldDefinitionsData(TypedDict):
    pass

class OptionalCustomFieldDefinitionsData(TypedDict, total=False):
    # The description of this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This is used as a tooltip on the create and update pages.
    description: typing.Union[str, none_type]

    # The identifier string for the [Custom Field Definition](https://developers.intellihr.io/docs/v1/).
    id: str

    # Name given to this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: str

    # The api name given to this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This name is used to uniquely identify the custom field in the api and is used as the key when modifying the custom field on a record.
    apiName: str

    # Whether or not this [Custom Field Definition](https://developers.intellihr.io/docs/v1/) is enabled to be used.
    isEnabled: bool

    # Whether or not this [Custom Field Definition](https://developers.intellihr.io/docs/v1/) is marked as sensitive information.
    isSensitive: bool

    # The model that this custom field relates to and can be attached to. Enum: `ADDRESS`, `BUSINESS_ENTITY`, `BUSINESS_UNIT`, `EMAIL_ADDRESS`, `JOB`, `LOCATION`, `PERSON`, `POSITION_TITLE`, `PHONE_NUMBER`, `REMUNERATION`, `TRAINING`.
    modelType: str

    # The type of data this field records. Enum: `SINGLE_SELECT`, `MULTI_SELECT`, `TEXT`, `NUMBER`, `PEOPLE_DROPDOWN`.
    type: str

    # This key's values change depending on the \"type\" key. It is used to store additional information pertinent to that key. For more information on custom field configurations, see our [knowledge base article on custom fields](https://intellihr.zendesk.com/hc/en-us/articles/4402637180303-Custom-Fields)
    definitions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class CustomFieldDefinitionsData(RequiredCustomFieldDefinitionsData, OptionalCustomFieldDefinitionsData):
    pass
