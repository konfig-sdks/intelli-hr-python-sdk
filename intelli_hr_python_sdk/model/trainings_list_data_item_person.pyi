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


class TrainingsListDataItemPerson(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The [Person](https://developers.intellihr.io/docs/v1/) who did the [Training](https://developers.intellihr.io/docs/v1/).
    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            displayName = schemas.StrSchema
            
            
            class employeeNumber(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.NoneSchema
                    one_of_1 = schemas.StrSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'employeeNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            autoIncrementIntellihrId = schemas.NumberSchema
            link = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "displayName": displayName,
                "employeeNumber": employeeNumber,
                "autoIncrementIntellihrId": autoIncrementIntellihrId,
                "link": link,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoIncrementIntellihrId"]) -> MetaOapg.properties.autoIncrementIntellihrId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "displayName", "employeeNumber", "autoIncrementIntellihrId", "link", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> typing.Union[MetaOapg.properties.employeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoIncrementIntellihrId"]) -> typing.Union[MetaOapg.properties.autoIncrementIntellihrId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "displayName", "employeeNumber", "autoIncrementIntellihrId", "link", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        autoIncrementIntellihrId: typing.Union[MetaOapg.properties.autoIncrementIntellihrId, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TrainingsListDataItemPerson':
        return super().__new__(
            cls,
            *args,
            id=id,
            displayName=displayName,
            employeeNumber=employeeNumber,
            autoIncrementIntellihrId=autoIncrementIntellihrId,
            link=link,
            _configuration=_configuration,
            **kwargs,
        )
