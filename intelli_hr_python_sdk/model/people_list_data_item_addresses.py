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


class PeopleListDataItemAddresses(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of addresses that belong to this Person.
    """


    class MetaOapg:
        
        
        class items(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    addressType = schemas.StrSchema
                    fullAddress = schemas.StrSchema
                    country = schemas.StrSchema
                    postcode = schemas.StrSchema
                    state = schemas.StrSchema
                    street = schemas.StrSchema
                    suburb = schemas.StrSchema
                    isPrimary = schemas.BoolSchema
                
                    @staticmethod
                    def customFields() -> typing.Type['CustomFieldsResponse']:
                        return CustomFieldsResponse
                    __annotations__ = {
                        "addressType": addressType,
                        "fullAddress": fullAddress,
                        "country": country,
                        "postcode": postcode,
                        "state": state,
                        "street": street,
                        "suburb": suburb,
                        "isPrimary": isPrimary,
                        "customFields": customFields,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["addressType"]) -> MetaOapg.properties.addressType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fullAddress"]) -> MetaOapg.properties.fullAddress: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["postcode"]) -> MetaOapg.properties.postcode: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["street"]) -> MetaOapg.properties.street: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["suburb"]) -> MetaOapg.properties.suburb: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["isPrimary"]) -> MetaOapg.properties.isPrimary: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> 'CustomFieldsResponse': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["addressType", "fullAddress", "country", "postcode", "state", "street", "suburb", "isPrimary", "customFields", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["addressType"]) -> typing.Union[MetaOapg.properties.addressType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fullAddress"]) -> typing.Union[MetaOapg.properties.fullAddress, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["postcode"]) -> typing.Union[MetaOapg.properties.postcode, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["street"]) -> typing.Union[MetaOapg.properties.street, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["suburb"]) -> typing.Union[MetaOapg.properties.suburb, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["isPrimary"]) -> typing.Union[MetaOapg.properties.isPrimary, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union['CustomFieldsResponse', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addressType", "fullAddress", "country", "postcode", "state", "street", "suburb", "isPrimary", "customFields", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                addressType: typing.Union[MetaOapg.properties.addressType, str, schemas.Unset] = schemas.unset,
                fullAddress: typing.Union[MetaOapg.properties.fullAddress, str, schemas.Unset] = schemas.unset,
                country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
                postcode: typing.Union[MetaOapg.properties.postcode, str, schemas.Unset] = schemas.unset,
                state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
                street: typing.Union[MetaOapg.properties.street, str, schemas.Unset] = schemas.unset,
                suburb: typing.Union[MetaOapg.properties.suburb, str, schemas.Unset] = schemas.unset,
                isPrimary: typing.Union[MetaOapg.properties.isPrimary, bool, schemas.Unset] = schemas.unset,
                customFields: typing.Union['CustomFieldsResponse', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    addressType=addressType,
                    fullAddress=fullAddress,
                    country=country,
                    postcode=postcode,
                    state=state,
                    street=street,
                    suburb=suburb,
                    isPrimary=isPrimary,
                    customFields=customFields,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PeopleListDataItemAddresses':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)

from intelli_hr_python_sdk.model.custom_fields_response import CustomFieldsResponse
