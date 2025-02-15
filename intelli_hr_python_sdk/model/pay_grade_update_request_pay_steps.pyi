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


class PayGradeUpdateRequestPaySteps(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of Paygrade Step Rates. This will replace the current Pay Steps with a new list.  Providing an `id` for an existing Pay Step will update that record instead of createing a new Pay Step.
    """


    class MetaOapg:
        
        
        class items(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class id(
                        schemas.StrSchema
                    ):
                        pass
                    name = schemas.StrSchema
                    permanentHourlyRate = schemas.NumberSchema
                    
                    
                    class permanentHourlyRateCurrency(
                        schemas.StrSchema
                    ):
                        pass
                    casualHourlyRate = schemas.NumberSchema
                    
                    
                    class casualHourlyRateCurrency(
                        schemas.StrSchema
                    ):
                        pass
                    annualSalary = schemas.NumberSchema
                    
                    
                    class annualSalaryCurrency(
                        schemas.StrSchema
                    ):
                        pass
                    __annotations__ = {
                        "id": id,
                        "name": name,
                        "permanentHourlyRate": permanentHourlyRate,
                        "permanentHourlyRateCurrency": permanentHourlyRateCurrency,
                        "casualHourlyRate": casualHourlyRate,
                        "casualHourlyRateCurrency": casualHourlyRateCurrency,
                        "annualSalary": annualSalary,
                        "annualSalaryCurrency": annualSalaryCurrency,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["permanentHourlyRate"]) -> MetaOapg.properties.permanentHourlyRate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["permanentHourlyRateCurrency"]) -> MetaOapg.properties.permanentHourlyRateCurrency: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["casualHourlyRate"]) -> MetaOapg.properties.casualHourlyRate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["casualHourlyRateCurrency"]) -> MetaOapg.properties.casualHourlyRateCurrency: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["annualSalary"]) -> MetaOapg.properties.annualSalary: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["annualSalaryCurrency"]) -> MetaOapg.properties.annualSalaryCurrency: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "permanentHourlyRate", "permanentHourlyRateCurrency", "casualHourlyRate", "casualHourlyRateCurrency", "annualSalary", "annualSalaryCurrency", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["permanentHourlyRate"]) -> typing.Union[MetaOapg.properties.permanentHourlyRate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["permanentHourlyRateCurrency"]) -> typing.Union[MetaOapg.properties.permanentHourlyRateCurrency, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["casualHourlyRate"]) -> typing.Union[MetaOapg.properties.casualHourlyRate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["casualHourlyRateCurrency"]) -> typing.Union[MetaOapg.properties.casualHourlyRateCurrency, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["annualSalary"]) -> typing.Union[MetaOapg.properties.annualSalary, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["annualSalaryCurrency"]) -> typing.Union[MetaOapg.properties.annualSalaryCurrency, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "permanentHourlyRate", "permanentHourlyRateCurrency", "casualHourlyRate", "casualHourlyRateCurrency", "annualSalary", "annualSalaryCurrency", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                permanentHourlyRate: typing.Union[MetaOapg.properties.permanentHourlyRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                permanentHourlyRateCurrency: typing.Union[MetaOapg.properties.permanentHourlyRateCurrency, str, schemas.Unset] = schemas.unset,
                casualHourlyRate: typing.Union[MetaOapg.properties.casualHourlyRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                casualHourlyRateCurrency: typing.Union[MetaOapg.properties.casualHourlyRateCurrency, str, schemas.Unset] = schemas.unset,
                annualSalary: typing.Union[MetaOapg.properties.annualSalary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                annualSalaryCurrency: typing.Union[MetaOapg.properties.annualSalaryCurrency, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    id=id,
                    name=name,
                    permanentHourlyRate=permanentHourlyRate,
                    permanentHourlyRateCurrency=permanentHourlyRateCurrency,
                    casualHourlyRate=casualHourlyRate,
                    casualHourlyRateCurrency=casualHourlyRateCurrency,
                    annualSalary=annualSalary,
                    annualSalaryCurrency=annualSalaryCurrency,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PayGradeUpdateRequestPaySteps':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
