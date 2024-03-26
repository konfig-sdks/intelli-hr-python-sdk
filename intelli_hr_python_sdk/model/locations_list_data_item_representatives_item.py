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


class LocationsListDataItemRepresentativesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Representative model
    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 36
                    min_length = 36
        
            @staticmethod
            def person() -> typing.Type['LocationsListDataItemRepresentativesItemPerson']:
                return LocationsListDataItemRepresentativesItemPerson
        
            @staticmethod
            def representativeType() -> typing.Type['LocationsListDataItemRepresentativesItemRepresentativeType']:
                return LocationsListDataItemRepresentativesItemRepresentativeType
            __annotations__ = {
                "id": id,
                "person": person,
                "representativeType": representativeType,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["person"]) -> 'LocationsListDataItemRepresentativesItemPerson': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["representativeType"]) -> 'LocationsListDataItemRepresentativesItemRepresentativeType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "person", "representativeType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["person"]) -> typing.Union['LocationsListDataItemRepresentativesItemPerson', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["representativeType"]) -> typing.Union['LocationsListDataItemRepresentativesItemRepresentativeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "person", "representativeType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        person: typing.Union['LocationsListDataItemRepresentativesItemPerson', schemas.Unset] = schemas.unset,
        representativeType: typing.Union['LocationsListDataItemRepresentativesItemRepresentativeType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LocationsListDataItemRepresentativesItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            person=person,
            representativeType=representativeType,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.locations_list_data_item_representatives_item_person import LocationsListDataItemRepresentativesItemPerson
from intelli_hr_python_sdk.model.locations_list_data_item_representatives_item_representative_type import LocationsListDataItemRepresentativesItemRepresentativeType
