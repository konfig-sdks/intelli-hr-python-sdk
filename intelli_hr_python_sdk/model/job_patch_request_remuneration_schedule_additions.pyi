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


class JobPatchRequestRemunerationScheduleAdditions(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of Additions for the base salary.
    """


    class MetaOapg:
        
        
        class items(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "defaultRemunerationComponent",
                    "name",
                    "type",
                    "value",
                }
                
                class properties:
                    name = schemas.StrSchema
                    type = schemas.StrSchema
                    value = schemas.StrSchema
                    
                    
                    class currency(
                        schemas.StrSchema
                    ):
                        pass
                    
                    
                    class defaultRemunerationComponent(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                
                                
                                class id(
                                    schemas.StrSchema
                                ):
                                    pass
                                name = schemas.StrSchema
                                __annotations__ = {
                                    "id": id,
                                    "name": name,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                            name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'defaultRemunerationComponent':
                            return super().__new__(
                                cls,
                                *args,
                                id=id,
                                name=name,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "name": name,
                        "type": type,
                        "value": value,
                        "currency": currency,
                        "defaultRemunerationComponent": defaultRemunerationComponent,
                    }
        
            
            defaultRemunerationComponent: MetaOapg.properties.defaultRemunerationComponent
            name: MetaOapg.properties.name
            type: MetaOapg.properties.type
            value: MetaOapg.properties.value
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["defaultRemunerationComponent"]) -> MetaOapg.properties.defaultRemunerationComponent: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "type", "value", "currency", "defaultRemunerationComponent", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["defaultRemunerationComponent"]) -> MetaOapg.properties.defaultRemunerationComponent: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "type", "value", "currency", "defaultRemunerationComponent", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                defaultRemunerationComponent: typing.Union[MetaOapg.properties.defaultRemunerationComponent, dict, frozendict.frozendict, ],
                name: typing.Union[MetaOapg.properties.name, str, ],
                type: typing.Union[MetaOapg.properties.type, str, ],
                value: typing.Union[MetaOapg.properties.value, str, ],
                currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    defaultRemunerationComponent=defaultRemunerationComponent,
                    name=name,
                    type=type,
                    value=value,
                    currency=currency,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'JobPatchRequestRemunerationScheduleAdditions':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
