# coding: utf-8

"""
    intelliHR Public API

    You can find developer's guide and more documentation on [https://developers.intellihr.io](https://developers.intellihr.io)

    The version of the OpenAPI document: V1
    Contact: support@intellihr.co
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from intelli_hr_python_sdk import schemas  # noqa: F401


class CustomFieldDefinitionCreateRequestSelectDefinitionOptions(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    List of options
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CustomFieldDefinitionCreateRequestSelectDefinitionOptionsItem']:
            return CustomFieldDefinitionCreateRequestSelectDefinitionOptionsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CustomFieldDefinitionCreateRequestSelectDefinitionOptionsItem'], typing.List['CustomFieldDefinitionCreateRequestSelectDefinitionOptionsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CustomFieldDefinitionCreateRequestSelectDefinitionOptions':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CustomFieldDefinitionCreateRequestSelectDefinitionOptionsItem':
        return super().__getitem__(i)

from intelli_hr_python_sdk.model.custom_field_definition_create_request_select_definition_options_item import CustomFieldDefinitionCreateRequestSelectDefinitionOptionsItem
