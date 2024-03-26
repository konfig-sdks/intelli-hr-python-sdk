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


class BusinessEntitiesCreateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            code = schemas.StrSchema
            legalName = schemas.StrSchema
            number = schemas.StrSchema
            isEnabled = schemas.BoolSchema
        
            @staticmethod
            def customFields() -> typing.Type['BusinessEntitiesCreateRequestCustomFields']:
                return BusinessEntitiesCreateRequestCustomFields
            __annotations__ = {
                "name": name,
                "code": code,
                "legalName": legalName,
                "number": number,
                "isEnabled": isEnabled,
                "customFields": customFields,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEnabled"]) -> MetaOapg.properties.isEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> 'BusinessEntitiesCreateRequestCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "code", "legalName", "number", "isEnabled", "customFields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalName"]) -> typing.Union[MetaOapg.properties.legalName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEnabled"]) -> typing.Union[MetaOapg.properties.isEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union['BusinessEntitiesCreateRequestCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "code", "legalName", "number", "isEnabled", "customFields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        legalName: typing.Union[MetaOapg.properties.legalName, str, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, str, schemas.Unset] = schemas.unset,
        isEnabled: typing.Union[MetaOapg.properties.isEnabled, bool, schemas.Unset] = schemas.unset,
        customFields: typing.Union['BusinessEntitiesCreateRequestCustomFields', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BusinessEntitiesCreateRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            code=code,
            legalName=legalName,
            number=number,
            isEnabled=isEnabled,
            customFields=customFields,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.business_entities_create_request_custom_fields import BusinessEntitiesCreateRequestCustomFields
