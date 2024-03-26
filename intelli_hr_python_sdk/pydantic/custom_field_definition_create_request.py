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

from intelli_hr_python_sdk.pydantic.custom_field_definition_create_request_select_definition import CustomFieldDefinitionCreateRequestSelectDefinition
from intelli_hr_python_sdk.pydantic.custom_field_definition_create_request_text_definition import CustomFieldDefinitionCreateRequestTextDefinition

class CustomFieldDefinitionCreateRequest(BaseModel):
    # Name given to this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This name would normally be shown to users of the system.
    name: str = Field(alias='name')

    # The api name given to this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This name is used to uniquely identify the custom field in the api and is used as the key when modifying the custom field on a record.
    api_name: str = Field(alias='apiName')

    # The model that this custom field relates to and can be attached to. Enum: `ADDRESS`, `BUSINESS_ENTITY`, `BUSINESS_UNIT`, `EMAIL_ADDRESS`, `JOB`, `LOCATION`, `PERSON`, `POSITION_TITLE`, `PHONE_NUMBER`, `REMUNERATION`, `TRAINING`.
    model_type: str = Field(alias='modelType')

    # The type of data this field records. Enum: `SINGLE_SELECT`, `MULTI_SELECT`, `TEXT`, `NUMBER`, `PEOPLE_DROPDOWN`.
    type: str = Field(alias='type')

    # The description of this [Custom Field Definition](https://developers.intellihr.io/docs/v1/). This is used as a tooltip on the create and update pages.
    description: typing.Optional[typing.Union[str, none_type]] = Field(None, alias='description')

    # Whether or not this [Custom Field Definition](https://developers.intellihr.io/docs/v1/) is marked as sensitive information.
    is_sensitive: typing.Optional[bool] = Field(None, alias='isSensitive')

    select_definition: typing.Optional[CustomFieldDefinitionCreateRequestSelectDefinition] = Field(None, alias='selectDefinition')

    text_definition: typing.Optional[CustomFieldDefinitionCreateRequestTextDefinition] = Field(None, alias='textDefinition')

    # This field is `required` when type `PEOPLE_DROPDOWN` is used
    people_dropdown_definition: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='peopleDropdownDefinition')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
