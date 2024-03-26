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


class JobCreateRequestPerson(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    [Person](https://developers.intellihr.io/docs/v1/) to whom this [Job](https://developers.intellihr.io/docs/v1/) belongs. This [Person](https://developers.intellihr.io/docs/v1/) is specified as a search object, which will match the person who best fits the keys for this object.
      Multiple keys can be used together to further narrow search results (for example, if there are multiple people with the same name, email address
      can be used as well to limit to a single person. A validation error will be thrown if this search is unable to be narrowed to a single [Person](https://developers.intellihr.io/docs/v1/).
    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            name = schemas.StrSchema
            primaryEmailAddress = schemas.StrSchema
            employeeNumber = schemas.StrSchema
            autoIncrementIntellihrId = schemas.StrSchema
            autoIncrementingIntellihrId = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "primaryEmailAddress": primaryEmailAddress,
                "employeeNumber": employeeNumber,
                "autoIncrementIntellihrId": autoIncrementIntellihrId,
                "autoIncrementingIntellihrId": autoIncrementingIntellihrId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryEmailAddress"]) -> MetaOapg.properties.primaryEmailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoIncrementIntellihrId"]) -> MetaOapg.properties.autoIncrementIntellihrId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoIncrementingIntellihrId"]) -> MetaOapg.properties.autoIncrementingIntellihrId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "primaryEmailAddress", "employeeNumber", "autoIncrementIntellihrId", "autoIncrementingIntellihrId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryEmailAddress"]) -> typing.Union[MetaOapg.properties.primaryEmailAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> typing.Union[MetaOapg.properties.employeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoIncrementIntellihrId"]) -> typing.Union[MetaOapg.properties.autoIncrementIntellihrId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoIncrementingIntellihrId"]) -> typing.Union[MetaOapg.properties.autoIncrementingIntellihrId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "primaryEmailAddress", "employeeNumber", "autoIncrementIntellihrId", "autoIncrementingIntellihrId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        primaryEmailAddress: typing.Union[MetaOapg.properties.primaryEmailAddress, str, schemas.Unset] = schemas.unset,
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, str, schemas.Unset] = schemas.unset,
        autoIncrementIntellihrId: typing.Union[MetaOapg.properties.autoIncrementIntellihrId, str, schemas.Unset] = schemas.unset,
        autoIncrementingIntellihrId: typing.Union[MetaOapg.properties.autoIncrementingIntellihrId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobCreateRequestPerson':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            primaryEmailAddress=primaryEmailAddress,
            employeeNumber=employeeNumber,
            autoIncrementIntellihrId=autoIncrementIntellihrId,
            autoIncrementingIntellihrId=autoIncrementingIntellihrId,
            _configuration=_configuration,
            **kwargs,
        )
