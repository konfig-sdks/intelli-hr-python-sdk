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


class JobPatchResponseDataRecruitment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The recruitment details stored for this [Job](https://developers.intellihr.io/docs/v1/).
    """


    class MetaOapg:
        
        class properties:
            
            
            class cost(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.NumberSchema
                    one_of_1 = schemas.NoneSchema
                    
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
                ) -> 'cost':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class currency(
                schemas.StrSchema
            ):
                pass
            
            
            class source(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class one_of_0(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                
                                
                                class id(
                                    schemas.StrSchema
                                ):
                                    pass
                                name = schemas.StrSchema
                                link = schemas.StrSchema
                                __annotations__ = {
                                    "id": id,
                                    "name": name,
                                    "link": link,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "link", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "link", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                            name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                            link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'one_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                id=id,
                                name=name,
                                link=link,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    one_of_1 = schemas.NoneSchema
                    
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
                ) -> 'source':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "cost": cost,
                "currency": currency,
                "source": source,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost"]) -> MetaOapg.properties.cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cost", "currency", "source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost"]) -> typing.Union[MetaOapg.properties.cost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cost", "currency", "source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cost: typing.Union[MetaOapg.properties.cost, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobPatchResponseDataRecruitment':
        return super().__new__(
            cls,
            *args,
            cost=cost,
            currency=currency,
            source=source,
            _configuration=_configuration,
            **kwargs,
        )
