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


class PeopleUpdateRequestCustomFields(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The custom field values for this [Person](https://developers.intellihr.io/docs/v1/)
    """


    class MetaOapg:
        
        
        class additional_properties(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class value(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            any_of_0 = schemas.StrSchema
                            
                            
                            class any_of_1(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        label = schemas.StrSchema
                                        __annotations__ = {
                                            "label": label,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["label", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["label", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        label=label,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class any_of_2(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        
                                        
                                        class labels(
                                            schemas.ListSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                items = schemas.StrSchema
                                        
                                            def __new__(
                                                cls,
                                                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                            ) -> 'labels':
                                                return super().__new__(
                                                    cls,
                                                    arg,
                                                    _configuration=_configuration,
                                                )
                                        
                                            def __getitem__(self, i: int) -> MetaOapg.items:
                                                return super().__getitem__(i)
                                        __annotations__ = {
                                            "labels": labels,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["labels", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["labels", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    labels: typing.Union[MetaOapg.properties.labels, list, tuple, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_2':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        labels=labels,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class any_of_3(
                                schemas.ListSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    
                                    class items(
                                        schemas.DictSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            
                                            class properties:
                                                
                                                
                                                class person(
                                                    schemas.DictSchema
                                                ):
                                                
                                                
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
                                                    ) -> 'person':
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
                                                
                                                
                                                class job(
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
                                                    ) -> 'job':
                                                        return super().__new__(
                                                            cls,
                                                            *args,
                                                            id=id,
                                                            name=name,
                                                            _configuration=_configuration,
                                                            **kwargs,
                                                        )
                                                __annotations__ = {
                                                    "person": person,
                                                    "job": job,
                                                }
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["person"]) -> MetaOapg.properties.person: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["job"]) -> MetaOapg.properties.job: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                        
                                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["person", "job", ], str]):
                                            # dict_instance[name] accessor
                                            return super().__getitem__(name)
                                        
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["person"]) -> typing.Union[MetaOapg.properties.person, schemas.Unset]: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["job"]) -> typing.Union[MetaOapg.properties.job, schemas.Unset]: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                        
                                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["person", "job", ], str]):
                                            return super().get_item_oapg(name)
                                        
                                    
                                        def __new__(
                                            cls,
                                            *args: typing.Union[dict, frozendict.frozendict, ],
                                            person: typing.Union[MetaOapg.properties.person, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                                            job: typing.Union[MetaOapg.properties.job, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                        ) -> 'items':
                                            return super().__new__(
                                                cls,
                                                *args,
                                                person=person,
                                                job=job,
                                                _configuration=_configuration,
                                                **kwargs,
                                            )
                            
                                def __new__(
                                    cls,
                                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'any_of_3':
                                    return super().__new__(
                                        cls,
                                        arg,
                                        _configuration=_configuration,
                                    )
                            
                                def __getitem__(self, i: int) -> MetaOapg.items:
                                    return super().__getitem__(i)
                            
                            @classmethod
                            @functools.lru_cache()
                            def any_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.any_of_0,
                                    cls.any_of_1,
                                    cls.any_of_2,
                                    cls.any_of_3,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'value':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "value": value,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["value", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["value", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    *args,
                    value=value,
                    _configuration=_configuration,
                    **kwargs,
                )
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
    ) -> 'PeopleUpdateRequestCustomFields':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
