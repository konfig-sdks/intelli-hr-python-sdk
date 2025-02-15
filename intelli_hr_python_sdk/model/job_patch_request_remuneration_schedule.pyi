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


class JobPatchRequestRemunerationSchedule(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    remuneration schedule. This will replace the current schedule with a new schedule. Please include all fields of which to replace the current remuneration schedule with, any fields / items that are not provided will not be included.
    """


    class MetaOapg:
        required = {
            "hoursPerCycle",
            "payCycle",
        }
        
        class properties:
            payCycle = schemas.StrSchema
            hoursPerCycle = schemas.NumberSchema
            type = schemas.StrSchema
            
            
            class currency(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def employmentCondition() -> typing.Type['JobPatchRequestRemunerationScheduleEmploymentCondition']:
                return JobPatchRequestRemunerationScheduleEmploymentCondition
            baseAnnualSalary = schemas.NumberSchema
            baseHourlyRate = schemas.NumberSchema
        
            @staticmethod
            def additions() -> typing.Type['JobPatchRequestRemunerationScheduleAdditions']:
                return JobPatchRequestRemunerationScheduleAdditions
        
            @staticmethod
            def additionsToTotal() -> typing.Type['JobPatchRequestRemunerationScheduleAdditionsToTotal']:
                return JobPatchRequestRemunerationScheduleAdditionsToTotal
        
            @staticmethod
            def breakdowns() -> typing.Type['JobPatchRequestRemunerationScheduleBreakdowns']:
                return JobPatchRequestRemunerationScheduleBreakdowns
        
            @staticmethod
            def customFields() -> typing.Type['JobPatchRequestRemunerationScheduleCustomFields']:
                return JobPatchRequestRemunerationScheduleCustomFields
            __annotations__ = {
                "payCycle": payCycle,
                "hoursPerCycle": hoursPerCycle,
                "type": type,
                "currency": currency,
                "employmentCondition": employmentCondition,
                "baseAnnualSalary": baseAnnualSalary,
                "baseHourlyRate": baseHourlyRate,
                "additions": additions,
                "additionsToTotal": additionsToTotal,
                "breakdowns": breakdowns,
                "customFields": customFields,
            }
    
    hoursPerCycle: MetaOapg.properties.hoursPerCycle
    payCycle: MetaOapg.properties.payCycle
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payCycle"]) -> MetaOapg.properties.payCycle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hoursPerCycle"]) -> MetaOapg.properties.hoursPerCycle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employmentCondition"]) -> 'JobPatchRequestRemunerationScheduleEmploymentCondition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseAnnualSalary"]) -> MetaOapg.properties.baseAnnualSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseHourlyRate"]) -> MetaOapg.properties.baseHourlyRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additions"]) -> 'JobPatchRequestRemunerationScheduleAdditions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionsToTotal"]) -> 'JobPatchRequestRemunerationScheduleAdditionsToTotal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breakdowns"]) -> 'JobPatchRequestRemunerationScheduleBreakdowns': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> 'JobPatchRequestRemunerationScheduleCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payCycle", "hoursPerCycle", "type", "currency", "employmentCondition", "baseAnnualSalary", "baseHourlyRate", "additions", "additionsToTotal", "breakdowns", "customFields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payCycle"]) -> MetaOapg.properties.payCycle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hoursPerCycle"]) -> MetaOapg.properties.hoursPerCycle: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employmentCondition"]) -> typing.Union['JobPatchRequestRemunerationScheduleEmploymentCondition', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseAnnualSalary"]) -> typing.Union[MetaOapg.properties.baseAnnualSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseHourlyRate"]) -> typing.Union[MetaOapg.properties.baseHourlyRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additions"]) -> typing.Union['JobPatchRequestRemunerationScheduleAdditions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionsToTotal"]) -> typing.Union['JobPatchRequestRemunerationScheduleAdditionsToTotal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breakdowns"]) -> typing.Union['JobPatchRequestRemunerationScheduleBreakdowns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union['JobPatchRequestRemunerationScheduleCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payCycle", "hoursPerCycle", "type", "currency", "employmentCondition", "baseAnnualSalary", "baseHourlyRate", "additions", "additionsToTotal", "breakdowns", "customFields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hoursPerCycle: typing.Union[MetaOapg.properties.hoursPerCycle, decimal.Decimal, int, float, ],
        payCycle: typing.Union[MetaOapg.properties.payCycle, str, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        employmentCondition: typing.Union['JobPatchRequestRemunerationScheduleEmploymentCondition', schemas.Unset] = schemas.unset,
        baseAnnualSalary: typing.Union[MetaOapg.properties.baseAnnualSalary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        baseHourlyRate: typing.Union[MetaOapg.properties.baseHourlyRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        additions: typing.Union['JobPatchRequestRemunerationScheduleAdditions', schemas.Unset] = schemas.unset,
        additionsToTotal: typing.Union['JobPatchRequestRemunerationScheduleAdditionsToTotal', schemas.Unset] = schemas.unset,
        breakdowns: typing.Union['JobPatchRequestRemunerationScheduleBreakdowns', schemas.Unset] = schemas.unset,
        customFields: typing.Union['JobPatchRequestRemunerationScheduleCustomFields', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobPatchRequestRemunerationSchedule':
        return super().__new__(
            cls,
            *args,
            hoursPerCycle=hoursPerCycle,
            payCycle=payCycle,
            type=type,
            currency=currency,
            employmentCondition=employmentCondition,
            baseAnnualSalary=baseAnnualSalary,
            baseHourlyRate=baseHourlyRate,
            additions=additions,
            additionsToTotal=additionsToTotal,
            breakdowns=breakdowns,
            customFields=customFields,
            _configuration=_configuration,
            **kwargs,
        )

from intelli_hr_python_sdk.model.job_patch_request_remuneration_schedule_additions import JobPatchRequestRemunerationScheduleAdditions
from intelli_hr_python_sdk.model.job_patch_request_remuneration_schedule_additions_to_total import JobPatchRequestRemunerationScheduleAdditionsToTotal
from intelli_hr_python_sdk.model.job_patch_request_remuneration_schedule_breakdowns import JobPatchRequestRemunerationScheduleBreakdowns
from intelli_hr_python_sdk.model.job_patch_request_remuneration_schedule_custom_fields import JobPatchRequestRemunerationScheduleCustomFields
from intelli_hr_python_sdk.model.job_patch_request_remuneration_schedule_employment_condition import JobPatchRequestRemunerationScheduleEmploymentCondition
