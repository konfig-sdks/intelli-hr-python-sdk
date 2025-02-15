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


class WebhookJobEndDateFinalised(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    event = schemas.AnyTypeSchema
                    start_date = schemas.StrSchema
                    inclusive_end_date = schemas.StrSchema
                    
                    
                    class links(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                _self = schemas.StrSchema
                                selfEncoded = schemas.StrSchema
                                __annotations__ = {
                                    "self": _self,
                                    "selfEncoded": selfEncoded,
                                }
                    
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["selfEncoded"]) -> MetaOapg.properties.selfEncoded: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["self", "selfEncoded", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["selfEncoded"]) -> typing.Union[MetaOapg.properties.selfEncoded, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["self", "selfEncoded", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            selfEncoded: typing.Union[MetaOapg.properties.selfEncoded, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'links':
                            return super().__new__(
                                cls,
                                *args,
                                selfEncoded=selfEncoded,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "event": event,
                        "start_date": start_date,
                        "inclusive_end_date": inclusive_end_date,
                        "links": links,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["event"]) -> MetaOapg.properties.event: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inclusive_end_date"]) -> MetaOapg.properties.inclusive_end_date: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["event", "start_date", "inclusive_end_date", "links", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["event"]) -> typing.Union[MetaOapg.properties.event, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inclusive_end_date"]) -> typing.Union[MetaOapg.properties.inclusive_end_date, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event", "start_date", "inclusive_end_date", "links", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                event: typing.Union[MetaOapg.properties.event, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
                inclusive_end_date: typing.Union[MetaOapg.properties.inclusive_end_date, str, schemas.Unset] = schemas.unset,
                links: typing.Union[MetaOapg.properties.links, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    event=event,
                    start_date=start_date,
                    inclusive_end_date=inclusive_end_date,
                    links=links,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                WebhookEventBasic,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookJobEndDateFinalised':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.webhook_event_basic import WebhookEventBasic
