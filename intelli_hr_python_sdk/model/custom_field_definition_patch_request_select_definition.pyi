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


class CustomFieldDefinitionPatchRequestSelectDefinition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    This field is becomes `required` with type `MULTI_SELECT` or `SINGLE_SELECT`
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def options() -> typing.Type['CustomFieldDefinitionPatchRequestSelectDefinitionOptions']:
                return CustomFieldDefinitionPatchRequestSelectDefinitionOptions
            __annotations__ = {
                "options": options,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'CustomFieldDefinitionPatchRequestSelectDefinitionOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['CustomFieldDefinitionPatchRequestSelectDefinitionOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        options: typing.Union['CustomFieldDefinitionPatchRequestSelectDefinitionOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldDefinitionPatchRequestSelectDefinition':
        return super().__new__(
            cls,
            *args,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.custom_field_definition_patch_request_select_definition_options import CustomFieldDefinitionPatchRequestSelectDefinitionOptions
