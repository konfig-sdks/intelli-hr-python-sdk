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


class TrainingsPatchRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def coordinatorPerson() -> typing.Type['TrainingsPatchRequestCoordinatorPerson']:
                return TrainingsPatchRequestCoordinatorPerson
            completionDate = schemas.StrSchema
            cost = schemas.StrSchema
            
            
            class currency(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[A-Z]{3}$',
                    }]
            hours = schemas.StrSchema
        
            @staticmethod
            def job() -> typing.Type['TrainingsPatchRequestJob']:
                return TrainingsPatchRequestJob
            name = schemas.StrSchema
        
            @staticmethod
            def person() -> typing.Type['TrainingsPatchRequestPerson']:
                return TrainingsPatchRequestPerson
        
            @staticmethod
            def provider() -> typing.Type['TrainingsPatchRequestProvider']:
                return TrainingsPatchRequestProvider
        
            @staticmethod
            def type() -> typing.Type['TrainingsPatchRequestType']:
                return TrainingsPatchRequestType
        
            @staticmethod
            def customFields() -> typing.Type['TrainingsPatchRequestCustomFields']:
                return TrainingsPatchRequestCustomFields
        
            @staticmethod
            def status() -> typing.Type['TrainingsPatchRequestStatus']:
                return TrainingsPatchRequestStatus
            __annotations__ = {
                "coordinatorPerson": coordinatorPerson,
                "completionDate": completionDate,
                "cost": cost,
                "currency": currency,
                "hours": hours,
                "job": job,
                "name": name,
                "person": person,
                "provider": provider,
                "type": type,
                "customFields": customFields,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coordinatorPerson"]) -> 'TrainingsPatchRequestCoordinatorPerson': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completionDate"]) -> MetaOapg.properties.completionDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost"]) -> MetaOapg.properties.cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job"]) -> 'TrainingsPatchRequestJob': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["person"]) -> 'TrainingsPatchRequestPerson': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> 'TrainingsPatchRequestProvider': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'TrainingsPatchRequestType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> 'TrainingsPatchRequestCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'TrainingsPatchRequestStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["coordinatorPerson", "completionDate", "cost", "currency", "hours", "job", "name", "person", "provider", "type", "customFields", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coordinatorPerson"]) -> typing.Union['TrainingsPatchRequestCoordinatorPerson', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completionDate"]) -> typing.Union[MetaOapg.properties.completionDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost"]) -> typing.Union[MetaOapg.properties.cost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> typing.Union[MetaOapg.properties.hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job"]) -> typing.Union['TrainingsPatchRequestJob', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["person"]) -> typing.Union['TrainingsPatchRequestPerson', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union['TrainingsPatchRequestProvider', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['TrainingsPatchRequestType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union['TrainingsPatchRequestCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['TrainingsPatchRequestStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["coordinatorPerson", "completionDate", "cost", "currency", "hours", "job", "name", "person", "provider", "type", "customFields", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        coordinatorPerson: typing.Union['TrainingsPatchRequestCoordinatorPerson', schemas.Unset] = schemas.unset,
        completionDate: typing.Union[MetaOapg.properties.completionDate, str, schemas.Unset] = schemas.unset,
        cost: typing.Union[MetaOapg.properties.cost, str, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        hours: typing.Union[MetaOapg.properties.hours, str, schemas.Unset] = schemas.unset,
        job: typing.Union['TrainingsPatchRequestJob', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        person: typing.Union['TrainingsPatchRequestPerson', schemas.Unset] = schemas.unset,
        provider: typing.Union['TrainingsPatchRequestProvider', schemas.Unset] = schemas.unset,
        type: typing.Union['TrainingsPatchRequestType', schemas.Unset] = schemas.unset,
        customFields: typing.Union['TrainingsPatchRequestCustomFields', schemas.Unset] = schemas.unset,
        status: typing.Union['TrainingsPatchRequestStatus', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TrainingsPatchRequest':
        return super().__new__(
            cls,
            *args,
            coordinatorPerson=coordinatorPerson,
            completionDate=completionDate,
            cost=cost,
            currency=currency,
            hours=hours,
            job=job,
            name=name,
            person=person,
            provider=provider,
            type=type,
            customFields=customFields,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.trainings_patch_request_coordinator_person import TrainingsPatchRequestCoordinatorPerson
from intelli_hr_python_sdk.model.trainings_patch_request_custom_fields import TrainingsPatchRequestCustomFields
from intelli_hr_python_sdk.model.trainings_patch_request_job import TrainingsPatchRequestJob
from intelli_hr_python_sdk.model.trainings_patch_request_person import TrainingsPatchRequestPerson
from intelli_hr_python_sdk.model.trainings_patch_request_provider import TrainingsPatchRequestProvider
from intelli_hr_python_sdk.model.trainings_patch_request_status import TrainingsPatchRequestStatus
from intelli_hr_python_sdk.model.trainings_patch_request_type import TrainingsPatchRequestType
